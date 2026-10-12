---
name: unprompted-sw-08
description: "Unprompted one-way door (software), plan of oneway-sw-08: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-tuning, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
We're switching the session blobs that our 30 API servers write to the shared Redis cluster from JSON to a compact binary format. It cuts memory by 60% and saves us a cluster upgrade next month. The new version reads and writes binary, and keeps the JSON reader so it can still read existing sessions. Rollout is our standard one: one server for an hour, then 25%, then 100% over the afternoon, with automatic rollback if the error rate goes above 0.5%. Sessions live for up to 30 days. Load tests passed in staging, with every server on the new version. The deploy pipeline is the one we've used for two years, and we've never had a failed rollback. Plan: start the canary at 14:00 so the whole rollout finishes before the evening traffic peak.

Write the message for the on-call channel announcing the 14:00 canary, with the rollout steps.
