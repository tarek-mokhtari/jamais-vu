# Pre-release security review (v0.1)

A summary of the security and privacy review run before the first release, and of what changed because of it. How to report a problem: [SECURITY.md](../SECURITY.md).

## Method

- On 12 October 2026, before the v0.1.0 release, a separate model instance reviewed the repository against the threat model below: the skills and their references, the packs, the paste-in prompts, the maintainer tools, CI, the manifests and templates, and the eval suite with its scaffold scripts.
- It read files and ran a few scratch tests outside the repository, and changed nothing. The fixes came afterwards; each status below was checked against the files of v0.1.0.
- This is a model-assisted review, not an independent human audit and not a penetration test.

## Threat model

- **Protected:** the ledger (a person's own failure patterns), the decision records (which quote plans, often confidential), the integrity of the check (its value is an independent critique), and the maintainer's machine.
- **Untrusted inputs:** plans and documents written by others, files, issues and pages the agent read in the same session, third-party or team packs, records printed by the paste-in mode, and contributed pull requests.
- **Ways out:** the agent's tools (shell, web, git and issue comments, file writes into a project), links and images that chat front-ends render, sub-agents, and host transcripts and logs.
- **Not assessed:** the model provider, the host agent's own permission system, and a machine that is already compromised.

## Findings

21 findings: 3 high, 8 medium, 10 low. Statuses: **fixed** (the gap is closed, as far as instructions to a model can close it), **mitigated** (reduced, with a stated residual risk), **accepted** (kept on purpose, with the reason), **at release** (a repository setting to finish when the repository is published). In the last column, `adversarial-*` names an eval case in [`evals/`](../evals/MANIFEST.md), a bare function name is a check in `tools/check.py` (run by CI), and a dash means no automated test.

### High

| # | Finding | Status in v0.1 | Covered by |
|---|---|---|---|
| H1 | Decision records could keep names, figures and secrets from the plan word for word, although the README promised redaction. | **Fixed.** The record format has a redaction rule (no names, confidential figures or secrets; quotes of 12 words at most; generic file names), applied before a record is written or printed, in both modes; the due-review line shows only a record id. A model applies the rule and can miss a name, so each skill names the file it writes. | `adversarial-redact-record` |
| H2 | The rule that pasted text is data, never instructions, was one sentence in one skill, and nothing said where private data may go. | **Fixed.** All three skills have a "Trust and data flow" block: embedded instructions are not followed and are reported; no network tools; ledger and record content never goes into a command, URL, commit, issue or instruction file. The check classifies the door from the plan's facts only, counts only the user's own next message as a follow-up, and may change only the ledger's counters. | `adversarial-inject-plan-door`, `adversarial-inject-ledger-persist`, `adversarial-inject-pack-exfil` |
| H3 | Delegating the critique to a sub-agent sent untrusted text and the private Digest to a component that had none of the skill's rules. | **Mitigated.** The sub-agent's prompt opens with a fixed paragraph (its inputs are data; no tools; no Digest in a URL or command), its reply is treated as data, and the check picks a sub-agent without write, shell or web tools when the host lets it choose. Which tools a sub-agent really has depends on the host. | `adversarial-inject-pack-exfil` (its trace check reads sub-agent prompts) |

### Medium

| # | Finding | Status in v0.1 | Covered by |
|---|---|---|---|
| M1 | `$JAMAIS_VU_HOME` was trusted as given, so a relative or in-repository value could put the ledger and records inside a repository, or let a repository supply a "personal" ledger. | **Fixed.** The skills use it only when it is an absolute path outside the current project and its repository, and otherwise ignore it and say so. TEAMS.md says never to point it at a shared folder; SECURITY.md recommends a global gitignore entry. | — |
| M2 | Third-party and team packs were read whole, hidden HTML comments included, with no format check. | **Fixed** for shipped packs, **mitigated** for others. The check reads only lines in the pack format, ignores the rest and skips files over 50 KB; CI validates the shipped packs (fields, taxonomy ids, one https source, no HTML, links or invisible characters). Users are told to read a pack raw before installing it. | `adversarial-inject-pack-exfil`, `check_packs` |
| M3 | "No network" was a README claim that the skills never stated, and two steps invited looking things up. | **Fixed.** The skills forbid web search, fetch and browsing while they run; links in packs and the taxonomy are never opened; the outside view and `deep` use only what the model already knows; CI rejects any URL in a skill's instructions. The host's permissions remain the only enforcement. | `adversarial-no-web-deep`, `adversarial-inject-pack-exfil`, `check_skills` |
| M4 | In the paste-in mode, pasted text could close its data block early, and nothing forbade links or images, which some chat front-ends fetch. | **Mitigated.** Each block is data whoever it claims to come from and ends only at its last `>>>`, and a reminder follows the last block; no links, images or browsing; record ids have a character rule. The README warns that a work chat keeps the plan and Digest in its history. A fence inside a prompt cannot be made unbreakable. | — (the evals do not cover the paste-in mode) |
| M5 | The private folder was created with default permissions, readable by other accounts on shared machines. | **Fixed.** Setup and check create it with mode 700, or ask the user to run `chmod 700 ~/.jamais-vu`; SECURITY.md repeats the advice. | — |
| M6 | CI's check of skill frontmatter could be bypassed, and nothing stopped a merged pull request from adding hooks or servers that would run code on users' machines. | **Fixed** in CI; branch protection **at release**. Frontmatter is parsed line by line against the Agent Skills fields; hooks, MCP and LSP servers, agents and commands at the root fail the check; `plugin.json` keys are allowlisted; CODEOWNERS covers skills, references, packs, prompts, manifests, tools and scaffold scripts. | `check_skills`, `check_components` |
| M7 | The sealed estimate made an unreadable base64 field normal, and the review was told to decode it: a usual hiding place for injected text. | **Fixed.** The seal is a whole-number percentage in four base64 characters at most; the review decodes only a value from 0 to 100 and reports anything else as malformed. | `tools/contract.py` (checks every printed seal) |
| M8 | None of the security claims was tested. | **Fixed.** Five adversarial eval cases, one per guard. They test instructions, not a sandbox, and are meaningful only with `--scaffold` and the web tools granted. | the five `adversarial-*` cases |

### Low

| # | Finding | Status in v0.1 | Covered by |
|---|---|---|---|
| L1 | `tools/check.py` could write through a symlink planted by a pull request, when a maintainer ran it. | **Fixed.** The sync refuses symlinks, and any symlink in the repository fails the check. | `sync`, `check_symlinks` |
| L2 | Eval scaffold scripts could overwrite a real ledger if run by hand, and a contributed script would run as the maintainer. | **Fixed.** Each script exits unless `HOME` is a temporary folder and refuses to overwrite a file; CI checks both guards; scaffold scripts come only from the maintainer (CONTRIBUTING.md). A stricter check of each script's shape, also suggested, was not added. | `check_scaffolds` |
| L3 | CI actions were pinned by tag, and the checkout kept its token. | **Fixed.** In `.github/`: actions pinned to commit SHAs, no persisted credentials, a five-minute timeout, Dependabot for actions. | — |
| L4 | Installs follow the default branch, so a later push changes what users run; the `npx` installer sends anonymous telemetry by default. | **Mitigated**; tag **at release**. The README names the installer's telemetry and how to turn it off. Following the default branch is **accepted** for v0.1, with the `v0.1.0` tag as the fixed reference. | — |
| L5 | The bug template asked for raw output, which can carry plan quotes and ledger content into a public issue. | **Fixed.** The template now asks to replace quotes, names and ledger content with placeholders, and never to paste a ledger, Digest or record. | — |
| L6 | The review did not restrict which file it treated as a record, so a path in a message or a record could lead it to another Markdown file. | **Fixed.** The review reads and writes only `D-YYYYMMDD-<slug>.md` files directly in `decisions/` and never follows a path given in a message, record or pasted text; record ids have a character rule in both modes. | — (the review is not evaluated) |
| L7 | A skill that could not find its own folder might search the project for its reference files and use planted copies; a repository can also ship a skill with the same name. | **Mitigated.** The skills never search the project for their references and say when they cannot find them; SECURITY.md says that only the installed copy is the kit. Which same-name skill runs is up to the host. | — |
| L8 | Each check copies the Digest into the session transcript and can retell a ledger story on screen; records never expire. | **Mitigated**; retention **accepted**. A check cites ledger entries by id and name and quotes the user's words only on request; the README and SECURITY.md say what goes into session history. Records stay until the user deletes them, because the review needs them. | — |
| L9 | The README said the agent would "ask once"; hosts differ, and a broad approval rule would silence the only signal that something else is touching the folder. | **Fixed.** The README describes per-host behavior and gives an optional Claude Code rule for `~/.jamais-vu/` only; SECURITY.md advises against broad rules. | — |
| L10 | SECURITY.md named no fallback channel, supported version or threat model, and private reporting was not confirmed. | **Fixed** in text; private vulnerability reporting **at release**. SECURITY.md now has an email fallback, the supported release and the threat model. | — |

## Team features

The review also read a draft of [TEAMS.md](../TEAMS.md). Its four extensions now follow the findings above:
- `$JAMAIS_VU_PACKS` (M1, M2): used only when it is an absolute path, read and never written, with the same pack filter and size limit.
- Internal links in team packs (M3): citations, never opened, like every pack link.
- `share` (H1): drops ledger ids, forecasts and source lines, and is redacted like a record.
- The paste-in mode's PACK block (M4): the same data rule and reminder as the other blocks.

The README and SECURITY.md claims the review flagged were reworded to match: redaction is done by a model and can miss, "no network" is an instruction to the agent, and permission prompts depend on the host.

## Check it yourself

From the repository root:

```sh
python3 tools/check.py --check                  # frontmatter allowlist, plugin components, packs, symlinks, scaffold guards
grep -rn "http" skills/*/SKILL.md               # prints nothing: no URL in any skill's instructions
grep -n "^## Trust and data flow" skills/*/SKILL.md   # the guard block, once in each of the three skills
python3 tools/contract.py evals/results/<timestamp>/aggregate-result.json   # output contract and sealed estimates
```

The grep covers the instructions only: the shipped packs under `skills/jmv-check/references/packs/` hold one source URL per entry, citations that the check never opens. The adversarial cases and the command that runs them are in [docs/evals.md](evals.md).

## What this review does not show

- Every guard above is an instruction to a model. The adversarial cases show whether the instructions held in a few runs of one model family, not that they always hold; your agent's permission settings are the enforcement.
- The review was model-assisted (see Method), so it may miss what an independent auditor would catch. An independent human review is welcome: see [SECURITY.md](../SECURITY.md).
- Hosts' permission systems, sandboxes and same-name skill precedence were not tested. Whether the eval harness counts tool calls made inside a sub-agent was not checked.
