# UE Game Dev Agent Workflow

This repository ships the `UE Game Dev` Codex plugin and its marketplace mirror.

## Tracker And Branches

- Repository: `https://github.com/zhaocw/ue-game-dev`
- Primary branch: `main`
- Chinese branch: `ue-game-dev-zh`
- Feature branches should use the `codex/` prefix.
- Release-facing plugin updates must be synced to GitHub on both `main` and `ue-game-dev-zh`.

## Source Of Truth

- Edit root plugin files first: `.codex-plugin/`, `skills/`, `rules/`, `templates/`, `README.md`, `CHANGELOG.md`, `NOTICE`, and tests.
- Regenerate `plugins/ue-game-dev/` with `python scripts\sync_marketplace_package.py`.
- Install or refresh the local Codex App copy with `python scripts\update_codex_app_plugin.py` when validating plugin-list display or `@ue-game-dev` behavior.

## Domain Documents

- `README.md` describes the public skill surface.
- `CHANGELOG.md` records release-facing behavior changes.
- `CONTRIBUTING.md` records validation and sync rules.
- `docs/architecture.md` records the repository architecture.
- `docs/agents/` records agent-facing workflow notes.
- UE project state created by the plugin belongs in `Saved/CodexWorkflow/`.

## External Flow Skills

`mattpocock/skills` is used as a process reference only. Keep the UE owner skill first, then suggest the external workflow when it helps:

- `diagnose`: after UE log triage or runtime debug routing when the work needs reproduce -> minimize -> hypotheses -> instrumentation -> fix -> regression test.
- `tdd`: after UE implementation planning or automation-test routing when the user asks for test-first delivery.
- `grill-with-docs`: after `ue-feature-brief` when requirements, terms, or project language need pressure-testing against context and ADRs.
- `improve-codebase-architecture`: after onboarding or `ue-architecture` when module boundaries, dependency direction, or test seams are the main problem.

Do not copy full external skill text into this plugin. Summarize handoffs in UE-specific routing, tests, and documentation.

## Validation

Run this sequence before commit:

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```
