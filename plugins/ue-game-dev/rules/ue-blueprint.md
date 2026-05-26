# UE Blueprint Rules

## Graph Shape

- Keep Blueprint graphs readable: small functions, clear event ownership, no duplicate input events.
- Prefer one visible execution story per graph; move reusable logic into functions, macros, components, or C++.
- Name custom events by intent, not by implementation detail.
- Always state exact node search names, exec pins, data pins, target objects, and compile validation.

## Blueprint And C++ Boundary

- Prefer Blueprint for designer-authored tuning, composition, UI behavior, animation/VFX hooks, and simple event wiring.
- Prefer C++ for reusable systems, authority-sensitive logic, performance-sensitive loops, and stable APIs.
- Keep authoritative gameplay state out of arbitrary widgets and level-only Blueprints.
- Use Blueprint Interfaces or event dispatchers when the caller should not know the concrete class.

## Input And Events

- Do not bind the same key or Enhanced Input action in multiple unrelated Blueprints.
- When using Enhanced Input, verify `IA_` assets, `IMC_` mapping contexts, trigger pins, value type, and subsystem context addition.
- Put local player input routing in PlayerController, Pawn, or an input component owner; keep UI focus handoff explicit.

## Widget Blueprint Updates

- Prefer explicit refresh events over expensive per-frame property bindings.
- Use timers or invalidation-friendly updates for UI that changes periodically.
- Avoid Tick-driven widget animation when Sequencer, UMG animation, timers, or state changes are enough.
- Keep widgets as presentation surfaces; route inventory, save data, and network authority through gameplay owners or view models.

## Anti-Patterns

- Long Event Graphs with unrelated workflows mixed together.
- Repeated key/input events in multiple Blueprints.
- Per-frame casts, broad `Get All Actors Of Class`, or expensive UI bindings.
- Deep Cast chains where an interface, component lookup, or C++ API would be clearer.
- Hidden authoritative state mutation from arbitrary widgets.
- Copy-pasted graph islands that should be a function, macro, component, or C++ helper.

## Validation

- Do not assume `.uasset` content can be inspected as text; use filenames and ask for editor details when needed.
- Validate Blueprint compile status, runtime warnings, and PIE/editor behavior before claiming done.
- For graph instructions, include the expected visible result and the first check a designer can run in the editor.
