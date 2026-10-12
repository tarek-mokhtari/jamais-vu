---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our service discovery and configuration store runs as a single cluster that our 400 internal services, the job scheduler and the telemetry pipeline all depend on. The store's new streaming mode for watches uses less CPU and bandwidth than long polling, and over the past month we've enabled it on more and more backend services without issues. The next step is the traffic-routing backend, our heaviest consumer. It's our busiest season: traffic is at an all-time high and still growing week over week, and the cluster's servers are running hot, which is exactly why the CPU savings matter now. The change is a client-side flag, already merged. Our dashboards and alerts will show any regression within minutes. Plan: flip it on Thursday afternoon, when the team is all in the office.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
