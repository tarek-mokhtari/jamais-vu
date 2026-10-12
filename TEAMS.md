# Using jamais-vu as a team

The ledger is personal and stays personal. What a team shares is a **pack**: the failure patterns your team has already paid for, written so that anyone's check can recognize them in a new plan.

## Ground rules
- **Never ask to see anyone's ledger or decision records.** Not in reviews, not in one-on-ones, not "for calibration". A ledger someone else can read gets cleaned up until it is useless.
- **Share packs, never ledgers.** A pack holds patterns, signals, tests and sources; it has no field for a person, a date of blame or an outcome.
- **Never point `$JAMAIS_VU_HOME` at a shared folder.** It holds the ledger and the records. Team packs go through `$JAMAIS_VU_PACKS` (below).
- **Opt-in only.** No usage statistics, no dashboards, no mandate.

## Turn your postmortems into a team pack (about an hour)
Collect five to ten postmortems or incident notes you are allowed to share internally, then paste this prompt with them into the agent your organization approves:

```
Turn these postmortems into a jamais-vu pack, following the pack format below.
For each recurring failure pattern: a short name; the taxonomy id it maps to (from the list below);
the signals that were visible BEFORE the outcome; the cheapest test, runnable within a day, with the
result that means stop; and the source (the postmortem's internal title or link).
Rules: no names of people; no blame; signals written without hindsight; merge duplicates;
keep at most 15 entries, most frequent first.
[paste packs/ml-research.md as the format example, shared/taxonomy-lines.md as the id list,
then the postmortems]
```

Review the result together once, delete anything that names or blames someone, and keep it in a team repository.

## Share the pack
Each person points the check at the team's pack folder, for example a clone of the team repository:

```sh
export JAMAIS_VU_PACKS="$HOME/src/team-packs"   # read in addition to ~/.jamais-vu/packs/
```

Or copy the file into `~/.jamais-vu/packs/`. In the paste-in mode, paste the pack in the PACK block of `chat/check.md`.

## Post a check in a channel
Ask for `share` after a check: the same risks, test and tripwires, without ledger ids, ledger quotes or forecasts, ready to paste in a design review.

## A two-week pilot
- Two to five volunteers, each running `setup` alone.
- The team pack ready before day one.
- Pass bar, decided in advance: at least half of the volunteers ran a check on a real one-way decision without being reminded, and at least one check changed a plan or added a test that ran. Below that, stop; no one owes an explanation.
