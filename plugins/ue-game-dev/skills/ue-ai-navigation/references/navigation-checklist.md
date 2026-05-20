# Navigation Checklist

## NavMesh Configuration

- Confirm Nav Mesh Bounds Volume covers all navigable areas.
- Match agent radius, height, max step height, and walkable slope to the AI Pawn capsule.
- Configure multiple supported agents when different AI types have different sizes.
- Check tile size and cell size for resolution vs. performance tradeoffs.
- Rebuild navigation after level geometry or settings changes.

## Dynamic Navigation

- Use Nav Modifier Volumes for runtime area cost changes.
- Use Nav Link Proxies for jumps, drops, ladders, and custom traversal.
- Confirm dynamic obstacles update NavMesh or use avoidance rather than blocking silently.
- Validate that runtime NavMesh regeneration is enabled when level geometry changes at runtime.

## Pathfinding

- Use AI Controller `MoveToLocation`/`MoveToActor` for standard path requests.
- Set acceptance radius appropriate for the gameplay action at the destination.
- Handle path failure: no path found, partial path, path invalidated mid-move.
- Use path following events or delegates to trigger gameplay at waypoints.
- For crowd movement, configure RVO avoidance with appropriate radius and priority.

## Query Filters

- Use custom navigation query filters to prefer or avoid specific area classes.
- Set area costs intentionally: roads cheaper, rough terrain expensive, restricted areas excluded.
- Apply filters per-query when different AI types should navigate differently.

## Debugging

- Use `Show Navigation` to visualize NavMesh in editor and PIE.
- Check `RecastNavMesh` properties for generation diagnostics.
- Use `AI Debugging` and `GameplayDebugger` for live path and avoidance visualization.
- Log path request results, remaining path points, and move status near failing AI movement.
