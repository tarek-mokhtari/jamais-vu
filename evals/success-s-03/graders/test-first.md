---
type: llm
weight: 1
---
Judge whether the agent proposes a concrete de-risking test that can run within about a day and states an explicit stop criterion.

Decision under review: start moving order writes to the sharded cluster, cohort by cohort, beginning with the test merchants.

PASS if the output contains at least one test that meets all three conditions:
- Concrete: it says what to run or check, on what, and which result to look at. "Test more", "run more experiments" or "validate the approach" are not concrete.
- About a day: it can be done within roughly one day of work or compute (minutes to about a day), not a multi-week effort such as the full run, the full migration or a long A/B test.
- Stop criterion: it states the result that would stop, change or delay the plan (a threshold, a mismatch, a count, a failed check), explicitly or as an unmistakable if-then.
The test must address a risk in this plan; where it appears in the answer does not matter. One test that would pass here (others can too): list the queries and batch jobs that touch orders across merchants (query logs over a full month, month-end included) and run them against the cluster; hold the first cohort if any fails or exceeds its time budget.

FAIL if no proposed test meets all three conditions.
