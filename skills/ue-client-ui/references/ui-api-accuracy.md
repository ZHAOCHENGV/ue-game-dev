# Runtime UI API Accuracy Notes

Use this reference when writing or reviewing UMG, CommonUI, MVVM, HUD, or Slate-in-runtime guidance.

## UMG And Widget Lifecycle

- `UUserWidget` setup often belongs in `NativeOnInitialized`, `NativeConstruct`, and `NativeDestruct`; bind/unbind according to lifetime.
- Avoid expensive per-frame Blueprint bindings and widget `Tick` when event-driven updates are possible.
- Use `FText` for player-visible labels and localized text.
- Keep gameplay mutation outside passive display widgets unless the project explicitly uses command widgets.

## CommonUI

- Respect activatable widget stacks, input actions, back handling, focus, and platform prompts.
- Define ownership by local player/controller/subsystem rather than global singleton UI state.
- Validate keyboard/mouse and gamepad flows when focus changes.

## MVVM And View Models

- Keep replicated/gameplay state in gameplay systems; expose presentation-ready values through view models or UI state objects.
- Document delegate/event subscription and teardown when widgets listen to gameplay systems.
- Separate local predicted UI from server-confirmed state in multiplayer.

## Slate Boundary

- Runtime Slate can be valid when the project already uses it, but editor panels, details customization, tab spawners, ToolMenus, and UICommands belong to `$ue-editor-tooling-slate`.

## Evidence

- Check at least one narrow and one wide viewport or DPI scale for layout changes.
- Include focus/navigation validation when menus or CommonUI screens are touched.
