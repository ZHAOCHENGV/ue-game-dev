---
name: ue-game-features
description: Unreal Engine Game Features workflow for Game Feature Plugins, ModularGameplay, GameFeatureAction, GameFrameworkComponentManager, Lyra-style Experiences, runtime activation, plugin state transitions, ability/input/UI grants, and modular gameplay architecture. Use when requests involve Game Feature plugins, ModularGameplay, Lyra Experience patterns, or feature plugins that grant components, abilities, actions, or data at runtime.
---

# UE Game Features

Use this skill for UE5 Game Feature Plugins and modular gameplay features. Keep plugin activation, runtime grants, assets, and rollback behavior explicit.

## First Pass

1. Read the `.uproject`, relevant `.uplugin`, enabled Game Feature plugins, `DefaultGame.ini`, module `.Build.cs`, and existing experience/action assets.
2. Identify whether the work is a Game Feature Plugin, ModularGameplay component injection, Lyra-style Experience, ability/input/UI grant, or data-only feature pack.
3. Map activation lifecycle: registered, loaded, active, deactivating, error, and how assets or components are cleaned up.
4. Check whether the feature touches GAS, Enhanced Input, UI, Data Assets, replication, or save state; route those details to focused skills after owning the Game Feature boundary.
5. Define validation: activation, deactivation, missing asset behavior, packaged cook inclusion, multiplayer authority, and rollback.

## Design Rules

- Keep Game Feature plugins focused on one gameplay capability or content pack.
- Put runtime modules in the feature plugin only when the feature owns reusable runtime code; keep editor helpers in a paired editor module.
- Use `UGameFeatureAction` assets for declarative activation work such as component injection, ability grants, input mappings, data registration, or UI entries.
- Prefer stable data assets and soft references for feature-owned content that may load on demand.
- Keep feature activation idempotent; repeated activation/deactivation should not duplicate components, input mappings, abilities, or delegates.
- For Lyra-style Experience work, define the Experience asset, action set, pawn data, ability grants, input config, and UI layer changes as a single activation story.

## Integration Rules

- Use `$ue-gas-networking` after the feature boundary is clear when the feature grants abilities, attributes, effects, or gameplay cues.
- Use `$ue-input-enhanced` when the feature adds Input Actions or Mapping Contexts.
- Use `$ue-client-ui` when the feature adds HUD layers, menus, or CommonUI entries.
- Use `$ue-plugin-module-dev` for `.uplugin`, module descriptor, `.Build.cs`, and packaged plugin structure.
- Use `$ue-data-management` for feature-owned Primary Assets, bundles, cook rules, and chunking.

## Verification

- Validate activation and deactivation in PIE, including repeated toggles when possible.
- Check logs for Game Feature state errors and missing asset references.
- Confirm packaged builds include feature-owned assets and do not rely on editor-only references.
- For multiplayer features, test server authority and client-visible grants with at least two clients.

## References

- Read `references/game-feature-checklist.md` before adding or reviewing Game Feature plugins, actions, or Lyra-style Experience flows.
