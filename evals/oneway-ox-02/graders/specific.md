---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Next Tuesday our creator analytics page and the partner reporting API switch their headline number from total plays to a new metric, average watch time, and sales starts quoting it in the media kit for advertisers. It is total watch time divided by the number of qualified views. Total watch time comes from the playback events table, which logs every play; qualified views come from the views rollup, which counts plays of 3 seconds or more, our standard view definition since 2019. Both tables already feed billing, so they are well tested. On last month's data the new metric runs about 70% above the old time-per-play figure, which we put down to the 3-second rule screening out accidental autoplays. Advertisers will set next year's budgets with it, comparing us with other platforms. Partners' dashboards pull the API nightly, and our partner terms require 90 days' notice to change a published definition.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
