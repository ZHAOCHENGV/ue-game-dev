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

## Evidence Order

1. Repro steps and expected vs. observed result.
2. Output Log, compile output, callstack, or Blueprint compile errors.
3. Runtime ownership: world, actor, component, local player, controller, role, and net mode.
4. Asset/config state: map, game mode, plugin, input mapping, data asset, redirector, or class default.
5. Minimal hypothesis and the cheapest command/editor check that can disprove it.

## Console And Editor Tools

- Use `stat unit`, `stat game`, `stat fps`, `stat net`, `stat anim`, `stat audio`, or `stat niagara` when timing or subsystem cost matters.
- Use `showdebug abilitysystem`, `showdebug enhancedinput`, `showdebug animation`, or domain-specific `showdebug` pages when available.
- Use Gameplay Debugger for AI, perception, behavior tree, EQS, and gameplay category overlays.
- Use `Show Navigation`, collision view modes, bounds visualization, and actor/component details for spatial bugs.

## Editor Commandlet Reports

- Use `scripts/ue_editor_command_report.py` to generate DataValidation, CompileAllBlueprints, and MapCheck command lines.
- The helper is read-only because it only prints commands.
- Launching Unreal Editor commandlets requires explicit user approval and should be treated as an external-state-changing validation step.

## Breakpoints And PIE

- Prefer conditional breakpoints or targeted log categories over broad breakpoint sweeps.
- For Blueprint debugging, set the debug object instance before stepping graph execution.
- For PIE multiplayer, name the net mode, client count, dedicated/listen server mode, and which window reproduced the issue.
- Capture role/owner/instigator when debugging RPC, RepNotify, possession, input, or GAS symptoms.

## Validation Workflow

- For C++, run a targeted build or syntax/UHT check.
- For Blueprint, compile the asset and check missing variables, broken pins, duplicate events, latent context, and parent API availability.
- For networking, test server plus at least one client and log role/owner/instigator/prediction key where relevant.
- For assets, verify existence, path, class type, redirectors, and required plugin availability.
- For UI, check focus owner, input mode, viewport size, DPI scale, and widget lifetime.
- For rendering/VFX, validate bounds, scalability level, material parameter values, and platform renderer path.

## Fix Discipline

- Change one hypothesis at a time and rerun the smallest repro.
- Remove temporary logs, debug widgets, console variables, or editor-only helpers before handoff unless they are intentionally kept.
- When the issue touches a more specific domain, route to that skill after evidence identifies the failing owner.

## Common Issues

| Symptom | Likely Cause | First Check |
|---------|--------------|-------------|
| Tick runs but state does not change | Wrong instance, authority guard, or overwritten data | Log object name, role, owner, and the exact value before/after Tick |
| Blueprint node looks wired but does nothing | Debug object mismatch or latent context issue | Set the correct PIE debug object and compile the asset |
| Works in PIE but not packaged | Editor-only reference, missing cook asset, or config difference | Check `WITH_EDITOR`, module dependencies, and packaged logs |
| Multiplayer client disagrees with server | Ownership, RPC direction, or RepNotify order | Log role, remote role, owner, instigator, and replication timestamp |

## References

- Read `references/debug-checklist.md` for fault-domain triage and validation.
- Read `references/debug-templates.md` for log category setup, network debug logging, pointer validation, and console command reference.
