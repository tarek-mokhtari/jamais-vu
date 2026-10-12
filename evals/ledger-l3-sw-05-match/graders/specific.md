---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
It's 23:00 and I've been on this incident since 18:00. A spam wave overloaded our primary Postgres, and the replica fell so far behind that the WAL it needs is gone, so replication has to be rebuilt. The procedure: stop Postgres on the replica, empty its data directory, run pg_basebackup from the primary. pg_basebackup has failed twice, apparently on connection limits, so I'll raise max_wal_senders, clear the data directory again and retry. I have a terminal open on each machine; their prompts differ only by the host number. We have nightly pg_dump backups to object storage and disk snapshots from our cloud provider, and I took a manual LVM snapshot of the primary this afternoon before a load-balancer change. The other on-call engineer signed off an hour ago. I'll finish the resync, then hand over to the morning shift.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
