# Blueprint API Design From C++

## Exposure Choices

- Use `BlueprintCallable` for actions with side effects.
- Use `BlueprintPure` only for cheap queries without side effects.
- Use `BlueprintImplementableEvent` when Blueprint should own the implementation.
- Use `BlueprintNativeEvent` when C++ provides a default and Blueprint can override.
- Use dynamic multicast delegates for event notifications that designers or widgets bind to.

## Property Rules

- Prefer `BlueprintReadOnly` for authoritative state.
- Use `EditDefaultsOnly` for class defaults and `EditInstanceOnly` for placed actor overrides.
- Use `TSubclassOf` for class picks and soft references for assets that should not force-load.
- Keep categories stable and meaningful; Blueprint users see these as API.

## Hybrid Pattern

- C++ owns validation, authority, replication, save/load, and reusable logic.
- Blueprint owns default assets, effects, simple event responses, timelines, and designer tuning.
- Expose small functions with clear names instead of asking Blueprints to mutate internal state directly.

## Required Blueprint Implementation Steps

When a C++ change adds or changes any Blueprint-facing API, include this section in the user response:

```text
Blueprint implementation / call steps:
1. Open: <target Blueprint asset or child class>.
2. Confirm parent/API: <C++ parent class, component, interface, function, event, or delegate>.
3. Add node: right-click in <graph name> and search for <exact node/event/function display name>.
4. Wire exec pins: <event/caller> -> <new C++ API node> -> <next node>.
5. Wire data pins: <parameter name> comes from <variable/node>; <return/output> goes to <consumer>.
6. Add guards if needed: Is Valid, authority check, branch, cast, interface check, or widget ownership check.
7. Compile and validate: compile Blueprint, run PIE/editor scenario, and observe <expected effect/log/UI/replication>.
```

## API Type To Blueprint Guidance

| C++ exposure | Blueprint guidance to include |
| --- | --- |
| `BlueprintCallable` | Where to call it, which exec chain triggers it, each input pin source, and what result or side effect to expect. |
| `BlueprintPure` | Where to read it, what value it returns, and where to feed the output pin without implying side effects. |
| `BlueprintImplementableEvent` | Which child Blueprint implements the event, how to add the event node, and what visual/UI/audio/gameplay response belongs inside it. |
| `BlueprintNativeEvent` | Whether Blueprint should override the event, when to call parent behavior, and what the default C++ behavior already handles. |
| Dynamic multicast delegate | Which Blueprint binds to the delegate, where binding happens, which custom event receives parameters, and when to unbind if needed. |
| `BlueprintReadOnly` / editable property | Which Details panel or variable getter uses it, what designers can tune, and what they should not mutate directly. |

## Example Response Fragments

For:

```cpp
UFUNCTION(BlueprintImplementableEvent, Category = "Interaction")
void OnInteractFeedback(AActor* InstigatorActor);
```

Include:

```text
Blueprint implementation:
1. Open the Blueprint child of this C++ class, for example BP_InteractableDoor.
2. In Event Graph, right-click and search "Event On Interact Feedback".
3. Use InstigatorActor to read actor location, controller, or team if needed.
4. Play Niagara, sound, animation, or UI feedback from this event.
5. Compile the Blueprint and trigger interaction in PIE to verify the event fires once per interaction.
```

For:

```cpp
UFUNCTION(BlueprintCallable, Category = "Outline")
void SetOutlineEnabled(bool bEnabled);
```

Include:

```text
Blueprint call:
1. In the Blueprint that owns a reference to this actor/component, drag from the reference and search "Set Outline Enabled".
2. Connect the triggering exec pin, such as BeginPlay, clicked, hover, or UI button event, into Set Outline Enabled.
3. Set bEnabled to true when the outline should appear and false when it should be cleared.
4. Compile and run PIE; verify the outline changes on the intended actor only.
```
