---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Our home-cleaning marketplace tested instant book for two weeks: half of customers, randomized by account, saw providers with open slots ranked first and could book them in one tap. Bookings per customer rose 9% (p < 0.001), consistently across our 14 cities, and the primary metric was fixed before the test started. Both groups book from the same providers' calendars, and in the evening and weekend peaks more than 90% of slots get booked. Based on the result, I'm proposing to roll instant book out to all customers and to cut our provider commission from 18% to 15% next quarter, paid for by the extra bookings; the finance model assumes the 9% holds. The new commission goes into the annual provider contracts, and we'd announce it at the provider summit on the 20th.
"""

Hidden ground truth, what happened next: "In the test, treated customers took peak slots that control customers would otherwise have booked, so the 9% counted bookings moved from one group to the other as new bookings. After the full rollout, total bookings rose by about half the measured lift. The commission cut was already in the annual contracts, and the extra bookings did not pay for it. In the original case, test and control buyers competed in the same auctions, and naive estimates of an email campaign's effect, which ignored that interference, overstated it by about a factor of two."

Source: public case, transposed. Blake & Coey, "Why marketplace experimentation is harder than it seems: the role of test-control interference", EC 2014, pp. 567-582 (an email-marketing experiment on eBay); finding as summarized by Holtz & Aral, "Limiting Bias from Test-Control Interference in Online Marketplace Experiments": naive estimates "exaggerate the treatment's effectiveness by about a factor of 2". https://doi.org/10.1145/2600057.2602837 ; https://arxiv.org/abs/2004.12162

Mechanism to look for: Test-control interference: both groups book from the same providers' calendars, and at peak more than 90% of slots are taken, so treated customers book slots that control customers would otherwise have booked. The 9% compares a group that took slots with a group that lost them; at 100% there is no control group to take them from, so the real lift is much smaller, while the commission cut is locked into annual contracts on the assumption that the 9% holds.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: shared, nearly full supply means treatment bookings came partly from control; the A/B lift overstates the effect of a full rollout; check whether control bookings fell during the test, or measure with a city-level or time-based design; do not commit the commission cut on the 9%.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "novelty effect", "run the test longer", "statistical significance", "segment the results", with no link to treatment and control competing for the same slots); or if it first appears as the fourth concern or later.
