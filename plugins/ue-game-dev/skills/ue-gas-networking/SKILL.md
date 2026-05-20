---
name: ue-gas-networking
description: Unreal Engine Gameplay Ability System and multiplayer ability networking workflow. Use for GAS abilities, attributes, gameplay effects, gameplay cues, prediction, ability tasks, Blueprint ability integration, ASC replication modes, RPC authority for ability activation, dedicated server behavior, listen server edge cases, and multiplayer ability implementation or review. Use `ue-save-load-sync` for SaveGame persistence or non-GAS durable state synchronization.
---

# UE GAS Networking

Use this skill when gameplay correctness depends on authority, prediction, replication, or GAS state.

## First Pass

1. Identify the GAS network model: single-player, listen server, dedicated server, client prediction, simulated proxy, or replay.
2. Identify ASC ownership, avatar, replication mode, and predicted versus authoritative ability state.
3. For GAS, locate the `AbilitySystemComponent`, attribute sets, initialization path, avatar/owner actor relationship, and input binding path.
4. Read existing abilities/effects/cues before adding new patterns.
5. Identify whether ability logic lives in Blueprint abilities, C++ ability classes, or a hybrid with Blueprint-authored effects/cues.

## GAS Rules

- Initialize ASC consistently on server and client, especially after possession and avatar changes.
- Keep gameplay effects data-driven where designers need tuning; keep ability activation logic in C++ when it coordinates state.
- Use gameplay tags for state gates and cancellation rules instead of scattered booleans.
- Separate authoritative effects from cosmetic cues. Gameplay Cues should not be the only source of gameplay truth.
- Use prediction windows only around actions that are safe to predict and can reconcile cleanly.
- Prefer ability tasks for async waits, targeting, montage events, and gameplay events when they match existing project style.
- Keep Blueprint abilities focused on orchestration, animation/VFX/SFX hooks, and designer-tuned effects; move validation, reusable targeting, and authority-sensitive logic to C++ when needed.

## GAS Networking Rules

- Server owns authoritative ability outcomes. Clients request/predict intent; the server validates and reconciles.
- Use GAS replication, Gameplay Cues, and attributes for ability-visible state.
- Avoid multicast for effects that should be represented by Gameplay Cues or replicated ability/attribute state.
- For owner-only data, use owner-only replication conditions or ASC replication mode consistent with the project.
- Use `$ue-save-load-sync` when the state must persist across sessions or restore after load.

## Debugging

- Reproduce with at least two clients when the issue is network-visible.
- Log role, local role, remote role, owner, instigator, prediction key, ability spec handle, and gameplay tags near the failing path.
- Check both server and client logs before changing code.

## References

- Read `references/gas-patterns.md` for ability/effect/cue structure and prediction decisions.
- Read `references/networking-checklist.md` for replication and RPC review.
- Use `$ue-blueprint-workflow` for Blueprint ability graph wiring and `$ue-cpp-gameplay` for C++ ability/component implementation.
