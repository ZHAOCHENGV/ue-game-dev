---
name: ue-stage-detect
description: Use when a user asks where an Unreal Engine project stands, what workflow stage it is in, what is missing before implementation/testing/packaging, or wants a read-only stage and gap analysis for an existing UE project.
---

# UE Stage Detect

## Overview

Use this skill for read-only UE project stage detection. Scan project artifacts, classify the current workflow stage, identify gaps, and recommend the next UE skill without editing project files.

## Stage Model

| Stage | Meaning |
|-------|---------|
| Onboarding | Existing project must be understood before changes. |
| Feature Brief | Request is known but scope, ownership, or assets are unclear. |
| Implementation Plan | Requirements are clear enough to split C++, Blueprint, assets, config, and tests. |
| Implementation | Work is actively changing code/assets. |
| Validation | Feature needs build, Blueprint compile, PIE, automation, or asset validation. |
| Packaging Readiness | Project needs release readiness, cook/package diagnostics, or performance checks. |
| Explicit Packaging | User explicitly asks to package/build/archive with RunUAT, BuildCookRun, Project Launcher, or CI. |

## Detection Workflow

1. Locate `.uproject`, `Source/`, `Plugins/`, `Config/`, `Content/`, target files, `.uplugin`, and existing `Saved/CodexWorkflow/` state files if present.
2. Count and classify evidence:
   - Existing project structure and modules.
   - Feature brief/task files.
   - C++/Blueprint asset naming signals.
   - Test files, automation specs, functional maps, or validation notes.
   - Build/package scripts, logs, or release artifacts.
3. Prefer explicit user intent over heuristics. "打包" with `RunUAT` means Explicit Packaging; "是否能打包" means Packaging Readiness.
4. Report gaps as questions or next actions, not as silent assumptions.
5. Do not create or update `Saved/CodexWorkflow/` unless the user explicitly asks to establish persistent workflow state.

## Output

```text
UE Stage Report
- Detected stage:
- Confidence:
- Evidence:
- Missing or risky artifacts:
- Recommended next skill:
- Suggested state files, if the user wants persistence:
```

## References

- Read `references/stage-report-template.md` when producing a structured report.
- Use `$ue-project-onboarding` for old project read-only analysis.
- Use `$ue-gate-check` when the user asks whether the project is ready to advance.
