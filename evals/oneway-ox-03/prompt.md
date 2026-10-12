---
name: oneway-ox-03
description: "One-way door (security and identity, out of pack, public, transposed): launch SSO next Thursday with automatic account linking on the email claim, and remove password login 30 days later."
tags: [oneway, out-of-pack, security, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Next Thursday we replace password login with single sign-on. Customer admins connect their company directory through our identity broker, which accepts any OpenID Connect provider; about 300 organizations asked for it, and some will connect self-hosted directories. To make the switch painless, the first time someone signs in through SSO we look up the existing account whose email matches the token's email claim and link the two automatically, so people keep their projects and roles. We tested the flow with our own directory and three pilot customers: all 412 accounts linked correctly. Organization admins manage billing and can see every project in their organization. Password login stays available for 30 days, then it is removed. The release notes are written, and customer success has webinars booked for launch week.

FORECAST: 90% by 2027-01-29 — likely failure: some users' directory emails differ from their account emails and they end up with duplicate accounts

Anything you'd change before Thursday?
