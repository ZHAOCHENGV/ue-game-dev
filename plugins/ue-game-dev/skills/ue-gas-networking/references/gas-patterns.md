# GAS Patterns

## ASC Initialization

- Confirm ASC owner and avatar are set on server and owning client.
- Reinitialize after possession, respawn, pawn swap, or player state handoff.
- Bind input after the ASC and ability specs are ready.

## Abilities

- Use activation requirements and gameplay tags to gate behavior.
- Keep authority-sensitive mutations on the server.
- Predict only responsive actions that can be corrected cleanly.
- End abilities on all paths: success, cancel, failure, montage interrupt, target loss, and owner destruction.

## Effects And Attributes

- Use gameplay effects for tunable attribute changes and duration policies.
- Keep attribute clamping consistent, usually in attribute set hooks or project-standard aggregators.
- Treat replicated attributes as gameplay state, not UI-only display values.

## Gameplay Cues

- Use cues for cosmetics tied to gameplay events or effect state.
- Do not store authoritative gameplay state only in cue notifies.
- Validate cue execution paths for dedicated server, listen server, owning client, and simulated proxies.
