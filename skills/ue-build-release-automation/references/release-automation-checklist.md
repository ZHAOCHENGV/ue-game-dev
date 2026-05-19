# Release Automation Checklist

## Preflight

```text
[ ] .uproject path is resolved and quoted.
[ ] Engine path is resolved and version matches the project.
[ ] Target platform and build configuration are explicit.
[ ] Archive directory is outside Intermediate/Saved.
[ ] Default maps are set in Project Settings > Maps & Modes.
[ ] MapsToCook or Primary Asset rules include required maps.
[ ] Runtime plugins support the target platform.
[ ] Editor-only modules are not referenced by runtime modules.
[ ] Project builds in the same configuration used for packaging.
[ ] Packaging container mode follows the project convention: pak or IoStore.
[ ] Signing credentials are present when platform requires them.
```

## Execution

- Print the exact command before running.
- Keep the output log path.
- Preserve the first `Error:` or `AutomationTool exiting with ExitCode=` block.
- Do not delete previous artifacts unless the user asked for clean packaging.
- Do not upload, sign, notarize, or publish artifacts unless the user explicitly requested that step.

## Post-Package Smoke

```text
[ ] Packaged executable exists.
[ ] Build launches outside the editor.
[ ] Startup map loads.
[ ] Logs do not contain fatal startup errors.
[ ] Basic input path works.
[ ] Save/log directory is writable.
[ ] Version/build identifier is visible or recorded.
```

## Failure Triage

1. Report the first blocking error, not the last wall of log noise.
2. Classify failure as build, cook, stage, archive, signing, platform SDK, missing asset, plugin dependency, or runtime startup.
3. Suggest the smallest next command or editor check to unblock.
4. Route to `$ue-performance-packaging` if the issue is a cook/package diagnostic task rather than automation generation.
