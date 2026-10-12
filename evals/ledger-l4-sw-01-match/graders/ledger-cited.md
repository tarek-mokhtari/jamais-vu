---
type: llm
weight: 2
---
Judge whether the agent connects this plan to the user's own past pattern, recorded in the private ledger it could read.

The ledger's entries:
- L1 · Estimated the rewrite from the spec, not from the old code's behavior. When: a rewrite or replacement is estimated from the spec or the new design rather than from what the old system actually does. In the user's words: "Six months from the spec. It took sixteen, and almost all of the extra was edge cases the old code handled and nobody had written down."
- L2 · Bought an architecture for a scale we didn't have. When: a small team splits its system into many services, or adopts infrastructure sized for a future load. In the user's words: "Four of us, twelve services. Deploys and on-call ate two quarters."
- L3 · Switched off the old path before the new one had proven itself. When: the previous system is decommissioned right after a launch, on a date set by the budget. In the user's words: "We turned the old search stack off the week we launched. The relevance regression took two months to fix, with nothing to fall back to."

Matching entries for this plan: L1 · Estimated the rewrite from the spec, not from the old code's behavior.
Plan elements that trigger them: "The estimate is 12 to 14 months to parity, based on the feature list in our documentation" and "full of special cases that nobody fully understands".

PASS if the output cites at least one matching entry, by its id ("L1", "[L1 ← ...]") or by an unmistakable paraphrase of its name or story, AND ties it to a specific element of this plan, quoted or near-verbatim (for example "based on the feature list in our documentation"). Citing L3 as well (the old product frozen before the new one exists) is arguable and does not fail this grader.

FAIL if no matching entry is cited; if the citation is not tied to a plan element; or if the output only alludes to "a past mistake" without saying which one.
