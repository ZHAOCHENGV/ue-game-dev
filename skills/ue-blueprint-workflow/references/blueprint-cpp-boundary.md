# Blueprint And C++ Boundary

## Prefer Blueprint When

- Designers need to tune values or compose behavior.
- The change is simple event wiring, UI behavior, animation, timeline, VFX/audio hook, or content-driven logic.
- Iteration speed matters more than reusable runtime architecture.
- The behavior is local presentation and failure cost is low.
- The graph depends on assets that designers are expected to swap or tune.

## Prefer C++ When

- Behavior is reused across many Blueprints.
- Logic is performance-sensitive or runs often.
- Network authority, prediction, save/load, or replication correctness matters.
- The feature needs custom components, subsystems, latent actions, async work, or low-level engine APIs.
- The API must stay stable across multiple teams, modules, or plugin boundaries.
- The task needs automated tests around pure gameplay logic.

## Prefer Hybrid When

- C++ should own state and validation while Blueprint owns presentation and tuning.
- A system needs stable APIs but designers still need extension points.
- The task combines gameplay, UI, VFX, and data assets.
- Blueprint should call narrow C++ commands and respond to delegates/events.

## Decision Questions

1. Who owns durable state: server, component, subsystem, save slot, or widget?
2. How often does the logic run: once, on input, on event, on tick, or per particle/actor?
3. Who must iterate on it: programmer, designer, UI artist, animator, or technical artist?
4. What must be validated: build, Blueprint compile, PIE, multiplayer, save/load, or packaged runtime?

## Boundary Examples

- Inventory count: C++ component owns data; Blueprint widget listens to change event and refreshes text.
- Door interaction: Blueprint can own simple animation; C++ or component owns locked/unlocked state if reused or replicated.
- Ability activation: GAS/C++ owns authority and prediction; Blueprint owns montage, cue, and UI presentation hooks.
- UI button: Widget Blueprint owns visual click flow; PlayerController/subsystem handles gameplay command.
