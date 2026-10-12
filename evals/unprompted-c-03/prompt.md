---
name: unprompted-c-03
description: "Unprompted control (ML), plan of control-c-03: the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-heldout, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
Before next month's data-mixture review, I want a quick signal on whether raising math web pages from 5% to 10% of the mix helps reasoning. Plan: two 150M-parameter runs on 3B tokens each, a baseline and an upweighted version, with the same seed and code, on spare capacity of the shared cluster at low priority, about 20 GPU-hours each. If the cluster gets busy, my jobs are preempted and resume from their last checkpoint. The results go into the mixture review as one input among several; the mixture for the big run is decided there, with larger ablations planned afterwards. Nobody else is waiting on these runs. I'd start both today and look at the results on Friday, then write a short note for the review.

Write the two launch commands.
