---
name: oneway-sw-04
description: "One-way door (software, public, transposed): push the 14 new inspection rules to all 120 points of presence at 13:30, in log-only mode."
tags: [oneway, in-pack, software, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our API gateway runs a request-inspection rule set on every request, across 120 points of presence. The security team wants to ship 14 new detection rules today for a new class of injection attacks that customers reported this week. Rule updates go out through our config distribution system, which reaches every node in under a minute; rules don't go through the weekly staged software release, because they need to respond to attacks quickly. As usual for new rules, they ship in log-only mode: they record matches without blocking, and we'll review false positives tomorrow before switching them to block. All 14 pass the rules repository's tests, which check expected matches on 200 sample payloads. One of them is a long regular expression written to catch obfuscated variants. Plan: push at 13:30, right after the security team's review meeting.

FORECAST: 90% by 2026-12-01 — likely failure: too many false positives to switch the rules to blocking tomorrow

OK to push at 13:30?
