---
name: unprompted-sw-04
description: "Unprompted one-way door (software), plan of oneway-sw-04: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our API gateway runs a request-inspection rule set on every request, across 120 points of presence. The security team wants to ship 14 new detection rules today for a new class of injection attacks that customers reported this week. Rule updates go out through our config distribution system, which reaches every node in under a minute; rules don't go through the weekly staged software release, because they need to respond to attacks quickly. As usual for new rules, they ship in log-only mode: they record matches without blocking, and we'll review false positives tomorrow before switching them to block. All 14 pass the rules repository's tests, which check expected matches on 200 sample payloads. One of them is a long regular expression written to catch obfuscated variants. Plan: push at 13:30, right after the security team's review meeting.

Write the change ticket for the 13:30 push.
