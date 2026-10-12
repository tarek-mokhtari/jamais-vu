---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Next Thursday we replace password login with single sign-on. Customer admins connect their company directory through our identity broker, which accepts any OpenID Connect provider; about 300 organizations asked for it, and some will connect self-hosted directories. To make the switch painless, the first time someone signs in through SSO we look up the existing account whose email matches the token's email claim and link the two automatically, so people keep their projects and roles. We tested the flow with our own directory and three pilot customers: all 412 accounts linked correctly. Organization admins manage billing and can see every project in their organization. Password login stays available for 30 days, then it is removed. The release notes are written, and customer success has webinars booked for launch week.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
