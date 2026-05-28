# Character Movement Checklist

Use this checklist for CharacterMovementComponent tuning, custom movement modes, network prediction, root motion, and locomotion bugs.

## Discovery

- Locate character class, movement component class, controller input binding, animation blueprint, ability hooks, and movement config values.
- Check capsule size, collision profile, floor checks, step height, slope limit, braking, acceleration, gravity, and movement mode transitions.
- Identify whether motion comes from input, CharacterMovement simulation, root motion, launch/impulse, ability task, or physics.

## Networking

- Confirm local role, remote role, owner, autonomous proxy, simulated proxy, and server correction behavior.
- Reproduce with two clients when movement affects gameplay.
- Log velocity, acceleration, movement mode, base actor, root motion state, and correction events.

## Custom Movement

- Define entry and exit conditions.
- Keep physics update deterministic enough for prediction.
- Avoid mixing manual transform updates with CharacterMovement unless explicitly synchronized.
- Provide animation state handoff for custom modes.

## Evidence

- Local PIE movement feel check.
- Two-client correction or smoothing check when network-visible.
- Animation/root motion sync note when locomotion visuals are involved.
