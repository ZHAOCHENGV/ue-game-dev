# UE Workflow State Templates

Create only the files that match the user's request. Keep every section short, factual, and source-linked.

## project-context.md

```markdown
# Project Context

- Project:
- Path:
- UE version or EngineAssociation:
- Primary modules:
- Enabled plugins:
- Target platforms:
- Asset conventions:
- Main maps:
- Startup flow:
- Input flow:
- UI flow:
- Gameplay Tags:
- Input/UI/GAS conventions:
- Runtime/Editor split:
- Networking/GAS/AI/rendering notes:
- API verification notes:
- External context references:
  - `CONTEXT.md`:
  - `CONTEXT-MAP.md`:
  - `docs/adr/`:
  - `.agents/ue-project-context.md`:
- Last refreshed:
- Evidence:
```

When these external context files exist, read them as reference material only. Do not overwrite them from `Saved/CodexWorkflow/`; summarize the relevant terms, ADRs, and API verification notes here with source links.

For a fuller production template, use `ue-project-onboarding/references/project-context-template.md`. It keeps the same `Saved/CodexWorkflow/project-context.md` target but expands engine version, modules, plugins, target platforms, asset conventions, Gameplay Tags, input/UI/GAS conventions, Runtime/Editor split, and API verification notes.

## Project Context Template

Use `ue-project-onboarding/references/project-context-template.md` when onboarding or workflow-state refresh needs a stable project context record.
Existing `CONTEXT.md`, `CONTEXT-MAP.md`, `docs/adr/`, and `.agents/ue-project-context.md` are read-only inputs by default; import terminology, decisions, and constraints into `Saved/CodexWorkflow/project-context.md` with source links instead of overwriting the user's documents.

## Freshness

- Last scan time:
- Engine version at scan:
- Git branch at scan:
- Git commit at scan:
- Uproject hash:
- Source module hash summary:
- Config hash summary:
- Stale when:
  - EngineAssociation changes.
  - `.uproject` modules/plugins change.
  - `Source/**.Build.cs` changes.
  - `Config/Default*.ini` changes.

## module-map.md

```markdown
# Module Map

| Module | Type | Dependencies | Key classes | Notes |
|--------|------|--------------|-------------|-------|

## Boundaries
- Runtime modules:
- Editor modules:
- Public headers that are stable APIs:
- Private implementation areas:
```

## asset-index.md

```markdown
# Asset Index

| Asset or folder | Type inferred from name/path | Used by | Notes |
|-----------------|------------------------------|---------|-------|

## Unknowns
- Assets that require editor inspection:
```

## decisions.md

```markdown
# Decisions

| Date | Decision | Reason | Approved by | Evidence |
|------|----------|--------|-------------|----------|
```

## known-risks.md

```markdown
# Known Risks

| Risk | Area | Evidence | Mitigation | Status |
|------|------|----------|------------|--------|
```

## active-task.md

```markdown
# Active Task

- Goal:
- Scope:
- Out of scope:
- Planned files/assets:
- Validation path:
- Current status:
- Handoff notes:
```
