#!/usr/bin/env python3
"""Deterministic output contract for jmv-check, applied to eval results.

    python3 tools/contract.py evals/results/<run>/aggregate-result.json [more.json ...]

For every with-plugin run, it checks the kit's own promises without a judge model:
  - the answer starts with a "jamais-vu check" header naming the door;
  - two-way: the block is at most 4 lines of at most 120 characters;
  - one-way: the block is at most 20 lines, has at most 3 risks, each tagged with a known
    source id and either a quote found verbatim in the plan (never in the FORECAST line)
    or an `absent:` note; every tripwire ends with an action, not "reconsider" or "monitor";
  - no banned phrase anywhere in the answer;
  - a printed record seals the kit's estimate as base64 of a whole number from 0 to 100.
Prints one line per violation and a summary. Exit code 1 if any run violates the contract.
"""
import base64
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BANNED = re.compile(
    r"consider scalability|ensure adequate testing|communicate better|monitor closely|"
    r"great question|it'?s important to|\bcoach|\bjourney\b|\bmindset\b|\bempower|\bunlock|"
    r"\bmindful|lessons learned|\bgrowth as\b|[\U0001F300-\U0001FAFF]",
    re.IGNORECASE,
)
WEAK_ACTIONS = re.compile(r"^\s*(reconsider|re-?evaluate|reassess|discuss|monitor|revisit|review)\b", re.I)
ID_RE = re.compile(r"^(L\d+|[a-z]+-\d{2}|[a-z]+(?:-[a-z]+)+)$")


def taxonomy_ids():
    text = (ROOT / "shared/taxonomy.md").read_text(encoding="utf-8")
    return set(re.findall(r"^### ([a-z0-9-]+) ·", text, re.M))


def plan_text(case_dir):
    prompt = Path(case_dir) / "prompt.md"
    if not prompt.exists():
        prompt = ROOT / "evals" / Path(case_dir).name / "prompt.md"
    body = prompt.read_text(encoding="utf-8").split("---", 2)[2]
    return re.split(r"^FORECAST:", body, flags=re.M)[0]


def norm(s):
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip().lower()


def quote_in_plan(quote, plan):
    fragments = [f for f in re.split(r"\[?…\]?|\.\.\.", quote) if norm(f)]
    return bool(fragments) and all(norm(f) in norm(plan) for f in fragments)


def answer_of(run):
    texts = [g.get("evidence") or "" for g in run.get("graders", [])]
    return max(texts, key=len) if texts else ""


def check_answer(answer, plan, ids):
    problems = []
    lines = [l.rstrip() for l in answer.splitlines()]
    start = next((i for i, l in enumerate(lines) if "jamais-vu check" in l.lower()), None)
    if start is None:
        return ["no 'jamais-vu check' header"]
    header = lines[start].lower()
    record_at = next((i for i, l in enumerate(lines) if "BEGIN JAMAIS-VU RECORD" in l), len(lines))
    block = [l for l in lines[start:record_at] if l.strip() and not l.lower().startswith("ignored:")]
    for m in BANNED.finditer(answer):
        problems.append(f"banned phrase: {m.group(0)!r}")
    if "two-way" in header:
        go = []
        for l in lines[start:]:
            if not l.strip():
                break
            go.append(l)
        if len(go) > 4:
            problems.append(f"two-way block has {len(go)} lines (max 4)")
        for l in go:
            if len(l) > 120:
                problems.append(f"two-way line over 120 characters ({len(l)})")
        if record_at < len(lines):
            problems.append("record printed for a two-way door")
        return problems
    if "one-way" not in header:
        return problems + ["header names no door"]
    end = next((i for i, l in enumerate(block) if l.lower().startswith("recorded")), len(block) - 1)
    if end + 1 > 20:
        problems.append(f"one-way block has {end + 1} lines (max 20)")
    risks = [l for l in block if re.match(r"^\s*\d+\.\s*\[", l)]
    covered = "no risk beyond what the plan already covers" in answer.lower()
    if not risks and not covered:
        problems.append("no tagged risk")
    if len(risks) > 3:
        problems.append(f"{len(risks)} risks (max 3)")
    for r in risks:
        m = re.match(r"^\s*\d+\.\s*\[([^\]←]+?)\s*←\s*(.*?)\]", r)
        if not m:
            problems.append(f"risk without '[id ← source]' tag: {r[:60]!r}")
            continue
        rid, anchor = m.group(1).strip(), m.group(2).strip()
        if not ID_RE.match(rid) or (re.match(r"^[a-z]+(?:-[a-z]+)+$", rid) and rid not in ids):
            problems.append(f"unknown source id: {rid!r}")
        if anchor.lower().startswith("absent:"):
            continue
        q = re.match(r'^"(.*)"$', anchor)
        if not q:
            problems.append(f"risk anchor is neither a quote nor absent: {anchor[:50]!r}")
        elif not quote_in_plan(q.group(1), plan):
            problems.append(f"quote not found in the plan: {q.group(1)[:60]!r}")
    for l in block:
        m = re.search(r"\bif\b.*?,\s*then\b(.*)$", l, re.I)
        if m and WEAK_ACTIONS.match(m.group(1)):
            problems.append(f"tripwire ends without an action: {m.group(1)[:40]!r}")
    if record_at < len(lines):
        seal = next((l for l in lines[record_at:] if l.strip().startswith("forecast_kit:")), "")
        if "none (no fresh context)" in seal:
            return problems
        m = re.search(r"sealed:\s*([A-Za-z0-9+/=]+)", seal)
        try:
            value = int(base64.b64decode(m.group(1)).decode().strip().rstrip("%")) if m and len(m.group(1)) <= 4 else None
        except (ValueError, UnicodeDecodeError):
            value = None
        if value is None or not 0 <= value <= 100:
            problems.append(f"forecast_kit not sealed as base64 of 0-100: {seal.strip()[:50]!r}")
    return problems


def main(paths):
    ids = taxonomy_ids()
    total = bad = 0
    for path in paths:
        result = json.loads(Path(path).read_text(encoding="utf-8"))
        for case in result.get("cases", []):
            plan = plan_text(case.get("dir") or case["name"])
            for i, run in enumerate(case.get("arms", {}).get("with", []), 1):
                total += 1
                problems = check_answer(answer_of(run), plan, ids)
                if problems:
                    bad += 1
                    for p in problems:
                        print(f"{case['name']} run {i}: {p}")
    print(f"{bad} of {total} with-plugin runs violate the output contract")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
