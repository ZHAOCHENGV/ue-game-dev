---
name: ue-blueprint-workflow
description: Unreal Engine Blueprint graph workflow for feature implementation, input events, function chains, event graph edits, Widget Blueprint logic, node and pin wiring, Blueprint/C++ integration, and graph validation. Use when requests involve adding or changing Blueprint logic, designer-authored behavior, keyboard/input graph behavior, pin-level connection guidance, or Blueprint compile/debug work.
---

# UE Blueprint Workflow

Use this skill for Blueprint-first development. Treat Blueprints as a first-class Unreal workflow, not as a fallback for missing C++.

## First Pass

1. Identify the target Blueprint asset, parent class, graph name, and whether the change belongs in Event Graph, function graph, macro, animation graph, construction script, or Widget Blueprint.
2. Confirm the requested behavior as an event -> conditions -> actions -> output chain.
3. Discover related Input Actions, Mapping Contexts, widgets, components, variables, and C++ parent APIs before naming or wiring nodes.
4. Decide whether the request can remain Blueprint-only or should escalate to C++ for reusable runtime logic, custom nodes, replication-heavy behavior, performance, or engine APIs.

## Graph Workflow

- Reuse existing events and functions when present; avoid duplicate key/input events.
- For keyboard features, create or reuse the dedicated input/key event path before guessing generic node classes.
- Build the smallest clear graph: event node, validation guards, branch/sequence as needed, function calls, data assignments, and output feedback.
- Connect execution pins and data pins explicitly. If pin names may vary by node variant, inspect pins before wiring.
- Keep pure functions side-effect free and put state mutation behind explicit exec flow.
- Validate compile status, missing variables, broken pins, latent action context, and runtime ownership assumptions.

## Boundary Hand-Off

- Keep this skill focused on graph behavior and validation.
- Use `references/blueprint-cpp-boundary.md` only when the requested graph change may need a C++ API, custom node, reusable component, or authority-sensitive implementation.
- Use `$ue-cpp-gameplay` after the decision is made to implement the C++ side.

## References

- Read `references/graph-checklist.md` for node/pin, input, and compile validation.
- Read `references/blueprint-cpp-boundary.md` when deciding whether work belongs in Blueprint, C++, or both.
