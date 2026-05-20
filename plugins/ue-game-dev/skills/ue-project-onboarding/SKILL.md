---
name: ue-project-onboarding
description: Use when a request asks Codex to understand, audit, take over, inherit, familiarize itself with, or prepare secondary development for an existing Unreal Engine project before making changes, including old projects, legacy projects, unfamiliar UE codebases, and project handoff analysis.
---

# UE Project Onboarding

Use this skill before implementation when the user wants Codex to learn an existing UE project first. The goal is to build project understanding, identify safe extension points, and produce a handoff report before changing code or assets.

## Core Rule

Stay read-only until the user approves a concrete follow-up task. Do not edit C++, Blueprint assets, config files, plugins, or generated files during onboarding.

## Discovery Order

1. Locate the `.uproject` and read engine association, project modules, enabled plugins, and target type.
2. Map `Source/`, `Plugins/`, `Config/`, `Content/`, `Build.cs`, `.Target.cs`, `.uplugin`, and plugin module descriptors.
3. Identify primary entry points: GameMode, GameInstance, PlayerController, Character/Pawn, PlayerState, HUD, Subsystems, Components, AbilitySystem setup, and editor modules.
4. Discover assets by filename only unless deeper inspection is needed: Blueprints, Widget Blueprints, Input Actions, Input Mapping Contexts, Gameplay Tags, DataAssets, Animation Blueprints, Behavior Trees, Niagara systems, materials, maps.
5. Read nearest representative code before drawing architecture conclusions. Prefer small high-signal files over bulk reading.

## Analysis Passes

- Architecture: module boundaries, Runtime vs Editor split, Public/Private exposure, dependency direction, subsystem ownership.
- Gameplay: actor lifecycle, input flow, possession, interaction, save/load, ability activation, replication authority.
- Blueprint/C++ split: which behavior is designer-authored, which APIs are exposed from C++, and where hidden asset dependencies may live.
- Production health: build risks, plugin dependencies, naming consistency, redirectors, hard-coded paths, editor-only dependencies in runtime code, missing validation or test seams.
- Extension planning: safe extension points, files that should not be touched casually, likely smoke tests, and the smallest next task.

## Output Format

Produce a concise "UE Project Onboarding Report" with:

- Project snapshot: path, UE version, project name, modules, enabled plugins.
- Code structure: key modules, important classes, plugin layout, config files.
- Asset structure: important Content folders and discovered asset categories.
- Main flows: startup, input, gameplay, UI, save/load, networking/GAS/AI/rendering if present.
- Blueprint/C++ boundary: what appears to live where, plus unknowns that require editor inspection.
- Risk list: build, module boundary, asset reference, networking, editor/runtime, naming, or packaging risks.
- Safe next steps: recommended follow-up skill and the smallest implementation/debug task to do next.

Use `references/onboarding-report-template.md` when a structured report helps. Use `references/project-audit-checklist.md` for a deeper audit.

## Routing After Onboarding

After the report, route the next task to the most specific sibling skill:

- `$ue-architecture` for module boundaries or refactor strategy.
- `$ue-plugin-module-dev` for plugin/module structure.
- `$ue-cpp-gameplay` for runtime gameplay C++.
- `$ue-blueprint-workflow` for Blueprint graph work.
- `$ue-debug-validation` for broken behavior or uncertain symptoms.
- `$ue-testing-automation` for regression, smoke, PIE, or asset validation.

## Common Mistakes

- Starting implementation before reading `.uproject`, `Build.cs`, and the nearest existing class.
- Treating `.uasset` files as text source of truth. Use filenames for discovery and ask for editor/Blueprint details when needed.
- Assuming a standard template project layout. UE projects often move input, UI, GAS, and editor tooling into custom modules.
- Reporting every file instead of explaining the project shape and the safest next move.
