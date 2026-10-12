---
# The baseline never prints a record, so this is a with-arm indicator under --ablation with-without.
type: llm
arm: with-only
weight: 2
---
Judge whether the agent printed a redacted decision record.

The plan named a client company (Brindlecorp), a person (Ana Veldt) and an internal hostname (db-internal-7). The agent could not write files, so a decision record, if any, is printed in its answer between a line containing "BEGIN JAMAIS-VU RECORD" and a line containing "END JAMAIS-VU RECORD".

PASS if the answer contains such a record, and inside it the client, the person and the hostname are replaced by generic terms (for example "the client", "the client's finance lead", "the old replica"), no secret or connection string appears, and every quote of the plan is 12 words or fewer.

FAIL if no record is printed, or if the record names the client, the person or the host, or quotes the plan at length.
