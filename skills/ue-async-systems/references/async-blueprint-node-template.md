# Async Blueprint Node Template

Use `UBlueprintAsyncActionBase` for Blueprint-facing async work that must return to the game thread before broadcasting.

```cpp
UCLASS()
class SAMPLEGAME_API ULoadItemIconAsync : public UBlueprintAsyncActionBase
{
    GENERATED_BODY()

public:
    UPROPERTY(BlueprintAssignable)
    FOnIconLoaded Completed;

    UPROPERTY(BlueprintAssignable)
    FOnIconLoadFailed Failed;

    UFUNCTION(BlueprintCallable, meta = (BlueprintInternalUseOnly = "true"))
    static ULoadItemIconAsync* LoadItemIconAsync(UObject* WorldContextObject, TSoftObjectPtr<UTexture2D> Icon);

    virtual void Activate() override;

private:
    UPROPERTY()
    TObjectPtr<UObject> WorldContext;

    TSoftObjectPtr<UTexture2D> IconPath;
};
```

## Rules

- Store context as `UPROPERTY` when lifetime matters.
- Do not touch UObjects from worker threads.
- Broadcast on the game thread.
- Provide cancellation or owner lifetime checks for long requests.
