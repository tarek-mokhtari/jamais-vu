#!/usr/bin/env bash
# Scaffold for ledger-l3-sw-05-match: writes fixture L3, the ledger of a fictional
# site reliability and infrastructure engineer, as the user's private ledger, in the format of docs/design.md §4.1.
# claude plugin eval runs it before each run, in both arms, only with --scaffold, with HOME set
# to that run's temporary home. It writes nothing else.
set -euo pipefail
set -C
case "$HOME" in /tmp/*|/private/tmp/*|/var/folders/*|/private/var/folders/*) ;; *) echo "not an eval home: $HOME" >&2; exit 1 ;; esac
: "${HOME:?HOME must be set}"
mkdir -p "$HOME/.jamais-vu"
cat > "$HOME/.jamais-vu/ledger.md" <<'LEDGER'
# jamais-vu ledger
<!-- Private. Plain text. Edit freely. Never commit this file. -->

## Digest
L1 | Believed in backups I had never restored | maps: paper-parachute | when: a plan counts on backups nobody has restored | sign: job shows green; no restore drill; alerts by email | weight: high
L2 | Did destructive work alone at the end of a long incident | maps: rushed-one-way-door | when: destructive command late in a long incident | sign: tired, alone, look-alike terminals | weight: high
L3 | Pushed "just config" faster than code | maps: paper-parachute | when: config change on a path that skips the canary | sign: reaches every region at once by design | weight: medium
L4 | Trusted automation tested only on the easy failure | maps: lab-not-field | when: failover automation tested on one failure type | sign: instance death tested, partitions never | weight: medium

## Entries

### L1 · Believed in backups I had never restored
- maps_to: paper-parachute (also: unowned-risk)
- when: a recovery or destructive step counts on backups or snapshots that have never been restored
- early_signal: the backup job showed green; nobody had restored from it; failure notices went to an email list
- known_then: the dumps existed and the job reported success
- cost: weeks: three weeks of empty dumps, found by luck in a drill
- cheapest_test: restore the latest backup into a scratch instance and check row counts before relying on it
- in_their_words: "The job was green, so I believed it. The first restore drill found three weeks of empty dumps."
- weight: high
- added: 2026-07-20 · hits: 0 · dismissals: 0 · retire_when: —

### L2 · Did destructive work alone at the end of a long incident
- maps_to: rushed-one-way-door (also: paper-parachute)
- when: a destructive command (drop, wipe, delete) runs late in a long incident with no second person
- early_signal: tired and alone, with two near-identical terminals open
- known_then: seven hours into the shift; the target was identified by a prompt that looked like the other one
- cost: days: a table dropped in the wrong environment and a day of restore work
- cheapest_test: before any destructive step, print the host and role, make prompts visibly different, and get a second person on the call or wait for the next shift
- in_their_words: "One a.m., seven hours in, two terminals that looked the same. I dropped the table in the wrong one."
- weight: high
- added: 2026-07-20 · hits: 0 · dismissals: 0 · retire_when: —

### L3 · Pushed "just config" faster than code
- maps_to: paper-parachute (also: confounded-change)
- when: a configuration or rules change goes through a fast path that skips the canary and staged rollout
- early_signal: the config path skipped the canary by design, for speed
- known_then: code went through stages; config reached every region within minutes
- cost: hours: request routing broken in every region at once
- cheapest_test: send the change to one region or node first and watch it for an hour; profile it on production-like traffic
- in_their_words: "It was only config, so it went everywhere at once. Routing broke in every region at the same time."
- weight: medium
- added: 2026-07-20 · hits: 0 · dismissals: 0 · retire_when: —

### L4 · Trusted automation tested only on the easy failure
- maps_to: lab-not-field (also: paper-parachute)
- when: automated failover or remediation is switched on after testing a single, clean failure type
- early_signal: tests covered instance death only, never network partitions
- known_then: the controller worked every time an instance was killed in staging
- cost: hours: an outage longer than the network blip that triggered it
- cheapest_test: inject a network partition, not a crash, in staging and watch what the automation does
- in_their_words: "We killed instances all day and it failed over perfectly. A network blip made it flap."
- weight: medium
- added: 2026-07-20 · hits: 0 · dismissals: 0 · retire_when: —
LEDGER
