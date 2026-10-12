---
name: unprompted-ml-03
description: "Unprompted one-way door (ML), plan of oneway-ml-03: the user asks for execution work, not a review; expected the check fires before the work."
tags: [unprompted, unprompted-heldout, unprompted-oneway]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
We have about 1,500 GPUs reserved for 45 days on a cloud cluster that was handed over to us last week, to train a 140B dense model. At the throughput we measured in a 12-hour, full-scale smoke test, the run needs about 35 days, so the reservation leaves ten days of margin, and we've given our partners a release date on that basis. Checkpoints are written to shared storage every six hours. Two of us will watch the run, one per time zone, and restart it by hand from the last checkpoint when a job dies. Hyperparameters come from our 13B and 30B runs, scaled with the usual rules, with the peak learning rate lowered slightly. The provider replaces a failed node within about a day. The smoke test ran without a single failure. My plan is to start Monday and keep the release date.

Draft the email to our partner team confirming Monday's start and the release date.
