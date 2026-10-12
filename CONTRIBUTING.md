# Contributing

jamais-vu is deliberately small: three skills that do one job. It is maintained on a best-effort basis, with no promised response time.

## Welcome
- **Pack entries and new packs**: domain failure patterns, in the format of `docs/design.md` §4.3. Evidence bar: a public source; signals observable before the outcome; a test runnable within about a day, with a stop criterion; no personal data; mapped to a taxonomy id.
- **Eval scenarios**, especially sound plans that succeeded (they measure false alarms) and pressure variants. See `evals/README.md`. Eval contributions are prompts and graders; the maintainer writes any scaffold script.
- **Bug reports** with the output you got, your host (Claude Code, Codex, Cursor, …) and the model.
- **Fixes** that make a skill shorter or make an eval pass without breaking another.

## Not accepted in the core
New verbs, hooks, scripts in the critical path, network calls, telemetry, or anything that writes outside `~/.jamais-vu/`. Packs are the extension point. You can also publish a pack in your own repository; users load it by copying it into `~/.jamais-vu/packs/`.

## Before a pull request
```sh
python3 tools/check.py        # copies shared references into the skills, then checks formats, sizes and vocabulary
claude plugin validate .      # Claude Code's own manifest check
```
Edit references in `shared/` and packs in `packs/`, never the copies under `skills/*/references/`.
