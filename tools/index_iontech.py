"""Inventory IonTech without loading its configurations in MythicMobs."""

from collections import Counter, defaultdict
import json
from pathlib import Path
import re

from index_dataset_batch import ROOT, inspect


SOURCE = ROOT / "incoming/IonTech/IonTech-s-Modular-Systems-main"
OUTPUT = ROOT / "knowledge/modular-design"
PRIORITY = (
    ("01-vector-math-variables", {"vector-skills.yml", "knockback_core.yml", "insertion_sort-demo.yml"}),
    ("02-slash-projectile", {"advanced_slash-mechanic.yml", "projectile-skills.yml",
                             "fractal.yml", "particle_spiral-vfx.yml", "particle_shockwave-vfx.yml",
                             "chain_missile.yml", "spiral_shot.yml", "shot.yml"}),
    ("03-handlers", {"spell_handler.yml", "spell_cast-defaults.yml", "modifier_handler.yml",
                     "damage_core.yml", "click_combo-mechanic-skills.yml", "setRandomID.yml"}),
)
CALL = re.compile(r"(?i)(?:\bskill:([\w.-]+)|"
                  r"\b(?:skill|sudoskill|vskill|variableskill|foreach(?:value)?|randomskill)\{\s*(?:s|skill|skills)=([\w.-]+)"
                  r"|\b(?:onStart|onEnd|onTick|onHit|onHitBlock|onPoint|o[sethpx]|ohb)="
                  r"([\w.-]+)|\b(?:orelsecast|castinstead|cast)\s+([\w.-]+)|^\s*Skill:\s*([\w.-]+))"
                  r"(?=[;},\s?\]]|$)")
ASSET = re.compile(r"(?i)\b(summon|projectile|missile|orbital)\{[^{}]*?\b(?:mob|type)=([\w.-]+)(?=[;}])")


def categories(path, body):
    name = path.name.lower()
    key = path.as_posix().lower()
    rules = {
        "Input Handlers": "input mechanics" in key or "combo" in name,
        "Spell Handlers": "spell_handler" in name or "skill handlers" in key,
        "Damage Systems": any(token in name for token in ("damage", "knockback", "melee", "hit_evaluation")),
        "Vector / Math": bool(re.search(r"(?i)\b(?:sqrt|sin|cos|atan2)\(|\.normalized|\btype=vector", body)),
        "Variables": bool(re.search(r"(?i)\b(?:setvar|setvariable|varmath|variablemath|foreachvalue)\b", body)),
        "Projectile": bool(re.search(r"(?im)^\s*-.*\b(?:projectile|missile)\{", body)),
        "Slash": "slash" in name or bool(re.search(r"(?im)^\s*-.*\bslash\{", body)),
        "Modifiers": "modifier" in name or "modifier-trigger" in body,
        "VFX": any(token in name for token in ("vfx", "animation", "indicator")),
        "Demo": "demo" in key or "test items" in key or name == "dummy-mobs.yml",
        "Deprecated": "deprecated skills" in key,
        "Incomplete": "# INCOMPLETE" in body,
    }
    return [label for label, matched in rules.items() if matched] or ["Support"]


def scan(path):
    relative = path.relative_to(SOURCE)
    raw = path.read_bytes()
    body = raw.decode("utf-8-sig")
    row = inspect(relative.as_posix(), "iontech", raw)
    calls = []
    evidence = defaultdict(list)
    owner = None
    definitions_by_line = {entry["line"]: entry for entry in row["definitions"]}
    for line, content in enumerate(body.splitlines(), 1):
        if line in definitions_by_line:
            owner = definitions_by_line[line]["id"]
        if content.lstrip().startswith("#"):
            continue
        content = re.split(r"\s+#\s", content, maxsplit=1)[0]
        for call in CALL.finditer(content):
            target = next(filter(None, call.groups()))
            if target.lower() not in {"true", "false"}:
                calls.append({"from": owner, "to": target, "line": line, "kind": "metaskill"})
        template = re.match(r"(?i)^\s*template:\s*([\w.-]+)\s*$", content)
        if template and row["kind"] in {"item", "mob"}:
            calls.append({"from": owner, "to": template[1], "line": line, "kind": row["kind"]})
        for mechanic, mob in ASSET.findall(content):
            if mechanic.lower() == "summon" or mob.upper() not in {"NORMAL", "METEOR"}:
                calls.append({"from": owner, "to": mob, "line": line, "kind": "mob"})
        if re.search(r"(?i)\bvskill\b[^\n]*<|\bvariableskill\b[^\n]*<", content):
            evidence["dynamic_calls"].append(line)
        if re.search(r"(?i)%math_", content):
            evidence["placeholderapi-math"].append(line)
        if re.search(r"(?i)%string_", content):
            evidence["placeholderapi-string"].append(line)
        if re.search(r"(?i)\b(?:model|state|submodel)\{", content):
            evidence["modelengine-candidate"].append(line)
        if re.search(r"(?i)~(?:onUse|onSwing|onRightClick|onSwap|onDrop)\b", content) and row["kind"] == "item":
            evidence["item-trigger-candidate"].append(line)
    return {
        "path": relative.as_posix(), "sha256": row["sha256"], "kind": row["kind"],
        "categories": categories(relative, body), "status": row["status"],
        "ids": [{"id": entry["id"], "line": entry["line"]} for entry in row["definitions"]],
        "duplicate_keys": row["duplicate_keys"], "parse_error": row.get("parse_error"),
        "literal_edges": calls, "dependency_signals": dict(evidence),
    }


def write_json(name, value):
    (OUTPUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    paths = sorted(path for path in SOURCE.rglob("*") if path.suffix.lower() in {".yml", ".yaml"})
    staged = set()
    batches = []
    for label, names in PRIORITY:
        selected = [path for path in paths if path.name in names]
        batches.append((label, selected))
        staged.update(selected)
    remaining = [path for path in paths if path not in staged]
    batches.extend((f"{i // 28 + 4:02d}-inventory", remaining[i:i + 28])
                   for i in range(0, len(remaining), 28))
    rows = []
    checkpoints = []
    for label, entries in batches:
        batch_rows = [scan(path) for path in entries]
        rows.extend(batch_rows)
        checkpoints.append({"batch": label, "yaml": len(batch_rows),
                            "files": [row["path"] for row in batch_rows]})
        write_json(f"iontech-{label}.json", batch_rows)
        write_json("iontech-checkpoint.json", {"source": SOURCE.relative_to(ROOT).as_posix(),
                    "inventory_total": len(paths), "inventoried": len(rows), "batches": checkpoints})

    owners = defaultdict(list)
    for row in rows:
        for entry in row["ids"]:
            owners[row["kind"], entry["id"]].append(row["path"])
    edges = []
    for row in rows:
        for edge in row["literal_edges"]:
            targets = owners.get((edge["kind"], edge["to"]), [])
            edges.append({**edge, "source": row["path"], "candidates": targets})
    report = {"yaml": len(rows), "kinds": Counter(row["kind"] for row in rows),
              "definitions": Counter({kind: sum(len(row["ids"]) for row in rows if row["kind"] == kind)
                                      for kind in sorted({row["kind"] for row in rows})}),
              "categories": Counter(category for row in rows for category in row["categories"]),
              "parse_errors": [row["path"] for row in rows if row["parse_error"]],
              "duplicate_key_files": [row["path"] for row in rows if row["duplicate_keys"]],
              "duplicate_ids": [{"kind": kind, "id": name, "files": files}
                                for (kind, name), files in owners.items() if len(files) > 1],
              "edge_count": len(edges), "unresolved_candidates": sum(not edge["candidates"] for edge in edges),
              "batches": [batch["batch"] for batch in checkpoints], "edges": edges}
    write_json("iontech-dependencies.json", report)
    print(json.dumps({key: value for key, value in report.items() if key != "edges"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
