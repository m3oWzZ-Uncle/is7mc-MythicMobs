"""Publish an authored research batch using wiki evidence and indexed source YAML."""

import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

from build_catalog import KNOWLEDGE, ROOT, Wiki, article, plain, tables, write_json


def attributes(html):
    groups = []
    for anchor, rows in tables(html):
        headers = [plain(cell) for cell in rows[0]]
        if headers[0] != "Attribute":
            continue
        groups.append((anchor, [
            {column: plain(cell) for column, cell in zip(headers, row) if column != "Description"}
            for row in rows[1:]
        ]))
    return groups


def markdown(entry, detail, examples, groups, date):
    source = entry["source_url"]
    aliases = ", ".join(f"`{a}`" for a in entry["aliases"]) or "Chưa ghi alias trong chỉ mục."
    lines = [
        f"# {entry['name']}", "",
        f"**Loại** `{entry['type']}` · **Plugin** `{entry['plugin']}` · **Alias** {aliases}", "",
        f"**Nguồn đọc ngày {date}.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức]({source})",
        "", "## Chức năng và cú pháp", "", f"**FACT · wiki.** {detail['function']} [Trang mục]({source})",
        "", f"Cú pháp đọc trong nguồn: `{detail['syntax']}`.", "",
        "## Thuộc tính và mặc định", "",
    ]
    if groups:
        lines.append("Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.")
        for anchor, rows in groups:
            lines.extend(["", f"[{anchor.replace('-', ' ').capitalize()}]({source.split('#', 1)[0]}#{anchor})", "",
                          "| Thuộc tính | Alias | Kiểu nếu có | Mặc định |", "| --- | --- | --- | --- |"])
            for row in rows:
                values = [row.get(k) or "—" for k in ("Attribute", "Aliases", "Type", "Default")]
                lines.append("| " + " | ".join(v.replace("|", "&#124;").replace("<", "&lt;") for v in values) + " |")
        lines.append("")
    lines.extend([detail["attributes"], "", "## Chọn target, condition và trigger", "", detail["selection"],
                  "", "## Ví dụ và cách dùng khác nhau", ""])
    for example in examples:
        link = "../../" + quote(example["path"], safe="/") + f"#L{example['line']}"
        lines.extend([f"**FACT · YAML.** {example['note']} [Dòng YAML gốc]({link})", "",
                      "```yaml", example["text"], "```", ""])
    if not examples:
        lines.extend(["Chưa có dòng ví dụ trong dataset đã phân tích.", ""])
    lines.extend([f"**INFERENCE.** {detail['comparison']}", "", "## Giới hạn và kiểm chứng", "",
                  f"**INFERENCE.** {detail['risk']}", "",
                  f"**Bằng chứng.** {entry['verification']['level']} trong phạm vi {entry['verification']['scope']}. "
                  "Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. "
                  "[Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)"])
    for link in detail.get("patterns", []):
        lines.extend(["", f"[Pattern liên quan](../patterns/{link})"])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=Path, help="JSON research notes for at most 30 entries")
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--offline", action="store_true")
    args = parser.parse_args()
    batch = json.loads(args.batch.read_text(encoding="utf-8"))
    catalog_path = KNOWLEDGE / "catalog.json"
    checkpoint_path = KNOWLEDGE / "research-checkpoint.json"
    catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    by_id = {e["id"]: e for e in catalog["entries"]}
    details = batch["entries"]
    ids = [detail["id"] for detail in details]
    if not 1 <= len(ids) <= checkpoint["batch_limit"] or len(ids) != len(set(ids)):
        raise ValueError("Batch must have 1–30 unique entries")
    if all(by_id[eid]["research_status"] == "researched" for eid in ids):
        if any(b["id"] == batch["id"] and b["completed"] == ids for b in checkpoint["batches"]):
            print(f"Batch {batch['id']} already published")
            return
        raise ValueError("Entries already researched in a different batch")
    if any(by_id[eid]["research_status"] == "researched" for eid in ids):
        raise ValueError("Batch includes already completed research")
    index = json.loads((KNOWLEDGE / batch["dataset"]).read_text(encoding="utf-8"))
    files = {r["path"]: r for r in index["files"]}
    wiki = Wiki(args.cache, batch["checked_on"], args.offline)
    pending_docs = {}
    yaml_lines = {}
    for detail in details:
        entry = by_id[detail["id"]]
        source = entry["source_url"]
        raw_html = wiki.get(source)
        html = article(raw_html) if '<div class="wiki-content">' in raw_html else raw_html
        examples = []
        for path, line, note in detail["examples"]:
            source_file = files[path]
            if source_file["status"] != "syntax-checked":
                raise ValueError(f"Source YAML has no parse evidence: {path}")
            if path not in yaml_lines:
                raw = (ROOT / path).read_bytes()
                if hashlib.sha256(raw).hexdigest() != source_file["sha256"]:
                    raise ValueError(f"YAML differs from dataset receipt: {path}")
                yaml_lines[path] = raw.decode("utf-8-sig").splitlines()
            if not 1 <= line <= len(yaml_lines[path]):
                raise ValueError(f"Example line out of range: {path}:{line}")
            text = yaml_lines[path][line - 1]
            refs = [r for r in source_file["refs"] if r["line"] == line]
            examples.append({"path": path, "line": line, "note": note, "text": text,
                             "sha256": source_file["sha256"], "references": refs})
        checked = any(r.get("resolution") in {"local", "model-filename-match"}
                      for example in examples for r in example["references"])
        level = "Reference Checked" if checked else "YAML Parsed" if examples else "Documented"
        document = "entries/" + entry["id"].replace(":", "--") + ".md"
        entry.update(document=document, research_status="researched", gameplay=detail["gameplay"],
                     examples=examples, research={"batch": batch["id"], "dataset": batch["dataset"],
                                                 "source_sha256": wiki.sources[source]["sha256"],
                                                 "checked_on": batch["checked_on"]},
                     verification={"level": level, "scope": (
                         "các cạnh có đích khớp được liệt kê" if checked else
                         "các ví dụ được liệt kê" if examples else "trang tài liệu"),
                                   "evidence": [source, "knowledge/" + batch["dataset"]]})
        pending_docs[document] = markdown(entry, detail, examples, attributes(html), batch["checked_on"])

    (KNOWLEDGE / "entries").mkdir(exist_ok=True)
    for document, content in pending_docs.items():
        (KNOWLEDGE / document).write_text(content, encoding="utf-8")
    checkpoint["batches"].append({"id": batch["id"], "checked_on": batch["checked_on"],
                                  "completed": ids, "blocked": {}})
    write_json(catalog_path, catalog)
    write_json(checkpoint_path, checkpoint)
    print(f"Published {len(ids)} documents for batch {batch['id']}")


if __name__ == "__main__":
    main()
