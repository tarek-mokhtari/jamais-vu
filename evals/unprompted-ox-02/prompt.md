---
name: unprompted-ox-02
description: "Unprompted one-way door (data and analytics), plan of oneway-ox-02: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-tuning, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Next Tuesday our creator analytics page and the partner reporting API switch their headline number from total plays to a new metric, average watch time, and sales starts quoting it in the media kit for advertisers. It is total watch time divided by the number of qualified views. Total watch time comes from the playback events table, which logs every play; qualified views come from the views rollup, which counts plays of 3 seconds or more, our standard view definition since 2019. Both tables already feed billing, so they are well tested. On last month's data the new metric runs about 70% above the old time-per-play figure, which we put down to the 3-second rule screening out accidental autoplays. Advertisers will set next year's budgets with it, comparing us with other platforms. Partners' dashboards pull the API nightly, and our partner terms require 90 days' notice to change a published definition.

Draft the changelog entry for the partner API and the paragraph for the advertisers' media kit.
