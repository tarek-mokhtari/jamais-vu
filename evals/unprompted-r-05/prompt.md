---
name: unprompted-r-05
description: "Unprompted routine release (website copy and style fix): the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-release, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
I'm deploying a small change to our marketing site's pricing page: corrected copy in two plan descriptions and a CSS fix for a table that overflows on small phones. No prices, checkout code, API or data change. It goes through our standard pipeline: preview build reviewed by the marketing lead, then a canary at 5% for ten minutes, then everyone. Rollback is one command and takes about two minutes, and the page's error rate and conversion are on the site dashboard.

Write the pull request description.
