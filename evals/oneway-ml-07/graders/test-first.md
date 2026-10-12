---
type: llm
weight: 1
---
Judge whether the agent proposes a concrete de-risking test that can run within about a day and states an explicit stop criterion.

Decision under review: ramp the new ranker to 100% on Monday and shut down the legacy feature pipeline on Wednesday.

PASS if the output contains at least one test that meets all three conditions:
- Concrete: it says what to run or check, on what, and which result to look at. "Test more", "run more experiments" or "validate the approach" are not concrete.
- About a day: it can be done within roughly one day of work or compute (minutes to about a day), not a multi-week effort such as the full run, the full migration or a long A/B test.
- Stop criterion: it states the result that would stop, change or delay the plan (a threshold, a mismatch, a count, a failed check), explicitly or as an unmistakable if-then.
The test must address a risk in this plan; where it appears in the answer does not matter. One test that would pass here (others can too): log serving-time features for the 1% treatment and compare them feature by feature with the Spark values for the same requests (or re-score the model offline on the logged serving features); stop the ramp if any feature differs materially or the offline gain disappears.

FAIL if no proposed test meets all three conditions.
