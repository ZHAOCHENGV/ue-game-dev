---
name: ue-procedural-generation
description: Unreal Engine procedural generation workflow for PCG, PCG Graphs, ProceduralMeshComponent, InstancedStaticMesh, HierarchicalInstancedStaticMesh, splines, runtime generation, deterministic seeds, streaming integration, collision, navmesh, and cook/runtime asset boundaries. Use when requests involve PCG, procedural worlds, generated geometry, instanced meshes, spline generation, or runtime content generation.
---

# UE Procedural Generation

Use this skill for PCG graphs, runtime generation, instancing, and generated-world workflows. Keep determinism, streaming, collision, and performance explicit.

## First Pass

1. Identify whether generation is editor-authored PCG, runtime PCG, ProceduralMesh, ISM/HISM placement, spline generation, or custom C++ generation.
2. Read the `.uproject`, enabled PCG/procedural plugins, generation assets, target maps, World Partition/Data Layer setup, and nearby naming conventions.
3. Define ownership of generated output: editor-baked assets, runtime transient actors, saved state, replicated state, or deterministic regeneration from seed.
4. Map dependencies: source data, seed, bounds, biome/data assets, collision, navmesh, streaming grid, and cleanup.
5. Define validation: deterministic results, performance, collision/navmesh, packaged build, and streaming behavior.

## PCG Rules

- Use PCG graphs for designer-authored spatial generation and data-driven placement.
- Keep inputs, bounds, seeds, filters, and output actors/components explicit.
- Avoid hidden dependencies on editor-only actors or uncooked assets.
- Validate graph cost and generated instance counts before broadening bounds.
- Store generation configuration in data assets when designers need iteration.

## Runtime Generation Rules

- Use ISM/HISM for high-count repeated meshes; avoid spawning many full actors for static decoration.
- Use ProceduralMesh or runtime mesh approaches only when geometry truly changes at runtime.
- Define collision generation and navmesh update behavior up front.
- Keep deterministic seeds stable when generated state must sync across sessions or network peers.
- Separate generation orchestration from gameplay state mutation.

## Integration Rules

- Use `$ue-world-streaming` when generation depends on World Partition, Data Layers, runtime grids, or level streaming.
- Use `$ue-data-management` for biome tables, generation rule assets, soft references, Asset Manager rules, or cook inclusion.
- Use `$ue-performance-packaging` when instance count, collision cost, cook size, or packaged behavior is the main risk.

## References

- Read `references/procedural-generation-checklist.md` before implementing PCG graphs, runtime generation, instancing, or generated collision.
