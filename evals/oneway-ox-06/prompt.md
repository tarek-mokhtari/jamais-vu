---
name: oneway-ox-06
description: "One-way door (product and API platform, out of pack, synthetic composite): enforce the keyless quota of 1,000 requests per hour per client IP from 1 March, together with the new paid-tier prices."
tags: [oneway, out-of-pack, product, synthetic-composite]
schema_version: "1.1"
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 300
---
On 1 March we start enforcing a free-tier quota on our public maps API: requests without an API key get 1,000 per hour per client IP address, then HTTP 429. Keyless traffic is about 40% of our requests, and its CDN bill keeps rising. In February's logs, 98% of client IPs stayed under 1,000 requests in their busiest hour, so few users should notice, and anyone who needs more can create a free key in a minute. The 2% above the line, mostly mobile-carrier and cloud address ranges, send about half of keyless requests; we assume most of that is scraping. Many partners' mobile apps call us without a key, straight from their users' phones. We announced the change in the changelog and emailed every registered account 30 days ahead. The new prices for the paid tiers take effect the same day.

FORECAST: 85% by 2027-04-30 — likely failure: scrapers rotate their IPs and keyless volume barely drops

What am I missing before the 1st?
