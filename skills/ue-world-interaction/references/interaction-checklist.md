# World Interaction Checklist

## Interaction Models

- Overlap: proximity-based, needs collision setup and duplicate guard.
- Trace: camera/cursor/use-key based, needs channel and range policy.
- Explicit target: UI-selected or lock-on, needs validity refresh.
- Ability targeting: integrate with GAS target data and authority rules.

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

## Feedback

- UI prompt.
- Highlight/outline.
- Audio/VFX.
- Failure reason.
- Replicated confirmation for multiplayer.
