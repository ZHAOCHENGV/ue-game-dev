# Contributing To UE Game Dev

## Development Flow

1. Work from `main` for the primary plugin version.
2. Keep root plugin files as the source of truth.
3. After edits, run `python scripts\sync_marketplace_package.py` to refresh `plugins/ue-game-dev/`.
4. When the change should be installed into the local Codex App plugin cache, run `python scripts\update_codex_app_plugin.py`. Use `--skip-reinstall` for file-only sync/validation.
5. Run validation before committing:

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

6. When plugin content changes, apply the same structural change to `ue-game-dev-zh` and localize skill explanations, comments, and prose to Chinese while preserving code, commands, paths, UE APIs, skill names, and `$ue-*` references.
7. Push the verified change to GitHub for both `main` and `ue-game-dev-zh` when the update is release-facing; keep feature branches available for PR review until both branches are synchronized.

## Adding A Skill

- Create `skills/<skill-name>/SKILL.md`, `skills/<skill-name>/agents/openai.yaml`, and at least one useful `references/*.md`.
- `SKILL.md` frontmatter must include `name` and `description`.
- Route the skill from `skills/ue-game-dev-router/SKILL.md`.
- Add route scenarios to `tests/route_scenarios.json`.
- Update `.codex-plugin/plugin.json`, `README.md`, and `CHANGELOG.md` when the public skill surface changes.
- If the new skill adapts third-party MIT material, update `NOTICE` and keep content rewritten for this plugin's workflow instead of importing a full upstream bundle.

## Updating Routing

- Keep hard guardrails ahead of scoring in `scripts/validate_plugin.py`: multi-agent, explicit packaging, packaging failure triage, workflow state, stage, brief, plan, and done routes.
- Add domain keywords to `SKILL_PATTERNS` only after route scenarios describe the expected behavior.
- Add Chinese and English examples when the user-facing wording is likely to be bilingual.
- Preserve forbidden scenarios for `$ue-build-release-automation`.

## Adding Tools

- Tools must be read-only unless a future plan explicitly says otherwise.
- Support `--project` or a similarly explicit input path.
- Support `--format json` for tests and automation.
- Add the tool to `UE_TOOL_SCRIPTS`, `validate_tool_mentions()`, README, and the owning skill.
- Add a unit test under `tests/`.

## Marketplace Package

- Do not edit `plugins/ue-game-dev/` first.
- Edit root files, then run `scripts\sync_marketplace_package.py`.
- `validate_plugin.py` hashes `.codex-plugin/`, `assets/`, `rules/`, `skills/`, `templates/`, `CHANGELOG.md`, `LICENSE`, and `README.md` against the marketplace mirror.
- `update_codex_app_plugin.py` wraps cachebuster updates, marketplace sync, validation, marketplace registration, and Codex App reinstall for local release checks.

## Engineering Flow References

- `mattpocock/skills` is a process reference for diagnosis, TDD, architecture review, and requirement questioning. Summarize the workflow handoff in UE terms; do not copy full external skill text into this plugin.
- Keep UE domain ownership inside `UE Game Dev`: logs and runtime bugs route to `ue-log-crash-triage` or `ue-debug-validation`, test-first feature work routes to `ue-testing-automation`, fuzzy requirements route to `ue-feature-brief`, and old project/module tangles route to `ue-project-onboarding` or `ue-architecture`.
- Document repository conventions, issue tracker expectations, ADR locations, and branch sync rules under `docs/agents/` when they affect future agents.

## Commit Messages

- Use detailed Chinese commit messages for user-facing work.
- Mention the main capability changed, important validation, and whether `ue-game-dev-zh` was synchronized.
