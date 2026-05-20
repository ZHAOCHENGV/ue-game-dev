# UE Networking Rules

- Server owns gameplay-critical state.
- Define authority path before implementation: local input, server RPC, replicated property, RepNotify, or GAS activation.
- Use `DOREPLIFETIME` and replication conditions intentionally.
- Use RPCs sparingly and validate client-provided data on the server.
- State prediction, reconciliation, relevancy, and dormancy assumptions when applicable.
- Multiplayer validation must name the minimum PIE or dedicated server scenario and client count.
- Replicate state, not cosmetic noise; route cosmetics through cues, events, or client-side prediction when safe.
