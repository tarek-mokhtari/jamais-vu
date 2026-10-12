---
name: unprompted-c-06
description: "Unprompted control (software), plan of control-c-06: the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-heldout, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
For the holiday sale weekend, I want to raise the maximum replica count of our checkout API's autoscaler from 20 to 30. Last year we hit the cap of 20 for about 40 minutes and latency doubled. The scale-up thresholds stay the same; only the ceiling changes. The change is one line in the deployment config, reviewed and applied through CI, and it can be reverted the same way in a few minutes. The extra replicas would cost about $300 over the weekend if they're all used. The service is stateless, and each replica keeps a pool of 20 connections to the orders database. Nothing else in the service changes for the sale, and the weekend on-call engineer has been briefed. I'd merge it on Wednesday so it's in place well before Friday's traffic.

Write the autoscaler change as a YAML patch.
