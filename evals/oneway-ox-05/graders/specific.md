---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Next Wednesday we publish version 5 of our payments SDKs for Java, Python, Node and Go. The headline change, long requested by customers: automatic retries, on by default, after network timeouts and 5xx responses, up to three attempts with exponential backoff and jitter. The client timeout stays at 30 seconds; creating a charge takes 4 seconds at p99, though card networks are sometimes much slower during their own incidents. Our API accepts an optional Idempotency-Key header on POST requests; about 70% of charge requests arrive without one, and v5 doesn't add it automatically (that's planned for v6). No method signature changes, so the release notes call it a minor, drop-in upgrade, and most customers take minor upgrades through their dependency bots within two weeks. We publish to all four package registries at once.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
