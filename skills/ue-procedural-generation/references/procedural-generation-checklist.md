# Procedural Generation Checklist

Use this checklist when a task involves PCG, runtime generation, instanced placement, spline generation, or generated geometry.

## Inputs

- Generation bounds and source actors.
- Seed and determinism requirements.
- Rule assets, biome data, DataTables, curves, or tags.
- Mesh/material references and cook inclusion path.

## Output Model

- Editor-baked output, runtime transient output, saved output, or deterministic regeneration.
- Actor count versus ISM/HISM instance count.
- Collision generation and navmesh update behavior.
- Cleanup and regeneration policy.

## Performance

- Estimate instance counts and spawned actor counts.
- Check construction script/editor-time cost separately from runtime cost.
- Avoid generating expensive collision or navmesh updates every frame.
- Include scalability rules for dense foliage, props, or crowds.

## Evidence

- PIE generation result with expected seed.
- Packaged asset availability note.
- Collision/navmesh validation when gameplay depends on generated content.
