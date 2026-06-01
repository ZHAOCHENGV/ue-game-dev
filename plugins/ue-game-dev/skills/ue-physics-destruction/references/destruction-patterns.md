# Destruction Patterns

## Geometry Collection Ownership

- Use Geometry Collections for authored fracture; keep ordinary StaticMesh simulation for non-breaking props.
- Define cluster hierarchy, damage thresholds, collision particles, and removal rules before Blueprint or C++ hooks.
- Separate gameplay state from destruction presentation. Let authoritative gameplay decide "destroyed"; let Chaos present fracture when appropriate.

## Damage Flow

1. Validate hit/overlap or gameplay damage source.
2. Apply damage through a narrow component or interface, not scattered Blueprint graph calls.
3. Trigger fracture, VFX, audio, camera shake, and gameplay rewards from one state transition.
4. Persist only the gameplay state unless the project explicitly needs fracture-piece persistence.

## Performance Guardrails

- Limit active shards and debris lifetime.
- Use clustering to avoid too many rigid bodies at once.
- Profile with representative platform scalability settings.
- Provide fallback behavior for low-end platforms: pre-broken meshes, lower shard counts, or non-simulated destruction.

## Validation

- Test editor PIE, standalone, and packaged build when fields/cached simulations are used.
- Confirm replicated projects do not let clients independently decide break state.
- Check navmesh, collision blocking, and save/load behavior after destruction.
