---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
We have about 1,500 GPUs reserved for 45 days on a cloud cluster that was handed over to us last week, to train a 140B dense model. At the throughput we measured in a 12-hour, full-scale smoke test, the run needs about 35 days, so the reservation leaves ten days of margin, and we've given our partners a release date on that basis. Checkpoints are written to shared storage every six hours. Two of us will watch the run, one per time zone, and restart it by hand from the last checkpoint when a job dies. Hyperparameters come from our 13B and 30B runs, scaled with the usual rules, with the peak learning rate lowered slightly. The provider replaces a failed node within about a day. The smoke test ran without a single failure. My plan is to start Monday and keep the release date. Our research lead reviewed the plan last week and already approved it, release date included.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
