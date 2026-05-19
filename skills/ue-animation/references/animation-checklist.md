# Animation Checklist

## Animation Blueprint

- Confirm Animation Blueprint parent class matches the Skeletal Mesh Skeleton.
- Verify state machine has clear entry state and all states have valid animations assigned.
- Check transition rules use cached boolean properties, not expensive per-frame calculations.
- Validate Blend Space axes match gameplay parameter ranges (speed, direction, lean).
- Keep Event Graph lightweight; move heavy logic to the owning Character or C++ Anim Instance.
- For multi-threaded animation, confirm property access uses `BlueprintThreadSafeUpdateAnimation`.

## Montages

- Verify Montage Skeleton matches the target Skeletal Mesh.
- Confirm Montage sections are named and stable for gameplay code references.
- Check all Anim Notifies and Notify States are assigned and configured.
- Validate blend-in and blend-out settings for smooth transitions.
- Handle `OnMontageEnded`, `OnMontageBlendingOut`, and `OnMontageInterrupted` in gameplay code.
- For networked play, confirm Montage is triggered from server or through replicated events.

## IK And Control Rig

- Verify IK chain setup: effector, root, pole vector, and solver type.
- Test foot IK on flat ground, slopes, stairs, and ledges.
- Check hand IK for weapon grip, object interaction, and ledge grab.
- Validate Control Rig evaluation order and performance impact.
- Keep IK influence driven by animation curves or gameplay state, not hardcoded.

## State Machine

- Every state should have at least one valid exit transition (avoid dead-end states).
- Transition rules should be deterministic: avoid multiple transitions with overlapping conditions.
- Validate automatic rule evaluation vs. explicit transition triggers.
- Check transition blend durations for visual quality.
- Test rapid state changes: interrupt scenarios, animation cancels, and quick direction reversals.

## Root Motion

- Confirm Root Motion Mode on Character Movement Component matches Animation Blueprint settings.
- Test root motion with collision, slopes, and movement mode changes.
- Validate network authority for root motion in multiplayer.
- Check that root motion animations have correct root bone movement baked in.

## Anim Notifications

- Confirm Notify triggers at correct frame/time in the animation.
- Validate Notify State begin/end timing, especially for interrupted or blended animations.
- Check that gameplay-critical Notifies (damage windows, input windows) handle edge cases.
- Keep Notify handler logic lightweight; delegate heavy work to gameplay systems.
