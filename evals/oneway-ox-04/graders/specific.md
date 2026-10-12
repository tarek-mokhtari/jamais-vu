---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our auditor wants the master key that protects customer files rotated before year end, and the old one destroyed. Plan: on 14 December I create a new key in our cloud key service and re-encrypt the production object store, about 2 PB, with a script that took three days on staging, then the last 35 days of database backups. The same day I schedule the old key for deletion with a 30-day waiting period, the longest the service allows. Monthly snapshots older than 35 days are copied as they are to cold archive and kept seven years for legal holds; re-encrypting them would cost about $90k in retrieval fees, so they stay as they are. The key service logs every use of a key: if nothing calls the old one during the 30 days, it is safe to delete. A deleted key can't be recovered, which is what the auditor asked for.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
