# Blueprint Graph Checklist

## Before Editing

- Confirm target asset path, parent class, graph name, and whether the graph is event/function/macro/widget/animation.
- Discover existing variables, functions, events, components, Input Actions, and Mapping Contexts.
- Check whether a C++ parent already exposes the needed API.

## Input Events

- Reuse existing input/key/action events when present.
- Avoid duplicate input events that compete in the same graph.
- For Enhanced Input, verify action asset names and mapping context setup before binding graph behavior.

## Node And Pin Wiring

- Build event -> guard -> action -> feedback flow.
- Inspect node pins when names or types may differ by node variant.
- Keep data pins type-compatible; add conversions intentionally.
- Avoid hidden side effects in pure functions.

## Validation

- Compile the Blueprint.
- Check broken pins, missing variables, stale references, latent action context, and parent class API changes.
- Validate runtime ownership, especially player controller, pawn, widget, and actor component references.
