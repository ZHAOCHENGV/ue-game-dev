---
name: ue-game-dev-router
description: Route Unreal Engine game and client development requests to the most specific UE workflow skill. Use as the entry point when the domain or best skill is unclear, or when the request spans project intake, stage detection, gate checks, workflow state, log/crash triage, feature brief, implementation planning, completion handoff, onboarding, multi-agent coordination, Blueprint, C++, plugins, modules, editor tooling, GAS, networking, input, AI, animation, rendering, UI, physics, data, testing, debugging, performance, or packaging.
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
- Use `$ue-async-systems` for `AsyncTask`, `Async()`, `UE::Tasks`, `FRunnable`, `ParallelFor`, `UBlueprintAsyncActionBase`, game-thread handoff, cancellation, async lifetime, and non-blocking gameplay/client operations.
- Use `$ue-external-services` for HTTP, REST, JSON, WebSocket, TCP sockets, backend API clients, streaming responses, heartbeats, reconnects, request queues, auth headers, and external process or service integration.
- Use `$ue-audio` for MetaSound, Sound Cues, AudioComponents, Sound Classes, Sound Mixes, Sound Concurrency, Quartz timing, spatialization, attenuation, and audio performance.
- Use `$ue-world-streaming` for World Partition, Data Layers, HLOD, Level Streaming, Level Streaming Volumes, Large World Coordinates, runtime grid setup, and actor loading/unloading.
- Use `$ue-game-features` for Game Feature Plugins, ModularGameplay, `UGameFeatureAction`, `UGameFrameworkComponentManager`, Lyra-style Experiences, activation/deactivation, ability/input/UI grants, and modular gameplay feature packs.
- Use `$ue-mass-entity` for Mass Entity, Mass AI, Mass Crowd, `MassProcessor`, `MassFragment`, `MassTag`, `MassObserver`, Mass spawners, ZoneGraph/Smart Object crowd behavior, and high-volume data-oriented agents.
- Use `$ue-procedural-generation` for PCG graphs, procedural generation, runtime generated worlds, `ProceduralMeshComponent`, ISM/HISM, spline generation, deterministic seeds, generated collision, and generated content cook/runtime boundaries.
- Use `$ue-state-trees` for StateTree assets, tasks, evaluators, conditions, transitions, schemas, hierarchical AI/gameplay state machines, and Mass StateTree behavior.
- Use `$ue-sequencer-cinematics` for Sequencer, Level Sequence, camera cuts, cutscenes, event tracks, Take Recorder, Movie Render Queue, cinematic playback, and rendered cinematic output.
- Use `$ue-character-movement` for `CharacterMovementComponent`, locomotion tuning, movement modes, custom movement, root motion, movement replication, smoothing, and network prediction.
- Use `$ue-physics-destruction` for Chaos Physics, collision channels/profiles, Physical Materials, Geometry Collections, Fracture, ragdoll, Physics Constraints, physics animation blending, and physics debugging.
- Use `$ue-data-management` for Primary Asset Manager, Data Assets, DataTables, CurveTables, DataRegistry, soft/hard references, async asset loading, cook rules, chunks, and gameplay data validation.
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

If the request involves another domain without a dedicated sibling skill, handle it directly within this router using general Unreal best practices and note the coverage gap.

## External Engineering Flow Handoffs

Keep UE Game Dev as the Unreal domain router. Do not copy or replace general engineering skills from mattpocock/skills; mention them as follow-up process handoffs only when they sharpen the UE workflow.

- For UE bugs, runtime regressions, performance regressions, or logs that need follow-up after `$ue-log-crash-triage`, keep the UE owner as `$ue-log-crash-triage` or `$ue-debug-validation`, then recommend the external `diagnose` loop for reproduce -> minimize -> hypotheses -> instrumentation -> fix -> regression test.
- For new UE features that explicitly ask for TDD, test-first work, regression tests, or test-driven implementation, route the UE owner to `$ue-testing-automation` or `$ue-implementation-plan` as appropriate, then recommend external `tdd` for the red/green/refactor discipline.
- For fuzzy requirements, overloaded terms, unclear domain language, or plans that need pressure-testing before implementation, route the UE owner to `$ue-feature-brief`, then recommend external `grill-with-docs` style questioning against project context and ADRs.
- For inherited UE projects, module tangles, Runtime/Editor dependency issues, shallow module boundaries, or poor test seams, route the UE owner to `$ue-project-onboarding` or `$ue-architecture`, then recommend external `improve-codebase-architecture` for deeper architecture review.

## Chinese Routing Hints

- 中文 "Game Feature / 模块化玩法 / ModularGameplay / Lyra Experience / 功能插件 / 特性插件" should route to `$ue-game-features`.
- 中文 "Mass Entity / Mass AI / Mass Crowd / 群体 AI / 大量 NPC / 人群模拟" should route to `$ue-mass-entity`.
- 中文 "PCG / 程序化生成 / 生成地形 / 生成植被 / 样条生成 / 实例化网格" should route to `$ue-procedural-generation`.
- 中文 "StateTree / 状态树 / 状态机任务 / 状态转换" should route to `$ue-state-trees`.
- 中文 "Sequencer / Level Sequence / 过场动画 / 电影渲染 / Movie Render Queue / 镜头轨道" should route to `$ue-sequencer-cinematics`.
- 中文 "CharacterMovementComponent / 角色移动 / 自定义移动模式 / 移动网络预测 / 运动复制" should route to `$ue-character-movement`.
- 中文 "粒子特效 / 后处理 / 材质球 / 着色器" should route to `$ue-render-vfx`.
- 中文 "角色动画 / 动画蓝图 / 蒙太奇 / 状态机 / IK" should route to `$ue-animation`.
- 中文 "行为树 / 巡逻 / 寻路 / AI感知 / 导航网格" should route to `$ue-ai-navigation`.
- 中文 "存档 / 读档 / 数据持久化" should route to `$ue-save-load-sync`.
- 中文 "布娃娃 / 物理约束 / 破坏系统 / 碰撞通道" should route to `$ue-physics-destruction`.
- 中文 "DataTable / 数据表 / 数据资产 / 软引用 / 异步加载 / 资产管理" should route to `$ue-data-management`.
- 中文 "诊断 / 稳定复现 / 插桩 / 运行时 bug" should route to `$ue-debug-validation`, with `diagnose` as a follow-up discipline when needed.
- 中文 "TDD / 测试先行 / 回归测试 / 自动化测试" should route to `$ue-testing-automation`, with `tdd` as the test-first discipline when the user asks for it.
- 中文 "需求模糊 / 术语不清 / 追问 / 澄清需求" should route to `$ue-feature-brief`, with `grill-with-docs` as a follow-up discipline when project language matters.
- 中文 "架构复盘 / 模块太乱 / 可测试性 / test seam" should route to `$ue-architecture`, with `improve-codebase-architecture` as a follow-up discipline when module depth is the real problem.

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
- For async work, separate off-thread computation or IO from game-thread UObject access, and define cancellation before starting work.
- For external service work, keep backend clients in subsystems or service objects, parse typed results, and do not confuse HTTP/WebSocket/TCP service calls with Unreal gameplay replication.
- For multiplayer work, define which machine owns the state, how it replicates, and what is predicted locally.
- For rendering/VFX work, check scalability, platform, material instruction cost, Niagara bounds, tick cost, and shader permutations.
- For UI work, separate presentation from gameplay state where the project already has view models, controllers, managers, or subsystems.
- For production-facing features, include an appropriate test or smoke validation path unless the user explicitly asks for exploration only.
- For feature lifecycle work, preserve the intake/brief/plan/done chain when it adds clarity, but do not force it on small direct fixes.
- For multi-agent work, require a coordinator synthesis, role statuses, file ownership boundaries, and focused follow-up skills before implementation.
- Use the shared `rules/` guidance when a task touches C++, Blueprint, networking, assets, naming, performance, or packaging.

## Verification

- Prefer a targeted Unreal build for touched modules.
- For feature work, include a targeted `$ue-testing-automation` path when automated tests, editor smoke tests, Functional Tests, PIE scenarios, or asset validation can catch regressions.
- When a full editor build is expensive, still run a syntax/build check that matches the available engine version.
- For Blueprint work, validate graph compile status, event uniqueness, pin compatibility, and asset references.
- For networking, state the minimum PIE or dedicated server scenario to validate.
- For rendering, include an editor viewport/PIE visual check and a performance sanity check.
- For UI, include at least one viewport-size or DPI sanity check when layout changes.
- For packaging/performance, separate editor-only behavior from packaged runtime behavior.
