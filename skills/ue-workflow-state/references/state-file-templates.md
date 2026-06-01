# UE Workflow State Templates

Create only the files that match the user's request. Keep every section short, factual, and source-linked.

## project-context.md

```markdown
# Project Context

- Project:
- Path:
- UE version or EngineAssociation:
- Engine source/API baseline:
- Target platforms:
- Primary modules:
- Enabled plugins:
- Game Feature plugins:
- Main maps:
- Startup flow:
- Input flow:
- Input/UI/GAS conventions:
- UI flow:
- Gameplay Tags:
- Networking/GAS/AI/rendering notes:
- Asset conventions:
- C++ conventions:
- Blueprint conventions:
- Runtime/Editor split:
- API verification notes:
- Imported context:
  - `CONTEXT.md` present:
  - `CONTEXT-MAP.md` present:
  - `docs/adr/` present:
  - `.agents/ue-project-context.md` present:
  - Read-only import summary:
- Last refreshed:
- Evidence:
```

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
