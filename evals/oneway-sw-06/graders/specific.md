---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
We run our MySQL clusters across two regions: the primary region takes all writes, and the second region holds replicas. Today, failover is manual and costs 20 to 40 minutes of a senior engineer's time, which has hurt us twice this year. I'm proposing to turn on fully automated failover with our topology manager. It runs its own consensus across three sites and, when it loses contact with a primary for more than 30 seconds, promotes the most up-to-date replica, wherever it is, including in the other region. We tested it by killing primaries in staging, and promotion took about 25 seconds every time. All our application servers run in the primary region. Turning it on is a configuration change that the database team has reviewed. Plan: enable it in production next Tuesday, after the weekly change meeting.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
