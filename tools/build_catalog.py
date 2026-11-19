"""Build the catalog from official reference pages and preserve completed research."""

import argparse
import hashlib
import json
import re
from collections import defaultdict
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE = ROOT / "knowledge"
BASE = "https://wiki.mythiccraft.io/"
RELEASE = "https://hangar.papermc.io/Lumine/MythicMobs/versions/v5.14.0"
CHANGELOG = BASE + "mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd"
INDEXES = {
    "mechanics": "mechanic", "conditions": "condition", "targeters": "targeter",
    "triggers": "trigger", "placeholders": "placeholder", "ai-goals": "ai-goal",
    "ai-targets": "ai-target",
}


def page_key(url):
    return urlsplit(url).path.rstrip("/").casefold()


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def plain(html):
    return " ".join(unescape(re.sub(r"<[^>]+>", "", html)).split())


def article(html):
    return html.split('<div class="wiki-content">', 1)[1].split("</article>", 1)[0]


def sections(html):
    return [(m[1], plain(m[2])) for m in re.finditer(
        r'<h[1-6][^>]*id="([^"]+)"[^>]*>(.*?)</h[1-6]>', html, re.S
    )]


def tables(html):
    """Yield each table with the nearest preceding heading anchor."""
    anchor = ""
    for match in re.finditer(r'<h[1-6][^>]*id="([^"]+)"[^>]*>.*?</h[1-6]>|<table[^>]*>(.*?)</table>', html, re.S):
        if match[1]:
            anchor = match[1]
            continue
        rows = [re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)
                for row in re.findall(r"<tr[^>]*>(.*?)</tr>", match[2], re.S)]
        if rows:
            yield anchor, rows


def alias_list(cell):
    return [s.strip() for s in re.split(r"[,·]", plain(re.sub(r"<br\s*/?>", ",", cell))) if s.strip()]


class Wiki:
    def __init__(self, cache, checked_on, offline):
        self.cache = cache
        self.checked_on = checked_on
        self.offline = offline
        self.sources = {}

    def get(self, path):
        url = urljoin(BASE, path)
        parts = urlsplit(url)
        prefix = "" if parts.netloc == "wiki.mythiccraft.io" else parts.netloc + "_"
        name = prefix + parts.path.strip("/").replace("/", "_") + ".html"
        file = self.cache / name
        if url in self.sources:
            return file.read_text(encoding="utf-8")
        if not self.offline:
            request = Request(url, headers={"User-Agent": "MythicMobs-Knowledge-Base/1.0"})
            with urlopen(request, timeout=25) as response:
                raw = response.read()
            self.cache.mkdir(parents=True, exist_ok=True)
            file.write_bytes(raw)
        else:
            raw = file.read_bytes()
        self.sources[url] = {"checked_on": self.checked_on, "sha256": hashlib.sha256(raw).hexdigest()}
        return raw.decode("utf-8")


def write_json(path, payload):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def build(wiki):
    entries = {}

    def add(name, kind, plugin, url, index, *, aliases=(), category=None, qualifier=None, dependencies=()):
        # Qualify homonyms by owning plugin, type and context.
        key = f"{plugin}:{kind}:{slug(name)}" + (f":{slug(qualifier)}" if qualifier else "")
        if key in entries and entries[key]["name"].casefold() != name.casefold():
            suffix = hashlib.sha256(name.encode()).hexdigest()[:8]
            key += ":" + suffix
        if key in entries and page_key(url) != page_key(entries[key]["source_url"]):
            suffix = hashlib.sha256(page_key(url).encode()).hexdigest()[:8]
            key += ":" + suffix
        if key in entries:
            e = entries[key]
            e["aliases"] = sorted(set(e["aliases"]) | set(aliases), key=str.casefold)
            e["index_urls"] = sorted(set(e["index_urls"]) | {index})
            return
        entries[key] = {
            "id": key, "name": name, "type": kind, "plugin": plugin, "aliases": sorted(set(aliases), key=str.casefold),
            "category": category, "dependencies": list(dependencies or ((plugin,) if plugin != "mythicmobs" else ())), "source_url": url,
            "index_urls": [index], "version": {"confirmed": None, "evidence_url": None},
            "verification": {"level": "Documented", "scope": "index", "evidence": [index]},
            "research_status": "indexed", "gameplay": [], "document": None,
        }

    mechanics = "mythicmobs/Skills/Mechanics"
    mechanics_html = article(wiki.get(mechanics))
    meta = {page_key(urljoin(BASE, unescape(link))) for anchor, rows in tables(mechanics_html)
            if anchor == "meta-mechanics" for row in rows[1:]
            for link in re.findall(r'href="([^"]+)"', row[0])}
    for index, kind in INDEXES.items():
        html = wiki.get(index)
        match = re.search(r'<script[^>]*id="reference-browser-payload"[^>]*>(.*?)</script>', html, re.S)
        if not match:
            raise ValueError(f"Missing wiki catalog data at {index}")
        for e in json.loads(match[1])["entries"]:
            if e["source"] != "wiki":
                raise ValueError(f"Unexpected source kind at {index}: {e['source']}")
            plugin = e["wiki_slug"]
            entry_type = "meta-mechanic" if kind == "mechanic" and page_key(e["url"]) in meta else kind
            add(e["name"], entry_type, plugin, e["url"], BASE + index,
                aliases=e["aliases"], category=e["category"], dependencies=(plugin,) if plugin != "mythicmobs" else ())

    def load(path):
        return article(wiki.get(path)), BASE + path

    # Check table coverage against each plugin index and retain explicit addon namespaces.
    reference_pages = [(mechanics, "mechanic"), ("mythicmobs/Skills/Conditions", "condition"),
                       ("mythicmobs/Skills/Targeters", "targeter"), ("mythicmobs/Skills/Triggers", "trigger")]
    reference_pages += [(f"modelengine/Skills/{p}", kind) for p, kind in
                        [("Mechanics", "mechanic"), ("Conditions", "condition"), ("Targeters", "targeter")]]
    known = {(e["plugin"], page_key(e["source_url"])): e["id"] for e in entries.values()}
    for path, kind in reference_pages:
        html, index = (mechanics_html, BASE + path) if path == mechanics else load(path)
        plugin = path.split("/")[0]
        for anchor, rows in tables(html):
            if plain(rows[0][0]).casefold() != kind:
                continue
            for row in rows[1:]:
                href = re.search(r'href="([^"]+)"', row[0])
                if not href:
                    continue
                url = urljoin(index, unescape(href[1]))
                if page_key(url).split("/")[1] != plugin:
                    continue
                name = plain(row[0]).lstrip("@~").strip()
                existing = known.get((plugin, page_key(url)))
                aliases = alias_list(row[1]) if len(row) > 2 and plain(rows[0][1]) == "Shorthand" else []
                if existing:
                    entry = entries[existing]
                    entry["aliases"] = sorted(set(entry["aliases"]) | set(aliases), key=str.casefold)
                    entry["index_urls"] = sorted(set(entry["index_urls"]) | {index})
                else:
                    add(name, "meta-mechanic" if anchor == "meta-mechanics" else kind, plugin, url, index, aliases=aliases)

    vars_html, index = load("mythicmobs/Skills/Variables")
    for anchor, rows in tables(vars_html):
        if anchor in {"variable-types", "variable-scopes"}:
            for row in rows[1:]:
                add(plain(row[0]), "variable-type" if anchor == "variable-types" else "variable-scope",
                    "mythicmobs", index + "#" + anchor, index)
    for anchor, title in sections(vars_html):
        if anchor in {"variable-placeholders", "variable-fallback", "nested-variable", "mob-variables"}:
            add(title, "variable-feature", "mythicmobs", index + "#" + anchor, index)

    metaskills, index = load("mythicmobs/Skills/Metaskills")
    add("Metaskills", "metaskill", "mythicmobs", index, index)
    for anchor, title in sections(metaskills):
        if anchor not in {"examples", "what-is-a-metaskill", "breaking-down-the-metaskills-configuration"}:
            add(title, "condition-context" if anchor in {"conditions", "targetconditions", "triggerconditions"}
                else "metaskill-field" if anchor in {"internal-skillname", "cancelifnotargets", "hidden", "failedconditionsskill",
                  "cooldown", "oncooldownskill", "skill", "skills"} else "metaskill-feature",
                "mythicmobs", index + "#" + anchor, index)
    path = "mythicmobs/Skills/Inline-Conditions"
    inline, index = load(path)
    for anchor, title in sections(inline):
        if title.casefold().replace(" ", "") in {"conditions", "targetconditions", "triggerconditions"}:
            add(title, "condition-context", "mythicmobs", index + "#" + anchor, index, qualifier="inline")
    condition_path = "mythicmobs/Skills/Conditions"
    for anchor, rows in tables(article(wiki.get(condition_path))):
        if anchor == "condition-actions":
            for row in rows[1:]:
                add(plain(row[0]).split()[0], "condition-action", "mythicmobs",
                    BASE + condition_path + "#" + anchor, BASE + condition_path)

    placeholder_pages = [
        ("mythicmobs/skills/Placeholders", "placeholder", "mythicmobs"),
        ("mythicmobs/Skills/Placeholders/Meta-Placeholders", "meta-placeholder", "mythicmobs"),
        ("modelengine/Skills/Placeholders", "placeholder", "modelengine"),
    ]
    for path, kind, plugin in placeholder_pages:
        html, index = load(path)
        for anchor, rows in tables(html):
            header = plain(rows[0][0])
            if header not in {"Placeholder", "Variable Placeholder", "PAPI Placeholder"}:
                continue
            for row in rows[1:]:
                name = plain(row[0])
                if not name:
                    continue
                # Keep the complete documented syntax, including typed meta-placeholder overloads.
                name_type = "papi-placeholder" if header == "PAPI Placeholder" else kind
                add(name, name_type, plugin, index + ("#" + anchor if anchor else ""), index,
                    qualifier=anchor if kind == "meta-placeholder" else None,
                    category=anchor or None, dependencies=("PlaceholderAPI",) if name_type == "papi-placeholder" else ())

    for path in [mechanics, "mythicmobs/Skills/Targeters", "mythicmobs/skills/Placeholders"]:
        html, index = load(path)
        for anchor, rows in tables(html):
            if plain(rows[0][0]) != "Attribute":
                continue
            for row in rows[1:]:
                add(plain(row[0]), "attribute", "mythicmobs", index + "#" + anchor, index,
                    qualifier=path.split("/")[-1] + "-" + anchor, category=anchor, aliases=alias_list(row[1]))

    attrs, index = load("mythicmobs/Items/Attributes")
    for anchor, title in sections(attrs):
        if re.fullmatch(r"[A-Z][A-Z_]+", title):
            add(title, "item-attribute", "mythicmobs", index + "#" + anchor, index)
    stats, index = load("mythicmobs/Stats")
    for anchor, rows in tables(stats):
        if plain(rows[0][0]) == "Stat":
            for row in rows[1:]:
                add(plain(row[0]), "stat", "mythicmobs", index + "#" + anchor, index)

    aura, index = load("mythicmobs/Skills/Mechanics/aura")
    for anchor, rows in tables(aura):
        if plain(rows[0][0]) != "Component":
            continue
        for row in rows[1:]:
            href = re.search(r'href="([^"]+)"', row[0])
            if href:
                add(plain(row[0]), "aura-component", "mythicmobs", urljoin(index, href[1]), index)

    path = "mythicmobs/Compatible-Plugins"
    html, index = load(path)
    for part in re.findall(r"<li[^>]*>(.*?)</li>", html, re.S):
        link = re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>', part, re.S)
        if link and " - " in plain(part):
            name = plain(link[2])
            add(name, "integration", slug(name), index, index, dependencies=(name,))

    for name, plugin, path in [
        ("ModelEngine 4", "modelengine", "modelengine/MythicMobs"),
        ("MythicLib", "mythiclib", "https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic"),
        ("MMOCore", "mmocore", "https://docs.phoenixdevt.fr/mmocore/skills/config.html"),
        ("MythicDungeons", "mythicdungeons", "mythicdungeons/Mythic-Mobs-Integration/Targeters"),
    ]:
        wiki.get(path)
        index = urljoin(BASE, path)
        add(name, "integration", plugin, index, index, dependencies=(name,))
        if plugin == "mythiclib":
            add("mmodamage", "mechanic", plugin, index, index, dependencies=(name,))
            add("mmoCanTarget", "condition", plugin, index, index, dependencies=(name,))

    # The release notes identify additions that may not be in the reference browser yet.
    changelog = article(wiki.get(CHANGELOG))
    release_notes = changelog.split('id="5140"', 1)[1].split('id="5130"', 1)[0]
    additions = {
        "mechanic": ("tickRate", "addDamageTag", "setTextOpacity", "setAudience", "addToAudience",
                     "removeFromAudience", "unsetAudience"),
        "condition": ("snowing", "isInAudience"),
        "targeter": ("bound",),
        "trigger": ("onPlayerEnter", "onPlayerExit", "onTotemPop", "onLeash", "onUnleash"),
        "metaskill-field": ("Hidden",),
    }
    for kind, names in additions.items():
        for name in names:
            token = r"@?" + re.escape(name) + (r"(?:: true)?" if name == "Hidden" else "")
            match = re.search(r"<code>" + token + r"</code>", release_notes, re.I)
            if not match:
                continue
            preceding = sections(release_notes[:match.start()])
            anchor = preceding[-1][0] if preceding else "5140"
            url = CHANGELOG + "#" + anchor
            key = f"mythicmobs:{kind}:{slug(name)}"
            if key not in entries:
                add(name, kind, "mythicmobs", url, CHANGELOG)
            entries[key]["version"] = {"confirmed": "5.14.0", "evidence_url": url}
            entries[key]["verification"]["evidence"].append(url)

    return entries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--checked-on", required=True, help="Date the source snapshot was read, YYYY-MM-DD")
    parser.add_argument("--offline", action="store_true", help="Rebuild from a previously retrieved HTML snapshot")
    args = parser.parse_args()
    wiki = Wiki(args.cache, args.checked_on, args.offline)
    path = KNOWLEDGE / "catalog.json"
    previous = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"entries": []}
    entries = build(wiki)
    for old in previous["entries"]:
        if old["research_status"] != "researched":
            continue
        current = entries.get(old["id"])
        if not current or current["source_url"] != old["source_url"]:
            raise ValueError(f"Review source change for researched entry {old['id']} before replacing the catalog")
        for key in ("version", "verification", "research_status", "gameplay", "document", "examples", "research"):
            if key in old:
                current[key] = old[key]
    data = {
        "schema_version": 1,
        "snapshot": {"checked_on": args.checked_on, "reference_release": "5.14.0",
                     "release_url": RELEASE, "changelog_url": CHANGELOG,
                     "scope": "Published wiki indexes and selected topical tables. Per-entry compatibility is separate."},
        "sources": wiki.sources,
        "entries": sorted(entries.values(), key=lambda e: e["id"]),
    }
    write_json(path, data)
    print(f"{len(entries)} entries from {len(wiki.sources)} indexes")


if __name__ == "__main__":
    main()
