---
name: ue-start
description: Use when a user begins an Unreal Engine task with unclear scope, asks where to start, mentions a new/old UE project, wants Codex to choose a workflow, or needs the request classified before onboarding, feature scoping, implementation, debugging, testing, performance, or packaging.
---

# UE Start

## Overview

Use this skill as the lightweight intake step for UE work. Classify the user's situation, ask only the missing question that blocks safe routing, then hand off to the right UE workflow skill.

## Intake

1. Identify project stage: old project onboarding, new feature, bug/debug, refactor, test/validation, performance/readiness, or explicit packaging automation.
2. Identify known context: `.uproject` path, UE version, target platform, module/plugin area, Blueprint/C++ ownership, and expected result.
3. If a local UE project is available, inspect `.uproject`, `Source/`, `Plugins/`, and `Config/` before recommending implementation.
4. If the user wants Codex to first understand an existing project, keep the pass read-only and route to `$ue-project-onboarding`.
5. If the request is a feature idea without enough detail, route to `$ue-feature-brief`.
6. If the request already has clear requirements and needs a work breakdown, route to `$ue-implementation-plan`.

## Stage Routing

| User intent | Route |
|-------------|-------|
| "先熟悉项目", "接手旧项目", "二开前分析" | `$ue-project-onboarding` |
| "我想做一个功能", unclear requirements | `$ue-feature-brief` |
| Clear feature, asks how to implement | `$ue-implementation-plan` then domain skill |
| Broken behavior, logs, crash, Blueprint not firing | `$ue-debug-validation` |
| Need tests or validation path | `$ue-testing-automation` |
| Performance, cook/package failure, release readiness | `$ue-performance-packaging` |
| Explicit package/build/release automation | `$ue-build-release-automation` |

## Output

Return a short intake result:

- Stage: one of onboarding, brief, plan, implementation, debug, validation, performance, packaging.
- Known facts: project path/version/domain if discovered.
- Missing blocker: the one question needed, if any.
- Next skill: exact `$skill-name` and why.
- Immediate next action: read-only scan, brief, plan, implementation, or verification.

## References

- Read `references/intake-checklist.md` when the request is ambiguous or spans multiple UE domains.
