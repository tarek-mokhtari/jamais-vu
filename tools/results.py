#!/usr/bin/env python3
"""Summarize eval results for the README: per case group, with-plugin vs baseline.

    python3 tools/results.py evals/final/*.json [--baseline older-run.json]

Baseline runs (no plugin) come from the given files' "without" arms; --baseline adds the
"without" arms of an earlier run for cases whose prompts and graders did not change.
Prints one Markdown table: pass rate per grader and group, with and without the kit.
"""
import json
import sys
from collections import defaultdict

GROUPS = [
    ("Hard-to-undo, in pack", lambda n, tags: n.startswith("oneway-") and not n.startswith("oneway-ox-")),
    ("Hard-to-undo, out of pack", lambda n, tags: n.startswith("oneway-ox-")),
    ("Reversible (expect a fast go)", lambda n, tags: n.startswith("control-")),
    ("Sound plans (expect no false alarm)", lambda n, tags: n.startswith("success-")),
    ("With a personal ledger", lambda n, tags: n.startswith("ledger-")),
    ("Under pressure", lambda n, tags: n.startswith("pressure-")),
    ("Pushback without evidence", lambda n, tags: n.startswith("pushback-")),
    ("Injection and privacy attacks", lambda n, tags: n.startswith("adversarial-")),
]
KEY = ["caught", "go-fast", "no-false-alarm", "ledger-cited", "no-forced-match", "no-capitulation",
       "risk-stands", "concise", "test-first", "tripwire", "specific", "triggered"]


def load(paths):
    cases = {}
    for path in paths:
        for case in json.load(open(path, encoding="utf-8"))["cases"]:
            tags = case.get("tags") or []
            entry = cases.setdefault(case["name"], {"tags": tags, "with": [], "without": []})
            for arm in ("with", "without"):
                entry[arm] += [r for r in case.get("arms", {}).get(arm, []) if not r.get("error")]
    return cases


def main(argv):
    base = []
    if "--baseline" in argv:
        i = argv.index("--baseline")
        base, argv = [argv[i + 1]], argv[:i] + argv[i + 2:]
    cases = load(argv)
    for name, entry in load(base).items():
        if name in cases and not cases[name]["without"]:
            cases[name]["without"] = entry["without"]
    print("| Group | Grader | With the kit | Same model, no kit |\n|---|---|---|---|")
    for label, match in GROUPS:
        stats = defaultdict(lambda: {"with": [0, 0], "without": [0, 0]})
        n = 0
        for name, entry in cases.items():
            if not match(name, entry["tags"]):
                continue
            n += 1
            for arm in ("with", "without"):
                for run in entry[arm]:
                    for g in run.get("graders", []):
                        if g.get("scored", True) and (g["name"] in KEY or label.startswith("Injection")):
                            stats[g["name"]][arm][0] += int(g["passed"])
                            stats[g["name"]][arm][1] += 1
        for grader in sorted(stats, key=lambda g: KEY.index(g) if g in KEY else 99):
            w, wo = stats[grader]["with"], stats[grader]["without"]
            fmt = lambda s: f"{s[0]}/{s[1]}" if s[1] else "—"
            print(f"| {label} ({n}) | {grader} | {fmt(w)} | {fmt(wo)} |")


if __name__ == "__main__":
    main(sys.argv[1:])
