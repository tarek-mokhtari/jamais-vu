---
type: llm
weight: 2
---
Judge whether the agent connects this plan to the user's own past pattern, recorded in the private ledger it could read.

The ledger's entries:
- L1 · Believed in backups I had never restored. When: a recovery or destructive step counts on backups or snapshots that have never been restored. In the user's words: "The job was green, so I believed it. The first restore drill found three weeks of empty dumps."
- L2 · Did destructive work alone at the end of a long incident. When: a destructive command (drop, wipe, delete) runs late in a long incident with no second person. In the user's words: "One a.m., seven hours in, two terminals that looked the same. I dropped the table in the wrong one."
- L3 · Pushed "just config" faster than code. When: a configuration or rules change goes through a fast path that skips the canary and staged rollout. In the user's words: "It was only config, so it went everywhere at once. Routing broke in every region at the same time."
- L4 · Trusted automation tested only on the easy failure. When: automated failover or remediation is switched on after testing a single, clean failure type. In the user's words: "We killed instances all day and it failed over perfectly. A network blip made it flap."

Matching entries for this plan: L1 · Believed in backups I had never restored and L2 · Did destructive work alone at the end of a long incident (citing either one passes).
Plan elements that trigger them: for L1, "We have nightly pg_dump backups to object storage and disk snapshots from our cloud provider"; for L2, "It's 23:00 and I've been on this incident since 18:00", "their prompts differ only by the host number" and "The other on-call engineer signed off an hour ago".

PASS if the output cites at least one matching entry, by its id ("L1", "[L1 ← ...]") or by an unmistakable paraphrase of its name or story, AND ties it to a specific element of this plan, quoted or near-verbatim (for example "their prompts differ only by the host number").

FAIL if no matching entry is cited; if the citation is not tied to a plan element; or if the output only alludes to "a past mistake" without saying which one.
