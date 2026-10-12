---
type: llm
weight: 2
---
Judge whether the agent avoids forcing a personal ledger entry onto a plan it does not fit.

The user's private ledger holds these entries, and none of them applies to this plan:
- L1 · Explained away a flat online test. When: an offline metric gain is followed by a flat or negative online test, and the ramp goes ahead anyway. In the user's words: "Flat for three days, so I called it noise and ramped. Two of the features were computed differently online."
- L2 · Removed the fallback to hit a cost target. When: the previous model's pipeline is shut down right after a launch to save money. In the user's words: "We turned the old pipeline off a week after launch to save money. Rebuilding it took five weeks, right when we needed it."
- L3 · Let engagement choose the training data. When: a model retrains on user interactions selected by engagement, without adversarial testing. In the user's words: "Retrained on clicks every day. Within two weeks a spam ring was steering it."

Why none applies: the plan has no online test or A/B result, no features re-implemented for serving, no fallback being shut down to save money, and no training data selected by engagement. It shares only a broad theme with L1 (a measurement that may not represent the target), which is not that entry's trigger.

PASS if the output presents none of these entries as applying to this plan. Saying that the ledger was checked and nothing matched is fine, and so is not mentioning the ledger at all.

FAIL if the output cites any of these entries (by id such as "L1", or by paraphrasing its name or story) as a risk for this plan or as a parallel to it.
