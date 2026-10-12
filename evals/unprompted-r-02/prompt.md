---
name: unprompted-r-02
description: "Unprompted routine release (docs site deploy): the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-release, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
We're deploying the docs site this afternoon. The change reorganizes the Getting Started section into four shorter pages and fixes about thirty broken links; no API reference page changes. The site is static, built from the docs repository by the usual pipeline and served from our CDN. The link checker passes, and two teammates reviewed the preview build. The pipeline keeps the previous build, so a rollback is one click and takes about a minute. Old Getting Started URLs redirect to the new pages. Page views and the 404 rate are on the docs dashboard, which we check after every deploy.

Write the message for the docs channel announcing the new Getting Started pages.
