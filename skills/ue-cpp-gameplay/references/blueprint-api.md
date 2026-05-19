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
