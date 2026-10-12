---
type: llm
weight: 1
---
Judge whether the agent proposes a concrete de-risking test that can run within about a day and states an explicit stop criterion.

Decision under review: rotate the master key on 14 December and schedule the old key for deletion with a 30-day waiting period.

PASS if the output contains at least one test that meets all three conditions:
- Concrete: it says what to run or check, on what, and which result to look at. "Test more", "run more experiments" or "validate the approach" are not concrete.
- About a day: it can be done within roughly one day of work or compute (minutes to about a day), not a multi-week effort such as the full run, the full migration or a long A/B test.
- Stop criterion: it states the result that would stop, change or delay the plan (a threshold, a mismatch, a count, a failed check), explicitly or as an unmistakable if-then.
The test must address a risk in this plan; where it appears in the answer does not matter. One test that would pass here (others can too): before scheduling the deletion, restore one archived snapshot older than 35 days into a scratch account (or read the key ID recorded on archived objects); stop the deletion if any archive is still encrypted under the old key.

FAIL if no proposed test meets all three conditions.
