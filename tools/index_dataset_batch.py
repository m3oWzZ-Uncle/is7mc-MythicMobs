"""Index an explicitly selected batch of loose YAML or ZIP members without extracting files."""

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
from zipfile import ZipFile

import yaml


ROOT = Path(__file__).resolve().parents[1]
LINE = re.compile(r"^([\w:-]+)(?=\{|\s|$)")
REFERENCE = re.compile(r"(?:^|[;{])\s*(s|skill|skills|ot|ontick|oh|onhit|oe|onend|os|onstart|ob|onhitblock)\s*=\s*([^;}]+)", re.I)
CALLERS = {"skill", "metaskill", "sudoskill", "randomskill", "auraremove", "projectile", "missile",
           "totem", "aura", "ondamaged", "onattack", "orbital"}
SECTIONS = ("Skills", "Conditions", "TargetConditions", "TriggerConditions", "Cooldown")


def pairs(node):
    return node.value if isinstance(node, yaml.MappingNode) else []


def scalars(node):
    if isinstance(node, yaml.ScalarNode):
        yield node
    elif isinstance(node, yaml.SequenceNode):
        for value in node.value:
            if isinstance(value, yaml.ScalarNode):
                yield value


def kind_for(path):
    parts = ("/" + path.lower().replace("!", "/")).split("/")
    if "mmocore" in parts:
        return "mmocore-class" if "classes" in parts else "mmocore-skill"
    if "mythiclib" in parts:
        return "mythiclib-registration"
    if "config" in parts or parts[-1] in {"packinfo.yml", "packinfo.yaml"}:
        return "metadata"
    for folder, kind in (("mobs", "mob"), ("skills", "metaskill"), ("items", "item")):
        if folder in parts:
            return kind
    return "unclassified"


def definitions(node, kind):
    if kind == "metadata":
        return []
    if kind.startswith("mmocore-"):
        return [(None, node)] if isinstance(node, yaml.MappingNode) else []
    return [(key, value) for key, value in pairs(node)
            if isinstance(key, yaml.ScalarNode) and isinstance(value, yaml.MappingNode)]


def literal_refs(section, mechanic, value):
    if section == "Skills" and mechanic in CALLERS:
        for field, raw in REFERENCE.findall(value):
            field = field.casefold()
            if field in {"s", "skill", "skills"} and mechanic not in {"skill", "metaskill", "sudoskill", "randomskill"}:
                continue
            for target in raw.strip().split(","):
                if re.fullmatch(r"[\w.\[\]-]+", target):
                    yield "metaskill", target
    if section == "Skills" and mechanic in {"summon", "projectile", "missile", "totem", "orbital"}:
        key = r"type|t|mob|m" if mechanic == "summon" else "mob"
        match = re.search(r"(?:^|[;{])(?:" + key + r")=([\w.\[\]-]+)(?=[;}]|$)", value, re.I)
        if match:
            yield "mob", match[1]
    if section in SECTIONS[1:4]:
        match = re.search(r"(?:^|\s)(?:castinstead|orelsecast|cast)\s+([\w.\[\]-]+)\s*$", value, re.I)
        if match:
            yield "metaskill", match[1]


def inspect(path, scope, content):
    kind = kind_for(path)
    row = {"path": path, "sha256": hashlib.sha256(content).hexdigest(), "kind": kind,
           "scope": scope, "status": "unverified", "definitions": [], "duplicate_keys": [], "metadata": {}}
    try:
        root = yaml.compose(content, Loader=yaml.SafeLoader)
    except (yaml.YAMLError, UnicodeError) as exc:
        row["parse_error"] = str(exc)
        return row
    row["status"] = "syntax-checked"
    if kind == "metadata":
        row["metadata"] = {k.value: v.value for k, v in pairs(root)
                           if k.value.casefold() in {"name", "version"} and isinstance(v, yaml.ScalarNode)}
    seen = set()
    pending = [root]
    while pending:
        node = pending.pop()
        if id(node) in seen:
            continue
        seen.add(id(node))
        if isinstance(node, yaml.MappingNode):
            keys = set()
            for key, value in pairs(node):
                if isinstance(key, yaml.ScalarNode):
                    if key.value in keys:
                        row["duplicate_keys"].append({"key": key.value, "line": key.start_mark.line + 1})
                    keys.add(key.value)
                pending.extend((key, value))
        elif isinstance(node, yaml.SequenceNode):
            pending.extend(node.value)
    for key, body in definitions(root, kind):
        entry = {"id": key.value if key else Path(path).stem, "line": (key or body).start_mark.line + 1,
                 "fields": [], "steps": [], "refs": []}
        for field, values in pairs(body):
            entry["fields"].append(field.value)
            if field.value == "mythicmobs-skill-id" and isinstance(values, yaml.ScalarNode):
                entry["refs"].append({"kind": "metaskill", "id": values.value, "line": values.start_mark.line + 1})
            if field.value not in SECTIONS:
                continue
            for value in scalars(values):
                text = value.value
                match = LINE.match(text)
                mechanic = match[1].casefold() if match else ""
                line = value.start_mark.line + 1
                entry["steps"].append({"section": field.value, "line": line, "operation": mechanic,
                                       "targeters": re.findall(r"(?:^|\s)@([\w]+)", text),
                                       "triggers": re.findall(r"(?:^|\s)~([\w:-]+)", text),
                                       "variables": re.findall(r"[\w.]*\.var\.[\w.-]+|<modifier\.[\w.-]+>|var=[\w.-]+", text, re.I)})
                entry["refs"].extend({"kind": target_kind, "id": target, "line": line}
                                     for target_kind, target in literal_refs(field.value, mechanic, text))
        row["definitions"].append(entry)
    return row


def source_bytes(path):
    outer, separator, member = path.partition("!")
    source = (ROOT / outer).resolve()
    if not source.is_relative_to(ROOT / "incoming"):
        raise ValueError(f"Source outside incoming: {path}")
    if not separator:
        return source.read_bytes()
    with ZipFile(source) as archive:
        matches = [entry for entry in archive.infolist() if entry.filename == member and not entry.is_dir()]
        if len(matches) != 1:
            raise ValueError(f"Missing or ambiguous ZIP entry: {path}")
        return archive.read(matches[0])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("batch", type=int)
    parser.add_argument("selection", type=Path, help="JSON map of scope to source paths")
    args = parser.parse_args()
    selection = json.loads(args.selection.read_text(encoding="utf-8-sig"))
    paths = [path for values in selection.values() for path in values]
    if not 1 <= len(paths) <= 30 or len(set(paths)) != len(paths):
        parser.error("select 1–30 distinct YAML paths")
    if any(not path.casefold().endswith((".yml", ".yaml")) for path in paths):
        parser.error("only YAML paths are supported")
    output = ROOT / f"knowledge/dataset-batch-{args.batch:02d}.json"
    if output.exists():
        parser.error(f"batch already exists: {output.name}")
    files = [inspect(path, scope, source_bytes(path)) for scope, values in selection.items() for path in values]
    known = defaultdict(list)
    prior = set()
    for document in sorted((ROOT / "knowledge").glob("dataset-batch-*.json")):
        for row in json.loads(document.read_text(encoding="utf-8"))["files"]:
            prior.add((row["path"], row["sha256"]))
            for entry in row["definitions"]:
                kind = entry.get("kind", row.get("kind"))
                if kind == "skill":  # The first batch used this name for a MythicMobs metaskill.
                    kind = "metaskill"
                known[(row["scope"], kind, entry["id"].casefold())].append(row["path"])
    for row in files:
        if (row["path"], row["sha256"]) in prior:
            parser.error(f"file already processed: {row['path']}")
        for entry in row["definitions"]:
            known[(row["scope"], row["kind"], entry["id"].casefold())].append(row["path"])
    resolutions = Counter()
    for row in files:
        for entry in row["definitions"]:
            for ref in entry["refs"]:
                ref["matches"] = known[(row["scope"], ref["kind"], ref["id"].casefold())]
                ref["resolution"] = {0: "not-found-in-scope", 1: "static-match"}.get(len(ref["matches"]), "ambiguous")
                resolutions[ref["resolution"]] += 1
    result = {"batch": args.batch, "yaml_limit": 30, "parser": f"PyYAML {yaml.__version__} compose",
              "files": files, "reference_counts": dict(resolutions)}
    with output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(f"{output.name}: {len(files)} YAML, {sum(len(r['definitions']) for r in files)} definitions, {dict(resolutions)}")


if __name__ == "__main__":
    main()
