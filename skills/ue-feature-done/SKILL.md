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
8. Produce a verification evidence table; use `templates/ue-test-evidence.md` when the user wants a saved artifact.
9. Report what was verified, what was not verified, and what the user should check in the editor.

## Done Output

Use this shape:

```text
UE Feature Done
- Scope completed:
- Files/assets changed:
- Verification run:
- Evidence table:
- Blueprint/editor handoff:
- Remaining manual checks:
- Risks or follow-ups:
```

## Evidence Table

Include this table in closeout responses:

| Check | Evidence | Result |
|-------|----------|--------|
| Targeted build | command or reason not run | PASS / CONCERNS / FAIL |
| Blueprint compile | asset/class and expected status | PASS / CONCERNS / FAIL / N/A |
| PIE/editor smoke | scenario | PASS / CONCERNS / FAIL / N/A |
| Automated test | command/filter | PASS / CONCERNS / FAIL / N/A |
| Multiplayer | client count / authority path | PASS / CONCERNS / FAIL / N/A |
| Packaging risk | readiness check or explicit package command | PASS / CONCERNS / FAIL / N/A |

## Completion Rules

- Do not say the work is complete unless a fresh verification command or explicit manual validation path supports it.
- Do not bury unverified Blueprint or asset work.
- Do not turn "ready for packaging" into automatic packaging.
- If verification cannot run locally, say exactly why and provide the next best editor or command-line check.

## References

- Read `references/done-checklist.md` before final handoff or commit.
- Use `templates/ue-test-evidence.md` if the user asks to save a verification record.
