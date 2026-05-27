# Chaos Physics Checklist

## Collision Setup

- Record component collision enabled mode: No Collision, Query Only, Physics Only, or Query and Physics.
- Confirm object type, trace channel responses, and named profile match the gameplay contract.
- Check `GenerateOverlapEvents`, `Simulation Generates Hit Events`, CCD, mass, damping, and sleep thresholds.
- Validate collision complexity; avoid complex-as-simple on movable simulated objects unless the cost is understood.

## Simulation

- Identify who owns simulation: static mesh, skeletal body, Geometry Collection, constraint chain, or custom component.
- Decide whether physics state is gameplay-authoritative, replicated, cosmetic, or restored from save data.
- Keep impulses and forces in the correct frame of reference and avoid applying physics from multiple owners.
- Validate substepping, async physics, and fixed timestep assumptions before tuning force magnitudes.

## Ragdoll And Constraints

- Verify Physics Asset bodies, constraints, profiles, and mass distribution.
- Test entry and exit states: animation pose capture, collision profile switch, input disable, recovery montage, and cleanup.
- Keep constraint limits stable; large mass ratios and hard angular limits often cause jitter.
- For multiplayer, state whether ragdoll simulation is local presentation or server-owned replicated state.

## Debug Evidence

- Use `show COLLISION`, `stat physics`, Chaos debug draw, and collision analyzer tools when available.
- Capture the smallest PIE repro with object names, expected collision response, and actual overlap/hit events.
- Include before/after collision profile values in handoff notes.
