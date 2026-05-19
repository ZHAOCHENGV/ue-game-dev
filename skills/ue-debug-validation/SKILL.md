---
name: ue-debug-validation
description: Unreal Engine debugging and validation workflow for output logs, asset checks, Blueprint compile issues, C++ failures, networking bugs, editor configuration, repro isolation, and regression triage. Use when requests involve troubleshooting why gameplay/UI/rendering does not work, validating expected behavior, narrowing a minimal repro, or producing concrete fix steps.
---

# UE Debug Validation

Use this skill when the main task is to learn what is actually failing before changing code.

## First Pass

1. Reproduce the issue with the smallest clear steps.
2. Collect recent logs, compile output, Blueprint compile status, relevant asset/class state, and net mode if applicable.
3. Classify the fault domain: data asset, Blueprint graph, C++, networking, rendering/VFX, UI focus, editor config, plugin, or packaging.
4. Compare expected behavior with observed behavior at each pipeline stage.

## Debug Workflow

- Start with observable evidence: logs, warnings, missing assets, invalid references, failed casts, ensure/crash lines, broken pins, and replicated role mismatch.
- Isolate the first bad transition, not every downstream symptom.
- Keep fixes narrow while diagnosing.
- If multiple hypotheses remain, rank them by probability and verification cost.
- Add temporary instrumentation only where it answers a specific question.

## Validation Workflow

- For C++, run a targeted build or syntax/UHT check.
- For Blueprint, compile the asset and check missing variables, broken pins, duplicate events, latent context, and parent API availability.
- For networking, test server plus at least one client and log role/owner/instigator/prediction key where relevant.
- For assets, verify existence, path, class type, redirectors, and required plugin availability.

## References

- Read `references/debug-checklist.md` for fault-domain triage and validation.
- Read `references/debug-templates.md` for log category setup, network debug logging, pointer validation, and console command reference.
