---
name: ue-gate-check
description: Use when a user asks whether an Unreal Engine project or feature is ready to move to implementation, validation, packaging readiness, or explicit release packaging, or wants a PASS/CONCERNS/FAIL gate verdict with blockers and evidence.
---

# UE Gate Check

## Overview

Use this skill for formal UE readiness checks between workflow stages. A gate verdict is advisory: report evidence and blockers, then let the user decide whether to proceed.

## Gate Types

| Gate | Checks |
|------|--------|
| Onboarding -> Brief | Project shape understood, safe extension points identified, no implementation before read-only report. |
| Brief -> Plan | Goal, ownership, Blueprint/C++ split, assets, constraints, and validation path are clear. |
| Plan -> Implementation | Files/assets, modules, dependencies, risks, and verification commands are identified. |
| Implementation -> Validation | Changed surface has build/Blueprint/PIE/test path and handoff notes. |
| Validation -> Packaging Readiness | Tests, asset references, module boundaries, runtime/editor split, and platform settings are reviewed. |
| Packaging Readiness -> Explicit Packaging | User explicitly asks to run/generate packaging automation; otherwise do not advance to automatic packaging. |

## Gate Workflow

1. Resolve requested gate or infer it from the user's wording.
2. Read local evidence: `.uproject`, modules, plans/briefs, changed files, validation logs, tests, package logs, and `Saved/CodexWorkflow/` notes when present.
3. For each required item, mark `PASS`, `CONCERNS`, `FAIL`, or `MANUAL`.
4. Use `FAIL` for missing artifacts that make the next phase unsafe, such as no `.uproject`, no owning module, no validation path for C++ changes, or automatic packaging without explicit user intent.
5. Use `CONCERNS` for gaps that can be addressed early in the next stage.
6. Never create missing artifacts just to pass the gate.

## Output

```text
UE Gate Check: <from> -> <to>
- Verdict: PASS / CONCERNS / FAIL
- Evidence checked:
- Required checks:
- Blockers:
- Advisory concerns:
- Recommended next skill:
- Optional state update:
```

## Required Boundaries

- Automatic packaging remains explicit-only. "Ready to package?" can pass into `$ue-performance-packaging`, not `$ue-build-release-automation`.
- Blueprint work must include compile and graph validation.
- C++ Blueprint API changes must include Blueprint node/pin handoff.
- Networking/GAS work must include authority and PIE/multiplayer validation.

## References

- Read `references/gate-check-template.md` for checklist output.
- Use `$ue-stage-detect` first when the current stage is unclear.
