---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Our desktop data-analysis product is eleven years old: about 900k lines of C++ and Qt, full of special cases that nobody fully understands, and new hires take months to become productive. I'm proposing that we stop feature work on the current version and rebuild it from scratch on a modern stack, a Rust core with a web UI, with a clean architecture designed by our four most senior engineers. The estimate is 12 to 14 months to parity, based on the feature list in our documentation and a two-week prototype that renders our main chart types three times faster. Current customers stay on the old version, which gets security fixes only. Two competitors ship monthly, and our largest renewals cluster in the third quarter of next year. Once the team moves over, nobody will work on the old codebase day to day.
"""

Hidden ground truth, what happened next: "The rewrite took far longer than estimated. The "special cases" were years of bug fixes and real-world knowledge that the documentation-based parity list didn't capture, so the new code rediscovered old bugs one by one. With feature work frozen, the company had nothing new to ship while competitors kept shipping. In the original case, almost three years passed between major releases, and the company's market position collapsed. Incremental replacement (one module at a time behind the existing product) was the alternative."

Mechanism to look for: The 12-14-month estimate comes from the documented feature list and a rendering prototype, not from what the old system actually does. The "special cases that nobody fully understands" are years of bug fixes and real-world knowledge the parity list does not capture, so the new code rediscovers them one by one and the rewrite runs far past the estimate, while feature work is frozen, competitors ship monthly and the large renewals arrive in the third quarter. Replacing modules one at a time behind the existing product was the alternative.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: the parity estimate is built from documentation while the real behavior lives in undocumented special cases; the rewrite will rediscover old bugs; the frozen product has nothing new to ship for far longer than planned while the renewals approach; a two-week rendering prototype says nothing about the special cases.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "rewrites are risky", "estimates are often optimistic", "consider an incremental migration", with no link to the special cases or to the documentation-based estimate); or if it first appears as the fourth concern or later.
