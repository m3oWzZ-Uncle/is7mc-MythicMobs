"""Import, search and check the local MythicMobs Wiki snapshot."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import sys
from urllib.parse import quote, unquote, urlsplit

from build_catalog import KNOWLEDGE, ROOT, write_json


WIKI = ROOT / "docs/wiki"
SNAPSHOT = WIKI / "MythicMobs"
INDEX = WIKI / "import-index.json"
CHECKPOINT = KNOWLEDGE / "wiki-research/checkpoint.json"
OFFICIAL = "https://wiki.mythiccraft.io/mythicmobs/"
OLD_WIKI = "/mythiccraft/mythicmobs/-/wikis/"
INLINE = re.compile(r'\]\(\s*(<[^>]+>|(?:[^\s()]+|\([^()]*\))+)')
DEFINITION = re.compile(r'^\s*\[([^\]]+)\]:\s*(<[^>]+>|\S+)', re.M)
REFERENCE = re.compile(r'\[([^\]\n]+)\]\[([^\]\n]*)\]')
WIKILINK = re.compile(r'\[\[([^\]\n]+)\]\]')
HTML_LINK = re.compile(r'\b(?:href|src)=["\']([^"\']+)', re.I)
HEADING = re.compile(r'^#{1,6}\s+(.+?)\s*#*$', re.M)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def hash_file(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def tree(directory):
    files, directories = [], []
    for path in sorted(directory.rglob("*")):
        rel = path.relative_to(directory)
        if ".git" in rel.parts:
            continue
        if path.is_symlink() or path.is_junction():
            raise ValueError(f"Reparse point needs review: {path}")
        if path.is_dir():
            directories.append(rel.as_posix())
        elif path.is_file():
            files.append(rel.as_posix())
    return files, directories


def route(path):
    return re.sub(r'\.(?:md|markdown)$', '', path.rstrip('/'), flags=re.I).casefold()


def href(path):
    return OFFICIAL + quote(re.sub(r'\.(?:md|markdown)$', '', path, flags=re.I), safe='/')


def markdown_body(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    return re.sub(r'^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text, flags=re.M | re.S)


def link_targets(body):
    refs = {m[1].casefold(): m[2] for m in DEFINITION.finditer(body)}
    values = [*INLINE.findall(body), *refs.values(), *HTML_LINK.findall(body)]
    for link in WIKILINK.findall(body):
        if link != "_TOC_":
            values.append(link.split('|', 1)[0])
    for label, key in REFERENCE.findall(body):
        if (key or label).casefold() in refs:
            values.append(refs[(key or label).casefold()])
    return sorted({value.strip('<>') for value in values})


def locate_link(source, raw, known):
    try:
        url = urlsplit(raw)
    except ValueError:
        return None
    path = unquote(url.path)
    if url.netloc:
        if url.netloc.casefold() == "wiki.mythiccraft.io" and path.casefold().startswith("/mythicmobs/"):
            path = path[len("/mythicmobs"):]
        elif url.netloc.casefold() == "git.mythiccraft.io" and path.casefold().startswith(OLD_WIKI):
            path = "/" + path[len(OLD_WIKI):]
        else:
            return None
    elif url.scheme:
        return None
    if not path:
        return {"url": raw, "path": source, "resolution": "same-document", "fragment": url.fragment}
    if path.casefold().startswith("/mythicmobs/"):
        path = path[len("/mythicmobs"):]
    parent = posixpath.dirname(source)
    candidates = [path.lstrip('/')] if path.startswith('/') else [posixpath.join(parent, path), path]
    for item in candidates:
        key = route(posixpath.normpath(item))
        targets = known.get(key, [])
        if len(targets) == 1:
            return {"url": raw, "path": targets[0], "resolution": "local-path", "fragment": url.fragment}
        if targets:
            return {"url": raw, "candidates": targets, "resolution": "ambiguous", "fragment": url.fragment}
    return {"url": raw, "resolution": "unresolved-local", "fragment": url.fragment}


def topic(path):
    parts = PurePosixPath(path).parts
    if parts[0] == "Skills":
        return "/".join(parts[:2] if len(parts) > 2 else ("Skills", PurePosixPath(path).stem))
    return parts[0] if len(parts) > 1 else "Root"


def import_snapshot(args):
    source = args.source.resolve()
    if not source.is_dir() or source == SNAPSHOT or source.is_relative_to(ROOT) or ROOT.is_relative_to(source):
        raise ValueError("Select the external wiki checkout directory")
    paths, dirs = tree(source)
    if not paths:
        raise ValueError("Empty source tree")
    if INDEX.exists():
        provenance = read(INDEX)["source"]
        if (provenance["folder"], provenance["commit"], provenance["upstream"]) != (
            source.as_posix(), args.commit, args.upstream
        ):
            raise ValueError("Current index belongs to a different snapshot. Review provenance before importing.")
    if SNAPSHOT.exists():
        tree(SNAPSHOT)
        if SNAPSHOT.is_symlink() or SNAPSHOT.is_junction():
            raise ValueError("Snapshot path is a reparse point")
    rows, conflicts = [], []
    for name in paths:
        origin, dest = source / name, SNAPSHOT / name
        digest = hash_file(origin)
        if dest.exists() and (not dest.is_file() or hash_file(dest) != digest):
            conflicts.append(name)
        rows.append({"path": name, "sha256": digest, "size": origin.stat().st_size})
    if conflicts:
        raise ValueError(f"Existing files differ and were kept: {', '.join(conflicts)}")
    for name in dirs:
        (SNAPSHOT / name).mkdir(parents=True, exist_ok=True)
    SNAPSHOT.mkdir(parents=True, exist_ok=True)
    copied = 0
    known = defaultdict(list)
    for row in rows:
        name = row["path"]
        target = SNAPSHOT / name
        if not target.exists():
            raw = (source / name).read_bytes()
            if hashlib.sha256(raw).hexdigest() != row["sha256"]:
                raise ValueError(f"Source changed during the import: {name}")
            with target.open("xb") as out:
                out.write(raw)
            copied += 1
        if hash_file(target) != row["sha256"]:
            raise ValueError(f"Copy hash mismatch: {name}")
        known[route(name)].append(name)
    for row in rows:
        name = row["path"]
        if PurePosixPath(name).suffix.casefold() not in {".md", ".markdown"}:
            continue
        data = (SNAPSHOT / name).read_bytes()
        try:
            body = markdown_body(data.decode("utf-8-sig"))
            encoding = "utf-8-sig" if data.startswith(b"\xef\xbb\xbf") else "utf-8"
        except UnicodeDecodeError:
            body = markdown_body(data.decode("cp1252", errors="replace"))
            encoding = "cp1252-fallback"
        titles = HEADING.findall(body)
        title = re.search(r'^#\s+(.+?)\s*#*$', body, re.M)
        row.update(title=title[1] if title else PurePosixPath(name).stem, topic=topic(name), encoding=encoding,
                   headings=titles, online_candidate=href(name),
                   internal_links=[record for url in link_targets(body)
                                   if (record := locate_link(name, url, known)) is not None])
    data = {"source": {"folder": source.as_posix(), "upstream": args.upstream, "commit": args.commit,
                       "commit_date": args.commit_date, "imported_on": args.date, "excluded": [".git/"]},
            "directories": dirs, "files": rows}
    write_json(INDEX, data)
    return {"copied": copied, "identical": len(rows) - copied, "files": len(rows),
            "markdown": sum("title" in r for r in rows), "directories": len(dirs)}


def joins(index, catalog):
    pages = defaultdict(list)
    for row in index["files"]:
        if "title" in row:
            pages[route(row["path"])].append(row["path"])
    matches, missing = {}, []
    for entry in catalog:
        url = urlsplit(entry["source_url"])
        if entry["plugin"] != "mythicmobs" or not url.path.casefold().startswith("/mythicmobs/"):
            continue
        key = route(unquote(url.path[len("/mythicmobs/"):]))
        targets = pages.get(key, [])
        if len(targets) == 1:
            matches.setdefault(targets[0], []).append(entry["id"])
        else:
            missing.append({"id": entry["id"], "url": entry["source_url"], "reason": "ambiguous" if targets else "no-path-match"})
    return matches, missing


def source_sections(path):
    """Return source positions to open without copying the Markdown prose."""
    raw = path.read_bytes()
    body = raw.decode("utf-8-sig", errors="replace")
    starts = {}
    fenced = False
    for number, line in enumerate(body.splitlines(), 1):
        if re.match(r'^\s*(`{3,}|~{3,})', line):
            fenced = not fenced
        if fenced:
            continue
        match = re.match(r'^\s*#{1,6}\s*(description|attributes|examples?|aliases|special notes)\s*#*\s*$', line, re.I)
        if match:
            starts.setdefault(match[1].casefold(), number)
    return starts


def validate(index, checkpoint, verify_hashes):
    rows = index["files"]
    indexed = {r["path"]: r for r in rows}
    if len(indexed) != len(rows) or checkpoint["snapshot_commit"] != index["source"]["commit"]:
        raise ValueError("Duplicate inventory paths or mismatched checkpoint commit")
    if verify_hashes:
        actual, dirs = tree(SNAPSHOT)
        if set(actual) != set(indexed) or dirs != index["directories"]:
            raise ValueError("Snapshot set differs from the import index")
        for name, row in indexed.items():
            if hash_file(SNAPSHOT / name) != row["sha256"]:
                raise ValueError(f"Snapshot hash mismatch: {name}")
    reviews = {}
    for batch_file in checkpoint["batches"]:
        batch = read(CHECKPOINT.parent / batch_file)
        if not 1 <= len(batch["pages"]) <= checkpoint["batch_limit"]:
            raise ValueError(f"Invalid batch size: {batch_file}")
        for result in batch["pages"]:
            path, note = result["path"], result.get("note")
            if path in reviews or path not in indexed or "title" not in indexed[path]:
                raise ValueError(f"Repeated or missing reviewed page: {path}")
            if result["status"] not in {"aligned", "differs", "outdated", "needs-verification"}:
                raise ValueError(f"Invalid review status: {path}")
            evidence = urlsplit(result["official_url"])
            if evidence.scheme != "https" or evidence.hostname != "wiki.mythiccraft.io" or not result["finding"]:
                raise ValueError(f"Missing official evidence: {path}")
            if note and not (KNOWLEDGE / note).is_file():
                raise ValueError(f"Missing knowledge note: {note}")
            reviews[path] = result
    return reviews


def coverage(index, entries, reviewed):
    matches, missing = joins(index, entries)
    topics, links = defaultdict(Counter), Counter()
    pages = [r for r in index["files"] if "title" in r]
    for row in pages:
        group, path = topics[row["topic"]], row["path"]
        group["indexed"] += 1
        group["checked"] += path in reviewed
        group["knowledge_notes"] += bool(reviewed.get(path, {}).get("note"))
        group["catalog_matched"] += path in matches
        links.update(link["resolution"] for link in row["internal_links"])
    return {"files": len(index["files"]), "markdown": len(pages), "checked": len(reviewed),
            "reviewed_note_files": len({r["note"] for r in reviewed.values() if r.get("note")}),
            "unchecked": len(pages) - len(reviewed), "statuses": dict(Counter(r["status"] for r in reviewed.values())),
            "links": dict(links), "topics": topics, "catalog_path_matches": sum(map(len, matches.values())),
            "catalog_research": dict(Counter(row["research_status"] for row in entries)),
            "catalog_working_evidence": dict(Counter(row["verification"]["level"] for row in entries)),
            "catalog_core_without_snapshot_path_match": len(missing)}


def search(index, entries, reviewed, query, limit, topic_prefix=None):
    matches, missing = joins(index, entries)
    by_id = {e["id"]: e for e in entries}
    query = query.strip().casefold().lstrip('@~')
    terms = set(re.findall(r'\w+', query))
    if not terms or limit < 1:
        raise ValueError("Provide a search term and a positive limit")
    hits = []
    for row in index["files"]:
        if "title" not in row or (topic_prefix and not row["topic"].casefold().startswith(topic_prefix.casefold())):
            continue
        path = row["path"]
        related = [by_id[eid] for eid in matches.get(path, [])]
        keys = [PurePosixPath(path).stem, row["title"], *[n for e in related for n in [e["name"], *e["aliases"]]]]
        exact = query in {n.casefold().lstrip('@~') for n in keys}
        tokens = set(re.findall(r'\w+', ' '.join([*keys, path, *row["headings"]]).casefold()))
        review = reviewed.get(path)
        if exact or terms <= tokens or query in path.casefold():
            hits.append((not exact, review is None, path, {
                "title": row["title"], "path": f"docs/wiki/MythicMobs/{path}", "topic": row["topic"],
                "status": review["status"] if review else "unchecked",
                "official_url": review["official_url"] if review else related[0]["source_url"] if related else None,
                "online_candidate": row["online_candidate"], "finding": (review or {}).get("finding"),
                "knowledge": f"knowledge/{review['note']}" if review and review.get('note') else None,
                "snapshot_commit": index["source"]["commit"],
                "catalog_notes": sorted({f"knowledge/{e['document']}" for e in related if e['document']}),
                "catalog_ids": matches.get(path, []),
            }))
    for gap in missing:
        entry = by_id[gap["id"]]
        names = {n.casefold().lstrip('@~') for n in [entry["name"], *entry["aliases"]]}
        url_path = unquote(urlsplit(entry["source_url"]).path[len("/mythicmobs/"):])
        group = topic(url_path)
        if query in names and (not topic_prefix or group.casefold().startswith(topic_prefix.casefold())):
            hits.append((False, True, entry["id"], {"title": entry["name"], "path": None, "topic": group,
                         "status": "no-snapshot-path-match", "official_url": entry["source_url"],
                         "catalog_ids": [entry["id"]]}))
    results = []
    for _, _, path, hit in sorted(hits, key=lambda item: item[:3])[:limit]:
        if hit["path"]:
            hit["sections"] = source_sections(SNAPSHOT / path)
        results.append(hit)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    imp = commands.add_parser("import")
    imp.add_argument("source", type=Path)
    for field in ("commit", "commit-date", "upstream", "date"):
        imp.add_argument(f"--{field}", required=True)
    query = commands.add_parser("search")
    query.add_argument("query")
    query.add_argument("--limit", type=int, default=8)
    query.add_argument("--topic", help="match a topic prefix, for example Skills/Mechanics")
    commands.add_parser("coverage")
    commands.add_parser("audit-gaps")
    queue = commands.add_parser("pending")
    queue.add_argument("--limit", type=int, default=20)
    queue.add_argument("--topic", help="match a topic prefix, for example Skills/Mechanics")
    commands.add_parser("validate")
    args = parser.parse_args()
    try:
        if args.command == "import":
            result = import_snapshot(args)
        else:
            index, checkpoint = read(INDEX), read(CHECKPOINT)
            entries = read(KNOWLEDGE / "catalog.json")["entries"]
            reviews = validate(index, checkpoint, args.command == "validate")
            if args.command == "search":
                result = search(index, entries, reviews, args.query, args.limit, args.topic)
            elif args.command == "pending":
                _, missing = joins(index, entries)
                if args.limit < 1:
                    raise ValueError("Use a positive limit")
                remaining = [r["path"] for r in index["files"] if "title" in r and r["path"] not in reviews
                             and (not args.topic or r["topic"].casefold().startswith(args.topic.casefold()))]
                priorities = [p for p in checkpoint["next"] if p in remaining]
                result = {"next": (priorities + [p for p in remaining if p not in priorities])[:args.limit],
                          "catalog_without_path_match": len(missing)}
            elif args.command == "audit-gaps":
                matches, missing = joins(index, entries)
                result = {"catalog_without_snapshot_path_match": missing,
                          "snapshot_pages_without_catalog_path_match": [r["path"] for r in index["files"]
                                                                        if "title" in r and r["path"] not in matches],
                          "reviews_requiring_attention": [r for r in reviews.values() if r["status"] != "aligned"],
                          "links_to_review": [{"path": r["path"], "links": links} for r in index["files"]
                                              if (links := [link for link in r.get("internal_links", [])
                                                             if link["resolution"] in {"unresolved-local", "ambiguous"}])]}
            else:
                result = coverage(index, entries, reviews)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as exc:
        print(f"Wiki library: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
