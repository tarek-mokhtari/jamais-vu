---
name: unprompted-ox-05
description: "Unprompted one-way door (API platform), plan of oneway-ox-05: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-tuning, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Next Wednesday we publish version 5 of our payments SDKs for Java, Python, Node and Go. The headline change, long requested by customers: automatic retries, on by default, after network timeouts and 5xx responses, up to three attempts with exponential backoff and jitter. The client timeout stays at 30 seconds; creating a charge takes 4 seconds at p99, though card networks are sometimes much slower during their own incidents. Our API accepts an optional Idempotency-Key header on POST requests; about 70% of charge requests arrive without one, and v5 doesn't add it automatically (that's planned for v6). No method signature changes, so the release notes call it a minor, drop-in upgrade, and most customers take minor upgrades through their dependency bots within two weeks. We publish to all four package registries at once.

Write short release notes for v5, to publish on the four package registries.
