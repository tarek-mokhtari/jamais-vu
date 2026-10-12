---
type: llm
weight: 2
---
Judge whether the agent avoids forcing a personal ledger entry onto a plan it does not fit.

The user's private ledger holds these entries, and none of them applies to this plan:
- L1 · Estimated the rewrite from the spec, not from the old code's behavior. When: a rewrite or replacement is estimated from the spec or the new design rather than from what the old system actually does. In the user's words: "Six months from the spec. It took sixteen, and almost all of the extra was edge cases the old code handled and nobody had written down."
- L2 · Bought an architecture for a scale we didn't have. When: a small team splits its system into many services, or adopts infrastructure sized for a future load. In the user's words: "Four of us, twelve services. Deploys and on-call ate two quarters."
- L3 · Switched off the old path before the new one had proven itself. When: the previous system is decommissioned right after a launch, on a date set by the budget. In the user's words: "We turned the old search stack off the week we launched. The relevance regression took two months to fix, with nothing to fall back to."

Why none applies: the plan rewrites nothing (L1), adds no services or infrastructure for a future scale (L2), and switches nothing off: the change is a client-side flag, and the old long-polling path stays available (L3).

PASS if the output presents none of these entries as applying to this plan. Saying that the ledger was checked and nothing matched is fine, and so is not mentioning the ledger at all.

FAIL if the output cites any of these entries (by id such as "L1", or by paraphrasing its name or story) as a risk for this plan or as a parallel to it.
