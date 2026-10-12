#!/usr/bin/env python3
"""Maintainer checks for the kit. Standard library only, Python 3.9+.

    python3 tools/check.py           sync references into the skills, then run every check
    python3 tools/check.py --check   run every check without writing (CI)

Checks: reference copies match their masters; skill frontmatter holds only Agent Skills spec
fields; no plugin component beyond skills; packs follow the pack format; no symlinks; size
budgets; banned vocabulary; manifests agree; eval scaffolds are guarded. Exit code 1 on any error.
"""
import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KIT = "jmv"

# master file -> skills that carry a copy (installed skills must be self-contained)
REFERENCES = {
    "shared/taxonomy.md": ["check", "setup", "review"],
    "shared/ledger-format.md": ["check", "setup", "review"],
    "shared/record-format.md": ["check", "review"],
}
PACKS_DIR = "packs"  # every packs/*.md is copied into the check skill's references/packs/

FRONT_TOP = re.compile(r"^(name|description|license|compatibility|metadata):( .*)?$")
FRONT_SUB = re.compile(r"^  [a-z_]+: .+$")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
PLUGIN_KEYS = {"name", "version", "description", "author", "homepage", "repository", "license", "keywords"}
FORBIDDEN_COMPONENTS = ["hooks", ".mcp.json", ".lsp.json", "agents", "commands"]
BANNED = [
    r"\bcoach(ing|es)?\b", r"\bjourney\b", r"\bmindset\b", r"\bempower\w*", r"\bunlock\w*",
    r"\b10x\b", r"great question", r"it'?s important to", r"\bmindful\w*", r"lessons learned",
]
LINT_DIRS = ["skills", "chat", "shared", "packs"]
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-⛿✀-➿]")
CHAT_LIMITS = {"chat/check.md": 8000, "chat/check-compact.md": 2600}  # templates; user data adds the rest
PACK_FIELDS = ("maps_to", "signals", "cheapest_test", "source")
SCAFFOLD_GUARDS = ["set -C", 'case "$HOME" in']

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def copies():
    pairs = []
    for master, skills in REFERENCES.items():
        for skill in skills:
            pairs.append((master, f"skills/{KIT}-{skill}/references/{Path(master).name}"))
    for pack in sorted((ROOT / PACKS_DIR).glob("*.md")):
        pairs.append((f"{PACKS_DIR}/{pack.name}", f"skills/{KIT}-check/references/packs/{pack.name}"))
    return pairs


def sync(write):
    for master, dest in copies():
        src, dst = ROOT / master, ROOT / dest
        if src.is_symlink() or dst.is_symlink():
            err(f"symlink refused: {master} or {dest}")
            continue
        if not src.exists():
            err(f"missing master: {master}")
            continue
        if write:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(src, dst)
        elif not dst.exists() or dst.read_bytes() != src.read_bytes():
            err(f"out of sync: {dest} (run python3 tools/check.py)")


def check_symlinks():
    for path in ROOT.rglob("*"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        if path.is_symlink():
            err(f"symlink in the repository: {path.relative_to(ROOT)}")


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    return text[4:end].splitlines(), text[end + 5:]


def check_skills():
    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        rel = skill_md.relative_to(ROOT)
        lines, body = split_frontmatter(skill_md.read_text(encoding="utf-8"))
        if lines is None:
            err(f"{rel}: no frontmatter")
            continue
        keys, in_meta = {}, False
        for line in lines:
            top = FRONT_TOP.match(line)
            if top:
                keys[top.group(1)] = (top.group(2) or "").strip()
                value = keys[top.group(1)]
                if ": " in value and not value.startswith(("'", '"')):
                    err(f"{rel}: unquoted ': ' in {top.group(1)} breaks YAML; quote the value")
                in_meta = top.group(1) == "metadata"
            elif in_meta and FRONT_SUB.match(line):
                continue
            else:
                err(f"{rel}: frontmatter line not allowed: {line!r}")
        folder = skill_md.parent.name
        if keys.get("name") != folder:
            err(f"{rel}: name '{keys.get('name')}' must match folder '{folder}'")
        if not NAME_RE.match(keys.get("name", "")) or len(keys.get("name", "")) > 64:
            err(f"{rel}: invalid name")
        desc = keys.get("description", "")
        if not desc or len(desc) > 1024:
            err(f"{rel}: description must be 1-1024 characters ({len(desc)})")
        elif len(desc) > 300:
            warn(f"{rel}: description is {len(desc)} characters (aim for 300 or fewer)")
        if body.count("\n") > 500:
            err(f"{rel}: body over 500 lines")
        if re.search(r"https?://", body):
            err(f"{rel}: skills must not reference URLs (no network)")
    for other in (ROOT / "skills").rglob("*"):
        if other.is_file() and other.suffix != ".md":
            err(f"{other.relative_to(ROOT)}: only Markdown is allowed under skills/")


def check_components():
    for name in FORBIDDEN_COMPONENTS:
        if (ROOT / name).exists():
            err(f"plugin component not allowed at the root: {name}")
    try:
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        err(f"manifest: {exc}")
        return
    extra = set(plugin) - PLUGIN_KEYS
    if extra:
        err(f"plugin.json: keys not allowed: {sorted(extra)}")
    names = {p.get("name") for p in market.get("plugins", [])}
    if plugin.get("name") not in names:
        err("manifest: plugin name missing from marketplace.json")
    for skill_md in (ROOT / "skills").glob("*/SKILL.md"):
        if f'version: "{plugin.get("version")}"' not in skill_md.read_text(encoding="utf-8"):
            warn(f"{skill_md.relative_to(ROOT)}: metadata version differs from plugin.json")


def taxonomy_ids():
    text = (ROOT / "shared/taxonomy.md").read_text(encoding="utf-8")
    return set(re.findall(r"^### ([a-z0-9-]+) ·", text, re.M))


def bad_char(ch):
    if 0xE0000 <= ord(ch) <= 0xE007F:
        return True
    return unicodedata.category(ch) in ("Cc", "Cf", "Co", "Cn") and ch not in "\n\t"


def check_packs():
    ids = taxonomy_ids()
    for pack in sorted((ROOT / PACKS_DIR).glob("*.md")):
        rel = pack.relative_to(ROOT)
        text = pack.read_text(encoding="utf-8")
        if len(text.encode("utf-8")) > 50_000:
            err(f"{rel}: over 50 KB")
        in_entry = False
        for n, line in enumerate(text.splitlines(), 1):
            if any(bad_char(c) for c in line):
                err(f"{rel}:{n}: control or invisible character")
            if "<" in line or "![" in line or "](" in line:
                err(f"{rel}:{n}: no HTML, images or Markdown links in packs")
            if line.startswith("### "):
                in_entry = True
                if not re.match(r"^### [a-z]+-\d{2} · \S", line):
                    err(f"{rel}:{n}: entry heading must read '### <prefix>-NN · <name>'")
                continue
            if not in_entry or not line.strip():
                if re.search(r"https?://", line):
                    err(f"{rel}:{n}: URL outside a source line")
                continue
            m = re.match(r"^- (\w+): (.+)$", line)
            if not m or m.group(1) not in PACK_FIELDS:
                err(f"{rel}:{n}: lines inside an entry must be one of {PACK_FIELDS}")
                continue
            field, value = m.groups()
            if field == "maps_to":
                for pid in re.findall(r"[a-z]+(?:-[a-z]+)+", value):
                    if pid not in ids:
                        err(f"{rel}:{n}: unknown taxonomy id '{pid}'")
            elif field == "source":
                urls = re.findall(r"https?://\S+", value)
                if len(urls) != 1 or not urls[0].startswith("https://"):
                    err(f"{rel}:{n}: source must hold exactly one https URL")
            elif re.search(r"https?://", value):
                err(f"{rel}:{n}: URL outside a source line")


def check_lint():
    for d in LINT_DIRS:
        for path in sorted((ROOT / d).rglob("*.md")):
            rel = path.relative_to(ROOT)
            for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                for pattern in BANNED:
                    if re.search(pattern, line, re.IGNORECASE):
                        err(f"{rel}:{n}: banned vocabulary /{pattern}/")
                if EMOJI_RE.search(line):
                    err(f"{rel}:{n}: emoji")


def check_sizes():
    for rel, limit in CHAT_LIMITS.items():
        path = ROOT / rel
        if path.exists():
            size = len(path.read_text(encoding="utf-8"))
            if size > limit:
                err(f"{rel}: {size} characters (limit {limit})")


def check_scaffolds():
    for script in sorted((ROOT / "evals").glob("*/*.sh")):
        text = script.read_text(encoding="utf-8")
        for guard in SCAFFOLD_GUARDS:
            if guard not in text:
                err(f"{script.relative_to(ROOT)}: missing guard '{guard}'")


def main():
    write = "--check" not in sys.argv[1:]
    check_symlinks()
    sync(write)
    check_skills()
    check_components()
    check_packs()
    check_lint()
    check_sizes()
    check_scaffolds()
    for w in warnings:
        print(f"warning: {w}")
    for e in errors:
        print(f"error: {e}")
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
