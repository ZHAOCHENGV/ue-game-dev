# HTTP Service 模板

用 Subsystem 或 Service Object 集中管理 HTTP 请求、JSON 解析、重试和 GameThread 分发。

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

## 规则

- auth header 和 base URL 不要散落在 Widget 中。
- 通知 Gameplay/UI 前先解析成 typed DTO。
- timeout、HTTP error、malformed JSON 和 empty response 分开处理。
- UI 更新在 GameThread 分发。
