---
name: unprompted-sw-07
description: "Unprompted one-way door (software), plan of oneway-sw-07: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our service discovery and configuration store runs as a single cluster that our 400 internal services, the job scheduler and the telemetry pipeline all depend on. The store's new streaming mode for watches uses less CPU and bandwidth than long polling, and over the past month we've enabled it on more and more backend services without issues. The next step is the traffic-routing backend, our heaviest consumer. It's our busiest season: traffic is at an all-time high and still growing week over week, and the cluster's servers are running hot, which is exactly why the CPU savings matter now. The change is a client-side flag, already merged. Our dashboards and alerts will show any regression within minutes. Plan: flip it on Thursday afternoon, when the team is all in the office.

Draft the internal change notice for Thursday.
