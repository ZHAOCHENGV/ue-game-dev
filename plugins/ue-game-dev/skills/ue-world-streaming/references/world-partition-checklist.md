# UE World Streaming Checklist

## Map Mode

- Identify whether the map uses World Partition, traditional sublevels, streaming volumes, or a hybrid migration state.
- Confirm persistent level ownership, map inclusion in cook settings, and whether One File Per Actor is enabled.
- List always-loaded actors, streamed actors, runtime-spawned actors, and actors controlled by Data Layers.

## World Partition

- Check runtime grid name, cell size, loading range, and whether the values match traversal speed and platform memory.
- Validate streaming sources: player, camera, custom component, teleport destination, cinematic rail, or server-managed source.
- Keep always-loaded actors intentional; move optional content into streamed cells or Data Layers.
- Use World Partition visualization to inspect loaded, activated, and unloaded cells in editor and PIE.

## Data Layers

- Define whether each Data Layer is editor-only organization, runtime world state, quest phase, biome variant, or mission content.
- Keep Data Layer names stable and document any Blueprint or C++ references.
- Test activate, deactivate, load, unload, save, and restore paths when runtime Data Layers change.

## HLOD

- Assign HLOD layers by asset type and distance role.
- Rebuild HLOD after large placement, mesh, material, or landscape changes.
- Validate proxy material quality, collision expectations, Nanite/Lumen interaction, and platform memory impact.
- Check HLOD behavior in cooked builds when release readiness matters.

## Traditional Level Streaming

- Name streaming levels and volumes clearly.
- Validate load/unload trigger, visibility, collision, lighting, navigation, and BeginPlay/EndPlay timing.
- Avoid references from persistent level assets that force optional sublevel content to stay loaded.

## Runtime And Packaging Validation

- Test fast traversal, teleport, respawn, late join, and save/restore near streaming boundaries.
- Capture memory, hitching, actor count, navigation, and physics symptoms when performance is the concern.
- Confirm required maps and World Partition data are cooked.
- Record the map path, grid/Data Layer names, reproduction route, and first failing symptom in handoff notes.
