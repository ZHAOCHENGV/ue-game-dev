---
name: ue-log-crash-triage
description: Use when a user provides or asks to analyze Unreal Engine logs, UBT compile errors, UHT reflection errors, linker errors, Blueprint compile errors, Editor crashes, callstacks, ensure/assert failures, UAT packaging failures, Cook errors, or Saved/Logs output before proposing fixes.
---

# UE Log Crash Triage

## Overview

Use this skill to diagnose Unreal logs and crashes from evidence before changing code. Find the first actionable failure, classify the subsystem, and produce fix or verification steps.

## Evidence Order

1. Prefer pasted error text, explicit log file paths, or the newest relevant file under `Saved/Logs/`.
2. For build failures, inspect UBT/UHT output from the first `error:` or `Error:` line upward for context.
3. For crashes, inspect the fatal line, callstack top frames, module names, and the last gameplay/editor actions before crash.
4. For packaging failures, separate Build, Cook, Stage, Pak/IoStore, Archive, and Deploy phases.
5. For Blueprint failures, identify the asset path, parent class, missing variable/function, broken pin, duplicate event, or invalid latent context.

## Phase-Aware Triage

Classify the earliest actionable failure before summarizing the final UAT or Cook failure.
Do not treat `AutomationTool exiting`, `UnknownCookFailure`, or `BUILD FAILED` as the root cause when an earlier UHT, linker, Blueprint, asset, or assertion line exists.

## Classification

| Signal | Likely route |
|--------|--------------|
| `UnrealHeaderTool`, `UCLASS`, `UPROPERTY`, generated header | `$ue-cpp-gameplay` or `$ue-plugin-module-dev` |
| `LNK`, unresolved external, module dependency | `$ue-architecture` or `$ue-plugin-module-dev` |
| `Blueprint Runtime Error`, compile failed, broken pin | `$ue-blueprint-workflow` |
| `PackagingResults`, `Cook failed`, `RunUAT`, `BuildCookRun` | `$ue-performance-packaging`; explicit packaging remains `$ue-build-release-automation` only when requested |
| `Fatal error`, `Assertion failed`, `ensure`, access violation | `$ue-debug-validation` after triage |
| RPC, NetDriver, prediction, authority, replicated property | `$ue-gas-networking` or `$ue-save-load-sync` |
| Slate, ToolMenus, editor module startup/shutdown | `$ue-editor-tooling-slate` |

## Triage Workflow

1. State the exact log source and timestamp if known.
2. Extract the first actionable error, not just the final summary.
3. Explain the probable root cause and why downstream errors are secondary.
4. List the minimum files/assets/config to inspect next.
5. Provide a narrow fix plan and a verification command or editor check.
6. If the issue is recurring or project-specific, suggest recording it with `$ue-workflow-state` in `known-risks.md`.

## Tooling

- Use `scripts/ue_log_triage.py --log <path> --format json` when a log file path is available and a quick first-failure extraction will help.
- The tool is read-only and returns the first actionable failure, phase classification, short evidence, probable root cause, and recommended next skill.
- For packaging failures, the tool keeps `packaging_boundary` as `review only`; it must not trigger `$ue-build-release-automation`.

## Output

```text
UE Log/Crash Triage
- Log source:
- First actionable failure:
- Failure phase:
- Probable root cause:
- Evidence:
- Next files/assets to inspect:
- Recommended fix path:
- Verification:
- Recommended next skill:
```

## Boundaries

- Do not guess from the last line if an earlier error explains it.
- Do not run packaging automation unless the user explicitly asks to package or run BuildCookRun.
- Do not edit code during triage unless the user asks for a fix after the diagnosis.
- Preserve uncertainty when logs are truncated; ask for the missing section around the first error.

## Common Issues

| Symptom | Likely Cause | First Check |
|---------|--------------|-------------|
| `Cook failed` after many warnings | Earlier asset load, Blueprint compile, or missing class error | Search upward for the first `Error:` before `Cook failed` |
| Linker unresolved external | Missing implementation, module dependency, or API macro | Inspect the symbol owner and `.Build.cs` dependencies |
| Blueprint compile error | Broken pin, renamed member, or missing parent API | Open the named Blueprint and compile it after C++ build |
| Crash callstack ends in engine code | Project callback passed invalid data earlier | Find the first project frame above engine frames |

## References

- Use `references/triage-report-template.md` for structured reports.
- Use `$ue-debug-validation` when logs point to runtime behavior that needs reproduction.
