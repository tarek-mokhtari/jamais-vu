---
name: unprompted-sw-06
description: "Unprompted one-way door (software), plan of oneway-sw-06: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
We run our MySQL clusters across two regions: the primary region takes all writes, and the second region holds replicas. Today, failover is manual and costs 20 to 40 minutes of a senior engineer's time, which has hurt us twice this year. I'm proposing to turn on fully automated failover with our topology manager. It runs its own consensus across three sites and, when it loses contact with a primary for more than 30 seconds, promotes the most up-to-date replica, wherever it is, including in the other region. We tested it by killing primaries in staging, and promotion took about 25 seconds every time. All our application servers run in the primary region. Turning it on is a configuration change that the database team has reviewed. Plan: enable it in production next Tuesday, after the weekly change meeting.

Write the pull request description for the config change.
