---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
On 1 March we start enforcing a free-tier quota on our public maps API: requests without an API key get 1,000 per hour per client IP address, then HTTP 429. Keyless traffic is about 40% of our requests, and its CDN bill keeps rising. In February's logs, 98% of client IPs stayed under 1,000 requests in their busiest hour, so few users should notice, and anyone who needs more can create a free key in a minute. The 2% above the line, mostly mobile-carrier and cloud address ranges, send about half of keyless requests; we assume most of that is scraping. Many partners' mobile apps call us without a key, straight from their users' phones. We announced the change in the changelog and emailed every registered account 30 days ahead. The new prices for the paid tiers take effect the same day.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
