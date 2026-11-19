"""Check sandbox YAML and report practice milestones based on recorded evidence."""

import argparse
from collections import Counter
import json
from pathlib import Path
import sys

from index_dataset_batch import inspect


SANDBOX = Path(__file__).resolve().parents[1] / "tests" / "training-sandbox"
REVIEWS = SANDBOX.parents[1] / "feedback" / "training"
INTERVAL = 5
CURRICULUM = "40-challenge"
CHALLENGES = 40


def read_case(folder):
    case = json.loads((folder / "case.json").read_text(encoding="utf-8-sig"))
    if case["id"] != folder.name or case["kind"] not in {"practice", "assessment"}:
        raise ValueError(f"{folder.name}: ID hoặc kind không hợp lệ")
    scenarios = case["required_scenarios"]
    if not scenarios or len(set(scenarios)) != len(scenarios):
        raise ValueError(f"{folder.name}: cần danh sách kịch bản khác nhau")
    if case.get("program") == CURRICULUM and case["kind"] == "practice":
        number = case.get("challenge")
        if type(number) is not int or not 1 <= number <= CHALLENGES:
            raise ValueError(f"{folder.name}: challenge phải nằm trong 1–{CHALLENGES}")
    if case["kind"] == "assessment":
        milestone = case["after_completed"]
        if type(milestone) is not int or milestone <= 0 or milestone % INTERVAL:
            raise ValueError(f"{folder.name}: mốc đánh giá không hợp lệ")
    if not (folder / "README.md").is_file():
        raise ValueError(f"{folder.name}: thiếu hướng dẫn bài")
    return case


def check_files(folder):
    rows = []
    for path in sorted(folder.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".yml", ".yaml"}:
            relative = path.relative_to(folder).as_posix()
            rows.append(inspect(relative, folder.name, path.read_bytes()))
    errors = []
    if not rows:
        errors.append("Không có YAML.")
    ids = Counter((row["kind"], entry["id"]) for row in rows for entry in row["definitions"])
    errors.extend(f"ID trùng: {kind}/{name}" for (kind, name), count in ids.items() if count > 1)
    references = 0
    for row in rows:
        path = row["path"]
        if "parse_error" in row:
            errors.append(f"{path}: {row['parse_error']}")
            continue
        if row["kind"] not in {"mob", "metaskill", "item"} or not row["definitions"]:
            errors.append(f"{path}: cần định nghĩa trong Mobs, Skills hoặc Items")
        for duplicate in row["duplicate_keys"]:
            errors.append(f"{path}:{duplicate['line']}: khóa trùng {duplicate['key']}")
        for entry in row["definitions"]:
            for ref in entry["refs"]:
                references += 1
                if (ref["kind"], ref["id"]) not in ids:
                    errors.append(f"{path}:{ref['line']}: thiếu {ref['kind']}/{ref['id']}")
    return rows, ids, references, errors


def has_artifact(folder, relative):
    if not relative or Path(relative).is_absolute():
        return False
    path = (folder / relative).resolve()
    return path.is_relative_to(folder.resolve()) and path.is_file() and path.stat().st_size > 0


def verification(folder, case, rows, ids, errors):
    if errors:
        return "unverified", "kiểm tra YAML hoặc tham chiếu chưa đạt"
    runtime = case.get("runtime")
    if not runtime:
        return "syntax-checked", "chờ log nạp và gameplay"
    revision = {row["path"]: row["sha256"] for row in rows}
    if runtime.get("yaml_sha256") != revision:
        return "syntax-checked", "hash YAML khác hồ sơ runtime"
    environment = runtime.get("environment", {})
    for key in ("minecraft", "server_build", "mythicmobs_build", "edition"):
        if not environment.get(key):
            return "syntax-checked", f"thiếu thông tin môi trường: {key}"
    if any(not environment.get("addons", {}).get(addon) for addon in case["dependencies"]):
        return "syntax-checked", "thiếu build addon"
    load = runtime.get("load", {})
    expected = {f"{kind}/{name}" for kind, name in ids}
    if (load.get("result") != "pass" or set(load.get("registered", [])) != expected
            or not has_artifact(folder, load.get("artifact"))):
        return "syntax-checked", "thiếu log nạp hoặc danh sách ID đăng ký"
    for scenario in case["required_scenarios"]:
        result = runtime.get("scenarios", {}).get(scenario, {})
        if (result.get("result") != "pass" or not result.get("observed", "").strip()
                or not has_artifact(folder, result.get("artifact"))):
            return "server-loaded", f"chưa có kết quả đạt kèm bằng chứng: {scenario}"
    if case.get("program") == CURRICULUM:
        acceptance = runtime.get("user_confirmation", {})
        if (not acceptance.get("date") or not acceptance.get("statement", "").strip()
                or not has_artifact(folder, acceptance.get("artifact"))):
            return "server-loaded", "đã có hồ sơ ca, chờ xác nhận trực tiếp của người dùng"
    return "verified-in-game", "hồ sơ nạp và toàn bộ kịch bản có bằng chứng"


def pending_assessments(records):
    completed = sum(case["kind"] == "practice" and status == "verified-in-game"
                    for case, status in records)
    assessed = {case["after_completed"] for case, status in records
                if case["kind"] == "assessment" and status == "verified-in-game"}
    pending = [milestone for milestone in range(INTERVAL, completed + 1, INTERVAL)
               if milestone not in assessed]
    return completed, pending


def review_candidates(records, milestone):
    ids = sorted({case["id"] for case, status in records
                  if case["kind"] == "practice" and status == "verified-in-game"})
    if len(ids) < milestone:
        return len(ids), []
    return len(ids), ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check = sub.add_parser("check")
    check.add_argument("id")
    status_parser = sub.add_parser("status")
    review = sub.add_parser("review")
    review.add_argument("milestone", type=int)
    for command in (status_parser, review):
        command.add_argument("--curriculum", action="store_true", help="Chỉ tính chương trình 40 bài")
    args = parser.parse_args()
    curriculum_only = getattr(args, "curriculum", False)
    if args.command == "review" and (args.milestone < INTERVAL or args.milestone % INTERVAL):
        review.error(f"Mốc phải là bội số dương của {INTERVAL}.")
    manifest_paths = sorted(SANDBOX.glob("*/case.json"))
    folders = [path.parent for path in manifest_paths
               if args.command != "check" or path.parent.name == args.id]
    if args.command == "check" and not folders:
        parser.error(f"Không tìm thấy bài {args.id}")
    records = []
    challenge_numbers = set()
    failed = False
    for folder in folders:
        try:
            case = read_case(folder)
            if curriculum_only and case.get("program") != CURRICULUM:
                continue
            if case.get("program") == CURRICULUM and case["kind"] == "practice":
                number = case["challenge"]
                if number in challenge_numbers:
                    raise ValueError(f"Bài chương trình bị ghi trùng: {number:02}")
                challenge_numbers.add(number)
            rows, ids, references, errors = check_files(folder)
            status, reason = verification(folder, case, rows, ids, errors)
        except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
            print(f"{folder.name}: hồ sơ lỗi: {exc}", file=sys.stderr)
            failed = True
            continue
        label = "GAMEPLAY_VERIFIED" if curriculum_only and status == "verified-in-game" else status
        print(f"{folder.name} [{case['level']}] {label} · {reason}")
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        failed |= bool(errors)
        records.append((case, status))
        if args.command == "check":
            print(f"  {len(rows)} YAML, {len(ids)} ID, {references} tham chiếu tĩnh nhận diện được")
            print(json.dumps({row["path"]: row["sha256"] for row in rows}, indent=2))
    if args.command == "status":
        completed, pending = pending_assessments(records)
        target = f"/{CHALLENGES}" if curriculum_only else ""
        print(f"Bài thực hành đã xác minh gameplay: {completed}{target}")
        print("Mốc đánh giá còn mở:", ", ".join(map(str, pending)) or "chưa đến hạn")
    if args.command == "review":
        prefix = "curriculum" if curriculum_only else "milestone"
        report = REVIEWS / f"{prefix}-{args.milestone:03}.md"
        completed, candidates = review_candidates(records, args.milestone)
        if report.is_file():
            print(f"Mở báo cáo đã lưu để dùng đúng nhóm bài đã chốt: {report}")
        elif candidates:
            print("Các bài hiện đủ bằng chứng:", ", ".join(candidates))
            print("Đối chiếu báo cáo trước và chọn 5 ID chưa được tổng kết.")
            print(f"Lưu đánh giá, bằng chứng và đề độc lập vào {report}")
        else:
            print(f"Mốc {args.milestone} chưa đến hạn ({completed} bài có bằng chứng gameplay).")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
