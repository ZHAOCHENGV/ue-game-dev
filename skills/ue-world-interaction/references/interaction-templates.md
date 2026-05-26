# 世界交互模板

## C++ 接口示例

```cpp
UINTERFACE(BlueprintType)
class UInteractable : public UInterface
{
    GENERATED_BODY()
};

class IInteractable
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category="Interaction")
    bool CanInteract(AActor* InstigatorActor) const;

    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category="Interaction")
    FText GetInteractionPrompt(AActor* InstigatorActor) const;

    UFUNCTION(BlueprintNativeEvent, BlueprintCallable, Category="Interaction")
    void Interact(AActor* InstigatorActor);
};
```

## 组件职责

```text
Interactor Component
- Trace/Overlap 查找候选目标
- 维护当前 focused target
- 通知 UI prompt
- 向 server 提交交互意图

Interactable Component / Interface
- 判断 CanInteract
- 提供 prompt
- 执行 Interact
- 播放或触发表现反馈
```

## Blueprint 接法

```text
1. 在可交互 Actor 上实现 IInteractable 或添加 Interactable Component。
2. 实现 CanInteract，返回是否满足距离、状态、权限或资源条件。
3. 实现 GetInteractionPrompt，返回玩家可见文本。
4. 实现 Interact，执行拾取、开门、生成、播放反馈等逻辑。
5. 在 Player/Pawn 上添加 Interactor Component，绑定 IA_Interact。
6. PIE 中验证焦点、提示、执行、失败和目标销毁路径。
```

## 失败结果结构

```cpp
UENUM(BlueprintType)
enum class EInteractResult : uint8
{
    Success,
    OutOfRange,
    Blocked,
    MissingRequirement,
    InvalidTarget
};
```

用明确结果替代静默失败，UI 和日志才能给出正确反馈。
