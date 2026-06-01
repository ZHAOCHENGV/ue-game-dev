---
name: ue-input-enhanced
description: Use when Unreal Engine requests involve Enhanced Input, Input Actions, Input Mapping Contexts, input modifiers/triggers, player controller or pawn input binding, runtime mapping changes, key rebinding, UI focus/input mode conflicts, local multiplayer input, or debugging input events that do not fire.
---

# UE Enhanced Input

## Overview

Use this skill for UE5 Enhanced Input design, implementation, Blueprint handoff, and debugging. Treat input as a chain from asset setup to local player subsystem, possession, binding, UI focus, and gameplay authority.

## First Pass

1. Confirm the project uses Enhanced Input and has the `EnhancedInput` module/plugin enabled.
2. Discover existing `IA_`, `IMC_`, Player Controller, Pawn/Character, HUD/UI, and save/settings assets before creating new input assets.
3. Identify ownership: who adds mapping contexts, who binds actions, who owns rebinding, and whether UI can consume input.
4. Confirm player lifecycle: controller creation, possession, `BeginPlay`, `SetupPlayerInputComponent`, seamless travel, respawn, split-screen, and multiplayer authority.
5. Decide whether the change belongs in C++, Blueprint, or hybrid:
   - C++ for stable binding, reusable components, settings persistence, custom triggers/modifiers, and network-sensitive commands.
   - Blueprint for designer-authored action responses, UI prompts, simple mapping setup, and iteration.
   - Hybrid when C++ exposes actions/events and Blueprint owns presentation or tuning.

## Implementation Workflow

1. Define Input Actions first: value type, trigger events, modifiers, and naming.
2. Add or update Input Mapping Contexts with priority rules and platform-specific bindings.
3. Add mapping contexts through `UEnhancedInputLocalPlayerSubsystem` for the correct local player.
4. Bind actions through `UEnhancedInputComponent` in the pawn/character/controller that owns the behavior.
5. Keep handler functions small: validate input value, call gameplay method, update state, then notify Blueprint/UI when needed.
6. For multiplayer, do not trust client-only input for authoritative state; route state changes through the correct server RPC or ability activation path.
7. For UI, state the active input mode, focus target, CommonUI/input routing if present, and whether gameplay mappings should remain active.

## Blueprint Handoff

When adding or changing input behavior that is visible to Blueprint, include exact Blueprint steps:

- Asset names to create or edit, such as `IA_Jump`, `IA_Move`, `IMC_Player`.
- Where to add mapping context nodes or which C++ class adds them.
- Which Event Graph node to search for, such as `Enhanced Input Action IA_Jump`.
- Trigger pin to use: `Started`, `Triggered`, `Completed`, `Canceled`, or `Ongoing`.
- Value pin type and conversion: bool, float, `Vector2D`, or `Vector`.
- Exec/data pin wiring, target actor/component, and validation prints or on-screen feedback.
- Compile/save steps and PIE test scenario.

## Debugging Rules

- If an input event does not fire, check mapping context addition before changing gameplay code.
- If it fires in one pawn but not another, check possession and `SetupPlayerInputComponent`.
- If keyboard works but gamepad does not, check action value type, mappings, and controller device assignment.
- If UI breaks gameplay input, check input mode, focus, CommonUI activation, and whether UI consumes the action.
- If rebinding does not persist, check settings save/load and when mapping contexts are rebuilt.
- If a C++ action is Blueprint-exposed, pair the C++ API with graph-level implementation instructions.

## Common Issues

| Symptom | Likely Cause | First Check |
|---------|--------------|-------------|
| Action never fires | Mapping context was not added to the local player subsystem | Log `AddMappingContext` owner and priority |
| Action fires twice | Duplicate binding in C++ and Blueprint or repeated setup | Inspect `SetupPlayerInputComponent` and Event Graph input nodes |
| UI consumes gameplay input | Input mode/focus/CommonUI activation owns the action | Check focused widget and active mapping contexts |
| Rebind disappears after restart | Settings were not saved or contexts rebuilt from defaults | Check save slot/config write and reload order |

## References

- Read `references/enhanced-input-checklist.md` for asset setup, binding, and validation.
- Read `references/rebinding-and-ui.md` for runtime mapping changes, user key rebinding, UI focus, and CommonUI/input mode issues.
