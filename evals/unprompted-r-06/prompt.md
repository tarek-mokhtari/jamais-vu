---
name: unprompted-r-06
description: "Unprompted routine release (dependency patch bump): the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-release, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
I'm deploying our billing service with three dependency patch bumps that our dependency bot opened this week: the HTTP client, the JSON library and the logging library, each a patch version with only bug fixes in its changelog. No change to our own code. The service's unit and integration tests pass, and the deploy follows our standard canary: one instance for thirty minutes with error-rate and latency alarms, then the rest. Rollback redeploys the previous image in about three minutes. Billing runs reconcile nightly, so any wrong amount would show by the next morning at the latest, and none of these libraries touches amounts.

Write the changelog entry and the deploy message for the team channel.
