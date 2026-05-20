# UE Editor Tooling Checklist

## Module And Dependencies

- Editor tooling belongs in an Editor module.
- Runtime logic used by shipped builds belongs in a Runtime module.
- Common editor dependencies include `UnrealEd`, `ToolMenus`, `Slate`, `SlateCore`, `EditorSubsystem`, `PropertyEditor`, `AssetTools`, `LevelEditor`, `EditorStyle`/`AppFramework`, and `Projects`.
- Do not add editor-only dependencies to runtime modules.

## Registrations

- Commands: register and unregister command lists/command infos.
- Menus/toolbars: register with ToolMenus or extenders and unregister owner entries.
- Tabs: register and unregister nomad tab spawners.
- Details panels: register and unregister custom class/property layouts.
- Asset tools: register and unregister asset type actions.
- Styles/icons: initialize and shutdown style sets.

## Editor UX

- Use transactions for undoable changes.
- Mark modified packages dirty.
- Respect selection state and multi-select behavior.
- Avoid blocking the game/editor thread for long operations.
- Provide progress and cancellation for expensive work.
- Validate assets before mutating them.

## Slate

- Keep widget ownership in `TSharedRef`/`TSharedPtr`.
- Avoid capturing raw UObject pointers in long-lived delegates without validity checks.
- Use weak pointers for editor objects that can be destroyed.
- Prefer event-driven refresh over polling.

## Validation

- Open the editor with the plugin enabled.
- Verify menu/tab/detail/action appears once.
- Verify command works after hot reload or editor restart.
- Verify shutdown/restart does not leave stale extenders or crash.
