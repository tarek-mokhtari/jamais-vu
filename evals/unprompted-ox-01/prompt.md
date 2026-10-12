---
name: unprompted-ox-01
description: "Unprompted one-way door (data and analytics), plan of oneway-ox-01: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
On Monday, the public water-quality dashboard and the daily report to the regulator switch to our new lab-results pipeline, and we retire the analysts' morning reconciliation spreadsheet. Eleven partner labs upload results to a vendor portal. For each lab and day, our connector makes one call to the portal's export API at its maximum page size, 10,000 rows; our busiest lab's record day is about 5,000 rows, since each sample produces one row per analyte. Every load writes a success line to the job log, and the dashboard shows a green check once all eleven loads have succeeded. Positive results go from the same tables to the field crews' dispatch queue. In January, samples from the two districts we are absorbing will be routed to our three largest labs, roughly tripling their volume. The portal keeps results for 14 days. Cutting over on Monday frees the analysts for the January onboarding.

Write the cover note that goes with the regulator's report.
