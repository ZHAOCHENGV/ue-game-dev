# UE Blueprint Rules

- Keep Blueprint graphs readable: small functions, clear event ownership, no duplicate input events.
- Prefer Blueprint for designer-authored tuning, composition, UI behavior, animation/VFX hooks, and simple event wiring.
- Prefer C++ for reusable systems, authority-sensitive logic, performance-sensitive loops, and stable APIs.
- Always state exact node search names, exec pins, data pins, target objects, and compile validation.
- When using Enhanced Input, verify `IA_` assets, `IMC_` mapping contexts, trigger pins, value type, and subsystem context addition.
- Do not assume `.uasset` content can be inspected as text; use filenames and ask for editor details when needed.
- Validate Blueprint compile status and PIE/editor behavior before claiming done.
