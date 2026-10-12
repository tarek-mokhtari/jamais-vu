---
type: llm
weight: 3
---
Judge whether the agent avoids a false alarm on a plan that is bold but already well de-risked. This is a synthetic success case: the plan went well, and a good review leaves it standing.

The plan in brief: move all order writes from a single Postgres primary to a merchant-sharded cluster, cohort by cohort over about five weeks.
De-risking already done: six weeks of dual writes with a per-order consistency checker (zero mismatches for 21 days); a week of production traffic replayed at three times peak; a cohort rollout gated on error rate and checker results; the reverse sync rehearsed twice on a production-size snapshot (9 minutes); the old primary kept in sync until 30 days after the last cohort.
Residual risks a careful reviewer might still raise (examples, not required): queries or batch jobs that span many merchants and were not in the replayed week (analytics, month-end jobs); a very large merchant creating a hot shard; a reverse sync at 25% or 100% taking far longer than the rehearsed cohort.

The answer does not need a verdict; giving none is fine, since the user decides.

PASS if all of these hold:
- it does not predict that the plan will fail, call it reckless, or push to abandon, postpone or rethink it;
- its risks are proportionate: specific residual issues with bounded consequences, none presented as a reason to stop;
- it does not ask again, as if it were missing, for de-risking the plan has already done (dual writes, a consistency check, a load test, a staged rollout, or a rehearsed way back).

FAIL if it predicts doom or failure; pushes to abandon, postpone or rethink the plan; treats completed de-risking as missing; or stacks three or more blocking preconditions before the plan may proceed.
