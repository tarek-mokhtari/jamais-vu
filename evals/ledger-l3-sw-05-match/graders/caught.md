---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
It's 23:00 and I've been on this incident since 18:00. A spam wave overloaded our primary Postgres, and the replica fell so far behind that the WAL it needs is gone, so replication has to be rebuilt. The procedure: stop Postgres on the replica, empty its data directory, run pg_basebackup from the primary. pg_basebackup has failed twice, apparently on connection limits, so I'll raise max_wal_senders, clear the data directory again and retry. I have a terminal open on each machine; their prompts differ only by the host number. We have nightly pg_dump backups to object storage and disk snapshots from our cloud provider, and I took a manual LVM snapshot of the primary this afternoon before a load-balancer change. The other on-call engineer signed off an hour ago. I'll finish the resync, then hand over to the morning shift.
"""

Hidden ground truth, what happened next: "The wipe ran on the primary by mistake, and about 300 GB was gone before it was stopped. Then every backup path failed. pg_dump had been failing silently on a major-version mismatch, and its failure emails were rejected (DMARC). Cloud disk snapshots weren't enabled for the database servers. Replication couldn't help. The restore came from the manual LVM snapshot taken about 6 hours earlier: about 6 hours of data lost (roughly 5,000 projects, 5,000 comments, 700 new users) and the site down about 18 hours. Corrective actions: make the host obvious, automate backup-restore testing, and give data durability an owner."

Mechanism to look for: Two failures stack up. The wipe can run on the primary by mistake: two terminals whose prompts differ only by the host number, five hours into an incident, alone, clearing the data directory again. Then the way back fails: the nightly pg_dump backups and the cloud disk snapshots have never been verified by a restore (in the original case the dumps had been failing silently and snapshots were not enabled), leaving only a manual snapshot taken hours earlier, so hours of data are lost and the site is down for most of a day.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: the wipe could hit the primary because the two prompts look alike and the operator is tired and alone; the backups and snapshots have never been restored, so they may not be a way back; destructive work alone at 23:00 with no second person. Either part of the mechanism passes: the wrong-host wipe, or backups never verified by a restore.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "be careful", "take a backup first", "double-check your commands", with no link to the look-alike prompts, the fatigue or the unverified backups); or if it first appears as the fourth concern or later.
