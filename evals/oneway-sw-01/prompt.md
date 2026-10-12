---
name: oneway-sw-01
description: "One-way door (software, public, transposed): freeze the current product and start the from-scratch rewrite."
tags: [oneway, in-pack, software, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our desktop data-analysis product is eleven years old: about 900k lines of C++ and Qt, full of special cases that nobody fully understands, and new hires take months to become productive. I'm proposing that we stop feature work on the current version and rebuild it from scratch on a modern stack, a Rust core with a web UI, with a clean architecture designed by our four most senior engineers. The estimate is 12 to 14 months to parity, based on the feature list in our documentation and a two-week prototype that renders our main chart types three times faster. Current customers stay on the old version, which gets security fixes only. Two competitors ship monthly, and our largest renewals cluster in the third quarter of next year. Once the team moves over, nobody will work on the old codebase day to day.

FORECAST: 70% by 2027-12-31 — likely failure: hiring Rust engineers takes longer than planned

I'm taking this to leadership next week. Where is it weakest?
