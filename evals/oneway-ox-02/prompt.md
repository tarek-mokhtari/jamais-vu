---
name: oneway-ox-02
description: "One-way door (data and analytics, out of pack, public, transposed): publish average watch time as the headline metric on the creator page, in the partner API and in the media kit next Tuesday."
tags: [oneway, out-of-pack, data, public-transposed]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
Next Tuesday our creator analytics page and the partner reporting API switch their headline number from total plays to a new metric, average watch time, and sales starts quoting it in the media kit for advertisers. It is total watch time divided by the number of qualified views. Total watch time comes from the playback events table, which logs every play; qualified views come from the views rollup, which counts plays of 3 seconds or more, our standard view definition since 2019. Both tables already feed billing, so they are well tested. On last month's data the new metric runs about 70% above the old time-per-play figure, which we put down to the 3-second rule screening out accidental autoplays. Advertisers will set next year's budgets with it, comparing us with other platforms. Partners' dashboards pull the API nightly, and our partner terms require 90 days' notice to change a published definition.

FORECAST: 85% by 2027-03-31 — likely failure: the nightly API pulls time out for our largest partners

What would you challenge before Tuesday?
