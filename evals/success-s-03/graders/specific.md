---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our orders database has outgrown its single Postgres primary, and I'm proposing we move all writes to a sharded cluster keyed by merchant. Once merchants write to the new cluster, moving them back means a reverse sync and a maintenance window per cohort, so this is the step I'm checking. For six weeks the application has dual-written to both stores, and a consistency checker comparing every order has found zero mismatches over the last 21 days. We replayed a week of production traffic at three times peak against the cluster: p99 latency 18 ms, against 31 ms today. The rollout goes by cohort: our own test merchants for a week, then 5%, 25% and 100% of merchants over four weeks, each step gated on error rate and checker results. The reverse sync for a cohort was rehearsed twice in staging on a production-size snapshot and took 9 minutes. The old primary stays live and in sync until 30 days after the last cohort moves. I'd start with the test merchants on Monday.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if every risk the output raises is specific. Raising no risk also passes when the output says that the plan already covers the risks it found (for example "No risk beyond what the plan already covers."): for this de-risked plan, that is a correct review.
4. FAIL if the output raises no risk and does not say that the plan already covers them, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
