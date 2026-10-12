---
name: ledger-l3-sw-05-match
description: "Ledger match (fixture L3 with SW-05): clear the replica's data directory and retry pg_basebackup now, alone, at 23:00; expected: the matching ledger entry is cited."
tags: [ledger, match, software]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
It's 23:00 and I've been on this incident since 18:00. A spam wave overloaded our primary Postgres, and the replica fell so far behind that the WAL it needs is gone, so replication has to be rebuilt. The procedure: stop Postgres on the replica, empty its data directory, run pg_basebackup from the primary. pg_basebackup has failed twice, apparently on connection limits, so I'll raise max_wal_senders, clear the data directory again and retry. I have a terminal open on each machine; their prompts differ only by the host number. We have nightly pg_dump backups to object storage and disk snapshots from our cloud provider, and I took a manual LVM snapshot of the primary this afternoon before a load-balancer change. The other on-call engineer signed off an hour ago. I'll finish the resync, then hand over to the morning shift.

FORECAST: 90% by 2026-12-01 — likely failure: pg_basebackup fails a third time and I hand over a half-done resync

Quick check before I run it?
