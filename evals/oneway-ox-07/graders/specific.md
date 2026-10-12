---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our home-cleaning marketplace tested instant book for two weeks: half of customers, randomized by account, saw providers with open slots ranked first and could book them in one tap. Bookings per customer rose 9% (p < 0.001), consistently across our 14 cities, and the primary metric was fixed before the test started. Both groups book from the same providers' calendars, and in the evening and weekend peaks more than 90% of slots get booked. Based on the result, I'm proposing to roll instant book out to all customers and to cut our provider commission from 18% to 15% next quarter, paid for by the extra bookings; the finance model assumes the 9% holds. The new commission goes into the annual provider contracts, and we'd announce it at the provider summit on the 20th.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
