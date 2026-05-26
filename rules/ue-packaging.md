# UE Packaging Rules

## Explicit Boundary

- Automatic packaging is explicit-only: do not run or generate package automation unless the user asks for packaging, `RunUAT`, `BuildCookRun`, Project Launcher, or CI build.
- Readiness checks belong to `$ue-performance-packaging`; build automation belongs to `$ue-build-release-automation`.
- Do not delete previous artifacts, clean intermediates, sign, upload, or publish unless the user explicitly requests that step.

## Preflight Checklist

- Verify maps, default game mode, platform settings, plugin availability, runtime/editor split, asset references, and target configuration before packaging.
- Confirm required maps are included by maps-to-cook, Project Settings, or Primary Asset rules.
- Confirm Runtime modules do not depend on Editor modules.
- Confirm enabled plugins are available for the target platform.
- Use `-utf8output` on Windows `RunUAT` commands.

## Platform Notes

- Win64: check redistributables, target configuration, console/windowed expectations, and shipping log policy.
- Android: check SDK/NDK/JDK versions, texture format, package name, signing, and storage permissions.
- iOS: check provisioning profile, bundle identifier, signing team, Metal settings, and remote build requirements on Windows.
- Dedicated server: confirm server target, cooked maps, no client-only UI assumptions, and correct config files.

## Cook Failure Patterns

- Missing or moved assets referenced by maps or Blueprints.
- Editor-only classes referenced from runtime assets.
- Runtime module depending on editor-only modules.
- Required maps not included by maps-to-cook or Primary Asset rules.
- Blueprint compile errors hidden until cook.
- Plugin content not enabled, not mounted, or not marked for cooking.

## Config Checklist

- `DefaultGame.ini`: maps, GameMode, Primary Asset rules, and project-specific cook settings.
- `DefaultEngine.ini`: platform settings, rendering/RHI choices, network settings, and plugin subsystem config.
- `DefaultInput.ini`: legacy input only; Enhanced Input assets still need runtime mapping setup.
- Project Launcher or CI configs: archive path, staging directory, target platform, and build configuration.

## Reporting

- Report artifact directory, UAT log path, exit code, and first blocking error when packaging is executed.
- Separate first actionable error from follow-on noise.
- If only a readiness review was requested, do not synthesize packaging commands as if they were run.
