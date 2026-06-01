# Game Feature Checklist

Use this checklist when a task involves Game Feature Plugins, ModularGameplay, GameFeatureAction assets, or Lyra-style Experience setup.

## Discovery

- Locate `.uproject`, the feature `.uplugin`, feature modules, `Config/`, `Content/`, and any existing Experience or action-set assets.
- Confirm the plugin type, loading phase, enabled state, and whether the feature is meant to be always-on, selectable, streamed, or DLC-like.
- Identify dependencies on GameplayAbilities, EnhancedInput, CommonUI, ModularGameplay, GameFeatures, AssetManager, and project-specific framework modules.

## Activation Model

- State what should happen on register, load, activate, deactivate, and error.
- Ensure actions are idempotent: no duplicate components, input mappings, ability specs, delegates, UI layers, or data registration.
- Define cleanup on deactivation for every grant made on activation.
- Keep server-authoritative gameplay grants separate from client-only presentation grants.

## Lyra-Style Experience Review

- Identify Experience, Experience Action Set, Pawn Data, Ability Set, Input Config, HUD layout, and default gameplay tags.
- Check asset references and bundles so feature content cooks and loads without editor-only paths.
- Keep cross-feature dependencies explicit; avoid hidden assumptions that another feature has already activated.

## Completion Evidence

- PIE activation/deactivation result.
- Log evidence for Game Feature state transitions.
- Asset/cook evidence for feature-owned content.
- Multiplayer evidence when abilities, input, pawn data, or replicated state are involved.
