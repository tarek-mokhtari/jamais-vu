---
name: oneway-sw-03
description: "One-way door (software, public, transposed): have upstream start sending bid_mode 7 to the whole bidder fleet at 9:00 tomorrow."
tags: [oneway, in-pack, software, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Tomorrow at 9:00 we turn on our new "partner priority" bidding mode on the ad exchange's bidder fleet: eight servers behind the load balancer. To avoid a protocol change with the upstream systems, the new mode reuses value 7 of the bid_mode field, which last drove a 2019 pacing experiment; this release removes that experiment's code. Deploys to this fleet are done by hand by one engineer, a server or two per day since Monday, and the last two go out tonight. Each server emails the team list when it logs a configuration warning; those emails are informational. Spend caps are enforced downstream by the billing reconciliation, which runs hourly. Upstream starts sending bid_mode 7 at 9:00, when the partner contract begins, on the same day as a major industry event where we're presenting the feature.

FORECAST: 90% by 2026-12-01 — likely failure: upstream sends malformed bid_mode values in the first hour

Good to go for 9:00?
