# Animation Performance

## Thread Safety

- Enable multi-threaded animation update when the project and Anim Instance support it.
- Use `BlueprintThreadSafeUpdateAnimation` instead of `BlueprintUpdateAnimation` for thread-safe property access.
- Avoid accessing game thread objects (GameState, PlayerController) from animation threads without proper synchronization.
- Mark custom Anim Instance properties for thread-safe access where applicable.

## LOD And Update Rate

- Configure Skeletal Mesh LODs to reduce bone count at distance.
- Use Update Rate Optimization (URO) to reduce animation evaluation frequency for distant or offscreen characters.
- Set `VisibilityBasedAnimTickOption` to skip animation for invisible meshes.
- Configure Anim Budget Allocator for large AI crowds to distribute animation cost.

## Bone Count And Complexity

- Keep runtime bone counts reasonable; consider mesh merging or LOD bone reduction for complex characters.
- Avoid unnecessary physics bodies on non-interactive bones.
- Use animation compression settings appropriate for quality vs. memory tradeoffs.
- Monitor per-character animation evaluation time with Unreal Insights or stat commands.

## Blend And Evaluation Cost

- Limit active blend graph complexity: too many layered blends or additive layers increase cost.
- Cache poses (`SaveCachedPose`) to avoid redundant evaluation of shared sub-graphs.
- Keep Blend Space dimensions to 1D or 2D; avoid unnecessary 3D blend spaces.
- Monitor IK solver iterations and Control Rig evaluation cost.

## Montage And Notify Cost

- Keep Anim Notify handlers lightweight; avoid spawning heavy actors or running expensive queries in Notify callbacks.
- For high-frequency Notifies (footsteps on many characters), use pooling or throttling.
- Batch Montage state updates where possible in networked scenarios.

## Profiling

- Use `stat anim`, Animation Insights, and Unreal Insights for animation thread profiling.
- Check `SkeletalMeshComponent` tick time, animation evaluation time, and cloth/physics simulation time.
- Profile with target character count and camera distance to catch crowd performance issues.
