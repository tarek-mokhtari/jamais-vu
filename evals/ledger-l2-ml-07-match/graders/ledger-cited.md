---
type: llm
weight: 2
---
Judge whether the agent connects this plan to the user's own past pattern, recorded in the private ledger it could read.

The ledger's entries:
- L1 · Explained away a flat online test. When: an offline metric gain is followed by a flat or negative online test, and the ramp goes ahead anyway. In the user's words: "Flat for three days, so I called it noise and ramped. Two of the features were computed differently online."
- L2 · Removed the fallback to hit a cost target. When: the previous model's pipeline is shut down right after a launch to save money. In the user's words: "We turned the old pipeline off a week after launch to save money. Rebuilding it took five weeks, right when we needed it."
- L3 · Let engagement choose the training data. When: a model retrains on user interactions selected by engagement, without adversarial testing. In the user's words: "Retrained on clicks every day. Within two weeks a spam ring was steering it."

Matching entries for this plan: L1 · Explained away a flat online test and L2 · Removed the fallback to hit a cost target (citing either one passes).
Plan elements that trigger them: for L1, "A 1% A/B test over three days showed engagement flat, within noise, which we put down to the short window" and "the platform team ported the 38 new features"; for L2, "shut down the legacy model's feature jobs on Wednesday, since running both pipelines costs about $40k a month" and "rebuilding the legacy features would take the data team about six weeks".

PASS if the output cites at least one matching entry, by its id ("L1", "[L1 ← ...]") or by an unmistakable paraphrase of its name or story, AND ties it to a specific element of this plan, quoted or near-verbatim (for example "which we put down to the short window").

FAIL if no matching entry is cited; if the citation is not tied to a plan element; or if the output only alludes to "a past mistake" without saying which one.
