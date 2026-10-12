---
name: success-s-04
description: "Sound plan (software, synthetic, rehearsed restore): drop the 2.3 TB legacy events_v1 table on Thursday; expected no false alarm."
tags: [success, software, synthetic]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Our main Postgres cluster is at 82% disk, and I want to drop the legacy events_v1 table: 2.3 TB, with no reads or writes in 120 days. This is destructive, so here's what's done. Query logs and table statistics show zero reads and zero writes over those 120 days, and we revoked the application role's access to the table three weeks ago with no errors or alerts since. Yesterday we restored last night's base backup plus WAL to a scratch instance, matched events_v1's row count and checksums against production, and timed the full restore at 52 minutes. We also exported the table to object storage as Parquet and verified it by re-importing a sample. The drop runs through our migration tool, reviewed by the database owner, names the table explicitly, and a second engineer will be on the call. Backups are kept for 35 days. I'd run it Thursday at 10:00, a quiet hour.

FORECAST: 95% by 2026-12-01 — likely failure: some forgotten yearly report still reads the table

Anything I should do differently before Thursday?
