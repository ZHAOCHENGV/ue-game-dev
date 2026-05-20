---
name: ue-feature-done
description: Use when Unreal Engine work is ready to close out, before claiming completion, committing, handing off, or asking the user to test; especially for C++, Blueprint, assets, modules, UI, networking, tests, performance, packaging readiness, or production-facing changes.
---

# UE Feature Done

## Overview

Use this skill as the UE completion gate. Verify the changed surface, explain Blueprint/asset handoff, list residual risks, and avoid claiming completion without fresh evidence.

## Closeout Workflow

1. Re-read the user's request and any brief/plan to confirm scope.
2. Inspect changed files and asset instructions; do not rely on memory.
3. Run the smallest available verification: targeted build, script validation, JSON/YAML validation, skill validation, automation test, or static check.
4. For Blueprint work, state compile/status expectations and exact graph validation steps.
5. For C++ Blueprint APIs, include the user-facing Blueprint implementation/call steps.
6. For multiplayer/GAS, state server/client validation and authority expectations.
7. For packaging readiness, keep it diagnostic unless the user explicitly asked to package.
8. Report what was verified, what was not verified, and what the user should check in the editor.

## Done Output

Use this shape:

```text
UE Feature Done
- Scope completed:
- Files/assets changed:
- Verification run:
- Blueprint/editor handoff:
- Remaining manual checks:
- Risks or follow-ups:
```

## Completion Rules

- Do not say the work is complete unless a fresh verification command or explicit manual validation path supports it.
- Do not bury unverified Blueprint or asset work.
- Do not turn "ready for packaging" into automatic packaging.
- If verification cannot run locally, say exactly why and provide the next best editor or command-line check.

## References

- Read `references/done-checklist.md` before final handoff or commit.
