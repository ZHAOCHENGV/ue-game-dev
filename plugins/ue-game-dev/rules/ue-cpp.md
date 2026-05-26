# UE C++ Rules

## Reflection And Ownership

- Use Unreal reflection intentionally: `UCLASS`, `USTRUCT`, `UFUNCTION`, `UPROPERTY`, and `GENERATED_BODY`.
- Keep reflected state narrow and intentional; expose only what designers or Blueprints need.
- Use `UPROPERTY` for UObject references that must be visible to GC.
- Prefer `TObjectPtr`, `TWeakObjectPtr`, `TSoftObjectPtr`, `TSubclassOf`, and `TSoftClassPtr` over raw UObject pointers.
- Use `CreateDefaultSubobject` for default components and `NewObject` for runtime UObject allocation.

### Good

```cpp
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Combat")
TObjectPtr<UCombatComponent> CombatComponent;
```

### Bad

```cpp
UCombatComponent* CombatComponent; // GC cannot see this reference.
```

## Blueprint Exposure

- Do not expose mutable authoritative state as broad `BlueprintReadWrite` unless designers truly need mutation.
- Prefer `BlueprintReadOnly` state plus narrow `BlueprintCallable` commands with validation.
- Any new Blueprint-exposed API must include Blueprint node search names, pins, graph placement, compile checks, and PIE/editor validation.
- Put stable gameplay contracts in C++; leave tuning values, presentation hooks, and simple composition in Blueprint.

### Bad

```cpp
UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Inventory")
TArray<FInventoryEntry> Items;
```

### Better

```cpp
UFUNCTION(BlueprintCallable, Category = "Inventory")
bool TryAddItem(FName ItemId, int32 Count);
```

## Header And Module Boundaries

- Keep public headers minimal; prefer forward declarations and private includes.
- Avoid leaking editor-only types from Runtime module public headers.
- Runtime modules must not depend on `UnrealEd`, `Blutility`, `AssetTools`, or editor-only UI modules.
- Put editor customization, asset factories, menu extenders, and details panels in Editor modules.

## Runtime Flow

- Avoid Tick unless per-frame behavior is required; prefer timers, delegates, async tasks, or event-driven flow.
- For async work, define ownership, cancellation, game-thread handoff, and UObject lifetime before writing code.
- Validate server authority before mutating gameplay-critical state.

## UE5 Notes

- Prefer `TObjectPtr` for reflected UObject references in UE5 and fix editor validation warnings early.
- Use `UE::Tasks` or task graph helpers for short-lived background work; keep UObject access on the game thread unless explicitly safe.
- Use `FInstancedStruct` when data-driven polymorphic structs are needed without UObject allocation.
- Use Chaos terminology and APIs for physics-facing examples; do not mix legacy PhysX assumptions into UE5 guidance.
