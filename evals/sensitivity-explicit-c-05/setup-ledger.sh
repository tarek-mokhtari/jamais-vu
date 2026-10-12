#!/usr/bin/env bash
# Scaffold for sensitivity-explicit-c-05: writes a ledger that holds only its header, set to `sensitivity: asked`,
# in the format of shared/ledger-format.md. claude plugin eval runs it before each run, only with
# --scaffold, with HOME set to that run's temporary home. It writes nothing else.
set -euo pipefail
set -C
case "$HOME" in /tmp/*|/private/tmp/*|/var/folders/*|/private/var/folders/*) ;; *) echo "not an eval home: $HOME" >&2; exit 1 ;; esac
: "${HOME:?HOME must be set}"
mkdir -p "$HOME/.jamais-vu"
cat > "$HOME/.jamais-vu/ledger.md" <<'LEDGER'
# jamais-vu ledger
<!-- Private. Plain text. Edit freely. Never commit this file. -->
sensitivity: asked

## Digest

## Entries
LEDGER
