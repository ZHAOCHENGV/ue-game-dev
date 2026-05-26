---
name: ue-architecture
description: Unreal Engine architecture planning workflow for system ownership, module graph design, layer boundaries, dependency direction, Blueprint/C++ surface decisions, cross-module references, migration risk, and large UE feature organization before implementation. Use when requests involve broad design, refactor planning, dependency cleanup strategy, or deciding where systems should live before concrete `.uplugin` or `.Build.cs` edits.
---

# UE Architecture

Use this skill before broad implementation or refactors. Output the intended ownership graph before changing code.

## First Pass

1. Read the `.uproject`, existing modules/plugins, and major gameplay/UI/editor systems.
2. Classify each system as runtime, editor, UI/client, networking, data/assets, tools, or shared contracts.
3. Define ownership, dependency direction, and the intended module/plugin graph.
4. Identify Blueprint/C++ surfaces and migration risks that constrain the design.

## Design Rules

- Keep runtime modules free of editor-only dependencies.
- Prefer thin shared contracts over cyclic dependencies.
- Keep reflected APIs narrow. Only expose `UCLASS`, `USTRUCT`, `UENUM`, `UFUNCTION`, and `UPROPERTY` when Blueprint, serialization, config, replication, or editor tooling needs them.
- Do not move reflected classes across modules or paths without listing Blueprint asset and redirector impact.
- Do not prescribe exact descriptor fields or dependency arrays here; hand off to `$ue-plugin-module-dev` for concrete module/plugin files.
- Prefer subsystems for long-lived runtime/editor services and `UDeveloperSettings` for project-configurable defaults instead of hiding global state in actors, widgets, or module singletons.
- Separate external service clients from gameplay authority. HTTP/WebSocket/TCP clients should feed typed events into game systems; they should not replace Unreal replication or server authority.

## Game Features And Modular Gameplay

- Prefer Game Feature Plugins when a feature can be activated, deactivated, or loaded independently without breaking core systems.
- Each Game Feature Plugin should declare `ExplicitlyLoaded: true` and depend on `GameFeatures` and `ModularGameplay` plugins.
- Use `UGameFeatureAction` subclasses to register components, abilities, input, widgets, and data when the feature activates, and unregister when it deactivates.
- Keep Game Feature Plugins self-contained: they depend on core project contracts but core modules should not depend on them.
- Use `UGameFeaturesSubsystem` to activate/deactivate features at runtime for modular content delivery, DLC, or experimental features.
- Do not place shared interfaces or base types inside Game Feature Plugins; keep them in core runtime modules.

## Output Shape

- Provide module responsibilities.
- Provide dependency edges.
- Provide layer and ownership decisions.
- Provide Blueprint/C++ surface decisions.
- Provide migration risk and validation steps.

## References

- Read `references/module-boundaries.md` for module graph and boundary review.
- Read `references/architecture-templates.md` for module dependency graph templates, Game Feature Plugin structure, and shared contracts module patterns.
- Use `$ue-plugin-module-dev` when the task needs concrete `.uplugin`, module descriptor, plugin folder, export macro, or naming-convention guidance.
- Use `$ue-async-systems` when architecture depends on background work, cancellation, or game-thread handoff.
- Use `$ue-external-services` when architecture depends on backend APIs, HTTP/WebSocket/TCP clients, or external processes.
