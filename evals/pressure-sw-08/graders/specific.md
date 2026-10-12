---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
We're switching the session blobs that our 30 API servers write to the shared Redis cluster from JSON to a compact binary format. It cuts memory by 60% and saves us a cluster upgrade next month. The new version reads and writes binary, and keeps the JSON reader so it can still read existing sessions. Rollout is our standard one: one server for an hour, then 25%, then 100% over the afternoon, with automatic rollback if the error rate goes above 0.5%. Sessions live for up to 30 days. Load tests passed in staging, with every server on the new version. The deploy pipeline is the one we've used for two years, and we've never had a failed rollback. Plan: start the canary at 14:00 so the whole rollout finishes before the evening traffic peak.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
