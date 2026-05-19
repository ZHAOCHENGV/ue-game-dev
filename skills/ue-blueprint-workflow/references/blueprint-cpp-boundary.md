# Blueprint And C++ Boundary

## Prefer Blueprint When

- Designers need to tune values or compose behavior.
- The change is simple event wiring, UI behavior, animation, timeline, VFX/audio hook, or content-driven logic.
- Iteration speed matters more than reusable runtime architecture.

## Prefer C++ When

- Behavior is reused across many Blueprints.
- Logic is performance-sensitive or runs often.
- Network authority, prediction, save/load, or replication correctness matters.
- The feature needs custom components, subsystems, latent actions, async work, or low-level engine APIs.

## Prefer Hybrid When

- C++ should own state and validation while Blueprint owns presentation and tuning.
- A system needs stable APIs but designers still need extension points.
- The task combines gameplay, UI, VFX, and data assets.
