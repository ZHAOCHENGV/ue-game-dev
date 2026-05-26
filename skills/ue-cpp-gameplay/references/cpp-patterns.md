# UE C++ 玩法模式

## ActorComponent 模式

- 可复用行为优先放 `UActorComponent`，由 Actor 组合。
- 组件负责自身状态、输入命令、事件和验证。
- owner 只负责创建组件、转发高层事件或提供上下文。

```cpp
UCLASS(ClassGroup=(Game), meta=(BlueprintSpawnableComponent))
class UInventoryComponent : public UActorComponent
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category="Inventory")
    bool TryAddItem(FName ItemId, int32 Count);

private:
    UPROPERTY()
    TArray<FInventoryEntry> Items;
};
```

## Subsystem 模式

- `UGameInstanceSubsystem`：跨地图、账号、外部服务、全局配置。
- `UWorldSubsystem`：世界级运行时系统、生成管理、关卡相关状态。
- `ULocalPlayerSubsystem`：本地玩家输入、UI、设置和账号视角。

Subsystem 不应变成万能全局变量；只存放与生命周期匹配的服务。

## DataAsset 模式

- 设计师可调的静态数据放 `UDataAsset` 或 `UPrimaryDataAsset`。
- 运行时状态不要写回 DataAsset。
- 需要异步加载、资产管理或大型表时考虑 Primary Asset。

## UObject 生命周期

- 明确 Outer，通常使用拥有它的 Actor、Component、Subsystem 或 Package。
- 被 UObject 持有的 UObject 引用要通过 `UPROPERTY` 可见。
- 后台任务和 delegate 使用 `TWeakObjectPtr` 防止 owner 销毁后回调。

## Blueprint API

- 用小函数表达命令：`TryAddItem`、`SetOutlineEnabled`、`CanInteract`。
- 返回 bool、enum 或 result struct，避免失败静默。
- 对设计师可调值提供 Category、Clamp、ToolTip 和默认值。
