# Contributing To UE Game Dev

## Development Flow

1. Work from `main` for the primary plugin version.
2. Keep root plugin files as the source of truth.
3. After edits, run `python scripts\sync_marketplace_package.py` to refresh `plugins/ue-game-dev/`.
4. Run validation before committing:

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```

5. To refresh the installed Codex App plugin after local edits, run:

```powershell
python scripts\update_codex_app_plugin.py
```

This updates the Codex cachebuster, syncs `plugins/ue-game-dev/`, validates the plugin, and runs `codex plugin add ue-game-dev@zhaochengv-ue` against the current user's Codex home. If the marketplace is still pointing at an older checkout, use:

```powershell
python scripts\update_codex_app_plugin.py --replace-marketplace
```

6. When plugin content changes, apply the same structural change to `ue-game-dev-zh` and localize skill explanations, comments, and prose to Chinese while preserving code, commands, paths, UE APIs, skill names, and `$ue-*` references.
7. Push both `main` and `ue-game-dev-zh` to GitHub after validation when the change affects public plugin behavior, marketplace metadata, routing, or Codex App installation.
8. When changing workflow-state templates, update both the root skill files and the mirrored `plugins/ue-game-dev` package, then refresh the local Codex App installation and push both `main` and `ue-game-dev-zh`.

## Engineering Flow References

- This repository may reference mattpocock/skills for process ideas such as `diagnose`, `tdd`, `grill-with-docs`, and `improve-codebase-architecture`.
- Do not vendor or copy those skills into UE Game Dev. Keep UE Game Dev focused on Unreal Engine workflow routing and mention those external skills only as optional handoffs.
- Keep the project-specific agent rules in `docs/agents/repo-workflow.md` aligned with this file when release, branch, or issue-tracking workflow changes.

## Adding A Skill

- Create `skills/<skill-name>/SKILL.md`, `skills/<skill-name>/agents/openai.yaml`, and at least one useful `references/*.md`.
- `SKILL.md` frontmatter must include `name` and `description`.
- Route the skill from `skills/ue-game-dev-router/SKILL.md`.
- Add route scenarios to `tests/route_scenarios.json`.
- Update `.codex-plugin/plugin.json`, `README.md`, and `CHANGELOG.md` when the public skill surface changes.

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

## Commit Messages

- Use detailed Chinese commit messages for user-facing work.
- Mention the main capability changed, important validation, and whether `ue-game-dev-zh` was synchronized.
