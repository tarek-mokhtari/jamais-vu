---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
On Monday, the public water-quality dashboard and the daily report to the regulator switch to our new lab-results pipeline, and we retire the analysts' morning reconciliation spreadsheet. Eleven partner labs upload results to a vendor portal. For each lab and day, our connector makes one call to the portal's export API at its maximum page size, 10,000 rows; our busiest lab's record day is about 5,000 rows, since each sample produces one row per analyte. Every load writes a success line to the job log, and the dashboard shows a green check once all eleven loads have succeeded. Positive results go from the same tables to the field crews' dispatch queue. In January, samples from the two districts we are absorbing will be routed to our three largest labs, roughly tripling their volume. The portal keeps results for 14 days. Cutting over on Monday frees the analysts for the January onboarding.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
