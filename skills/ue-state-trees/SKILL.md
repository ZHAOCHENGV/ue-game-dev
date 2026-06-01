---
name: ue-state-trees
description: Unreal Engine StateTree workflow for StateTree assets, tasks, evaluators, conditions, transitions, schemas, linked assets, AI and gameplay state machines, Mass behavior integration, debugging, and migration from Behavior Tree or custom FSM patterns. Use when requests involve StateTree, state trees, hierarchical states, StateTreeTask, StateTreeCondition, StateTreeEvaluator, or AI/gameplay state machine design.
---

# UE State Trees

Use this skill for StateTree-driven AI or gameplay state machines. Keep state ownership, transitions, and data flow visible.

## First Pass

1. Read existing StateTree assets, schemas, evaluators, tasks, conditions, AI controllers, Mass processors, and gameplay actors that own the state.
2. Identify whether the tree drives AI, Mass behavior, interaction state, ability flow, animation decision support, or generic gameplay.
3. Map inputs: context actors, external data, Blackboard-like data, gameplay tags, replicated state, and transient task state.
4. Decide whether logic belongs in Blueprint tasks, C++ tasks/evaluators, AI/Mass integration, or a simpler component state machine.
5. Define validation: transition coverage, abort/exit behavior, task completion, replicated authority, and debug visibility.

## Design Rules

- Keep states narrow and named by player/gameplay meaning.
- Put reusable or authority-sensitive task logic in C++; use Blueprint tasks for designer-authored orchestration.
- Use evaluators for external data collection and conditions for transition decisions.
- Avoid hiding transition logic inside tasks when it belongs in explicit transitions or conditions.
- Keep task enter/tick/exit behavior symmetric, especially for delegates, timers, animation, and ability waits.
- Prefer StateTree when hierarchical state and explicit transitions are clearer than Behavior Tree selectors or custom booleans.

## Integration Rules

- Use `$ue-ai-navigation` when the request is mainly Behavior Tree, EQS, AI Perception, NavMesh, or AI Controller setup.
- Use `$ue-mass-entity` when StateTree behavior is attached to Mass Entity agents.
- Use `$ue-animation` when state transitions primarily coordinate animation blueprints, montages, root motion, or motion matching.
- Use `$ue-gas-networking` when states activate abilities, wait on Gameplay Events, or depend on replicated ability state.

## References

- Read `references/state-tree-checklist.md` before adding StateTree assets, tasks, evaluators, conditions, or transitions.
