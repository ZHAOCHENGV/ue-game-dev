# UE Client UI Patterns

## Ownership

- Use PlayerController, HUD, LocalPlayerSubsystem, or project UI managers for screen orchestration.
- Keep widgets focused on presentation and user intent.
- Route gameplay mutations through gameplay systems rather than direct widget-side state changes.

## State Flow

- Prefer delegates, field notifications, view models, or explicit refresh methods over per-frame polling.
- Distinguish predicted local state from server-confirmed state for multiplayer UI.
- Represent loading, empty, disabled, error, and disconnected states explicitly.

## Input And Focus

- Set input mode intentionally for menus, gameplay, and mixed overlays.
- Validate keyboard, mouse, and gamepad navigation.
- Respect CommonUI action routing and back behavior when the project uses CommonUI.

## Performance And Layout

- Avoid heavy Blueprint bindings, widget tree searches, and per-frame formatting.
- Use invalidation, retainer boxes, or virtualization only when they solve measured problems.
- Check DPI scaling, safe zones, localization length, and narrow/wide viewport behavior.
