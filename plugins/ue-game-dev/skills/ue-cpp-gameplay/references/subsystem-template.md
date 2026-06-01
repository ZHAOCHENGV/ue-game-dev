# Subsystem Template

## GameInstance Subsystem

Use `UGameInstanceSubsystem` for services that live across world travel and belong to the running game instance.

```cpp
UCLASS()
class SAMPLEGAME_API UInventoryServiceSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()

public:
    virtual void Initialize(FSubsystemCollectionBase& Collection) override;
    virtual void Deinitialize() override;

    UFUNCTION(BlueprintCallable, Category = "Inventory")
    void RegisterItem(FName ItemId);
};
```

## World Subsystem

Use `UWorldSubsystem` for per-world services that should reset with PIE worlds, maps, or server/client worlds.

```cpp
UCLASS()
class SAMPLEGAME_API UInteractionQuerySubsystem : public UWorldSubsystem
{
    GENERATED_BODY()

public:
    bool QueryInteractables(const FVector& Origin, float Radius, TArray<AActor*>& OutActors) const;
};
```

## Checklist

- Choose subsystem lifetime before adding global state.
- Keep UObject references GC-visible with `UPROPERTY`.
- Avoid storing per-player state in global subsystems unless keyed by player.
- Add Blueprint-callable APIs only when designers need them.
