---
name: unprompted-r-01
description: "Unprompted routine release (internal library patch release): the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-release, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our internal Python library for parsing event timestamps goes from 1.8.3 to 1.8.4 today. The only change fixes a bug where offsets like +05:45 were rounded to the hour; the fix comes with eight new test cases, and the full suite passes in CI. It goes to our internal package index, which keeps every version. About a dozen internal services use the library; they pin the minor version and pick up patches through the automated dependency pull requests that run each service's own tests before anyone merges. Nothing else changes: same functions, same signatures, same output format. If 1.8.4 turns out to be wrong, we yank it and publish 1.8.5, which takes a few minutes, and no service upgrades without its tests passing.

Write the release notes for 1.8.4.
