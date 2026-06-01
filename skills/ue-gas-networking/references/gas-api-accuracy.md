# GAS API Accuracy Notes

Use this reference before writing or reviewing Gameplay Ability System code. It focuses on avoiding plausible but wrong GAS APIs and unclear network ownership.

## Core Classes

- `UAbilitySystemComponent` owns ability specs, attributes, active gameplay effects, gameplay tags, cues, and prediction keys.
- `UGameplayAbility` owns activation logic. Keep activation authority, cost, cooldown, targeting, montage, and end/cancel behavior explicit.
- `UGameplayEffect` is data-driven state modification. Do not hide gameplay truth only in cosmetic Gameplay Cues.
- `UAttributeSet` owns attributes and replicated attribute notification. Attribute replication needs normal UE replication setup plus GAS attribute macros/patterns used by the project.
- `UGameplayCueNotify_*` classes and cue assets are for presentation and event reactions, not authoritative state.

## Activation And Prediction

- Initialize actor info after owner/avatar relationships are valid, especially after possession.
- Client prediction is for responsive intent that the server can validate and reconcile.
- Server remains authoritative for ability outcomes, cost, cooldown, spawned gameplay actors, and durable state.
- Always define what happens on cancel, blocked activation, failed commit, montage interruption, and avatar destruction.

## Ability Tasks

- Prefer built-in ability tasks for waits, targeting, montage events, gameplay events, delays, and async ability flow when they fit.
- Custom ability tasks must handle activation, delegate binding, cancellation, task end, and avatar/ASC lifetime.
- Do not use ordinary async/threading helpers for ability lifecycle work unless there is a clear game-thread handoff and cancellation model.

## Blueprint Integration

- Blueprint abilities are good for designer-authored orchestration, animation, VFX/SFX, and data-driven hooks.
- C++ abilities are better for reusable targeting, validation, authority-sensitive flow, and shared network behavior.
- Document the Blueprint class, ability input binding, Gameplay Tags, GameplayEffects, GameplayCues, and validation path when handing off GAS work.

## Debug Evidence

- Log ASC owner/avatar, local role, prediction key, ability spec handle, activation result, tags, and active effects near failures.
- Reproduce with at least server plus one client for network-visible ability issues.
