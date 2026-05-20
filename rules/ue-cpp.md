# UE C++ Rules

- Use Unreal reflection intentionally: `UCLASS`, `USTRUCT`, `UFUNCTION`, `UPROPERTY`, and `GENERATED_BODY`.
- Prefer `TObjectPtr`, `TWeakObjectPtr`, `TSoftObjectPtr`, `TSubclassOf`, and `TSoftClassPtr` over raw UObject pointers.
- Use `CreateDefaultSubobject` for default components and `NewObject` for runtime UObject allocation.
- Keep public headers minimal; prefer forward declarations and private includes.
- Do not expose mutable authoritative state as broad `BlueprintReadWrite` unless designers truly need mutation.
- Any new Blueprint-exposed API must include Blueprint node search names, pins, graph placement, compile checks, and PIE/editor validation.
- Avoid Tick unless per-frame behavior is required; prefer timers, delegates, async tasks, or event-driven flow.
- Keep Runtime and Editor dependencies separate.
