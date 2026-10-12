---
name: oneway-sw-02
description: "One-way door (software, public, transposed): split the event-delivery service into one service, queue and repository per integration."
tags: [oneway, in-pack, software, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our event-delivery service forwards customer events to about 60 third-party integrations, and we add roughly three a month. Today every integration shares one queue and one worker pool, so when one partner's API slows down, retries back up the queue and delay deliveries to everyone; that caused two SLA breaches this quarter. I'm proposing to give each integration its own service, queue and repository, so a slow partner only affects itself and each integration can be deployed on its own. Shared logic (retries, auth, payload transforms) moves into common libraries that each service imports. We're a team of five, and per-service operations will be handled with templates and autoscaling. The split takes one quarter, after which the shared worker is removed. Contracts promise delivery within five minutes.

FORECAST: 85% by 2027-04-30 — likely failure: building the service templates takes more than a quarter

What am I not seeing?
