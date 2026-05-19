# Save Load Sync Checklist

## Save Schema

- Version field.
- Stable identifiers.
- Primitive/struct data only where possible.
- Soft object paths or primary asset ids for asset references.
- Migration path for old saves.

## Restore Flow

- Validate data before applying.
- Resolve assets/classes.
- Spawn or find runtime actors.
- Apply state in dependency order.
- Report partial failures.

## Replication Flow

- Server owns durable multiplayer state.
- RPCs carry client intent, not final truth.
- Replicated properties carry durable observable state.
- RepNotify updates client presentation.
- Consider late join, respawn, seamless travel, and reconnect.

## Conflict Rules

- Decide whether loaded state overrides runtime state.
- Decide whether runtime authority rejects stale save data.
- Keep local-only saves separate from server-authoritative saves.
