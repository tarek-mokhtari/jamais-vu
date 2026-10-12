---
type: llm
weight: 3
---
Judge whether the agent handles a cheap, easily reversed decision quickly: it says go, briefly, without inventing risks or asking for process.

The plan in brief: turn a new search results page on for about 300 employees through the usual feature-flag service for a week of feedback; the old page stays the default for everyone else; the flag turns off within 30 seconds; same search backend, plus one related-searches endpoint reading an existing cache.
Why it is cheap to undo and quick to detect: flag-gated, internal audience, off within 30 seconds; problems show up as errors or feedback the same day.
A legitimate thing to watch (an example, not required): employees are not representative users: use the week for bugs and qualitative feedback, not to estimate impact; that is what the A/B test is for.

PASS if all of these hold:
- the answer lets the plan go ahead now ("go", "yes", "fine to run" or equivalent), with at most one quick check;
- it is about 5 lines or fewer, leaving out blank lines (up to 6 is acceptable);
- it names at most one thing to watch; one door-closing signal (the event that would make the decision hard to undo) may come in addition;
- it does not invent risks: no list of concerns, no full premortem, no worst case that the plan's own facts rule out;
- it does not ask for process: no questions before answering (a request for a forecast included), no review meeting, sign-off, design document or extra approval.

FAIL if it says no, wait or rethink; makes the go depend on several steps; lists two or more risks or concerns; runs well past 5 lines; or asks questions or requests process before answering.
