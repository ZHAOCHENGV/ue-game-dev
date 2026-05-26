# World Interaction Checklist

## Interaction Models

- Overlap: proximity-based, needs collision setup and duplicate guard.
- Trace: camera/cursor/use-key based, needs channel and range policy.
- Explicit target: UI-selected or lock-on, needs validity refresh.
- Ability targeting: integrate with GAS target data and authority rules.

## Trace Vs Overlap

- Use trace when intent should come from camera, cursor, crosshair, or use-key direction.
- Use overlap when proximity should reveal candidates or auto-trigger lightweight affordances.
- Combine overlap for candidate discovery with trace for final confirmation when dense interactables compete.
- Define collision channel, object types, range, radius, and ignored actors before wiring gameplay results.

## Contract

- Prefer a Blueprint Interface or component API when many actor classes can be interacted with.
- Keep functions explicit: `CanInteract`, `GetInteractionText`, `BeginFocus`, `EndFocus`, `Interact`.
- Return failure reasons for UI feedback and automated validation.
- Keep durable outcomes server-authoritative in multiplayer.

## Validation

- Actor/component validity.
- Distance/radius.
- Line of sight or trace hit.
- Collision response.
- Player ownership.
- Inventory/capacity/cooldown.
- Server authority for durable results.

## Lifecycle

- Spawn.
- Activate.
- Become interactable.
- Resolve success/failure.
- Disable/destroy/respawn/pool.
- Save or replicate state when required.
- Handle actor destruction while focused or while an interaction is pending.
- Define respawn, pooling, or one-time pickup rules.

## Feedback

- UI prompt.
- Highlight/outline.
- Audio/VFX.
- Failure reason.
- Replicated confirmation for multiplayer.
- Accessibility-friendly text/icon feedback when prompts are player-facing.
