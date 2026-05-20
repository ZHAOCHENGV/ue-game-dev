---
name: ue-world-interaction
description: Unreal Engine world interaction workflow for pickups, spawners, overlap checks, trace checks, interact prompts, interaction radius checks, visual/audio feedback, actor lifecycle, and gameplay result handling. Use when requests involve interactive world actors, spawn logic, pickup behavior, use-key interactions, target validation, or interaction feedback.
---

# UE World Interaction

Use this skill for player-to-world gameplay objects and interaction loops.

## First Pass

1. Define the interaction model: overlap-driven, trace-driven, explicit use key, ability targeting, or UI-selected target.
2. Identify actor set: interactable actor, pickup, spawner, collision component, visual mesh/effect, data asset, UI prompt, and optional gameplay component.
3. Define runtime state transitions from spawn/activation to interaction resolution and cleanup.
4. Decide whether the implementation belongs in Blueprint, C++, or a hybrid actor/component plus Blueprint visuals.

## Implementation Rules

- Keep collision channels, object responses, trace channels, and overlap settings explicit.
- Validate distance, line of sight, owner, authority, cooldown, inventory capacity, and target validity before applying results.
- In multiplayer, let the client request intent and the server approve durable gameplay state.
- Guard repeated overlap/use events with active/in-progress/consumed state.
- Decide lifecycle explicitly: destroy, hide, disable collision, respawn, pool, or persist.
- Keep success/failure feedback structured so UI, audio, VFX, and gameplay can respond consistently.

## References

- Read `references/interaction-checklist.md` for overlap/trace/spawn/pickup validation.
- Read `references/interaction-templates.md` for interactable interface, trace interaction component, pickup actor, and overlap trigger code templates.
