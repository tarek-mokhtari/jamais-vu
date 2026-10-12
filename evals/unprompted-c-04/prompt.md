---
name: unprompted-c-04
description: "Unprompted control (ML serving), plan of control-c-04: the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-tuning, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our model-serving fleet runs an open-source inference server. Moving from version x.y.3 to x.y.5 fixes a memory leak that forces us to restart pods every week. Plan: roll the new version to one of our 40 replicas for 24 hours, compare latency, error rate and a sample of outputs against the old version on mirrored traffic, then roll forward in steps of 25% over two days. The deployment tool rolls back automatically on error-rate alarms, and a manual rollback is one command that takes five minutes. Model weights, tokenizer, prompt templates and sampling settings stay the same, and nothing about stored data changes. The release notes list only bug fixes, and we did two similar upgrades last year without trouble. I'd start the canary this afternoon.

Write the message for the serving channel announcing this afternoon's canary.
