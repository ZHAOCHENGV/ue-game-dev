---
name: ue-build-release-automation
description: Use only when the current user explicitly asks Codex to package an Unreal project, create or run one-click packaging, BuildCookRun, RunUAT, Project Launcher, CI release builds, archive artifacts, or automate packaged build delivery. Do not use for passive release readiness, performance review, or packaging smoke checks.
---

# UE Build Release Automation

## Overview

Use this skill for active Unreal packaged-build automation. It turns an explicit packaging request into a verified `RunUAT BuildCookRun` command, script, CI step, or executed build with clear logs and artifact paths.

## Invocation Boundary

- Use only when the current user actively asks to package, build a distributable, generate a packaging script, run `RunUAT`, run `BuildCookRun`, configure Project Launcher, or create a CI release pipeline.
- Do not use as a passive follow-up from performance checks, code edits, testing, release readiness review, or "is this ready to ship?" unless the user also asks to build/package.
- If the request is only readiness, diagnosis, smoke testing, or package failure analysis, use `$ue-performance-packaging` or `$ue-testing-automation` instead.
- If the user asks for a command or script, generate it without running it.
- If the user asks Codex to package now, run the packaging command after resolving the project path, engine path, platform, configuration, and archive directory.

## First Pass

1. Locate the `.uproject`, project name, target files, enabled plugins, and existing package output folders.
2. Resolve the Unreal Engine path and version: `.uproject` `EngineAssociation`, known installed engine directories, or the user's explicit engine path.
3. Confirm target platform, client/server build, configuration, archive directory, and whether this is local dev, QA, or release.
4. Inspect packaging-critical settings: default maps, maps to cook, target platform settings, plugin runtime/editor split, and project module build dependencies.
5. Decide the automation surface: direct `RunUAT`, a checked-in PowerShell/BAT script, Project Launcher profile guidance, or CI job.
6. Keep expensive or destructive flags explicit: `-clean`, deleting old builds, signing, uploading, or overwriting release artifacts.

## BuildCookRun Workflow

1. Build the command from known paths, not placeholders.
2. Prefer `RunUAT.bat BuildCookRun` for reproducible local and CI builds.
3. Include `-utf8output` on Windows so logs preserve readable diagnostics.
4. Use `Development` for local validation unless the user asks for `Shipping`, QA, release, or store submission.
5. For UE5 packaged games, include the project's established `-pak` or `-iostore` convention; do not switch container mode casually.
6. When running the build, capture the command, exit code, latest UAT log path, first blocking error, and final artifact directory.
7. If packaging fails, stop at the first actionable blocker and route diagnosis through `$ue-performance-packaging` only if deeper cook/package failure analysis is needed.

## Required Output

For every packaging automation response, include:

- Project path and engine path used.
- Platform, configuration, target type, and archive/stage directory.
- Exact command or script body.
- Whether the command was run or only generated.
- Log location and artifact location when executed.
- Next fix when the build fails.

## References

- Read `references/buildcookrun-commands.md` when generating `RunUAT BuildCookRun` commands or scripts.
- Read `references/release-automation-checklist.md` before running packaging or designing CI artifacts.
- Read `references/ci-build-templates.md` when the user asks for Jenkins, GitHub Actions, TeamCity, or other build machine automation.
