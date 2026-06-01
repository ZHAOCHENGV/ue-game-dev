---
name: ue-game-features
description: Unreal Engine Game Features and Modular Gameplay workflow for GameFeature plugins, GameFeatureData, GameFeatureActions, Lyra Experience-style activation, ability/input registration, component injection, feature lifecycle, and cross-domain handoff to GAS, Enhanced Input, UI, and asset validation.
---

# UE Game Features

Use this skill when a request involves Game Feature plugins, ModularGameplay, Lyra-style Experiences, runtime feature activation, or feature-owned registration of abilities, input, UI, components, assets, and game phases.

## First Pass

1. Identify whether the work is a Game Feature plugin, Lyra Experience, ModularGameplay component injection, content bundle, or ordinary plugin/module work.
2. Locate the owning `.uplugin`, `GameFeatureData`, actions, Runtime modules, content root, and activation policy before proposing changes.
3. Decide which systems are registered by activation: GAS abilities, Enhanced Input mapping contexts, components, UI extensions, data registries, or pawn data.
4. Keep activation and deactivation symmetric; every added ability, mapping, component, or UI extension needs a cleanup path.
5. Define validation in editor and packaged builds because Game Feature loading can differ from static plugin content.

## Implementation Rules

- Use Game Feature plugins for feature slices that can be enabled, disabled, or composed at runtime or by experience data.
- Keep hard dependencies small; prefer explicit registration through GameFeatureActions or project-approved extension points.
- Treat Lyra conventions as patterns, not mandatory architecture. Match the current project's pawn data, experience, ability, input, and UI extension style.
- Keep Game Feature content under its plugin content root and verify cook rules include required assets.
- If the feature grants GAS abilities or input mappings, route follow-up validation through `$ue-gas-networking` and `$ue-input-enhanced`.

## Verification

- Confirm the Game Feature transitions through registered, loaded, active, and deactivated states without stale registrations.
- Validate activation order in PIE, standalone, and packaged smoke tests when possible.
- Check that dependent assets are discoverable through Asset Manager or explicit plugin content references.
- For multiplayer, define whether feature activation is server-authoritative, client-local, or experience-driven.

## References

- Read `references/game-feature-checklist.md` before planning Game Feature activation or Lyra-style Experience work.
- Use `$ue-gas-networking` for ability grants, attributes, GameplayEffects, GameplayCues, and prediction.
- Use `$ue-input-enhanced` for Input Mapping Context registration, priorities, rebinding, and UI focus conflicts.
- Use `$ue-data-management` for Primary Asset Manager rules, content bundle discovery, and cook-aware references.
