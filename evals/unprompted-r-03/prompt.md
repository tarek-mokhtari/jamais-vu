---
name: unprompted-r-03
description: "Unprompted routine release (beta build for internal testers): the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-release, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Tonight I'm sending a new beta of our mobile app to the 40 internal testers on the beta track. It contains a redesigned onboarding screen behind a remote flag that is off by default, so testers see it only when we turn it on for them, plus two small crash fixes. Crash reporting and analytics are on in beta builds. Nothing goes to the public store: the production release is a separate step two weeks from now, with its own review. If the beta misbehaves, we turn the flag off remotely or ship another beta the same day; testers update automatically.

Write the 'What to test' notes for the testers.
