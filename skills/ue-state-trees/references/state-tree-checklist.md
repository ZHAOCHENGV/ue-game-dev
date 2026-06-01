# StateTree Checklist

Use this checklist for StateTree assets, C++ or Blueprint tasks, evaluators, conditions, transitions, and AI/gameplay state machines.

## Discovery

- Locate StateTree assets, schemas, task classes, evaluator classes, conditions, and owning actors or AI controllers.
- Identify the external data sources and whether they are authoritative, local-only, replicated, or transient.
- Check whether existing project convention prefers Behavior Tree, StateTree, Mass StateTree, or component FSM.

## Design Review

- State names describe domain meaning.
- Transitions and conditions are explicit.
- Tasks have clear enter, tick, completion, abort, and exit behavior.
- Evaluators gather data without mutating gameplay state unexpectedly.
- Linked assets and reusable tasks do not hide dependencies.

## Evidence

- StateTree debugger or log evidence for active state and transition.
- PIE scenario for success, failure, and abort path.
- Multiplayer note when state controls authoritative gameplay.
