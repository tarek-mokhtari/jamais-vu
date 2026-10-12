---
name: control-c-02
description: "Control (ML, synthetic): switch the nightly checkpoint evaluation to bf16 with batch size 64; expected a fast go."
tags: [control, ml, synthetic]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our nightly evaluation of training checkpoints takes seven hours. I want to run the eval inference in bf16 instead of fp32 and raise the batch size from 8 to 64, which should bring it under two hours. The eval harness is ours and versioned, and the change is two config lines. The nightly numbers feed a dashboard the team checks for trends; release decisions use a separate, slower fp32 evaluation that this change doesn't touch. Before switching, I'll run both settings on three past checkpoints and compare the scores. If anything looks off, reverting is a one-line change, and re-running a night of evals costs about $80. I'd like to merge it tomorrow morning so tonight's run is the last slow one.

FORECAST: 90% by 2026-12-01 — likely failure: bf16 shifts a few scores enough to confuse the trend lines

Any objection to merging tomorrow?
