# Game Feature Checklist

## Ownership

- Plugin descriptor: confirm `.uplugin` type, enabled state, dependencies, and content root.
- Runtime module: keep Game Feature runtime code out of editor-only modules.
- GameFeatureData: identify every GameFeatureAction and its activation order.
- Asset ownership: keep feature-owned assets under the feature plugin unless the project has a shared content rule.

## Activation

- Register abilities, attributes, input mappings, components, UI extensions, and data only during activation.
- Remove or reverse registrations during deactivation.
- Avoid assuming activation happens before all pawns, controllers, or UI layers exist.
- Treat Lyra Experience loading as project-specific; verify pawn data, ability sets, input config, and UI extension points in the current project.

## Cross-Domain Handoffs

- GAS: validate ability grants, prediction keys, GameplayCue availability, and server authority.
- Enhanced Input: validate mapping context priority, local player ownership, and rebinding.
- UI: validate extension point names, layer policy, focus, and gamepad navigation.
- Data: validate Primary Asset rules, bundle names, soft references, and packaged discovery.

## Verification

- PIE: activate and deactivate the feature twice in one editor session.
- Multiplayer: validate server and client see the same feature-owned gameplay state.
- Packaged: confirm feature assets cook and load without editor-only references.
- Logs: inspect GameFeatures, AssetManager, and ModularGameplay output for missing actions or unresolved assets.
