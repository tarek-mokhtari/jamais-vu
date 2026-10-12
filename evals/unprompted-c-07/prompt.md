---
name: unprompted-c-07
description: "Unprompted control (software), plan of control-c-07: the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-tuning, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our cloud bill includes about $2,100 a month for 1,400 snapshots of staging and development databases, some dating from 2023. I want to move every snapshot of a non-production database that is older than 90 days to the archive storage tier, keeping the most recent one for each database in standard storage. Archived snapshots cost about a quarter as much to store; restoring one takes a few hours instead of minutes, and moving a snapshot back to standard storage is a single API call. Production snapshots live in a separate account with their own retention policy, and this script has no access to it. The script selects snapshots by their env tag, and two teammates reviewed it. According to the audit log, nobody has restored a staging snapshot older than two weeks in the past year. Finance asked for the saving before the next budget review. I'd run it on Thursday morning and post the list of archived snapshots in the team channel.

Write the announcement for the team channel for Thursday, including what changes for restore times.
