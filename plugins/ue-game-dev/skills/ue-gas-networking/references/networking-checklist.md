# UE Networking Checklist

## Authority

- Identify who can request the action and who can approve it.
- Validate client requests on the server.
- Keep server-owned state authoritative and replicated.
- Avoid client-only changes to state that affects damage, inventory, movement, cooldowns, or scoring.

## Replication

- Prefer replicated properties for durable state.
- Prefer RPCs for transient events.
- Use replication conditions for owner-only or skip-owner data.
- Consider dormancy, relevancy, late join, respawn, and seamless travel.

## RPC Review

- Server RPC: validate ownership and input.
- Client RPC: send only to the owning connection unless a broader path is intentional.
- Multicast RPC: use for transient, non-durable events; avoid using it as state storage.

## Debug Logs

Log role, net mode, owner, instigator, actor name, connection, prediction key, and relevant gameplay tags near failing paths.

## Multiplayer Validation Matrix

| Check | Listen Server | Dedicated Server | High Ping | Packet Loss |
|---|---|---|---|---|
| Ability activation | required | required | required | optional for early prototype |
| GameplayEffect replication | required | required | required | required before release |
| GameplayCue presentation | required | required | required | required before release |
| Attribute prediction | required when predicted | required when predicted | required | required |
| Character movement ability | required | required | required | required when movement is predicted |

## Prediction Evidence

- Capture prediction key, ability spec handle, activation mode, and rollback/cancel path.
- Validate listen server and dedicated server separately; listen-server success does not prove dedicated-server correctness.
- Use packet lag or network emulation before claiming client prediction is stable.
