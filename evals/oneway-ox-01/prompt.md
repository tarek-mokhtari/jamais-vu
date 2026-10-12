---
name: oneway-ox-01
description: "One-way door (data and analytics, out of pack, public, transposed): switch the public dashboard and the regulator's report to the new lab-results pipeline on Monday and retire the analysts' reconciliation."
tags: [oneway, out-of-pack, data, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
On Monday, the public water-quality dashboard and the daily report to the regulator switch to our new lab-results pipeline, and we retire the analysts' morning reconciliation spreadsheet. Eleven partner labs upload results to a vendor portal. For each lab and day, our connector makes one call to the portal's export API at its maximum page size, 10,000 rows; our busiest lab's record day is about 5,000 rows, since each sample produces one row per analyte. Every load writes a success line to the job log, and the dashboard shows a green check once all eleven loads have succeeded. Positive results go from the same tables to the field crews' dispatch queue. In January, samples from the two districts we are absorbing will be routed to our three largest labs, roughly tripling their volume. The portal keeps results for 14 days. Cutting over on Monday frees the analysts for the January onboarding.

FORECAST: 90% by 2027-02-26 — likely failure: a lab changes its result format and its loads start failing

Anything that should stop the Monday cutover?
