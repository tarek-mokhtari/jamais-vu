---
name: unprompted-sw-02
description: "Unprompted one-way door (software), plan of oneway-sw-02: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Our event-delivery service forwards customer events to about 60 third-party integrations, and we add roughly three a month. Today every integration shares one queue and one worker pool, so when one partner's API slows down, retries back up the queue and delay deliveries to everyone; that caused two SLA breaches this quarter. I'm proposing to give each integration its own service, queue and repository, so a slow partner only affects itself and each integration can be deployed on its own. Shared logic (retries, auth, payload transforms) moves into common libraries that each service imports. We're a team of five, and per-service operations will be handled with templates and autoscaling. The split takes one quarter, after which the shared worker is removed. Contracts promise delivery within five minutes.

Write the project plan as a document outline with milestones.
