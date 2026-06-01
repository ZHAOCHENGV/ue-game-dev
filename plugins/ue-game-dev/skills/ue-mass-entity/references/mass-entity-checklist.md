# Mass Entity Checklist

Use this checklist for Mass Entity, Mass AI, crowd simulation, ZoneGraph-driven agents, and data-oriented gameplay simulation.

## Discovery

- Confirm enabled plugins such as MassEntity, MassGameplay, MassAI, MassCrowd, ZoneGraph, SmartObjects, and representation plugins.
- Locate processors, fragments, tags, traits, observers, spawners, config assets, and actor representation code.
- Check module dependencies before referencing Mass types in runtime modules.

## Data Model

- Fragments hold mutable per-entity data.
- Tags mark state without payload.
- Shared fragments hold common configuration.
- Traits compose initial entity data.
- Processors mutate fragments in a defined phase; observers react to composition changes.

## Runtime Review

- Define entity spawn source, archetype composition, and cleanup.
- Keep processors narrow and phase-aware.
- Avoid touching UObjects from Mass code unless a bridge is explicitly designed.
- Validate representation LOD and actor bridge behavior separately from pure Mass simulation.

## Evidence

- Entity counts before and after spawn/despawn.
- Processor phase and fragment query evidence.
- PIE performance or profiling note for intended scale.
- Multiplayer authority note when Mass state affects gameplay.
