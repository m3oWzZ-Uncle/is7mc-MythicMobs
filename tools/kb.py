"""Search the MythicMobs catalog, resume research and validate local evidence."""

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge"
LEVELS = {"Documented", "YAML Parsed", "Reference Checked", "Server Load Tested", "Gameplay Verified"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalized(value):
    return value.casefold().lstrip("@~")


def search(entries, args):
    query = normalized(args.query)
    matches = []
    for entry in entries:
        if args.type and entry["type"] != args.type:
            continue
        if args.plugin and normalized(args.plugin) not in {
            normalized(value) for value in [entry["plugin"], *entry["dependencies"]]
        }:
            continue
        if args.status and entry["research_status"] != args.status:
            continue
        if args.gameplay and normalized(args.gameplay) not in map(normalized, entry["gameplay"]):
            continue
        names = [normalized(x) for x in [entry["name"], *entry["aliases"]]]
        paths = [entry["id"], entry["source_url"], entry["document"] or ""]
        paths.extend(x["path"] for x in entry.get("examples", []))
        rank = 0 if query in names else 1 if any(x.startswith(query) for x in names) else 2
        if query and not any(query in value for value in [*names, *(normalized(x) for x in paths)]):
            continue
        matches.append((rank, entry["research_status"] != "researched", entry["id"], entry))
    return [item[-1] for item in sorted(matches)[:args.limit]]


def validate(entries, checkpoint):
    ids = [e["id"] for e in entries]
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate catalog IDs")
    datasets = {
        name: {r["path"]: r for r in read_json(KB / name)["files"]}
        for name in {e["research"]["dataset"] for e in entries if e["research_status"] == "researched"}
    }
    checked = {}
    docs = set()
    for entry in entries:
        eid = entry["id"]
        source = urlsplit(entry["source_url"])
        verification = entry["verification"]
        if source.scheme != "https" or not source.netloc or not verification["evidence"]:
            raise ValueError(f"Invalid source or missing evidence: {eid}")
        level = verification["level"]
        if level not in LEVELS:
            raise ValueError(f"Invalid verification level: {eid}")
        if level in {"Server Load Tested", "Gameplay Verified"}:
            for required in ("build", "artifact", "result"):
                if not verification.get(required):
                    raise ValueError(f"Runtime evidence missing {required}: {eid}")
            if not (ROOT / verification["artifact"]).is_file():
                raise ValueError(f"Missing evidence artifact: {eid}")
        if entry["version"]["confirmed"] and not entry["version"]["evidence_url"]:
            raise ValueError(f"Version assertion missing a source: {eid}")
        if entry["research_status"] != "researched":
            continue
        document = KB / entry["document"]
        if not document.is_file() or document in docs:
            raise ValueError(f"Missing or duplicated document: {eid}")
        docs.add(document)
        if not entry.get("research", {}).get("source_sha256"):
            raise ValueError(f"Missing detail source receipt: {eid}")
        for example in entry.get("examples", []):
            path = example["path"]
            row = datasets[entry["research"]["dataset"]].get(path)
            if not row or example["sha256"] != row["sha256"]:
                raise ValueError(f"Example is outside the indexed batch or changed: {eid} {path}")
            if path not in checked:
                file = ROOT / path
                checked[path] = (hashlib.sha256(file.read_bytes()).hexdigest(),
                                 file.read_text(encoding="utf-8-sig").splitlines())
            actual, lines = checked[path]
            line = example["line"]
            if actual != example["sha256"] or not 1 <= line <= len(lines) or lines[line-1] != example["text"]:
                raise ValueError(f"Example no longer matches {path}:{line}")
        if level in {"YAML Parsed", "Reference Checked"} and not entry.get("examples"):
            raise ValueError(f"Example evidence missing: {eid}")
        if level == "Reference Checked":
            references = {r["resolution"] for example in entry["examples"] for r in example.get("references", [])}
            if not references.intersection({"local", "model-filename-match"}):
                raise ValueError(f"No matched reference recorded: {eid}")
    completed = [eid for batch in checkpoint["batches"] for eid in batch["completed"]]
    researched = {e["id"] for e in entries if e["research_status"] == "researched"}
    if set(completed) != researched or len(completed) != len(researched):
        raise ValueError("Checkpoint and researched entries disagree")
    for batch in checkpoint["batches"]:
        attempted = set(batch["completed"]) | set(batch["blocked"])
        if len(attempted) > checkpoint["batch_limit"]:
            raise ValueError(f"Batch exceeds limit: {batch['id']}")
    if set(checkpoint["priority"]) - set(ids):
        raise ValueError("Priority contains unknown catalog IDs")
    for doc in [*docs, *KB.glob("patterns/*.md"), KB/"catalog-guide.md", KB/"README.md"]:
        for href in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", doc.read_text(encoding="utf-8")):
            if urlsplit(href).scheme:
                continue
            local, _, anchor = unquote(href).partition("#")
            target = doc.parent / local if local else doc
            if not target.is_file():
                raise ValueError(f"Broken link in {doc.name}: {href}")
            if re.fullmatch(r"L\d+", anchor):
                if not 1 <= int(anchor[1:]) <= len(target.read_text(encoding="utf-8-sig").splitlines()):
                    raise ValueError(f"Line outside source in {doc.name}: {href}")
    print(f"{len(entries)} entries, {len(researched)} researched, {len(checked)} example hashes checked")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    lookup = commands.add_parser("search")
    lookup.add_argument("query", nargs="?", default="")
    lookup.add_argument("--type")
    lookup.add_argument("--plugin")
    lookup.add_argument("--gameplay")
    lookup.add_argument("--status")
    lookup.add_argument("--limit", type=int, default=12)
    commands.add_parser("stats")
    next_batch = commands.add_parser("next")
    next_batch.add_argument("--limit", type=int, choices=range(1, 31), default=24, metavar="1–30")
    commands.add_parser("validate")
    args = parser.parse_args()
    entries = read_json(KB / "catalog.json")["entries"]
    checkpoint = read_json(KB / "research-checkpoint.json")
    if args.command == "validate":
        validate(entries, checkpoint)
        return
    if args.command == "stats":
        for key in ("research_status", "type"):
            print(key, dict(Counter(e[key] for e in entries)))
        return
    if args.command == "next":
        pending = {e["id"]: e for e in entries if e["research_status"] == "indexed"}
        priority = [eid for eid in checkpoint["priority"] if eid in pending]
        priority.extend(sorted(pending.keys() - set(priority)))
        for eid in priority[:args.limit]:
            print(f"{eid}\t{pending[eid]['source_url']}")
        return
    if args.limit < 1:
        parser.error("--limit must be positive")
    for entry in search(entries, args):
        doc = "knowledge/" + entry["document"] if entry["document"] else entry["source_url"]
        print(f"{entry['id']}\t{entry['verification']['level']}\t{entry['research_status']}\t{doc}")


if __name__ == "__main__":
    main()
