---
name: ue-client-ui
description: Unreal Engine runtime client UI development workflow for UMG, Widget Blueprints, CommonUI, HUDs, menus, widgets, view models, input focus, Enhanced Input UI flows, loading screens, localization, accessibility, DPI/layout behavior, Blueprint/C++ UI integration, and client-side gameplay presentation. Use when implementing, debugging, or reviewing in-game UI systems; use `ue-editor-tooling-slate` for editor tool Slate UI.
---

# UE Client UI

Use this skill for client-facing architecture and UI. Keep gameplay authority outside presentation code unless the project already centralizes it there.

## First Pass

1. Identify the runtime UI stack: UMG, CommonUI, MVVM, custom HUD manager, or project-specific UI framework.
2. Locate ownership: player controller, HUD, local player subsystem, game instance subsystem, widget tree, or view model.
3. Trace how gameplay state reaches UI: delegates, replicated state, ASC tags/attributes, data assets, polling, or direct references.
4. Check input mode, focus, cursor visibility, gamepad navigation, DPI scaling, and split-screen/local-player assumptions.
5. Decide whether behavior belongs in Widget Blueprint, C++ UMG wrapper, view model/subsystem, or a hybrid.

## Implementation Rules

- Keep widgets presentational where possible; route gameplay commands through controllers, subsystems, components, or existing managers.
- Bind to events/delegates carefully and unbind on teardown when lifetimes differ.
- Avoid heavy work in `Tick`, `NativePaint`, bindings, or per-frame Blueprint UI paths.
- Prefer data/view-model updates over direct widget tree searches from gameplay code.
- Make loading, empty, disabled, error, and disconnected states explicit for user-facing flows.
- For multiplayer UI, distinguish local predicted state from server-confirmed state.

## Runtime UI

- Use UMG/CommonUI for designer-authored runtime screens.
- Use Slate here only for runtime custom widgets already established by the project; use `$ue-editor-tooling-slate` for editor UI.
- For CommonUI, respect activatable widget stacks, input actions, back handling, and platform-specific prompts.
- Keep localization-friendly text in `FText`, not `FString`, for user-facing labels.
- For Widget Blueprint logic, use `$ue-blueprint-workflow` when graph-level node/pin details are needed.
- For C++ widget classes or runtime wrappers, expose the smallest Blueprint-facing API and keep gameplay mutation outside passive display widgets.

## Verification

- Validate with mouse/keyboard and gamepad when focus or navigation changes.
- Check at least one narrow and one wide viewport or DPI scale for layout work.
- For HUD tied to network state, test with two clients or simulated delayed confirmation.

## References

- Read `references/ui-patterns.md` for ownership, focus, view model, and performance review.
- Read `references/ui-code-templates.md` for HUD subsystem, view model pattern, CommonUI activatable widget, and input mode switching code templates.
- Read `references/ui-api-accuracy.md` before writing UMG lifecycle, CommonUI, MVVM, runtime Slate, or localization-sensitive UI guidance.
