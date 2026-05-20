# Performance And Packaging Checklist

## Performance

- Capture map, camera/player path, player count, scalability, renderer settings, and build config.
- Compare frame time, game thread, render thread, GPU, RHI, memory, async loading, and hitches.
- Inspect frequent Tick, timers, Blueprint bindings, Niagara systems, translucent overdraw, material cost, and streaming.
- Record before/after measurements.

## Packaging

- Confirm target platform, target file, configuration, maps, game mode, plugins, and project settings.
- Check cook errors, missing assets, editor-only references, redirectors, and third-party plugin build failures.
- Separate first blocking error from downstream noise.
- Validate startup map, input config, localization, and required runtime assets.

## Release Readiness

- Known blockers.
- Known warnings accepted.
- Required smoke tests.
- Packaging command/config used.
- Runtime verification result.
