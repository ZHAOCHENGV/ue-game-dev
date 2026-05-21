---
name: ue-cpp-gameplay
description: Unreal Engine C++ gameplay development workflow for Actors, ActorComponents, UObject types, DataAssets, Subsystems, input, interaction, spawning, inventory, combat, Blueprint-exposed APIs, save/load integration, and game feature implementation. Use when Codex needs to implement, debug, review, or refactor UE gameplay/client C++ code, especially when C++ should provide reusable systems or stable Blueprint extension points.
---

# UE C++ Gameplay

Use this skill for concrete Unreal C++ gameplay work. Favor project-local patterns over generic architecture.

## First Pass

1. Read the `.uproject`, target files, module `.Build.cs`, and the nearest existing class with similar behavior.
2. Identify the owning module and whether the feature belongs in runtime, editor, developer, or plugin code.
3. Map gameplay lifetime: construction, BeginPlay, possession, input binding, tick/timer/delegate use, teardown, save, and replication.
4. Check reflection needs before writing headers: Blueprint exposure, asset references, config, serialization, delegates, and editor editability.
5. If Blueprint ownership is unclear, read `ue-blueprint-workflow/references/blueprint-cpp-boundary.md` before implementing.

## Implementation Rules

- Keep includes minimal. Prefer forward declarations in headers and includes in `.cpp`.
- Use `TObjectPtr`, `TWeakObjectPtr`, `TSoftObjectPtr`, `TSubclassOf`, or `TSoftClassPtr` according to ownership and loading needs.
- Mark reflected fields with narrow metadata: `VisibleAnywhere`, `EditDefaultsOnly`, `BlueprintReadOnly`, `BlueprintCallable`, categories, and `meta` only when useful.
- Define the Blueprint-facing API intentionally: callable functions, pure queries, implementable/native events, assignable delegates, and protected extension points.
- When adding or changing any Blueprint-exposed C++ function, event, property, interface, or delegate, include a Blueprint implementation/call section that tells the user exactly where to add nodes, what to search for, how to connect exec and data pins, and how to compile and validate the graph.
- Prefer components and subsystems when behavior is reusable or lifetime-bound to an actor/world/game instance.
- Avoid binding delegates repeatedly; unbind when the listener can outlive the source.
- Use timers or events instead of Tick unless per-frame behavior is genuinely required.
- Keep authority checks explicit when gameplay state can matter in multiplayer, even if the current task is local-only.

## Common Patterns

- Interaction: trace or overlap -> validate target -> call interface -> perform authority-owned state change -> replicate or notify UI.
- Spawning: validate class/data -> choose transform/collision handling -> spawn on authority -> initialize through explicit method -> replicate references only when needed.
- Data-driven gameplay: prefer `UPrimaryDataAsset` or project data tables when designers need iteration; keep runtime mutable state out of static asset data.
- Input: use Enhanced Input if the project already does; bind in pawn/controller setup and keep action handlers small.
- Blueprint API: expose minimal stable calls and data; avoid `BlueprintReadWrite` for authoritative state unless designers truly need mutation.
- Blueprint handoff: after C++ changes, state the target Blueprint class/asset, parent C++ class, node/event/function name, expected input values, output handling, and the PIE/editor validation step.

## References

- Use `scripts/ue_blueprint_api_report.py --project <path> --format json` when reviewing or documenting Blueprint-exposed C++ APIs. It scans headers for `BlueprintCallable`, `BlueprintPure`, Blueprint events, and assignable/readable properties, then emits Blueprint handoff steps.
- Read `references/cpp-patterns.md` when touching UObject ownership, reflection, module boundaries, or gameplay class design.
- Read `references/blueprint-api.md` before exposing C++ to Blueprint or splitting work between C++ and Blueprint.
- Read `references/validation.md` before claiming a UE C++ change is complete.
