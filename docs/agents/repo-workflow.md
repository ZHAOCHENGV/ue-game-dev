# UE Game Dev Agent Workflow

## Issue Tracker

Track public work on GitHub for `zhaocw/ue-game-dev`. Local planning notes may live under `docs/superpowers/plans/`, but public plugin changes should be synchronized to GitHub branches.

## Domain Docs

This repository has a single plugin context. Use `README.md`, `docs/architecture.md`, `CONTRIBUTING.md`, and skill-local `references/*.md` as source-of-truth documentation. UE project memory generated for a user's game belongs in that project's `Saved/CodexWorkflow/`, not in this plugin repository.

## External Engineering Skills

`UE Game Dev` keeps Unreal routing and domain guidance in this plugin. When useful, it may hand off process discipline to local mattpocock/skills-style skills:

- `diagnose` for reproduce, minimize, hypotheses, instrumentation, fix, and regression-test loops after UE log or runtime triage.
- `tdd` for test-first implementation after UE automation or implementation planning identifies the behavior to lock down.
- `grill-with-docs` for fuzzy feature requests, overloaded domain terms, or plans that need pressure-testing against project language and ADRs.
- `improve-codebase-architecture` for old UE projects, shallow modules, weak test seams, Runtime/Editor dependency leaks, or architecture reviews.

Do not copy those skills into this plugin. Reference their names as optional handoffs only.

## Release Sync

After any public plugin change, run the validation sequence from `CONTRIBUTING.md`, sync `plugins/ue-game-dev/`, refresh the local Codex App install with `scripts/update_codex_app_plugin.py` when needed, then synchronize both `main` and `ue-game-dev-zh` to GitHub.

## Release Sync Checklist

1. Run validation on the implementation branch.
2. Merge or fast-forward `main`.
3. Run `python scripts\sync_marketplace_package.py`.
4. Run `python scripts\update_codex_app_plugin.py`.
5. Push `main`.
6. Fast-forward or merge `ue-game-dev-zh`.
7. Push `ue-game-dev-zh`.
8. Confirm Codex App plugin list shows `UE Game Dev` and readable Chinese prompts.
