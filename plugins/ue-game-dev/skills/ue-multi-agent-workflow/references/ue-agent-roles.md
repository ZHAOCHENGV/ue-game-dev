# UE Agent Roles

Use these roles only after `ue-multi-agent-workflow` has selected `lean` or `full` mode. For simple single-domain tasks, do not load this file; route directly to the focused UE skill.

## Core Roles

| Role | Use When | Owns | Must Not Do |
|------|----------|------|-------------|
| Coordinator | Any multi-agent run. | Scope, role selection, dependency order, conflicts, final synthesis. | Edit domain files without assigning ownership. |
| Project Explorer | Existing or old UE project, unclear structure, onboarding. | Read-only scan of `.uproject`, `Source/`, `Plugins/`, `Config/`, asset filenames, `Saved/CodexWorkflow/`. | Modify project files or infer binary asset internals. |
| UE Architecture Reviewer | Module, plugin, subsystem, Blueprint/C++ boundary, large refactor. | `.Build.cs`, module boundaries, Runtime/Editor split, ownership model, dependency risks. | Override user-approved product goals. |
| C++ Implementer | Runtime/editor code, reflected APIs, gameplay systems. | C++ files, headers, reflection exposure, UObject lifetime, compile risk. | Change Blueprint assets or packaging automation. |
| Blueprint Integrator | Blueprint handoff, asset wiring, Widget Blueprint, designer-facing behavior. | Node search names, pin wiring, default values, graph validation, asset setup instructions. | Pretend `.uasset` internals were inspected as text. |
| Verifier | Completion, risky change, cross-domain implementation. | Build/compile checks, Blueprint compile notes, PIE scenarios, test evidence, log triage summary. | Claim COMPLETE without fresh evidence. |

## Optional Specialists

| Role | Trigger |
|------|---------|
| GAS/Networking | Ability System, replication, RPC, prediction, authority, multiplayer PIE. |
| UI/UMG | Widget Blueprint, CommonUI, HUD, view models, input mode, DPI/layout. |
| Enhanced Input | Input Actions, Mapping Contexts, triggers/modifiers, rebinding, UI focus. |
| AI/Animation | Behavior Tree, EQS, StateTree, AI Perception, Anim Blueprint, montage, IK. |
| Render/VFX | Materials, Niagara, post process, shader, visual performance. |
| Packaging/Release | Release readiness, Project Launcher, RunUAT risk review, CI release concerns. |
| Log/Crash Triage | UBT/UHT/UAT errors, Saved/Logs, callstack, ensure/assert, first actionable failure. |

## Mode Guidance

- `lean`: Coordinator + 1-2 specialists. Use for old-project orientation, architecture concern, or one complex feature.
- `full`: Coordinator + Project Explorer + Architecture Reviewer + Verifier + only relevant domain specialists. Use for broad audits or release-risk work.
- `solo`: No role table. Return to `$ue-game-dev-router` and the focused skill.

## Ownership Rules

- One role owns each file or asset category at a time.
- Read-only roles may report risks but cannot propose edits as if approved.
- C++ and Blueprint roles must coordinate any reflected API handoff.
- Packaging/Release may review packaging risk, but packaging automation remains explicit-only.
- If two roles need the same file, the Coordinator serializes the work or marks the overlap as `BLOCKED`.
