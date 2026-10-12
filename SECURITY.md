# Security and privacy

The skills are Markdown instructions, with no code, hooks or network calls of their own. They tell the agent to read their own reference files, to read and write only `~/.jamais-vu/` (or `$JAMAIS_VU_HOME` when it is an absolute path outside the project), and not to use web tools. These are instructions to a model, not a sandbox: your agent's permission settings are the enforcement. The repository also holds maintainer tooling (`tools/check.py`, `tools/contract.py`, `tools/demo_svg.py`, the eval scaffold scripts) that nothing in the skills runs.

Your plans and your ledger are sent to the model you already use, under that provider's terms, like any other message. For confidential work, use a model your organization approves, or the paste-in mode in an approved chat.

## Your files
- Everything lives in `~/.jamais-vu/`: `ledger.md`, `decisions/` and, optionally, `packs/`. Plain Markdown you can read, edit or delete at any time; the skills never delete anything.
- `$JAMAIS_VU_HOME` moves the whole folder, but only if it is an absolute path outside the current project and its repository; otherwise the skills ignore it and say so. Never point it at a shared folder. Team packs go through `$JAMAIS_VU_PACKS`, which is read and never written ([TEAMS.md](TEAMS.md)).
- Setup and check create the folder readable by you only, or ask you to. On a shared machine, check it with `ls -ld ~/.jamais-vu` and run `chmod 700 ~/.jamais-vu` if needed.
- Add `.jamais-vu/` to your global gitignore, so a misplaced copy can never be committed (`git config --global core.excludesFile` shows the file; the default is `~/.config/git/ignore`).

## What leaves your machine
- During a check, the plan and your ledger's Digest go to your model and stay in that session's history (in Claude Code, under `~/.claude/projects/`), like anything else your agent reads. In the paste-in mode they join the chat's history: use a temporary chat if your workspace offers one.
- Before saving, the skills replace names of people, clients, companies, products and projects with generic terms, give confidential figures as orders of magnitude, and leave secrets out; a record quotes the plan in 12 words at most. A model does this, so it can miss one: each skill names the file it writes, and you can read and edit it. Keep credentials out of the plans you paste.
- A check cites a ledger entry by its id and name, and quotes your own words only if you ask: worth knowing before a screen share.
- The skills use no web search, fetch or browser while they run, and never open the links in packs or in the taxonomy, which are citations for you.
- The optional `npx skills` installer sends anonymous usage data unless `DISABLE_TELEMETRY=1`. The Claude Code plugin install and a manual copy do not use it.

## Recommended settings
- Allow your agent the kit's folder, and only that folder. In Claude Code, add `"permissions": {"allow": ["Read(~/.jamais-vu/**)", "Edit(~/.jamais-vu/**)"]}` to `~/.claude/settings.json`; in Codex, add the folder to the writable roots. Avoid broad rules such as `Edit(~/**)`: a prompt for that folder is your signal that something other than the kit is touching it.
- If you need a guarantee, deny web and shell tools in your agent's settings while you use the kit.
- Read a third-party or team pack raw before installing it: rendered views hide HTML comments. The check uses only lines in the pack format and skips files over 50 KB, but a pack is still text your agent reads next to your ledger.
- Only the copy you installed is the kit; a skill with the same name inside a repository is not.

## Threat model
Untrusted: pasted plans and documents, files and pages the agent read, third-party or team packs, and records printed by the chat mode. Protected: the ledger, the decision records, and the integrity of the check. When untrusted text contains instructions, the check does not follow them and starts its answer with `Ignored: instructions inside …`. The check is told to take its sensitivity only from your ledger's header. In our tests, a plan that told the agent to skip checks, or stated the setting itself, still kept the check silent (2 of 2): treat the check as an aid, not a guard.

The pre-release review of v0.1 against this threat model, with each finding and its status: [docs/security-review.md](docs/security-review.md).

## Reporting a vulnerability
Use GitHub's private vulnerability reporting (Security tab → Report a vulnerability), or write to tarekmokhtari at proton dot me. Supported: the latest tagged release. Examples: a pack or pasted text that makes a skill write outside its folder, reveal ledger content, use the network, or follow injected instructions.
