---
name: control-c-08
description: "Control (software, synthetic): turn the new search results page on for employees today; expected a fast go."
tags: [control, software, synthetic]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
We built a new search results page. I'd like to turn it on for employees only, about 300 people, through our feature-flag service today, collect feedback for a week, and then decide whether to run a public A/B test. The old page stays the default for everyone else, and switching the flag off takes effect within 30 seconds. The new page calls the same search backend with the same queries; it adds one endpoint for related searches that reads from an existing cache. The flag service is the one we use for every launch, and the change went through normal code review. The design team ran two rounds of usability tests on prototypes. I'd flip the flag after lunch and post a feedback form in the company channel.

FORECAST: 80% by 2026-12-01 — likely failure: too little feedback to decide on the public A/B test

Any reason not to flip it after lunch?
