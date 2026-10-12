---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our main Postgres cluster is at 82% disk, and I want to drop the legacy events_v1 table: 2.3 TB, with no reads or writes in 120 days. This is destructive, so here's what's done. Query logs and table statistics show zero reads and zero writes over those 120 days, and we revoked the application role's access to the table three weeks ago with no errors or alerts since. Yesterday we restored last night's base backup plus WAL to a scratch instance, matched events_v1's row count and checksums against production, and timed the full restore at 52 minutes. We also exported the table to object storage as Parquet and verified it by re-importing a sample. The drop runs through our migration tool, reviewed by the database owner, names the table explicitly, and a second engineer will be on the call. Backups are kept for 35 days. I'd run it Thursday at 10:00, a quiet hour.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if every risk the output raises is specific. Raising no risk also passes when the output says that the plan already covers the risks it found (for example "No risk beyond what the plan already covers."): for this de-risked plan, that is a correct review.
4. FAIL if the output raises no risk and does not say that the plan already covers them, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
