---
name: ue-character-movement
description: Unreal Engine CharacterMovementComponent workflow for walking, falling, jumping, sprinting, dashing, custom movement modes, root motion, network prediction, FSavedMove, client/server correction, movement replication, and multiplayer movement debugging.
---

# UE Character Movement

Use this skill for CharacterMovementComponent behavior, custom movement modes, movement replication, prediction, correction, root motion, sprint/dash mechanics, and locomotion bugs that are owned by character movement rather than animation presentation alone.

## First Pass

1. Identify the movement owner: CharacterMovementComponent, Pawn movement component, Gameplay Ability, animation root motion, or physics impulse.
2. Decide which machine owns the state: autonomous proxy prediction, server authority, simulated proxy smoothing, or cosmetic-only local movement.
3. Locate movement flags, saved moves, compressed flags, replicated variables, root motion sources, and ability activation hooks before proposing changes.
4. Separate movement intent from movement result; clients may predict intent, but the server validates authoritative movement state.
5. Define a multiplayer validation matrix before changing prediction-sensitive code.

## Implementation Rules

- Prefer extending `UCharacterMovementComponent` for reusable movement behavior instead of scattering movement math across Character, Controller, and Ability classes.
- For custom movement, define the prediction contract before code changes: saved move data, compressed flags, correction tolerance, montage/root-motion ownership, and minimum PIE/dedicated-server validation.
- Keep root motion ownership explicit. If GAS drives a montage or root motion source, route prediction and cancellation details through `$ue-gas-networking`.
- Avoid fixing server corrections by hiding visual smoothing only; investigate divergent client/server inputs, acceleration, velocity, movement mode, and timestamps.
- Keep animation Blueprint state machines downstream of movement state unless the project intentionally uses animation to author movement.

## Verification

- Run two-client PIE for sprint, dash, jump, and custom movement transitions.
- Test listen server and dedicated server when prediction or corrections are involved.
- Use `p.NetShowCorrections 1`, network emulation, logs, and replicated state inspection to prove corrections are acceptable.
- Validate packaged behavior for platform-specific input, frame rate, and movement smoothing differences.

## References

- Use `references/movement-prediction-matrix.md` for authority, prediction, correction, and evidence planning.
- Use `$ue-gas-networking` when movement is ability-driven or prediction-key dependent.
- Use `$ue-animation` when the issue is montage, state machine, root motion extraction, or pose presentation.
- Use `$ue-debug-validation` when the current evidence is unclear and a reproducible movement diagnosis loop is needed.
