# Async Blueprint Node 模板

Blueprint 需要异步节点，并且完成后必须回到 GameThread 广播时，使用 `UBlueprintAsyncActionBase`。

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

## 规则

- 生命周期重要的 context 用 `UPROPERTY` 保存。
- worker thread 不直接访问 UObject。
- 在 GameThread 广播结果。
- 长请求要提供取消或 owner lifetime 检查。
