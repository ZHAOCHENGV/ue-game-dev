# AI Behavior Checklist

## Behavior Tree

- Confirm Behavior Tree asset is assigned to the AI Controller and runs after possession.
- Verify Blackboard asset matches the tree and all referenced keys exist with correct types.
- Check that all tasks call `FinishLatentTask` on success, failure, and abort paths.
- Verify decorator observer settings: check condition changes vs. tick-based re-evaluation.
- Keep tree depth manageable; extract reusable branches into subtree assets.
- Validate that services update Blackboard at appropriate intervals, not every frame.

## Blackboard

- Use typed keys: Object, Class, Vector, Rotator, Float, Int, Bool, String, Name, Enum.
- Avoid storing raw UObject pointers; use Object keys with expected base class set.
- Keep key names stable; renaming breaks tree/decorator/service references.
- Clear stale keys when targets are destroyed or contexts change.

## EQS

- Test queries in EQS Testing Pawn before using in runtime trees.
- Limit generator item count to control query cost.
- Use distance tests early to cull far items before expensive trace tests.
- Validate scoring weights produce meaningful differentiation for the intended gameplay.
- Check that context actors/locations are valid at query time.

## AI Perception

- Configure each sense with explicit range, age, and affiliation filters.
- Register stimuli sources on actors that should be perceived.
- Use `OnTargetPerceptionUpdated` for reactive behavior instead of polling.
- Validate that team IDs and affiliations are set correctly for friend/enemy/neutral detection.
- In multiplayer, keep authoritative perception on the server; drive client visuals from replicated state.

## StateTree

- Confirm StateTree asset is assigned and evaluation starts at the correct lifecycle point.
- Keep states focused with clear enter/exit/tick behavior.
- Validate transition conditions and priorities.
- Test fallback/default transitions for unexpected states.
