---
name: ue-implementation-plan
description: Use when an Unreal Engine feature, bug fix, refactor, plugin/module change, Blueprint/C++ hybrid task, editor tool, UI flow, GAS/networking change, or production workflow needs a concrete implementation plan before files or assets are changed.
---

# UE Implementation Plan

## Overview

Use this skill to create a concrete UE implementation plan that separates code, Blueprint/assets, config, tests, and verification. The plan should be small enough to execute safely and specific enough to avoid inventing project patterns.

## Planning Workflow

1. Start from a feature brief, onboarding report, bug reproduction, or user requirement.
2. Inspect project-local conventions before planning new files: `.uproject`, `Source/`, `Plugins/`, `Config/`, `.Build.cs`, target files, and similar classes/assets.
3. Split work by UE ownership boundary:
   - C++ runtime/editor code.
   - Blueprint graph and asset setup.
   - Config and module descriptors.
   - Data assets, input assets, maps, widgets, VFX/audio/animation assets.
   - Tests and validation.
4. Assign the most specific domain skill to each work slice.
5. Include verification gates after each risky slice, not only at the end.
6. Keep explicit packaging automation out of the plan unless the user requested packaging.

## Plan Output

Use this shape:

```text
UE Implementation Plan
1. Discovery and constraints
2. C++/module changes
3. Blueprint/asset changes
4. Data/config changes
5. Test and validation path
6. Handoff notes
```

For each step include:

- Files or asset names to inspect/create/change.
- Owning skill, such as `$ue-cpp-gameplay` or `$ue-blueprint-workflow`.
- Expected change.
- Validation command or editor/PIE check.
- Rollback or risk note when touching shared systems.

## Required Gates

- C++ exposed to Blueprint: include Blueprint node search names, pins, and validation.
- Enhanced Input: include `IA_`, `IMC_`, subsystem context addition, and binding owner.
- Networking/GAS: include authority, prediction/replication, and PIE client count.
- Editor tooling: include registration/unregistration symmetry.
- Packaging: use `$ue-build-release-automation` only for explicit packaging requests.

## References

- Read `references/implementation-plan-template.md` when producing a user-facing plan.
