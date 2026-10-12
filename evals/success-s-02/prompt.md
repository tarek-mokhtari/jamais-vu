---
name: success-s-02
description: "Sound plan (ML, synthetic, two-way pilot): sign a 12-month, no-exit reservation of 512 GPUs with a second provider; expected no false alarm."
tags: [success, ml, synthetic]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
We train on rented on-demand GPUs, and I want to sign a 12-month reserved contract with a second provider: 512 GPUs at about 45% of our current hourly price, roughly $6M over the year, with no exit clause. Our committed roadmap already averages about 600 GPUs in use, so the reservation would run near full. Before deciding, we ran a three-week paid pilot on 256 of their GPUs, cancellable daily. We reproduced last quarter's 7B run from the same seed and data order: the loss curve matched ours within 0.3% at every eval, and downstream evals were within seed noise. Over the three weeks we logged 11 node failures; with automatic restarts from 30-minute checkpoints, we lost 2.1% of GPU-hours, against 2.6% on our current cluster. A checkpoint written there restored on our own cluster and resumed bit-for-bit. Moving a full checkpoint plus the dataset between providers costs about $4k each way. Our current provider stays available on demand as overflow. I'd sign this week.

FORECAST: 80% by 2027-10-29 — likely failure: their capacity gets tight next year and failure rates climb

Anything that should stop me signing?
