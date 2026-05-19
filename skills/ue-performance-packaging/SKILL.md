---
name: ue-performance-packaging
description: Unreal Engine performance and packaging readiness workflow for PIE performance checks, runtime stat review, profiling plans, asset reference validation, build configuration sanity, package failure diagnosis, platform settings, and release readiness. Use when requests involve optimization, packaged builds, cooking, shipping config, startup/load time, or go/no-go checklists.
---

# UE Performance Packaging

Use this skill when the task depends on measured runtime behavior or a packaged build.

## First Pass

1. Confirm target platform, engine version, build configuration, renderer path, net mode, and packaging goal.
2. Record the current symptom: frame time, hitch, memory, shader compile, load time, cook/package failure, crash, or visual quality regression.
3. Separate editor/PIE overhead from packaged runtime behavior.
4. Define a reproducible scenario: map, camera path, player count, scalability, device/profile, and capture duration.

## Performance Workflow

- Collect frame time, game thread, render thread, GPU, RHI, memory, async loading, and Niagara/material/UI suspects as relevant.
- Do not claim optimization wins without before/after measurements.
- Keep quality/scalability changes explicit.
- Prefer fixing unnecessary work before lowering visual quality.

## Packaging Workflow

- Validate maps, game mode, asset references, plugin availability, config files, platform settings, and build target.
- For failures, isolate the first blocking error and dependency chain.
- Check editor-only references leaking into runtime builds.
- Produce a go/no-go checklist with unresolved blockers.

## References

- Read `references/performance-packaging-checklist.md` for profiling and packaging review.
- Read `references/packaging-troubleshooting.md` for common cook/package failure diagnosis, pre-package checklist, and build configuration reference.
