# Rebinding And UI Input

## Runtime Rebinding

When the user asks for key rebinding, define four pieces explicitly:

1. Source asset: which `UInputMappingContext` or player mappable config is edited.
2. Runtime owner: local player subsystem, settings object, or custom input settings manager.
3. Persistence: SaveGame, config, platform user settings, or project-specific profile data.
4. Rebuild timing: when mappings are cleared, re-added, and reflected in UI prompts.

## Rebinding Checklist

```text
[ ] Action is marked or represented as player-remappable where the project expects it.
[ ] Conflicting bindings are detected before saving.
[ ] Keyboard, mouse, gamepad, and touch mappings are handled separately when needed.
[ ] Saved mappings are applied after local player creation and after profile changes.
[ ] UI prompt text is updated after rebinding.
[ ] Defaults can be restored.
```

## UI Focus And Gameplay Input

Before changing input code, identify the active mode:

| Mode | Expected Behavior |
|------|-------------------|
| Game only | Gameplay receives input; UI should not consume gameplay actions. |
| UI only | Focused widget receives input; gameplay mappings may be inactive. |
| Game and UI | Both can receive input; conflict rules must be explicit. |
| CommonUI active | Activatable widgets and input actions may consume or reroute input. |

## UI Debug Steps

1. Confirm the focused widget.
2. Check `SetInputModeGameOnly`, `SetInputModeUIOnly`, or `SetInputModeGameAndUI` usage.
3. Check whether mouse cursor, focus lock, and capture mode are intentional.
4. If CommonUI is present, inspect activatable widget stack and UI action bindings.
5. Temporarily print Enhanced Input action events and widget key events to see where input stops.

## Blueprint Handoff Template

```text
Blueprint asset:
- <BP_PlayerCharacter or WBP_Settings>

Nodes:
- Search: Enhanced Input Action <IA_Name>
- Use trigger pin: <Started/Triggered/Completed>
- Read value pin as: <bool/float/Vector2D>
- Call: <FunctionName or event>
- Update UI prompt: <TextBlock or CommonActionWidget>

Validation:
- Compile Blueprint.
- PIE with keyboard and gamepad.
- Rebind key, restart PIE, confirm saved mapping applies.
```
