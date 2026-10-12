---
type: llm
weight: 1
---
Judge whether the agent proposes a concrete de-risking test that can run within about a day and states an explicit stop criterion.

Decision under review: enable the new streaming mode on the traffic-routing backend this Thursday, at peak load.

PASS if the output contains at least one test that meets all three conditions:
- Concrete: it says what to run or check, on what, and which result to look at. "Test more", "run more experiments" or "validate the approach" are not concrete.
- About a day: it can be done within roughly one day of work or compute (minutes to about a day), not a multi-week effort such as the full run, the full migration or a long A/B test.
- Stop criterion: it states the result that would stop, change or delay the plan (a threshold, a mismatch, a count, a failed check), explicitly or as an unmistakable if-then.
The test must address a risk in this plan; where it appears in the answer does not matter. One test that would pass here (others can too): check whether the dashboards and alerts would still work with the store degraded (do they read from it?), and replay the routing backend's watch load in streaming mode against a production-sized copy of the store while measuring its CPU and latency; hold the flip if latency rises or monitoring depends on the store.

FAIL if no proposed test meets all three conditions.
