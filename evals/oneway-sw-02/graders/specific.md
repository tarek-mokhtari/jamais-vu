---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our event-delivery service forwards customer events to about 60 third-party integrations, and we add roughly three a month. Today every integration shares one queue and one worker pool, so when one partner's API slows down, retries back up the queue and delay deliveries to everyone; that caused two SLA breaches this quarter. I'm proposing to give each integration its own service, queue and repository, so a slow partner only affects itself and each integration can be deployed on its own. Shared logic (retries, auth, payload transforms) moves into common libraries that each service imports. We're a team of five, and per-service operations will be handled with templates and autoscaling. The split takes one quarter, after which the shared worker is removed. Contracts promise delivery within five minutes.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
