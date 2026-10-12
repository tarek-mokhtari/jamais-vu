---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Tomorrow at 9:00 we turn on our new "partner priority" bidding mode on the ad exchange's bidder fleet: eight servers behind the load balancer. To avoid a protocol change with the upstream systems, the new mode reuses value 7 of the bid_mode field, which last drove a 2019 pacing experiment; this release removes that experiment's code. Deploys to this fleet are done by hand by one engineer, a server or two per day since Monday, and the last two go out tonight. Each server emails the team list when it logs a configuration warning; those emails are informational. Spend caps are enforced downstream by the billing reconciliation, which runs hourly. Upstream starts sending bid_mode 7 at 9:00, when the partner contract begins, on the same day as a major industry event where we're presenting the feature.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
