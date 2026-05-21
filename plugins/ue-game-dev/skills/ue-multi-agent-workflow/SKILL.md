---
name: ue-multi-agent-workflow
description: Use when an Unreal Engine request explicitly asks for multi-agent, multi-expert, parallel specialist, team-style, or complex cross-domain coordination, especially old project onboarding, architecture review, large C++/Blueprint/UI/assets/test features, or packaging/log risk analysis that needs several independent UE perspectives.
---

# UE Multi-Agent Workflow

## Overview

Use this skill as a lightweight orchestration layer for complex UE work. It coordinates specialist perspectives, file ownership, dependency order, and verification without replacing the focused UE domain skills.

## Core Rule

Route simple single-domain tasks to the specific skill instead. Multi-agent work is for complex or explicit coordination, not a default wrapper around every UE request.

Do not load these references for simple single-domain work. Load them only after this skill selects `lean` or `full` mode:

- `references/ue-agent-roles.md` for role responsibilities, ownership boundaries, and optional specialists.
- `references/ue-agent-output-template.md` for the full report shape.
- `references/ue-agent-conflict-resolution.md` when roles disagree, file ownership overlaps, evidence conflicts, or packaging boundaries are at risk.

## Modes

| Mode | Use When | Shape |
|------|----------|-------|
| `solo` | The request says no multi-agent, or the task is narrow. | Use the normal router and one focused domain skill. |
| `lean` | Default for complex UE tasks with 2-3 independent perspectives. | Coordinator plus the minimum specialists needed. |
| `full` | The user asks for full review, architecture review, large refactor, release risk, or broad old-project analysis. | Coordinator plus all relevant specialists and a verifier. |

If the user names a mode, respect it. Otherwise choose `lean` unless the task spans 4+ domains or has release/blocking risk. If the request is narrow even though it mentions a UE domain, choose `solo` and explain the focused skill route in one sentence.

## Role Palette

Use only the roles needed:

- Coordinator: owns scope, dependency order, conflict resolution, final synthesis, and user-facing next steps.
- Project Explorer: read-only scan of `.uproject`, `Source/`, `Plugins/`, `Config/`, assets by filename, and existing `Saved/CodexWorkflow/`.
- UE Architecture Reviewer: module boundaries, `.Build.cs`, Runtime/Editor split, Blueprint/C++ ownership, subsystem boundaries.
- C++ Implementer: runtime/editor C++ APIs, reflection exposure, UObject lifetime, and compile risks.
- Blueprint Integrator: Blueprint graph handoff, node names, pins, event ownership, asset setup, and designer-facing steps.
- Verifier: build, Blueprint compile, PIE, automation tests, log/crash triage, and evidence checklist.
- Optional specialists: GAS/Networking, UI/UMG, Enhanced Input, AI/Animation, Render/VFX, Packaging/Release, Log/Crash Triage.

## Coordination Protocol

1. Identify whether the request is explicit multi-agent or genuinely cross-domain.
2. Select `solo`, `lean`, or `full`.
   - If `solo`, stop here and route to the focused sibling skill without producing a multi-agent report.
   - If `lean` or `full`, read only the reference files needed for the selected mode.
3. Create an Agent Plan before implementation:
   - goal and non-goals
   - selected roles
   - file or asset ownership boundaries
   - read-only discovery tasks that can run in parallel
   - dependent phases that must wait
   - packaging boundary status
4. Run independent discovery before dependent planning. If actual subagents are available and appropriate, dispatch independent read-only or disjoint write tasks in parallel; otherwise simulate the roles sequentially and label the result as a role pass.
5. Collect all role results before making cross-domain decisions.
6. Surface `BLOCKED` immediately when a role lacks required files, editor-only asset details, build access, or user approval.
7. Resolve conflicts through the Coordinator. No role may unilaterally change files outside its assigned ownership.
8. Route implementation slices to the focused sibling skills.

## Explicit Packaging Boundary

Multi-agent orchestration must not trigger `$ue-build-release-automation` by itself. Use packaging automation only when the current user explicitly asks to package, run packaging, generate `RunUAT`/`BuildCookRun`, create one-click packaging, or configure CI release automation.

For packaging failures, release readiness, or risk review without explicit automation, use `$ue-log-crash-triage` and `$ue-performance-packaging` perspectives inside the multi-agent plan.

## Output Format

Use this structure:

```text
UE Multi-Agent Plan
- Mode:
- Goal:
- Roles:
- Ownership boundaries:
- Parallel discovery:
- Dependent phases:
- Packaging boundary:

Parallel Discovery Results
- [Role]: COMPLETE / CONCERNS / BLOCKED

Coordinator Synthesis
- Decisions:
- Conflicts:
- Recommended next skills:
- Verification path:
- User action needed:
```

For implementation work, include exact follow-up skill routing such as `$ue-project-onboarding`, `$ue-architecture`, `$ue-cpp-gameplay`, `$ue-blueprint-workflow`, `$ue-testing-automation`, `$ue-log-crash-triage`, or `$ue-performance-packaging`.

## When Not To Use

- A single Enhanced Input issue, input event, or mapping context bug: use `$ue-input-enhanced`.
- A single Actor, Component, `UFUNCTION`, or `BlueprintCallable` handoff: use `$ue-cpp-gameplay`.
- A Blueprint-only node wiring issue: use `$ue-blueprint-workflow`.
- A plain `RunUAT` command generation request: use `$ue-build-release-automation`.
- A simple explanation question with no project coordination needs: answer directly or use the focused skill.

## Common Mistakes

- Spawning several agents that all read and edit the same files without ownership boundaries.
- Letting a packaging specialist run automation from a passive readiness or failure-analysis request.
- Producing separate role reports without a Coordinator synthesis.
- Skipping Blueprint handoff when C++ exposes new gameplay APIs.
- Treating generated `Intermediate/`, `Binaries/`, or stale logs as authoritative project state.
