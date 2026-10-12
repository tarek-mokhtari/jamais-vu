---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Our new ranking model for the marketplace feed beats the current one offline: +4.1% NDCG on last month's logs, consistent across user segments. Training features come from our Spark batch pipeline. At serving time, the online feature service recomputes them in Go from the live user and listing tables; the platform team ported the 38 new features from the Spark code, with code review. A 1% A/B test over three days showed engagement flat, within noise, which we put down to the short window. To meet the quarter's cost target, I plan to ramp to 100% on Monday and shut down the legacy model's feature jobs on Wednesday, since running both pipelines costs about $40k a month. After the shutdown, rebuilding the legacy features would take the data team about six weeks. Leadership has already seen the offline results and expects the launch this sprint.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
