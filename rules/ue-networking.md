# UE Networking Rules

## Authority

- Server owns gameplay-critical state.
- Define authority path before implementation: local input, server RPC, replicated property, RepNotify, or GAS activation.
- Validate ownership before accepting client RPCs.
- Never trust client-provided targets, damage, inventory counts, currency, or cooldown state without server-side checks.

## Replication

- Replicate server-owned observable state, not client intent.
- Use `DOREPLIFETIME` and replication conditions intentionally.
- Use `RepNotify` for client presentation updates that must react to state changes.
- State relevancy, dormancy, and initial replication assumptions when they affect the feature.

### Common Mistakes

- Forgetting `bReplicates = true` or component replication when the owning Actor is replicated.
- Adding `DOREPLIFETIME` but never mutating the property on the server.
- Mutating replicated state in `OnRep` instead of using it for presentation or cache repair.
- Replicating cosmetic noise instead of routing cosmetics through cues, events, or client-side prediction when safe.

## RPCs

- Use RPCs sparingly and keep payloads small.
- Rate-limit high-frequency client actions and prefer compressed intent over large structs.
- Use reliable RPCs only for events that must arrive; unreliable is often correct for frequent transient input or effects.
- Never send asset payloads, large arrays, or repeated JSON blobs through gameplay RPCs without a clear bandwidth budget.

## GAS Handoff

- For Gameplay Ability System work, define ASC owner/avatar, replication mode, prediction key path, and GameplayCue ownership.
- Route ability activation through GAS APIs instead of custom RPCs when prediction, costs, cooldowns, or cancellation matter.
- Replicate attributes through AttributeSets and use gameplay effects for state changes that need network semantics.

## Listen Server And Dedicated Server

- Test listen server behavior separately when the host is also a player; local authority can hide ownership mistakes.
- Dedicated server validation must not rely on viewport, local player controller, or client-only assets.
- Multiplayer validation must name the minimum PIE or dedicated server scenario and client count.

## Validation

- Capture expected server log, client log, replicated property value, and visible client result.
- Test late join, reconnect, or respawn when persistent replicated state is part of the feature.
- Keep packaging and network validation separate unless the request explicitly asks for release readiness.
