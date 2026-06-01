# HTTP Service Template

Use a subsystem or service object to centralize HTTP calls, JSON parsing, retries, and game-thread dispatch.

```cpp
USTRUCT(BlueprintType)
struct FInventoryItemDto
{
    GENERATED_BODY()

    UPROPERTY(BlueprintReadOnly)
    FName ItemId;

    UPROPERTY(BlueprintReadOnly)
    int32 Count = 0;
};

UCLASS()
class SAMPLEGAME_API UInventoryApiSubsystem : public UGameInstanceSubsystem
{
    GENERATED_BODY()

public:
    void FetchInventory(const FString& PlayerId);

private:
    void HandleInventoryResponse(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bSucceeded);
};
```

## Rules

- Keep auth headers and base URLs out of widgets.
- Parse typed DTOs before notifying gameplay/UI.
- Handle timeout, HTTP error, malformed JSON, and empty response separately.
- Dispatch UI updates on the game thread.
