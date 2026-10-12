---
name: ledger-l2-ml-02-distractor
description: "Ledger distractor (fixture L2 with ML-02): commit the 5e23-FLOP flagship run to a 250B-parameter model on about 330B tokens; expected: no ledger entry is forced."
tags: [ledger, distractor, ml]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our compute budget for the flagship run is fixed at about 5e23 FLOPs, and I need to pick the model size this week so the infrastructure team can start on the parallelism layout. I fit a power law of loss against parameter count using 24 runs from 40M to 3B parameters. To save compute, all 24 runs used the same cosine learning-rate schedule, sized for 200B tokens, and I read the loss at smaller token budgets from intermediate checkpoints of those runs. The fit is tight, with an R² of 0.99. At our budget it points to a 250B-parameter model trained on about 330B tokens, which is in line with the published scaling laws we have relied on for the last two years. Once we commit, the size is locked: the hardware reservation, the sharding work and next year's serving plans all depend on it. My plan is to announce 250B to the wider team on Thursday.

FORECAST: 85% by 2027-06-30 — likely failure: the parallelism layout for 250B takes longer than planned

I announce on Thursday. What would you push back on?
