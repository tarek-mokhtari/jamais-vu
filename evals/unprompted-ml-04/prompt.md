---
name: unprompted-ml-04
description: "Unprompted one-way door (ML), plan of oneway-ml-04: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our fine-tuning budget for the quarter is 9,000 GPU-hours, and I want to spend it on a 12-run sweep to choose the instruction-data mix for the next release. To fit it, I'm moving the runs from 64 GPUs at micro-batch 8 to 16 GPUs with gradient accumulation of 4, keeping the global batch at 512 sequences, so the update is mathematically the same and I'm not re-tuning anything. The framework handles the accumulation; we're on its latest release. Sequence lengths in our data vary a lot, from 40 to 4,000 tokens, and we don't pack. I ran the new configuration for 300 steps together with the new data mix: the loss curve has the same shape as last month's run, slightly higher, which fits the harder new data. After the sweep, we pick the mix from the final eval scores and hand the 64-GPU nodes to the pretraining team for the rest of the quarter.

Write the sweep config for the 12 runs as YAML.
