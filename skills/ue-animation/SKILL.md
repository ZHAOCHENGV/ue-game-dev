---
name: ue-animation
description: Unreal Engine animation workflow for Animation Blueprints, montages, blend spaces, state machines, IK, Control Rig, skeletal mesh, anim notifications, root motion, Motion Matching, Linked Anim Graphs, animation curves, pose snapshots, and animation debugging. Use when requests involve character animation, procedural animation, animation logic, or animation performance.
---

# UE Animation

Use this skill for character and gameplay animation systems. Treat animation as a blend of data-driven assets and runtime logic that bridges gameplay and visual presentation.

## First Pass

1. Read the `.uproject`, existing Animation Blueprints, Skeletons, Skeletal Meshes, Montages, Blend Spaces, and anim-related C++ classes.
2. Identify the animation framework: Animation Blueprint state machine, Linked Anim Layers, Control Rig, Motion Matching, or custom procedural animation.
3. Map the animation actor set: Character/Pawn, Skeletal Mesh Component, Animation Blueprint, Animation Instance, Montage assets, Blend Spaces, and Notify assets.
4. Determine whether animation logic belongs in Animation Blueprint graph, C++ Anim Instance, or gameplay code driving animation parameters.
5. Check Skeleton compatibility, retargeting setup, and shared Skeleton/IK Rig configuration before creating or modifying animation assets.

## Animation Blueprint Rules

- Keep Animation Blueprint state machines focused: one primary locomotion state machine with clear enter/exit transitions.
- Use Blend Spaces for multi-axis locomotion blending (speed/direction) instead of manual lerp logic.
- Use Linked Anim Layers and Linked Anim Graphs to share animation logic across multiple Animation Blueprints without duplication.
- Keep Event Graph logic minimal; prefer state machine transitions and cached poses over per-frame Blueprint graph complexity.
- Use thread-safe `BlueprintThreadSafeUpdateAnimation` for property access when the project enables multi-threaded animation.
- Avoid calling gameplay functions directly from Animation Blueprints; use cached properties set by the owning Character/Pawn.

## Montage Rules

- Use Montages for one-shot or triggered animations: attacks, abilities, reactions, interactions, and cinematics.
- Define Anim Notify States and Anim Notifies for gameplay-relevant timing: damage windows, sound cues, VFX spawns, combo windows.
- Keep Montage sections named clearly and stable; section names are referenced by gameplay code.
- Handle Montage completion, interruption, and blend-out explicitly in gameplay code.
- For multiplayer, play Montages through GAS or replicated events; avoid client-only Montage plays for authoritative actions.

## IK And Procedural Animation

- Use Control Rig or built-in IK nodes for foot placement, hand targeting, look-at, and procedural adjustments.
- Keep IK solver settings (chain length, precision, iteration count) tuned for quality vs. performance.
- Validate IK behavior on slopes, stairs, uneven terrain, and edge cases.
- For full-body IK or procedural motion, prefer Control Rig over manual bone transform manipulation.

## Motion Matching (UE 5.3+)

- Use Motion Matching when the project benefits from database-driven animation selection over hand-authored state machines.
- Keep the animation database well-organized with clear pose search schemas and trajectory matching.
- Validate transition quality and responsiveness vs. visual smoothness tradeoffs.
- Monitor runtime cost: database size, search frequency, and pose comparison complexity.

## Root Motion

- Decide root motion authority: animation-driven vs. gameplay-driven movement.
- Keep root motion mode consistent between Animation Blueprint and Character Movement Component.
- For networked characters, handle root motion authority on the server and replicate results.
- Validate root motion with collision, slopes, and movement mode transitions.

## State Machine Design

- Keep states named descriptively: `Idle`, `Walk`, `Run`, `Jump_Start`, `Jump_Loop`, `Jump_Land`, `Attack_Light`.
- Use transition rules with clear boolean conditions derived from cached gameplay properties.
- Avoid circular transition paths without explicit guards.
- Use transition blend settings intentionally: cross-fade duration, blend mode, and blend profile.
- Keep conduit nodes focused on routing logic, not as hidden state containers.

## Anim Notifications

- Use Notify States for duration-based events (damage windows, trail effects).
- Use Notifies for instant events (footstep sounds, particle spawns).
- Keep Notify names stable; they are referenced by C++ and Blueprint handlers.
- Implement `UAnimNotify` and `UAnimNotifyState` subclasses in C++ for reusable, performance-sensitive, or gameplay-critical notifications.
- Handle Notify firing in edge cases: interrupted Montages, blended animations, and low-frame-rate scenarios.

## Animation Curves

- Use animation curves for driving blend weights, material parameters, IK influence, and gameplay timing.
- Access curves from Animation Blueprint or gameplay code via `GetCurveValue`.
- Keep curve names stable and documented.

## Debugging

- Use Animation Insights, Anim Blueprint debugger, and skeleton debug rendering.
- Visualize active state, blend weights, Montage position, and IK targets.
- Log animation instance class, active Montage, state machine state, and blend parameters near failing paths.
- For performance, check animation thread time, bone count, LOD effectiveness, and update rate optimization.

## References

- Read `references/animation-checklist.md` for Animation Blueprint, Montage, IK, and state machine validation.
- Read `references/animation-performance.md` for animation LOD, threading, and optimization review.
- Use `$ue-cpp-gameplay` when animation needs custom Anim Instance, Notify, or component implementation.
- Use `$ue-gas-networking` when Montages or animation state integrate with GAS abilities or multiplayer replication.
