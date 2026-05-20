# UE Debug Validation Checklist

## Evidence

- Output Log errors/warnings/ensures.
- Blueprint compile status and broken pin list.
- C++ build/UHT errors.
- Missing assets, redirectors, invalid classes, failed loads.
- Runtime role/owner/net mode for multiplayer issues.

## Fault Domains

- Data: asset missing, wrong class, wrong defaults, stale redirector.
- Blueprint: duplicate event, broken pin, wrong parent API, bad cast, invalid widget lifecycle.
- C++: include/module dependency, reflection metadata, GC, lifetime, delegate/timer cleanup.
- Networking: wrong authority, missing replication, RPC ownership, RepNotify storm.
- Rendering/VFX: bounds, scalability, material parameter, unsupported feature.
- Config/plugin: disabled plugin, wrong map/game mode, packaging target mismatch.

## Triage

- Reproduce once.
- Remove unrelated variables.
- Find first bad transition.
- Add one targeted log/check at a time.
- Rank hypotheses by confidence and verification cost.
