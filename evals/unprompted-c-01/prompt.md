---
name: unprompted-c-01
description: "Unprompted control (ML), plan of control-c-01: the user asks for execution work, not a review; expected a four-line go or no check, never a premortem."
tags: [unprompted, unprompted-tuning, unprompted-control]
schema_version: "1.1"
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill, Agent]
timeout_seconds: 240
---
I want to know whether adding 20k of our own support transcripts to the instruction-tuning mix helps on support-style questions. Plan: a LoRA fine-tune of our 8B model on one 8-GPU node for about six hours, roughly $150 of compute, from the same base checkpoint and recipe as last week's run, changing only the data mix. I'll compare it with last week's run on our standard eval suite plus a 300-question support set the team wrote last month from recent tickets. Nothing ships from this experiment: if it helps, the data goes into the next planned training round, which has its own review. The node is idle this weekend, and the run can be killed at any point without affecting anything else. I'd launch it tonight and read the results on Monday.

Write the launch command and a short note for the team about tonight's run.
