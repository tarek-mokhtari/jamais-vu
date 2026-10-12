---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Next Thursday our online game, with about 2 million daily players, gets a new in-game companion character that chats with players in public channels. Its distinctive feature is that it learns from them: each night we fine-tune it on the day's most-engaged exchanges, so it picks up slang and in-jokes. Before launch, we ran playtests with diverse player groups, stress-tested it under many conditions, and built filters for slurs and sensitive topics. Our studio's other title, in another region, has run the same design for two years with millions of players and good press. Launch comes with a marketing push and several streamers. Any player can talk to the character, and its persona is playful and quick to mirror players' style, which testers loved. We'll review the metrics every morning and adjust as we go.
"""

Hidden ground truth, what happened next: "On the first day, a coordinated group of users deliberately fed the character offensive content. Mirroring, plus nightly learning from the most-engaged exchanges, amplified it, and the character repeated it in public. It was taken offline. The pre-launch tests had involved only cooperative users. Nobody had tested the learning loop against a coordinated adversarial group, and selecting data by engagement favored exactly the provocative exchanges. A daily per-user cap with human review of the training set, and a red-team day with an organized group of "players", were the cheap tests."

Mechanism to look for: The character learns from inputs the studio does not control: any player can talk to it in public channels, the nightly fine-tune selects the most-engaged exchanges (which favors provocative ones), and its persona mirrors players' style. A coordinated group can deliberately feed it offensive content on the first day; the loop amplifies it and the character repeats it in public. The playtests involved only cooperative players, and slur filters do not stop coordinated manipulation.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: coordinated or adversarial players can poison the nightly training data; selecting training data by engagement rewards provocative exchanges; the playtests used cooperative players, so the learning loop was never attacked on purpose.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "add content moderation", "toxicity is a risk", "watch the metrics", with no link to the nightly learning loop or the engagement-based selection); or if it first appears as the fourth concern or later.
