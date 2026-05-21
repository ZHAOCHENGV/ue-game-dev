---
name: ue-game-dev-router
description: Route Unreal Engine game and client development requests to the most specific UE workflow skill. Use as the entry point when the domain or best skill is unclear, or when the request spans project intake, stage detection, gate checks, workflow state, log/crash triage, feature brief, implementation planning, completion handoff, onboarding, multi-agent coordination, Blueprint, C++, plugins, modules, editor tooling, GAS, networking, input, AI, animation, rendering, UI, testing, debugging, performance, or packaging.
---

# UE Game Dev Router

Use this skill first when the request spans multiple Unreal Engine areas or the right workflow is unclear. Treat it as the UE production workflow entry point: classify stage first, then route to the most specific sibling skill.

## Route The Stage

- Use `$ue-start` when the user begins a UE task and scope, project stage, or next workflow is unclear.
- Use `$ue-stage-detect` when the user asks what stage an Unreal project is in, what is missing, or wants a read-only workflow gap report.
- Use `$ue-gate-check` when the user asks whether the project or feature is ready to move to implementation, validation, packaging readiness, or explicit release packaging.
- Use `$ue-feature-brief` when the user has a rough feature idea that needs a scoped UE brief before implementation.
- Use `$ue-implementation-plan` when requirements are clear enough to plan code, Blueprint, assets, config, tests, and verification before changes.
- Use `$ue-feature-done` when work is ready for closeout, handoff, commit, or "is this done?" verification.
- Use `$ue-project-onboarding` when the user asks to understand, audit, take over, inherit, familiarize itself with, or prepare secondary development for an existing Unreal Engine project before changing code or assets.
- Use `$ue-workflow-state` when the user asks to create, refresh, read, or use persistent project memory such as `Saved/CodexWorkflow/`, project context, module maps, asset indexes, decisions, known risks, or active task notes.
- Use `$ue-multi-agent-workflow` when the user explicitly asks for multi-agent, multi-expert, team-style, parallel specialist, `lean`, or `full` mode coordination, or when a complex request spans old-project onboarding, architecture review, C++/Blueprint/UI/assets/tests, and release/log risk analysis. Do not use it for narrow single-domain tasks.

## Route The Request

- Use `$ue-cpp-gameplay` for Actors, Components, UObject ownership, DataAssets, Subsystems, input-driven gameplay handlers, world interaction, save/load hooks, and general gameplay C++.
- Use `$ue-blueprint-workflow` for Blueprint graph logic, Event Graph changes, function graphs, input events, node/pin wiring, Widget Blueprint logic, and Blueprint compile validation.
- Use `$ue-plugin-module-dev` for UE plugin structure, `.uplugin`, module descriptors, Runtime/Editor module split, `.Build.cs`, export API macros, Public/Private folders, plugin content/config/resources, and UE asset/code naming conventions.
- Use `$ue-editor-tooling-slate` for editor plugins, Slate editor UI, ToolMenus, UICommands, toolbar/menu extensions, custom details panels, asset type actions, factories, tab spawners, and editor subsystems.
- Use `$ue-architecture` for module layout, `.Build.cs` dependencies, Public/Private boundaries, reflection exposure strategy, plugin boundaries, and large refactors.
- Use `$ue-gas-networking` for GAS abilities, attributes, effects, cues, prediction, replication, RPCs, authority flow, multiplayer debugging, and network relevance.
- Use `$ue-input-enhanced` for Enhanced Input, Input Actions, Input Mapping Contexts, input modifiers/triggers, pawn/controller binding, runtime mapping changes, key rebinding, local multiplayer input, UI focus/input mode conflicts, and input events that do not fire.
- Use `$ue-save-load-sync` for SaveGame schemas, serialization, restore flows, RepNotify, RPC entry points, and persistent state that intersects with network state.
- Use `$ue-world-interaction` for pickups, spawners, overlap/trace interactions, interaction radius checks, world actor lifecycle, and success/failure feedback.
- Use `$ue-render-vfx` for renderer settings, materials, material functions, shader code, post process, Niagara systems, particles, GPU simulation, LODs, and visual performance.
- Use `$ue-client-ui` for client architecture, UMG widgets, Slate, HUDs, CommonUI, view models, Enhanced Input UI flows, loading screens, localization, and UI performance.
- Use `$ue-log-crash-triage` when the user provides or asks to analyze logs, UBT/UHT compile errors, linker errors, Blueprint compile errors, Editor crashes, callstacks, ensures/asserts, UAT packaging failures, Cook errors, or `Saved/Logs` output.
- Use `$ue-debug-validation` when behavior is broken or unproven and the task is to diagnose runtime behavior, assets, Blueprints, C++, networking, or editor configuration after evidence is collected.
- Use `$ue-build-release-automation` only when the current user explicitly asks to package a project, create or run one-click packaging, generate `RunUAT`/`BuildCookRun` commands, configure Project Launcher, or create CI release build automation. Do not route here for passive readiness checks.
- Use `$ue-performance-packaging` for profiling, stat review, packaging failures, build configuration sanity, release readiness, packaging smoke checks, and go/no-go checklists.
- Use `$ue-ai-navigation` for Behavior Trees, Blackboards, EQS, NavMesh, AI Controllers, AI Perception, StateTree, crowd AI, and autonomous agent behavior.
- Use `$ue-animation` for Animation Blueprints, Montages, Blend Spaces, state machines, IK, Control Rig, Motion Matching, root motion, Anim Notifies, and animation performance.
- Use `$ue-testing-automation` for AutomationSpec, `FAutomationTestBase`, Functional Tests, editor tool smoke tests, PIE/multiplayer scenarios, asset validation, packaging smoke checks, and regression planning.

If a task crosses domains, start with the skill that owns the first failing or user-facing behavior, then bring in the others as needed.

If the user explicitly asks for multi-agent coordination, route to `$ue-multi-agent-workflow` first so it can define roles, ownership boundaries, parallel discovery, dependent phases, and the focused follow-up skills.

If the request involves audio, physics, destruction, level streaming, World Partition, or another domain without a dedicated sibling skill, handle it directly within this router using general Unreal best practices and note the coverage gap.

## Production Workflow

Use this sequence when the user wants broader help rather than one narrow fix:

```text
intake -> stage detect -> workflow state -> brief -> gate check -> implementation plan -> domain implementation -> log/debug triage -> feature done -> workflow state refresh
```

- Insert `$ue-multi-agent-workflow` before onboarding, architecture review, implementation planning, or log/release risk review only when the request is explicit multi-agent or genuinely complex enough to need role coordination.
- Keep onboarding read-only until the user approves implementation.
- Use briefs to remove ambiguity before designing architecture.
- Use stage detection to identify missing UE workflow artifacts without editing project files.
- Use workflow state to preserve project understanding across sessions in `Saved/CodexWorkflow/`.
- Use gate checks for PASS/CONCERNS/FAIL readiness decisions.
- Use implementation plans to split C++, Blueprint, assets, config, and validation.
- Use domain skills for actual UE implementation details.
- Use log/crash triage before debugging from UBT, UHT, UAT, Blueprint, Editor, or crash output.
- Use `$ue-feature-done` before claiming completion or handing work back.

## Explicit Packaging Boundary

- Treat automatic packaging as an active operation, not a passive suggestion.
- Do not invoke `$ue-build-release-automation` merely because a task touches release readiness, performance, testing, or package failure diagnosis.
- Route to `$ue-build-release-automation` only when the user uses intent such as "打包", "一键打包", "自动打包", "生成打包脚本", "运行打包", "BuildCookRun", "RunUAT", "Project Launcher", "CI 打包", "发版流水线", or equivalent explicit packaging automation wording.
- If the user asks whether a project is ready to package, route to `$ue-performance-packaging` until they explicitly ask to build/package.

## Blueprint And C++ Split

- Treat Blueprint and C++ as peer workflows. Do not assume a UE task should be solved in C++ just because code edits are possible.
- Use Blueprint when the request is graph-level, designer-authored, asset-tuned, input/event wiring, Widget Blueprint behavior, or quick gameplay composition.
- Use C++ when the request needs reusable runtime systems, custom components/classes, performance-sensitive loops, advanced networking, custom async/latent behavior, engine API access, or stable APIs for many Blueprints.
- For hybrid features, define the C++ base/API first, then describe the Blueprint extension points, default values, graph wiring, and validation steps.

## Pre-Flight Discovery

- Locate and read the `.uproject` file for engine association, modules, enabled plugins, and project name.
- Map `Source/`, `Content/`, `Config/`, `Plugins/`, target files, and module `.Build.cs` files before proposing changes.
- Discover existing Blueprint assets, Input Actions, Input Mapping Contexts, Widget Blueprints, Gameplay Tags, and GAS assets by filename before naming new assets.
- Read the nearest existing class, Blueprint naming pattern, or subsystem before introducing new architecture.
- Before creating files/assets, apply UE naming conventions: C++ type prefixes (`U`, `A`, `F`, `E`, `I`, `S`), module API macros, and asset names like `[AssetTypePrefix]_[AssetName]_[Descriptor]_[Variant]`.
- If the user wants Codex to first learn an old, unfamiliar, inherited, or existing project before implementation, keep the first pass read-only and route to `$ue-project-onboarding`; use `$ue-workflow-state` when the user wants that understanding saved or refreshed for future sessions.

## Working Rules

- Inspect the local UE project before editing: `.uproject`, `Source/`, `Plugins/`, `Config/`, and module `.Build.cs` files.
- Prefer existing project conventions, module boundaries, naming, and subsystem patterns.
- For C++ edits, keep Unreal reflection hygiene: correct `UCLASS`/`USTRUCT`/`UFUNCTION`/`UPROPERTY`, no raw UObject ownership without GC awareness, and minimal public headers.
- For Blueprint edits, describe graph-level flow first, then exact node/pin wiring; validate compile state and avoid duplicate input events.
- For plugin/module edits, keep Runtime and Editor dependencies separate and verify `.uplugin`, `.uproject`, and `.Build.cs` descriptors before code changes.
- For editor tooling, verify registration/unregistration symmetry and keep editor-only dependencies out of runtime modules.
- For gameplay features, identify authority, lifetime, ownership, save/replication needs, and editor asset requirements before changing code.
- For multiplayer work, define which machine owns the state, how it replicates, and what is predicted locally.
- For rendering/VFX work, check scalability, platform, material instruction cost, Niagara bounds, tick cost, and shader permutations.
- For UI work, separate presentation from gameplay state where the project already has view models, controllers, managers, or subsystems.
- For production-facing features, include an appropriate test or smoke validation path unless the user explicitly asks for exploration only.
- For feature lifecycle work, preserve the intake/brief/plan/done chain when it adds clarity, but do not force it on small direct fixes.
- For multi-agent work, require a coordinator synthesis, role statuses, file ownership boundaries, and focused follow-up skills before implementation.
- Use the shared `rules/` guidance when a task touches C++, Blueprint, networking, assets, or packaging.

## Verification

- Prefer a targeted Unreal build for touched modules.
- For feature work, include a targeted `$ue-testing-automation` path when automated tests, editor smoke tests, Functional Tests, PIE scenarios, or asset validation can catch regressions.
- When a full editor build is expensive, still run a syntax/build check that matches the available engine version.
- For Blueprint work, validate graph compile status, event uniqueness, pin compatibility, and asset references.
- For networking, state the minimum PIE or dedicated server scenario to validate.
- For rendering, include an editor viewport/PIE visual check and a performance sanity check.
- For UI, include at least one viewport-size or DPI sanity check when layout changes.
- For packaging/performance, separate editor-only behavior from packaged runtime behavior.
