---
name: ue-world-streaming
description: Unreal Engine world streaming workflow for World Partition, Data Layers, HLOD, Level Streaming, Level Streaming Volumes, Large World Coordinates, runtime grid setup, actor loading/unloading, streaming performance, and open-world validation.
---

# UE World Streaming

Use this skill for open-world map organization, World Partition, Data Layers, HLOD, level streaming, and runtime loading behavior. Keep authoring workflow, runtime streaming rules, and packaged validation connected.

## First Pass

1. Identify map mode: World Partition, traditional sublevels, streaming volumes, or a hybrid legacy setup.
2. Locate persistent level, sublevels, Data Layers, HLOD layers, runtime grid settings, and streaming sources.
3. Map which Actors must always load, stream by distance, stream by Data Layer, or be spawned at runtime.
4. Check platform memory, traversal speed, multiplayer needs, and packaged build constraints before changing streaming rules.
5. Decide whether changes belong in map settings, actor placement, World Partition config, Blueprint, C++, or automation.

## World Partition Rules

- Use World Partition for large UE5 worlds that need grid-based editor and runtime streaming.
- Keep runtime grid cell size and loading range tied to traversal speed and memory budget.
- Use streaming sources intentionally; do not rely on accidental player-camera behavior for all loading.
- Mark always-loaded actors deliberately and keep them few.
- Validate One File Per Actor and source-control workflow before large map edits.

## Data Layers And HLOD

- Use Data Layers for authored world state, variants, quest phases, or editor organization that maps to runtime needs.
- Keep Data Layer names stable when Blueprints, C++, or tools refer to them.
- Use HLOD for distant visual continuity; tune layer settings by asset type and target platform.
- Rebuild and validate HLOD after large placement, material, or mesh changes.

## Level Streaming Rules

- Use traditional level streaming when the project is legacy, small-scope, or built around authored sublevel transitions.
- Keep streaming volume, Blueprint-triggered, and code-triggered level loads explicit.
- Avoid hidden hard references from always-loaded levels to assets meant to stream.
- Validate load, unload, visibility, collision, navigation, and save/restore behavior around streaming boundaries.

## Verification

- Test editor viewport and PIE streaming behavior with streaming visualization enabled.
- Validate packaged behavior when cook rules, map inclusion, HLOD, or Data Layer runtime state are involved.
- Check memory spikes, hitching, navigation rebuilds, physics state, and actor BeginPlay/EndPlay timing across stream boundaries.
- For multiplayer, verify server authority, client streaming visibility, and late join behavior.

## References

- Read `references/world-partition-checklist.md` for World Partition, Data Layers, HLOD, runtime grid, and packaged validation checks.
- Use `$ue-performance-packaging` when streaming issues are primarily memory, hitching, cook, or release-readiness problems.
- Use `$ue-architecture` when streaming changes require module, subsystem, or ownership redesign.
- Use `$ue-save-load-sync` when streamed actors need persistent identifiers or restore behavior.
