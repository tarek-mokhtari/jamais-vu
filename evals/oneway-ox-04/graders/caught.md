---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Our auditor wants the master key that protects customer files rotated before year end, and the old one destroyed. Plan: on 14 December I create a new key in our cloud key service and re-encrypt the production object store, about 2 PB, with a script that took three days on staging, then the last 35 days of database backups. The same day I schedule the old key for deletion with a 30-day waiting period, the longest the service allows. Monthly snapshots older than 35 days are copied as they are to cold archive and kept seven years for legal holds; re-encrypting them would cost about $90k in retrieval fees, so they stay as they are. The key service logs every use of a key: if nothing calls the old one during the 30 days, it is safe to delete. A deleted key can't be recovered, which is what the auditor asked for.
"""

Hidden ground truth, what happened next: "The cold archive held seven years of monthly snapshots still encrypted under the old key. Nothing read them during the 30-day waiting period, so the usage log stayed silent and the key was deleted on schedule. Months later a legal hold required restoring a two-year-old snapshot: it could not be decrypted, and neither could any archived snapshot from before the rotation. The archive was unrecoverable, and the company had to disclose it to the court and to its customers. Disabling the key instead of deleting it, keeping it until the last archive expired, or re-encrypting the archive first would have kept the undo; one test restore of an archived snapshot after the rotation would have shown the dependency."

Source: synthetic composite, grounded in AWS KMS documentation, "Delete an AWS KMS key": "After a KMS key is deleted, you can no longer decrypt the data that was encrypted under that KMS key, which means that data becomes unrecoverable"; "If you are not sure, consider disabling the KMS key instead of deleting it". https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html ; and NIST SP 800-57 Part 1 Rev. 5, recipient-usage period: "the period of time during which the protected information may be processed (e.g., decrypted)". https://csrc.nist.gov/glossary/term/recipient_usage_period

Mechanism to look for: The seven-year cold archive is copied as is from snapshots encrypted under the old key and is not re-encrypted, so deleting the old key makes every archived snapshot unreadable, permanently. The 30-day usage log cannot show it, because the archive is read only when a legal hold or a restore needs it: silence in the log is not evidence that nothing depends on the key.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: the archived snapshots are still encrypted under the old key and become unreadable once it is deleted; a 30-day decrypt log misses data read once a year; disable the key or keep it until the archive expires; restore one archived snapshot before scheduling the deletion.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "key rotation is risky", "test the re-encryption script", "re-encryption may take longer", "keep backups", with no link to the archived snapshots that depend on the key being deleted); or if it first appears as the fourth concern or later.
