---
name: ue-workflow-state
description: Use when a user asks to create, refresh, read, or use persistent AI-readable memory for an Unreal Engine project, especially Saved/CodexWorkflow notes, project context, module maps, asset indexes, decisions, known risks, old project takeover, or continuing secondary development across sessions.
---

# UE Workflow State

## Overview

Use this skill to turn UE project understanding into small, durable markdown state files that future Codex sessions can read before changing code. Keep state factual, source-linked, and easy to refresh.

## State Location

Default to `Saved/CodexWorkflow/` inside the UE project unless the user requests another location.

| File | Purpose |
|------|---------|
| `project-context.md` | Project snapshot, UE version, modules, plugins, core gameplay/UI/input/networking flows. |
| `module-map.md` | Runtime/editor modules, dependencies, Public/Private boundaries, key classes. |
| `asset-index.md` | Important Content folders and discovered assets by filename, not binary inspection. |
| `decisions.md` | User-approved architecture, naming, Blueprint/C++ split, and workflow decisions. |
| `known-risks.md` | Build, asset, module, Blueprint, networking, packaging, and validation risks. |
| `active-task.md` | Current task scope, touched files, validation path, and handoff notes when useful. |

## Workflow

1. Find the `.uproject`, then read nearby `Source/`, `Plugins/`, `Config/`, `.Build.cs`, `.Target.cs`, and `.uplugin` files.
2. Read existing `Saved/CodexWorkflow/*.md` before creating or refreshing state.
3. Preserve user-approved facts. Mark uncertain items as `Unknown` or `Needs editor inspection`; do not invent Blueprint asset internals.
4. Update only the minimum state files needed for the request.
5. Link each important fact to evidence: file path, class name, asset filename, config section, or log excerpt.
6. After implementation, refresh `active-task.md`, `decisions.md`, and `known-risks.md` when the change affects future work.

## Use With Other Skills

- Use `$ue-project-onboarding` first when the project is unfamiliar and no state exists.
- Use `$ue-stage-detect` to decide which workflow state is missing.
- Use `$ue-implementation-plan` after state is current enough to plan changes.
- Use `$ue-feature-done` to refresh state during closeout.
- Use `$ue-log-crash-triage` to add recurring failures to `known-risks.md`.

## Output

When creating or refreshing state, report:

```text
UE Workflow State
- State folder:
- Files read:
- Files created or updated:
- Facts added:
- Unknowns preserved:
- Recommended next skill:
```

## Boundaries

- Do not edit gameplay code, Blueprint assets, config, or plugins as part of state refresh.
- Do not store secrets, tokens, local machine credentials, or private build service keys.
- Do not treat generated `Intermediate/`, `Binaries/`, or volatile `Saved/Logs/` output as durable truth.
- If state conflicts with source files, trust source files and note the stale state.

## References

- Use `references/state-file-templates.md` when creating the default markdown files.
