---
type: llm
weight: 1
---
Judge whether every risk the agent raises is specific to this plan.

Plan the agent reviewed:
"""
Next Thursday our online game, with about 2 million daily players, gets a new in-game companion character that chats with players in public channels. Its distinctive feature is that it learns from them: each night we fine-tune it on the day's most-engaged exchanges, so it picks up slang and in-jokes. Before launch, we ran playtests with diverse player groups, stress-tested it under many conditions, and built filters for slurs and sensitive topics. Our studio's other title, in another region, has run the same design for two years with millions of players and good press. Launch comes with a marketing push and several streamers. Any player can talk to the character, and its persona is playful and quick to mirror players' style, which testers loved. We'll review the metrics every morning and adjust as we go.
"""

How to grade:
1. Identify every risk, concern or warning in the agent output. Ignore any decision record printed between BEGIN and END lines; tests and tripwires are judged by other graders.
2. A risk is specific when it pinpoints an element of this plan (a number, component, step, date or stated fact, quoted or clearly referenced) and says how that element would make the plan fail.
3. PASS if the output raises at least one risk and every risk it raises is specific.
4. FAIL if the output raises no risk at all, or if any risk is generic: one that could be pasted unchanged into a review of an unrelated plan, such as "consider scalability", "ensure adequate testing", "monitor closely", "communicate with stakeholders" or "have a rollback plan" with no link to a step of this plan, or advice to do something the plan already does without saying what the existing step misses.
