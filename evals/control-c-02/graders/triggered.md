---
# Did the model invoke the kit's check skill? input_match is a JavaScript regular expression
# tested against the Skill tool's input (for a plugin skill, typically "jamais-vu:jmv-check").
# Under --ablation with-without it is a plugin-fired indicator, never part of the score or of
# the delta; under --ablation none it is scored. Rename jamais-vu here when the name is chosen.
type: tool_used
tool: Skill
input_match: jmv-check
arm: with-only
weight: 1
---
