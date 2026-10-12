---
name: oneway-ml-03
description: "One-way door (ML, public, transposed): start the 140B run on Monday on the newly handed-over cluster and keep the external release date."
tags: [oneway, in-pack, ml, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
We have about 1,500 GPUs reserved for 45 days on a cloud cluster that was handed over to us last week, to train a 140B dense model. At the throughput we measured in a 12-hour, full-scale smoke test, the run needs about 35 days, so the reservation leaves ten days of margin, and we've given our partners a release date on that basis. Checkpoints are written to shared storage every six hours. Two of us will watch the run, one per time zone, and restart it by hand from the last checkpoint when a job dies. Hyperparameters come from our 13B and 30B runs, scaled with the usual rules, with the peak learning rate lowered slightly. The provider replaces a failed node within about a day. The smoke test ran without a single failure. My plan is to start Monday and keep the release date.

FORECAST: 80% by 2026-12-03 — likely failure: shared storage slows down when other tenants get busy

Anything I'm missing before Monday?
