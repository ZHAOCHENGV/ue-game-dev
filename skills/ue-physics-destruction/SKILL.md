---
name: ue-physics-destruction
description: Unreal Engine physics and destruction workflow for Chaos Physics, collision channels, Physical Materials, Geometry Collections, Fracture, Ragdoll, Physics Constraints, physics animation blending, collision debugging, and physics performance. Use when requests involve physical simulation, breakable objects, collision response, ragdoll, or Chaos troubleshooting.
---

# UE Physics Destruction

Use this skill for UE5 Chaos Physics, collision setup, breakable objects, ragdolls, and physics debugging. Keep gameplay authority, collision data, asset authoring, and runtime performance connected.

## First Pass

1. Identify whether the request is collision filtering, rigid body simulation, ragdoll, constraint setup, Geometry Collection destruction, or physics performance.
2. Locate the owning Actor, mesh/component hierarchy, collision profiles, Physical Materials, Physics Asset, and relevant Blueprint/C++ setup.
3. Decide whether state is purely cosmetic, gameplay-authoritative, replicated, saved, or driven by animation.
4. Gather evidence with collision view, physics debugger, logs, and minimal PIE repro before changing profiles or assets.
5. Define the validation path: overlap/hit events, impulse response, constraint stability, fracture behavior, network authority, and packaged sanity.

## Collision And Simulation Rules

- Use project collision channels intentionally; avoid solving gameplay interactions with broad `BlockAll` or `OverlapAll` profiles.
- Keep object type, trace response, and collision enabled mode aligned: Query Only, Physics Only, or Query and Physics.
- Prefer named collision profiles for reusable gameplay categories.
- Validate `GenerateOverlapEvents`, `Simulation Generates Hit Events`, mass, damping, and collision complexity before debugging code.
- Use Physical Materials for surface behavior, footstep/VFX routing, and friction/restitution tuning; do not hard-code surface behavior by mesh name.

## Chaos And Destruction

- Use Geometry Collections for authored fracture and Chaos destruction, not ordinary StaticMeshComponent simulation.
- Define damage thresholds, clustering, collision particles, and removal/lifetime rules before gameplay hooks.
- Keep breakable gameplay authority explicit: server decides state, clients present fracture/VFX/audio unless the project has deterministic sync.
- Validate destruction in cooked builds when fields, cached simulations, or platform scalability matter.

## Ragdoll And Constraints

- Use Physics Assets and constraint profiles for skeletal simulation, hit reactions, and ragdoll.
- Blend animation and physics deliberately; define entry, recovery, and cleanup states.
- Keep constraints stable with sane angular limits, mass ratios, projection, and substepping when needed.
- For networked ragdolls, define whether the ragdoll is cosmetic client-side or server-authoritative.

## Performance And Debugging

- Use `show COLLISION`, Chaos Visual Debugger/Physics Debugger, `p.Chaos.DebugDraw.Enabled`, and `stat physics` when available.
- Reduce active simulated bodies, high-frequency overlap checks, and complex-as-simple collision on movable objects.
- Use substepping only when stability needs it; document platform cost.
- Include a minimal PIE scenario and expected collision/physics events in the final answer.

## References

- Read `references/chaos-physics-checklist.md` before changing collision, simulation, ragdoll, or constraints.
- Read `references/destruction-patterns.md` before implementing Geometry Collection or fracture workflows.
- Use shared `rules/ue-performance.md` when physics cost, tick rate, or platform scalability is part of the task.
