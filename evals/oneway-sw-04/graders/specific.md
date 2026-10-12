---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our API gateway runs a request-inspection rule set on every request, across 120 points of presence. The security team wants to ship 14 new detection rules today for a new class of injection attacks that customers reported this week. Rule updates go out through our config distribution system, which reaches every node in under a minute; rules don't go through the weekly staged software release, because they need to respond to attacks quickly. As usual for new rules, they ship in log-only mode: they record matches without blocking, and we'll review false positives tomorrow before switching them to block. All 14 pass the rules repository's tests, which check expected matches on 200 sample payloads. One of them is a long regular expression written to catch obfuscated variants. Plan: push at 13:30, right after the security team's review meeting.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
