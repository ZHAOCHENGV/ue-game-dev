# UE Performance Rules

## Tick And Timers

- Disable unused ticks with `PrimaryActorTick.bCanEverTick = false`.
- Prefer events or timers over low-value polling.
- Keep tick work bounded and visible in profiling.
- Avoid per-frame casts, asset searches, and `GetAllActorsOfClass` in gameplay loops.

## Memory And Asset Loading

- Use soft references for optional, large, cosmetic, or mode-specific assets.
- Preload at mode boundaries when first-use hitching matters.
- Keep DataTables and Data Assets from hard-referencing entire content catalogs unintentionally.
- Validate packaged cook coverage for soft references.

## Rendering

- Use LODs, cull distance, instancing, Nanite suitability checks, and material complexity review.
- Keep Niagara bounds and scalability settings explicit.
- Control shader permutations and material feature switches.
- Validate visual work on target scalability settings, not only editor defaults.

## Physics

- Reduce active simulated bodies and high-frequency overlap checks.
- Avoid complex-as-simple collision on movable simulated objects unless the cost is measured.
- Use substepping only when stability needs it.
- Limit destruction debris lifetime, collision, and shard counts.

## Networking

- Replicate minimal authoritative state.
- Use relevancy, dormancy, and frequency controls.
- Avoid high-frequency reliable RPCs.
- Profile multiplayer features with the minimum PIE or dedicated server scenario that matches the feature.

## Packaging

- Separate editor-only behavior from packaged runtime behavior.
- Treat release readiness, package failure diagnosis, and automatic packaging as separate workflows.
- Include a smoke test for features whose behavior depends on cook, config, soft references, or platform settings.
