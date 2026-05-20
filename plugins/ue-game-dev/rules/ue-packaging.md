# UE Packaging Rules

- Automatic packaging is explicit-only: do not run or generate package automation unless the user asks for packaging, `RunUAT`, `BuildCookRun`, Project Launcher, or CI build.
- Readiness checks belong to `$ue-performance-packaging`; build automation belongs to `$ue-build-release-automation`.
- Verify maps, default game mode, platform settings, plugin availability, runtime/editor split, asset references, and target configuration before packaging.
- Use `-utf8output` on Windows `RunUAT` commands.
- Do not delete previous artifacts, clean intermediates, sign, upload, or publish unless the user explicitly requests that step.
- Report artifact directory, UAT log path, exit code, and first blocking error when packaging is executed.
