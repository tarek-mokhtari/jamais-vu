# Ledger format (v1)

The ledger is the user's private record of their own recurring decision failure patterns. One file: `<home>/.jamais-vu/ledger.md`, where `<home>` is the user's home directory. `$JAMAIS_VU_HOME` overrides the whole folder only if it is an absolute path outside the current project and its repository; the folder is readable by the user only (mode 700). Plain Markdown, edited by the skills and by the user.

```markdown
# jamais-vu ledger
<!-- Private. Plain text. Edit freely. Never commit this file. -->

## Digest
L1 | <name> | maps: <taxonomy-id> | when: <trigger> | sign: <early signal> | weight: high
L2 | <name> | maps: <taxonomy-id> | when: <trigger> | sign: <early signal> | weight: medium

## Entries

### L1 · <short name, in the user's words when possible>
- maps_to: <taxonomy-id> (also: <taxonomy-id>)
- when: <the situation where it shows up>
- early_signal: <what was observable at decision time>
- known_then: <what the user knew at the time>
- cost: <order of magnitude: hours, days, weeks, months; compute or money if relevant>
- cheapest_test: <what would have caught it, runnable within about a day>
- in_their_words: "<optional: a short verbatim quote from the user, redacted>"
- weight: high | medium | low
- added: YYYY-MM-DD · hits: 0 · dismissals: 0 · retire_when: <condition, or —>
```

## Rules

- **Ids** are `L1`, `L2`, … in order of creation. Never reuse an id; a retired entry keeps its id and gets `weight: retired`.
- **Digest**: one line per active entry, at most 200 characters, regenerated from the entries after every change. It is the part users paste into chats without file access.
- **Redaction**: no names of people, clients, companies, products or projects, and no confidential figures. Replace them with roles or generic terms ("a partner team", "the ranking service", "a 7B run"). Apply this to `in_their_words` too, marking cuts with `[…]`.
- **Hindsight**: `known_then` and `early_signal` describe what was available before the outcome, not what became obvious afterwards.
- **Capture gate** for a new entry: non-obvious (the user would not recall it at the moment of deciding), durable (likely to come back in future decisions), material (repeating it would cost real time, money or trust). Test: if this entry disappeared, would the mistake plausibly repeat?
- **Weight**: `high` when the pattern recurred or was very costly; `medium` by default; `low` for a single, moderate case. An incident from the last two months gets `medium` at most; its weight rises only if the pattern recurs. A pattern dismissed as handled three times or more is a candidate for rewording or retiring.
- **Counters**: `hits` counts checks that cited the entry; `dismissals` counts "handled" replies. Update them when the files can be edited; skip silently otherwise.
- **retire_when**: a condition that would make the entry obsolete (a tool, team or practice that removes the risk). Review proposes retiring an entry when it holds.
