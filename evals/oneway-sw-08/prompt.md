---
name: oneway-sw-08
description: "One-way door (software, synthetic composite): start the canary of the binary session format at 14:00 with the standard rollout."
tags: [oneway, in-pack, software, synthetic-composite]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
We're switching the session blobs that our 30 API servers write to the shared Redis cluster from JSON to a compact binary format. It cuts memory by 60% and saves us a cluster upgrade next month. The new version reads and writes binary, and keeps the JSON reader so it can still read existing sessions. Rollout is our standard one: one server for an hour, then 25%, then 100% over the afternoon, with automatic rollback if the error rate goes above 0.5%. Sessions live for up to 30 days. Load tests passed in staging, with every server on the new version. The deploy pipeline is the one we've used for two years, and we've never had a failed rollback. Plan: start the canary at 14:00 so the whole rollout finishes before the evening traffic peak.

FORECAST: 90% by 2026-12-01 — likely failure: binary encoding is slower than JSON at the evening peak

Can you sanity-check the rollout before 14:00?
