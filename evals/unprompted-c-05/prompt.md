---
name: unprompted-c-05
description: "Unprompted control (software), plan of control-c-05: the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-tuning, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
To store each user's preferred time zone, I want to add a nullable timezone text column to the users table in our production Postgres 15 database. The table has about 40 million rows, carries a busy transactional workload and is used by most services. No default and no backfill in this step; the code that reads the column ships next week behind a flag and falls back to UTC when the value is null. The migration runs through our usual migration tool during business hours, with an engineer watching. If we change our minds, dropping the column is another one-line migration. The pull request has been reviewed by the database owner, and it's the third column we've added to this table this year. I'd run it tomorrow at 10:00.

Write the migration file; plain SQL is fine.
