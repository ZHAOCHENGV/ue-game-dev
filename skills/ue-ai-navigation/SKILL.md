---
name: ue-ai-navigation
description: Unreal Engine AI and navigation workflow for Behavior Trees, Blackboards, EQS, NavMesh, AI Controllers, AI Perception, StateTree, Mass Entity, crowd simulation, and AI debugging. Use when requests involve NPC behavior, pathfinding, environmental queries, AI sensing, or autonomous agent logic.
---

# UE AI Navigation

Use this skill for AI behavior, pathfinding, and autonomous agent systems. Keep AI logic authority-aware and data-driven where designers need iteration.

## First Pass

1. Read the `.uproject`, existing AI controllers, Behavior Trees, Blackboard assets, EQS queries, NavMesh configuration, and AI Perception setup.
2. Identify the AI framework in use: Behavior Tree + Blackboard, StateTree, custom FSM, or hybrid.
3. Map AI actor set: AI Controller, Pawn/Character, Blackboard, Behavior Tree, EQS, Perception Component, Navigation path, and gameplay subsystems.
4. Determine whether the AI logic belongs in Blueprint, C++, or a data-driven hybrid.
5. Check NavMesh generation settings, navigation bounds, agent profiles, and query filters before changing pathfinding behavior.

## Behavior Tree Rules

- Keep Behavior Tree structure shallow and readable; prefer subtrees for reusable branches.
- Use Blackboard keys with clear types and names; avoid overloading a single key for multiple purposes.
- Keep Blackboard key names stable after they are referenced by trees, decorators, and services.
- Implement custom tasks, decorators, and services in C++ when they need reusable logic, performance, or engine API access; use Blueprint tasks for designer-authored one-off behavior.
- End tasks explicitly with `FinishLatentTask` on all paths: success, failure, abort, and owner destruction.
- Use decorators for condition checks and observation rather than polling in task Tick.
- Use services for periodic Blackboard updates rather than per-frame polling.

## StateTree Rules

- Use StateTree when the project prefers a hierarchical state machine over Behavior Trees.
- Keep states focused; avoid monolithic state logic.
- Use conditions and transitions explicitly instead of ad-hoc checks inside state logic.
- Keep StateTree assets and evaluation schemas consistent with the project pattern.

## Navigation Rules

- Confirm NavMesh agent radius, height, step height, and slope match the AI Pawn dimensions.
- Use navigation query filters for terrain cost, area restrictions, and avoidance priorities.
- Set supported agents and navigation bounds intentionally; avoid relying on unbounded auto-generation.
- For dynamic obstacles, confirm dynamic modifier volumes or runtime NavMesh rebuilds are configured.
- Use `MoveToLocation`/`MoveToActor` through AI Controller or pathfinding component; avoid manual path segment management unless required.

## AI Perception Rules

- Configure sight, hearing, damage, touch, and team senses with explicit ranges and parameters.
- Use `OnPerceptionUpdated` or `OnTargetPerceptionUpdated` delegates instead of polling `GetCurrentlyPerceivedActors` every frame.
- Keep perception source registration explicit; actors that should be sensed need a stimuli source component or compatible affiliation.
- Validate perception in multiplayer: perception runs on the server for authoritative AI; keep client proxies cosmetic.

## EQS Rules

- Keep EQS queries modular: generator -> tests -> scoring.
- Prefer simple generators (grid, cone, actors) with focused tests over complex monolithic queries.
- Watch query cost: limit item count, avoid expensive traces per item, and use distance culling.
- Test EQS queries in the EQS Testing Pawn before relying on them in runtime Behavior Trees.

## Common Patterns

- Patrol: waypoint data asset or spline -> select next point via Blackboard/EQS -> MoveTo -> wait/observe -> repeat.
- Combat: perception detect -> evaluate threat -> select ability/attack -> execute via GAS or direct action -> evaluate result -> re-evaluate state.
- Cover: EQS query for cover points -> score by distance/exposure/threat direction -> MoveTo -> hold with decorator-gated observation.
- Investigate: stimulus location in Blackboard -> MoveTo -> search pattern -> timeout or confirm -> return to previous behavior.

## Debugging

- Use `AI Debugging` viewport mode and `GameplayDebugger` for live Behavior Tree, Blackboard, EQS, Perception, and NavMesh visualization.
- Log AI Controller name, Blackboard key values, current tree node, perception targets, and navigation request results near failing paths.
- For NavMesh issues, use `Show Navigation` and inspect agent-specific nav data generation.

## References

- Read `references/ai-behavior-checklist.md` for Behavior Tree, EQS, and Perception validation.
- Read `references/navigation-checklist.md` for NavMesh, pathfinding, and agent configuration review.
- Use `$ue-cpp-gameplay` when AI needs custom components, subsystems, or gameplay C++ implementation.
- Use `$ue-gas-networking` when AI abilities use GAS or need multiplayer authority handling.
