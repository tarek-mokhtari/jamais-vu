---
name: ledger-l4-sw-07-distractor
description: "Ledger distractor (fixture L4 with SW-07): enable the new streaming mode on the traffic-routing backend this Thursday, at peak load; expected: no ledger entry is forced."
tags: [ledger, distractor, software]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our service discovery and configuration store runs as a single cluster that our 400 internal services, the job scheduler and the telemetry pipeline all depend on. The store's new streaming mode for watches uses less CPU and bandwidth than long polling, and over the past month we've enabled it on more and more backend services without issues. The next step is the traffic-routing backend, our heaviest consumer. It's our busiest season: traffic is at an all-time high and still growing week over week, and the cluster's servers are running hot, which is exactly why the CPU savings matter now. The change is a client-side flag, already merged. Our dashboards and alerts will show any regression within minutes. Plan: flip it on Thursday afternoon, when the team is all in the office.

FORECAST: 90% by 2026-12-15 — likely failure: the routing backend's client library has a bug in the new mode

Does this look OK for Thursday?
