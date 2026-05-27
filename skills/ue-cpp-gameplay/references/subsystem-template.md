# Subsystem 模板

## GameInstance Subsystem

跨 world travel 存活、归属于运行中 GameInstance 的服务使用 `UGameInstanceSubsystem`。

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

随 PIE world、地图或 server/client world 重置的服务使用 `UWorldSubsystem`。

```cpp
UCLASS()
class SAMPLEGAME_API UInteractionQuerySubsystem : public UWorldSubsystem
{
    GENERATED_BODY()

public:
    bool QueryInteractables(const FVector& Origin, float Radius, TArray<AActor*>& OutActors) const;
};
```

## 检查清单

- 添加全局状态前先选择 Subsystem 生命周期。
- UObject 引用用 `UPROPERTY` 保持 GC 可见。
- 不要把 per-player 状态直接放入全局 Subsystem，除非按 player 分键管理。
- 只有设计师确实需要时才暴露 Blueprint-callable API。
