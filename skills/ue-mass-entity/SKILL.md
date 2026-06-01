---
name: ue-mass-entity
description: Unreal Engine Mass Entity workflow for MassEntity, MassProcessor, MassFragment, MassTag, MassObserver, MassSpawner, Mass Crowd, Mass AI, representation, ZoneGraph, Smart Objects, scalable NPC crowds, and data-oriented gameplay simulation. Use when requests involve Mass Entity, Mass AI, crowds, processors, fragments, observers, or high-volume agent simulation.
---

# UE Mass Entity

Use this skill for UE Mass Entity and high-volume data-oriented simulation. Keep processor ownership, fragment data, representation, and gameplay handoff explicit.

## First Pass

1. Read the `.uproject`, enabled Mass plugins, module `.Build.cs`, existing Mass processors, fragments, traits, spawners, ZoneGraph, and crowd setup.
2. Identify the entity domain: crowds, traffic, AI agents, perception-like simulation, representation-only actors, or gameplay bridge.
3. Map data ownership: fragments, tags, shared fragments, traits, processors, observers, subsystems, and actor representation.
4. Decide where behavior lives: Mass processor, StateTree/Mass behavior, AI Controller bridge, actor component, or pure gameplay actor.
5. Define validation: spawn count, processor phase, fragment mutation, representation, server/client behavior, and performance.

## Design Rules

- Model per-entity state as fragments and tags; avoid per-entity UObject state unless bridging to actors is required.
- Keep processors focused on one simulation concern and place them in the correct execution phase.
- Use observers for add/remove fragment reactions instead of broad polling.
- Keep actor representation lightweight; do not spawn full actors for every entity unless the project requires it.
- Use shared fragments for common configuration and avoid duplicating large immutable data per entity.
- Treat Mass as a simulation framework, not a replacement for every gameplay actor; define bridge points deliberately.

## Integration Rules

- Use `$ue-ai-navigation` for Behavior Tree, EQS, NavMesh, or AI Perception systems outside Mass.
- Use `$ue-state-trees` when Mass behavior is driven by StateTree tasks/evaluators.
- Use `$ue-performance-packaging` when crowd count, processor cost, representation LOD, or packaged behavior is the main risk.
- Use `$ue-cpp-gameplay` for actor/component bridges or gameplay C++ wrappers.

## Verification

- Validate processor execution order, fragment presence, and expected entity counts.
- Check crowd/representation LOD behavior and actor spawn/despawn transitions.
- Measure processor and representation cost for the target crowd scale.
- Include a minimal PIE scenario that proves entity spawn, update, and cleanup.

## References

- Read `references/mass-entity-checklist.md` before adding Mass processors, fragments, traits, observers, or crowd behavior.
