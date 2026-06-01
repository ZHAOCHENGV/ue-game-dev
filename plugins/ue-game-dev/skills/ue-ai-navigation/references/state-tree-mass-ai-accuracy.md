# StateTree And Mass AI Accuracy Notes

Use this reference when an AI/navigation request mentions StateTree, Mass Entity, crowd AI, or a mix of Behavior Trees and newer UE AI frameworks.

## Routing Boundary

- Use this AI/navigation skill for Behavior Tree, Blackboard, EQS, NavMesh, AI Controller, AI Perception, and traditional autonomous agents.
- Route to `$ue-state-trees` when the task is primarily StateTree tasks, evaluators, conditions, transitions, schemas, or hierarchical state design.
- Route to `$ue-mass-entity` when the task is primarily Mass processors, fragments, tags, observers, Mass spawners, Mass Crowd, or data-oriented high-volume agents.

## StateTree Integration

- StateTree can drive AI or gameplay state without Behavior Tree selectors.
- Keep conditions and transitions explicit. Avoid hiding transition decisions inside tasks.
- Use evaluators for external data collection and tasks for actions with clear enter/tick/exit behavior.
- Validate active state, transition path, and task completion with StateTree debug tools or targeted logs.

## Mass AI Integration

- Mass Entity uses fragments/tags/processors instead of per-agent UObject-heavy state.
- Actor representation is a bridge, not necessarily the source of truth.
- ZoneGraph, Smart Objects, StateTree, and representation LOD may all participate in crowd behavior.
- Validate entity counts, processor phases, representation transitions, and performance at intended scale.
