---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Our API gateway runs a request-inspection rule set on every request, across 120 points of presence. The security team wants to ship 14 new detection rules today for a new class of injection attacks that customers reported this week. Rule updates go out through our config distribution system, which reaches every node in under a minute; rules don't go through the weekly staged software release, because they need to respond to attacks quickly. As usual for new rules, they ship in log-only mode: they record matches without blocking, and we'll review false positives tomorrow before switching them to block. All 14 pass the rules repository's tests, which check expected matches on 200 sample payloads. One of them is a long regular expression written to catch obfuscated variants. Plan: push at 13:30, right after the security team's review meeting.
"""

Hidden ground truth, what happened next: "Log-only mode still executes every rule on every request. One regular expression backtracked catastrophically on ordinary traffic and drove CPU to nearly 100% on every serving machine at once. Because rules skip the staged rollout, every location failed together: a 27-minute global outage in the original case. A CPU-limit safeguard had been removed by mistake weeks earlier, and staff struggled to reach internal tools that sat behind the same edge. Fixes: staged rollouts for rules, regex engines with run-time guarantees, performance profiling of every rule in tests."

Mechanism to look for: Log-only mode still executes every rule on every request. The long regular expression written for obfuscated variants can backtrack catastrophically on ordinary traffic and drive CPU to nearly 100% on every serving machine at once; because rules skip the staged release and reach all 120 points of presence within a minute, every location fails together. The repository tests check matches on 200 sample payloads, not run-time cost.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: log-only still runs the rules, so a slow rule costs CPU on all traffic; the long regex risks catastrophic backtracking; the push reaches all 120 points of presence at once with no canary, so a performance failure becomes a global outage; the 200-payload tests check matches, not cost. Naming the all-at-once push alone passes only if the answer says a rule could break request serving on every node, not merely produce false positives.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "false positives", "rules might block legitimate traffic" (they do not, in log-only mode), "test the rules more", with no link to execution cost or to the global push); or if it first appears as the fourth concern or later.
