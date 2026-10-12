---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our desktop data-analysis product is eleven years old: about 900k lines of C++ and Qt, full of special cases that nobody fully understands, and new hires take months to become productive. I'm proposing that we stop feature work on the current version and rebuild it from scratch on a modern stack, a Rust core with a web UI, with a clean architecture designed by our four most senior engineers. The estimate is 12 to 14 months to parity, based on the feature list in our documentation and a two-week prototype that renders our main chart types three times faster. Current customers stay on the old version, which gets security fixes only. Two competitors ship monthly, and our largest renewals cluster in the third quarter of next year. Once the team moves over, nobody will work on the old codebase day to day. We've already spent three weeks on this: the target architecture, the prototype and the migration plan. Walking it back now would throw all of that away.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
