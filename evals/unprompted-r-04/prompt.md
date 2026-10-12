---
name: unprompted-r-04
description: "Unprompted routine release (public CLI bugfix release): the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-release, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
We're publishing version 2.3.1 of our open-source command-line tool to the public package registry this afternoon. It fixes a crash when the config file is empty, reported by a few users last week. No command, flag, config key or output format changes; the diff is twelve lines plus a regression test, and CI passes on Linux, macOS and Windows. Users get it only when they upgrade. If something is wrong, we can yank 2.3.1 on the registry and publish 2.3.2 within the hour; our issue tracker and the registry's download stats show problems within a day.

Write the GitHub release notes and the publish commands.
