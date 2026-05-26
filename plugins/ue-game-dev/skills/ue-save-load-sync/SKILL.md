---
name: ue-save-load-sync
description: Unreal Engine save/load and durable state synchronization workflow for SaveGame schema design, serialization, restore pipelines, persistent identifiers, version migration, replicated runtime state, RepNotify, RPC entry points, and server-authoritative validation. Use when requests involve persistence, loading state back into gameplay, checkpointing, late join restore, or deciding what must be saved versus replicated. Use `ue-gas-networking` for ability prediction, ASC setup, attributes, effects, and Gameplay Cues.
---

# UE Save Load Sync

Use this skill when gameplay state must persist, replicate, or both.

## First Pass

1. Define what must persist across sessions and what only exists as runtime replicated state.
2. Identify owners: SaveGame object, GameInstance, GameState, PlayerState, Character/Pawn, ActorComponent, subsystem, or world actor.
3. Define stable identifiers for actors/items/quests and a versioned schema.
4. Define restore timing: startup, level load, player login, respawn, streaming level activation, or manual checkpoint.

## Save/Load Rules

- Keep SaveGame schemas versionable; avoid fragile implicit ordering.
- Serialize stable data, not transient UObject pointers.
- Restore with validation and conflict handling.
- Report partial restore results instead of silently corrupting state.
- Keep designer-authored static asset defaults separate from mutable runtime state.

## Schema Choice

- Use `USaveGame` for ordinary slot-based player, profile, settings, checkpoint, and local progression data.
- Use custom `FArchive` or structured archives only when the project needs compact binary formats, custom versioning, streaming, encryption, or large data sets.
- Use Primary Asset Ids, soft object paths, stable GUIDs, or project-defined row keys for durable references.
- Store schema version and migration notes beside the data that needs migration.

## Restore Timing

- Restore global profile/settings before gameplay systems read them.
- Restore world state after required maps, streamed levels, and asset registries are available.
- Restore player state at login, respawn, possession, or checkpoint boundaries, not from arbitrary widgets.
- Defer presentation updates to RepNotify, delegates, or explicit refresh events after authoritative state is applied.

## Cloud And Local Sync

- Separate local slot format from cloud transport format.
- Define conflict policy: newest timestamp, server-authoritative revision, manual choice, or merge by subsystem.
- Keep write operations atomic where possible: temporary file, commit/rename, then update slot metadata.
- Report sync failures as recoverable states unless data corruption is confirmed.

## Network Sync Rules

- Server owns durable multiplayer gameplay state.
- Use RPCs for client intent and replicated properties/RepNotify for durable observable state.
- Do not assume single-player save logic can run unchanged in multiplayer.
- Reconcile loaded state with current replicated state, authority, late join, and respawn flows.
- Do not model GAS ability prediction or cue behavior here; use `$ue-gas-networking` for ASC and ability-specific replication.

## Migration And Validation

- Test loading the newest schema, at least one older schema, and an invalid/corrupt slot.
- Log migrated version, ignored fields, missing assets, and partial restore failures.
- Validate save timing under level travel, streaming activation, disconnect, reconnect, and shutdown.
- Keep destructive reset/delete operations explicit and user-approved.

## References

- Read `references/save-load-sync-checklist.md` for schema, restore, replication, and migration review.
- Read `references/save-load-templates.md` for SaveGame class, stable identifiers, save/load flow, and version migration code templates.
