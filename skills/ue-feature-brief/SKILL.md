---
name: ue-feature-brief
description: Use when an Unreal Engine feature idea, gameplay request, editor tool request, UI change, Blueprint/C++ hybrid task, or plugin/module request needs to be clarified into a scoped implementation brief before coding or planning.
---

# UE Feature Brief

## Overview

Use this skill to turn a rough UE request into a scoped feature brief. The brief should be specific enough that implementation can proceed without guessing about ownership, assets, networking, Blueprint handoff, or validation.

## Brief Workflow

1. Read local project context first when available: `.uproject`, module files, nearest similar classes, Blueprint asset names, input assets, and relevant config.
2. State the player/designer/editor outcome in one sentence.
3. Define ownership: C++, Blueprint, asset/data, UI, networking/GAS, editor module, or hybrid.
4. Capture required assets: Blueprint classes, widgets, input actions, data assets, maps, animations, materials, Niagara systems, sounds, or tests.
5. Capture constraints: UE version, platform, multiplayer authority, save/load, performance, packaging, and editor/runtime split.
6. Identify unknowns that block implementation; ask concise questions only when local inspection cannot answer them.
7. Produce a brief, then route to `$ue-implementation-plan` or the most specific domain skill.

## Brief Output

Use this shape:

```text
UE Feature Brief
- Goal:
- User-facing behavior:
- Owning system/module:
- C++ responsibilities:
- Blueprint/asset responsibilities:
- Data/config needed:
- Network/save/performance concerns:
- Validation path:
- Open questions:
- Recommended next skill:
```

## Quality Rules

- Do not propose new architecture before checking existing project patterns.
- Do not hide Blueprint work behind "implement in BP"; list exact graph or asset responsibilities.
- For C++ APIs exposed to Blueprint, require a later Blueprint handoff section.
- For networked features, name the authority owner and replication path.
- For production features, include at least one test, PIE, editor smoke, or package-risk validation path.

## References

- Read `references/feature-brief-template.md` when producing a brief for the user.
