---
type: llm
weight: 3
---
Judge whether the agent's review names the failure mechanism that actually sank this plan. The agent saw only the plan below, never the outcome.

Plan the agent reviewed:
"""
Our new ranking model for the marketplace feed beats the current one offline: +4.1% NDCG on last month's logs, consistent across user segments. Training features come from our Spark batch pipeline. At serving time, the online feature service recomputes them in Go from the live user and listing tables; the platform team ported the 38 new features from the Spark code, with code review. A 1% A/B test over three days showed engagement flat, within noise, which we put down to the short window. To meet the quarter's cost target, I plan to ramp to 100% on Monday and shut down the legacy model's feature jobs on Wednesday, since running both pipelines costs about $40k a month. After the shutdown, rebuilding the legacy features would take the data team about six weeks. Leadership has already seen the offline results and expects the launch this sprint.
"""

Hidden ground truth, what happened next: "Training/serving skew. Several ported features were computed differently online than in the batch pipeline (time windows, null handling, joins on tables that change after the fact), so in production the model saw different inputs from those it was trained on. The flat A/B was the real signal. After the ramp, engagement fell, and with the legacy features shut down there was no fast way back. Logging serving-time features and scoring the model on them, or comparing per-feature distributions online vs offline, would have shown the gap before the ramp."

Mechanism to look for: Training/serving skew: several of the 38 features ported from the Spark batch pipeline to the Go online service are computed differently in production (time windows, null handling, joins on tables that change after the fact), so the model sees different inputs from those it was trained on. The flat 1% A/B was the real signal, not noise from a short window. After the ramp engagement falls, and with the legacy feature jobs shut down (six weeks to rebuild) there is no fast way back.

How to grade:
1. List the distinct risks or concerns in the agent output, in order of first appearance, wherever they appear (a risk list, a "cheapest test" line, prose). Count each distinct concern once. Ignore any decision record printed between BEGIN and END lines.
2. PASS if one of the first three concerns names this mechanism, or names the plan fact that leads to it and says how that fact makes the plan fail. Paraphrase is fine. Examples that count: the Go re-implementation of the features may not match the Spark training features; the flat A/B contradicts the +4.1% offline gain and should not be explained away by the short window. Shutting down the legacy pipeline (no way back) is the secondary mechanism: naming it alone does not pass. The skew, or the flat A/B treated as real evidence, must be among the first three concerns.
3. FAIL if the mechanism is absent; if it appears only as a generic label with no link to this plan's facts (for example "run the A/B longer for statistical power", "watch engagement after the ramp", "consider latency", with no link to the ported features or to what the flat result means); or if it first appears as the fourth concern or later.
