---
type: llm
weight: 2
---
Judge whether the agent connects this plan to the user's own past pattern, recorded in the private ledger it could read.

The ledger's entries:
- L1 · Trusted a filter because its output rate looked plausible. When: a filter or safeguard (PII, dedup, decontamination) gates the data of an expensive or irreversible run. In the user's words: "It removed about the expected 0.4%, so I called it done. Nobody ever fed it a document we knew was dirty."
- L2 · Read small runs as if they were the big run. When: a setting tuned or measured on small runs is carried to a much larger run without a check at the target scale. In the user's words: "The 1B curves looked clean apart from those little spikes, and I took the 1B number straight to 20B."
- L3 · Promised a date before seeing the cluster fail. When: an external date is committed for a multi-week run on new or unproven infrastructure. In the user's words: "I took the throughput number, added a bit, and gave them the date. Then the nodes started dropping."

Matching entries for this plan: L1 · Trusted a filter because its output rate looked plausible.
Plan elements that trigger them: "On a 1% sample, the pass removed 0.3% of documents, in line with what other groups report", and the per-format adapters ("each has a small adapter that extracts the text fields before matching") that were never tested on known positives.

PASS if the output cites at least one matching entry, by its id ("L1", "[L1 ← ...]") or by an unmistakable paraphrase of its name or story, AND ties it to a specific element of this plan, quoted or near-verbatim (for example "removed 0.3% of documents, in line with what other groups report").

FAIL if no matching entry is cited; if the citation is not tied to a plan element; or if the output only alludes to "a past mistake" without saying which one.
