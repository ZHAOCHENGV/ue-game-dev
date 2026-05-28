---
name: ue-character-movement
description: Unreal Engine CharacterMovementComponent workflow for movement modes, custom movement, root motion, network prediction, movement replication, smoothing, floor checks, acceleration, braking, crouch/jump/falling/swimming/flying, ability-driven movement, and locomotion debugging. Use when requests involve CharacterMovementComponent, character locomotion, custom movement modes, movement prediction, replicated movement, or movement tuning.
---

# UE Character Movement

Use this skill for CharacterMovementComponent, locomotion tuning, custom movement modes, and replicated character movement. Keep prediction, animation, and authority boundaries explicit.

## First Pass

1. Read the character class, movement component subclass, controller input path, animation blueprint, ability hooks, and project movement settings.
2. Identify the movement concern: tuning, jump/fall/crouch/swim/fly, custom mode, root motion, network prediction, smoothing, collision, or animation mismatch.
3. Map authority: local input, client prediction, server correction, simulated proxy smoothing, replicated movement, and ability-driven movement.
4. Check collision capsule, floor checks, step height, slope limits, braking, acceleration, gravity scale, and movement mode transitions before changing code.
5. Define validation: local PIE feel, two-client correction behavior, animation sync, root motion, and edge surfaces.

## Movement Rules

- Prefer CharacterMovementComponent settings for standard locomotion before adding custom movement code.
- Use custom movement modes only when built-in walking/falling/swimming/flying/customizable settings cannot express the behavior.
- Keep movement input, movement simulation, and animation state separated.
- Treat root motion and network prediction carefully; define which source owns displacement.
- For ability-driven movement, state whether GAS starts movement, locks input, applies root motion, or only tags movement state.

## Networking Rules

- Server remains authoritative for movement; clients predict local movement and reconcile corrections.
- Log movement mode, role, velocity, acceleration, base, prediction/correction state, and root motion state when debugging.
- Validate listen server and dedicated server behavior separately when movement affects combat or traversal.
- Avoid multicast movement hacks when CharacterMovement replication or GAS root motion sources are the correct model.

## Integration Rules

- Use `$ue-animation` when locomotion state machine, blend space, montage, root motion authoring, or IK is the main issue.
- Use `$ue-gas-networking` when movement is ability-driven, tag-gated, predicted by GAS, or tied to GameplayEffects.
- Use `$ue-physics-destruction` when the issue is collision profile, physical material, ragdoll, or physics simulation.

## References

- Read `references/character-movement-checklist.md` before tuning CharacterMovementComponent, adding custom movement, or debugging replicated locomotion.
