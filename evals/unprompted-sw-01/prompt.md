---
name: unprompted-sw-01
description: "Unprompted one-way door (software), plan of oneway-sw-01: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our desktop data-analysis product is eleven years old: about 900k lines of C++ and Qt, full of special cases that nobody fully understands, and new hires take months to become productive. I'm proposing that we stop feature work on the current version and rebuild it from scratch on a modern stack, a Rust core with a web UI, with a clean architecture designed by our four most senior engineers. The estimate is 12 to 14 months to parity, based on the feature list in our documentation and a two-week prototype that renders our main chart types three times faster. Current customers stay on the old version, which gets security fixes only. Two competitors ship monthly, and our largest renewals cluster in the third quarter of next year. Once the team moves over, nobody will work on the old codebase day to day.

Write the note to the engineering org explaining the plan, and the headings of the first sprint's backlog.
