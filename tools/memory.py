"""Search and maintain the local MythicMobs memory records."""

import argparse
from collections import Counter
from datetime import date
import json
import os
from pathlib import Path
import re
import sys
from tempfile import NamedTemporaryFile
import unicodedata
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = (
    "profile", "decisions", "preferences", "corrections", "conversations",
    "questions", "patterns", "uncertainties",
)
CONFIDENCE = ("CONFIRMED", "OBSERVED", "INFERRED", "UNKNOWN")
CLAIMS = ("FACT", "INFERENCE", "PREFERENCE")
SOURCE_TYPES = ("user", "document", "yaml", "test", "observation")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIELDS = {
    "id", "category", "title", "summary", "topic", "scope", "claim", "confidence",
    "tags", "requires", "excludes", "sources", "context", "exceptions", "answer",
    "decision", "supersedes", "related", "status", "regression", "question",
    "result", "recorded", "verification", "resolves",
}


def normalized(value):
    value = value.casefold().replace("đ", "d")
    return "".join(char for char in unicodedata.normalize("NFD", value)
                   if not unicodedata.combining(char))


def words(value):
    return set(re.findall(r"[a-z0-9]+", normalized(value)))


def slug(value):
    return isinstance(value, str) and SLUG.fullmatch(value) is not None


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def date_string(value):
    try:
        return date.fromisoformat(value).isoformat() == value
    except (TypeError, ValueError):
        return False


def require(condition, message):
    if not condition:
        raise ValueError(message)


def record_path(record):
    return f"memory/{record['category']}/{record['id']}.json"


def evidence_path(root, value):
    path = (root / value).resolve()
    require(path.is_relative_to(root.resolve()) and path.is_file(), f"missing local evidence {value}")


def validate_record(root, row):
    require(isinstance(row, dict), "record must be a JSON object")
    require(not (row.keys() - FIELDS), f"unknown fields: {sorted(row.keys() - FIELDS)}")
    for field in ("id", "topic"):
        require(slug(row.get(field)), f"invalid {field}")
    for field in ("title", "summary", "context", "exceptions"):
        require(nonempty(row.get(field)), f"missing {field}")
    require(date_string(row.get("recorded")), "recorded must be YYYY-MM-DD")
    category = row.get("category")
    require(category in CATEGORIES, "invalid category")
    scope = row.get("scope")
    require(isinstance(scope, str) and (scope == "global" or
            (scope.startswith("project:") and slug(scope.removeprefix("project:")))), "invalid scope")
    claim, confidence = row.get("claim"), row.get("confidence")
    require(claim in CLAIMS and confidence in CONFIDENCE, "invalid claim or confidence")
    require(claim != "INFERENCE" or confidence in {"INFERRED", "UNKNOWN"},
            "an inference cannot be observed or confirmed; add a new evidence-backed claim")
    require(confidence != "INFERRED" or claim == "INFERENCE", "use INFERENCE for inferred claims")
    require(category != "preferences" or claim == "PREFERENCE", "preferences require a PREFERENCE claim")
    require(category != "decisions" or confidence == "CONFIRMED", "decisions must be confirmed")
    require(category != "uncertainties" or confidence != "CONFIRMED", "record the resolution separately")
    for field in ("tags", "requires", "excludes", "related", "supersedes", "resolves"):
        values = row.get(field, [])
        require(isinstance(values, list) and all(slug(v) for v in values), f"invalid {field}")
        require(len(set(values)) == len(values), f"duplicate {field}")
    require(not set(row.get("requires", [])) & set(row.get("excludes", [])), "contradictory context")
    sources = row.get("sources", [])
    require(isinstance(sources, list), "sources must be a list")
    for source in sources:
        require(isinstance(source, dict) and source.get("type") in SOURCE_TYPES and
                nonempty(source.get("ref")) and nonempty(source.get("note")), "invalid source")
        ref = source["ref"]
        if ref.startswith("https://"):
            require(bool(urlsplit(ref).netloc), f"invalid source URL {ref}")
        else:
            evidence_path(root, ref.partition("#")[0])
    if confidence in {"CONFIRMED", "INFERRED"}:
        require(sources, f"{confidence} requires evidence")
    if confidence == "OBSERVED":
        refs = {s["ref"] for s in sources if s["type"] in {"yaml", "test", "observation"}}
        require(len(refs) >= 2, "OBSERVED requires evidence from multiple cases")
    if claim == "PREFERENCE" or (category == "decisions" and confidence == "CONFIRMED"):
        require(confidence == "CONFIRMED" and any(s["type"] == "user" for s in sources),
                "a confirmed user preference or decision requires direct user evidence")
    if category in {"decisions", "preferences"} and confidence == "CONFIRMED":
        require(slug(row.get("answer")), "applicable records require a stable answer slug")
    if category == "questions":
        require(claim == "FACT" and confidence == "CONFIRMED" and slug(row.get("decision")),
                "answered questions must link a confirmed decision or preference")
    if category == "corrections":
        require(row.get("status") in ("open", "checking", "confirmed", "technical"), "invalid correction status")
        if row["status"] == "confirmed":
            require(confidence == "CONFIRMED" and any(s["type"] == "user" for s in sources),
                    "a confirmed correction needs the user's confirmation")
            require(nonempty(row.get("regression")), "a confirmed correction needs a regression case")
            evidence_path(root, row["regression"])
    verification = row.get("verification")
    require(verification in (None, "unverified", "syntax-checked", "server-loaded", "verified-in-game"),
            "invalid verification level")
    if verification in ("server-loaded", "verified-in-game"):
        require(any(s["type"] == "test" and all(nonempty(s.get(k)) for k in ("build", "result"))
                    for s in sources), "runtime verification requires test evidence with build and result")
    if row.get("result") is not None:
        require(category == "conversations" and row["result"] == "reused-answer" and slug(row.get("question"))
                and claim == "FACT" and confidence == "CONFIRMED",
                "reused-answer requires a confirmed conversation fact and a question ID")


def eligible_answer(record):
    return record["category"] in {"decisions", "preferences"} and record["confidence"] == "CONFIRMED"


def validate_links(records):
    for record in records.values():
        references = [*record.get("related", []), *record.get("supersedes", []), *record.get("resolves", [])]
        for field in ("decision", "question"):
            if field in record:
                references.append(record[field])
        for ref in references:
            require(slug(ref) and ref in records and ref != record["id"], f"{record['id']}: invalid reference {ref}")
        if record["category"] == "questions":
            decision = records[record["decision"]]
            require(eligible_answer(decision) and all(record[k] == decision[k] for k in ("scope", "topic")),
                    f"{record['id']}: answer must point to a confirmed decision on the same scope and topic")
        if record.get("result") == "reused-answer":
            question = records[record["question"]]
            require(question["category"] == "questions" and question["scope"] in ("global", record["scope"]),
                    "reuse requires an answered question in scope")
            require(record["recorded"] >= question["recorded"], "reuse predates the answered question")
        for ref in record.get("resolves", []):
            earlier = records[ref]
            same_context = all(set(record.get(k, [])) == set(earlier.get(k, []))
                               for k in ("requires", "excludes"))
            closes_correction = earlier["category"] == "corrections" and earlier["status"] in ("open", "checking")
            require(record["confidence"] == "CONFIRMED" and record["recorded"] >= earlier["recorded"] and
                    all(record[k] == earlier[k] for k in ("scope", "topic")) and same_context and
                    (earlier["category"] == "uncertainties" or earlier["confidence"] == "INFERRED" or
                     (closes_correction and record.get("status") == "confirmed")),
                    f"{record['id']}: incompatible resolution of {ref}")
        for ref in record.get("supersedes", []):
            earlier = records[ref]
            require(eligible_answer(record) and eligible_answer(earlier) and
                    record["topic"] == earlier["topic"] and record["recorded"] >= earlier["recorded"] and
                    earlier["scope"] in ("global", record["scope"]),
                    f"{record['id']}: incompatible supersedes reference {ref}")
            pending, visited = [ref], set()
            while pending:
                item = pending.pop()
                require(item != record["id"], f"cyclic supersedes at {record['id']}")
                if item not in visited:
                    visited.add(item)
                    pending.extend(records[item].get("supersedes", []))


def load(root):
    records = {}
    for category in CATEGORIES:
        for path in sorted((root / "memory" / category).glob("*.json")):
            try:
                row = json.loads(path.read_text(encoding="utf-8-sig"))
                validate_record(root, row)
                require(row["id"] not in records and path == root / record_path(row),
                        "duplicate ID or path does not match category and ID")
                records[row["id"]] = row
            except (OSError, ValueError) as exc:
                raise ValueError(f"{path.relative_to(root)}: {exc}") from exc
    validate_links(records)
    return records


def in_scope(row, project):
    return row["scope"] in {"global", f"project:{project}"}


def matches_context(row, context):
    return set(row.get("requires", [])) <= context and not set(row.get("excludes", [])) & context


def summary(row):
    result = {k: row[k] for k in ("id", "category", "title", "topic", "scope", "claim", "confidence")}
    result.update({k: row[k] for k in ("status", "verification") if k in row})
    result["path"] = record_path(row)
    return result


def search(records, query, project=None, categories=(), limit=8):
    terms = words(query)
    require(terms, "search requires a non-empty query")
    hits = []
    for row in records.values():
        if not in_scope(row, project) or (categories and row["category"] not in categories):
            continue
        key_terms = words(" ".join([row["id"], row["title"], row["topic"], *row.get("tags", [])]))
        details = words(" ".join((row["summary"], row["context"])))
        score = 3 * len(terms & key_terms) + len(terms & details)
        if score:
            exact = normalized(query) in {row["id"], row["topic"]}
            hits.append((not exact, -score, row["scope"] == "global", row["id"], summary(row)))
    return [hit[-1] for hit in sorted(hits)[:limit]]


def active_answers(rows):
    # Only an applicable replacement can supersede another answer in this context.
    replaced = {ref for row in rows for ref in row.get("supersedes", [])}
    return [row for row in rows if row["id"] not in replaced]


def resolve(records, topic, project, context, impact):
    rows = [r for r in records.values() if r["topic"] == topic and in_scope(r, project)]
    answers = active_answers([r for r in rows if eligible_answer(r) and matches_context(r, context)])
    resolved = {ref for r in rows if matches_context(r, context) for ref in r.get("resolves", [])}
    active_ids = {a["id"] for a in answers}
    questions = [r for r in rows if r["category"] == "questions" and matches_context(r, context)
                 and r["decision"] in active_ids]
    result = {"topic": topic, "project": project, "context": sorted(context),
              "matches": [summary(r) for r in answers],
              "review": [summary(r) for r in rows if r not in answers and r not in questions
                         and r["id"] not in resolved]}
    choices = {r["answer"] for r in answers}
    if len(choices) > 1:
        result.update(action="review-conflict", ask_if_unresolved=impact == "material")
    elif choices:
        result.update(action="apply", answer=next(iter(choices)), answered_questions=[summary(r) for r in questions])
    else:
        result.update(action="review-then-ask-if-needed" if impact == "material" else "use-reversible-default")
    return result


def report(records):
    rows = list(records.values())
    resolved = {ref for r in rows for ref in r.get("resolves", [])}
    pending = [r for r in rows if r["id"] not in resolved and (
        r["category"] == "uncertainties" or r["confidence"] in {"INFERRED", "UNKNOWN"}
        or (r["category"] == "corrections" and r.get("status") in {"open", "checking"})
    )]
    reuse = [r for r in rows if r.get("result") == "reused-answer"]
    return {
        "records": len(rows),
        "confirmed_decisions": sum(r["category"] == "decisions" and eligible_answer(r) for r in rows),
        "confirmed_preferences": sum(r["category"] == "preferences" and eligible_answer(r) for r in rows),
        "inferred_rules": sum(r["category"] == "patterns" and r["confidence"] == "INFERRED" for r in rows),
        "confidence": dict(Counter(r["confidence"] for r in rows)),
        "answered_questions": sum(r["category"] == "questions" for r in rows),
        "questions_reused": len({r["question"] for r in reuse}),
        "answer_reuse_events": len(reuse),
        "needs_verification": [summary(r) for r in pending],
    }


def serialized(data):
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def write_json(path, data, *, replace):
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=path.parent, prefix=".memory-", delete=False) as stream:
        staged = Path(stream.name)
        try:
            stream.write(serialized(data).encode("utf-8"))
            stream.close()
            if replace:
                staged.replace(path)
            elif os.name == "nt":
                staged.rename(path)  # Windows rename fails if the destination exists.
            else:
                os.link(staged, path)  # Publish the complete record without replacing an existing ID.
        finally:
            staged.unlink(missing_ok=True)


def add(root, records, record):
    validate_record(root, record)
    require(record["id"] not in records, f"record already exists: {record['id']}")
    proposed = {**records, record["id"]: record}
    validate_links(proposed)
    write_json(root / record_path(record), record, replace=False)
    return summary(record)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="workspace root (defaults to this project)")
    commands = parser.add_subparsers(dest="command", required=True)
    find = commands.add_parser("search", help="find records by ID, keywords, or topic")
    find.add_argument("query")
    find.add_argument("--project")
    find.add_argument("--category", action="append", choices=CATEGORIES, default=[])
    find.add_argument("--limit", type=int, default=8)
    check = commands.add_parser("resolve", help="check applicable confirmed answers for an exact topic")
    check.add_argument("topic")
    check.add_argument("--project")
    check.add_argument("--context", action="append", default=[])
    check.add_argument("--impact", choices=("minor", "material"), required=True,
                       help="minor for reversible details, material when a wrong choice changes the outcome")
    commands.add_parser("report", help="report actual evidence, reuse and unresolved cases")
    commands.add_parser("validate", help="check records, evidence paths and cross-references")
    commands.add_parser("index", help="rebuild the generated inventory and report")
    insert = commands.add_parser("add", help="validate and append a JSON record")
    insert.add_argument("file", help="UTF-8 JSON path, or - for stdin")
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        require((root / "memory").is_dir(), "workspace root must contain a memory directory")
        records = load(root)
        if getattr(args, "project", None) is not None:
            require(slug(args.project), "--project must be a slug, e.g. tutien")
        if args.command == "search":
            require(args.limit > 0, "--limit must be positive")
            result = search(records, args.query, args.project, args.category, args.limit)
        elif args.command == "resolve":
            require(slug(args.topic) and all(map(slug, args.context)), "topic and context must be slugs")
            result = resolve(records, args.topic, args.project, set(args.context), args.impact)
        elif args.command == "report":
            result = report(records)
        elif args.command == "index":
            result = {"version": 1, "records": [summary(records[key]) for key in sorted(records)],
                      "report": report(records)}
            write_json(root / "memory/index/records.json", result, replace=True)
            result = {"written": "memory/index/records.json", "records": len(records)}
        elif args.command == "add":
            raw = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8-sig")
            result = add(root, records, json.loads(raw.removeprefix("\ufeff")))
        else:
            result = {"valid_records": len(records)}
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Memory error: {exc}\n")
    print(serialized(result), end="")


if __name__ == "__main__":
    main()
