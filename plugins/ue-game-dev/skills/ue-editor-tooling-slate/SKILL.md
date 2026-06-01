---
name: ue-editor-tooling-slate
description: Unreal Engine editor tooling and Slate implementation workflow for Slate widgets, ToolMenus, UICommands, toolbar/menu extenders, details customizations, property type customizations, asset type actions, factories, editor subsystems, editor utility integration, selection tools, tab spawners, transactions, and registration/unregistration behavior. Use when creating, debugging, or reviewing concrete UE editor tools or plugin UI after the editor module boundary is known.
---

# UE Editor Tooling Slate

Use this skill for Unreal Editor extensions. Keep all editor-only code in editor modules and unregister everything registered at startup.

## First Pass

1. Confirm the editor module boundary already exists or use `$ue-plugin-module-dev` to create it.
2. Read the editor module `.Build.cs`, `StartupModule`, `ShutdownModule`, and any existing commands/style/menu registration.
3. Identify tool surface: menu, toolbar, tab, details panel, asset context menu, factory/importer, editor subsystem, viewport overlay, or standalone Slate widget.
4. Define state ownership: subsystem, module singleton, selected assets/actors, transient settings object, config UObject, or command context.

## Editor Tool Rules

- Register menus, commands, styles, tabs, asset actions, and custom layouts in startup or an explicit registration path.
- Unregister every registration in shutdown.
- Guard shutdown paths because modules may unload during editor exit.
- Avoid loading heavy assets or scanning the whole project during module startup.

## Slate And UI Rules

- Use `SCompoundWidget` or focused Slate widgets for custom editor UI.
- Use `TSharedRef`/`TSharedPtr` ownership correctly; avoid raw owning pointers for Slate objects.
- Keep UI state refresh event-driven. Avoid expensive polling in active timers or Tick.
- Keep long-running operations asynchronous or task-based and expose progress/cancel when practical.
- Keep editor transactions, undo/redo, dirty packages, and selection changes explicit.

## Common Tool Surfaces

- ToolMenus/UICommands: commands, shortcuts, toolbar buttons, and menu items.
- Nomad tabs: persistent editor panels with registered tab spawners.
- Details customization: `IDetailCustomization` and `IPropertyTypeCustomization`.
- Asset tools: `IAssetTypeActions`, factories, reimport handlers, and context menu actions.
- Editor subsystems: shared editor services that outlive individual widgets.

## References

- Read `references/editor-tooling-checklist.md` before implementing editor menus, commands, tabs, details panels, or asset tools.
- Read `references/editor-code-templates.md` for ToolMenus registration, UICommands, tab spawner, detail customization, and asset type actions code templates.
- Read `references/slate-panel-template.md` when the task needs a concise ToolMenus, tab, or Slate panel scaffold.
- Use `$ue-plugin-module-dev` for `.uplugin`, module split, and `.Build.cs` decisions.
