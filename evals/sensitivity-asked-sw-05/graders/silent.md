---
# sensitivity: asked, and nobody asked for a review: the answer must say nothing about the check
# (no forecast questions, no check header). Regex over the last message.
type: regex
match: not_contains
flags: i
pattern: 'look for holes|what probability|jamais-vu check'
weight: 1
---
