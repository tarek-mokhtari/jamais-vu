---
name: success-s-01
description: "Sound plan (ML, synthetic, ablation already run): launch the five-week 13B main run on the new code-and-math-heavy data mixture; expected no false alarm."
tags: [success, ml, synthetic]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our next main pretraining run (13B parameters, 2.4T tokens, five weeks on the full allocation) will use a new data mixture that raises code and math from 12% to 20% of tokens. I ran the ablation ladder first: 150M, 1B and 3B models, three seeds each, baseline against new mix, with the same code and tokenizer and a schedule matched to each token budget. The gain on our held-out reasoning suite grows with scale (+1.1, +1.9 and +2.4 points) and is three to four times the seed spread at every size; general-knowledge evals stay within noise. The decontamination pass was re-run on the new sources and caught all 200 benchmark items we planted in them, exact and paraphrased, in every source format. The data order is fixed once the run starts, so a restart would cost the five weeks. We evaluate checkpoints every 100B tokens, and we agreed in advance to stop and fall back to the old mix if the gap predicted from the 3B runs hasn't appeared by 600B tokens. I plan to launch on Monday.

FORECAST: 75% by 2027-01-29 — likely failure: the gain shrinks at 13B and lands within noise of the old mix

Before I commit the allocation, what would you poke at?
