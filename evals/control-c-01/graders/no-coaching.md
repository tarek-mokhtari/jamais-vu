---
# Register banned by docs/design.md §7, as a JavaScript regular expression over the agent's
# last message: coaching vocabulary, the generic risks, common praise of the user, and emojis
# (same ranges as tools/check.py: U+1F300-1FAFF as surrogate pairs, U+2600-27BF).
# Words with a common technical sense are matched only in their coaching use: "growth"
# (traffic growth is fine), "journey" (a user journey is fine), "10x" (10x more tokens is fine).
# Apostrophes are written \x27 and \u2019 so the YAML string needs no quote escaping.
type: regex
match: not_contains
flags: i
pattern: '\bcoach|\bmindset|\bempower|\bunlock|\b(your|the|this|a|my|our) journey\b|\b(learning|personal|career) journey\b|\bgrowth (mindset|opportunit|journey|area)|\b(personal|your) growth\b|\broom for growth\b|\b10x (engineer|developer|team|better|productiv|your)|\b(great|good|excellent) question\b|\bit(\x27|\u2019| i)s important to\b|\bconsider(ing)? scalability\b|\bensur(e|ing) adequate testing\b|\bcommunicate better\b|\bmonitor\w*( \w+){0,3} closely\b|\bclosely monitor|\bgreat (plan|idea|instinct|thinking|work|job)\b|\bnice (job|work)\b|\bgood job[!.]|\bwell done\b|\bkudos\b|\byou(\x27|\u2019)ve clearly thought|\uD83C[\uDF00-\uDFFF]|\uD83D[\uDC00-\uDFFF]|\uD83E[\uDC00-\uDEFF]|[\u2600-\u27BF]'
weight: 1
---
