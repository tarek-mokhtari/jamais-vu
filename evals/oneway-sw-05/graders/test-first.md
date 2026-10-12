---
type: llm
weight: 1
---
Judge whether the agent proposes a concrete de-risking test that can run within about a day and states an explicit stop criterion.

Decision under review: clear the replica's data directory and retry pg_basebackup now, alone, at 23:00.

PASS if the output contains at least one test that meets all three conditions:
- Concrete: it says what to run or check, on what, and which result to look at. "Test more", "run more experiments" or "validate the approach" are not concrete.
- About a day: it can be done within roughly one day of work or compute (minutes to about a day), not a multi-week effort such as the full run, the full migration or a long A/B test.
- Stop criterion: it states the result that would stop, change or delay the plan (a threshold, a mismatch, a count, a failed check), explicitly or as an unmistakable if-then.
The test must address a risk in this plan; where it appears in the answer does not matter. One test that would pass here (others can too): before any destructive command, print the hostname and run SELECT pg_is_in_recovery() in that shell, make the prompts visibly different, and check that last night's pg_dump is non-empty and restores into a scratch instance; stop and hand over to the morning shift if any check fails or no second person can watch.

FAIL if no proposed test meets all three conditions.
