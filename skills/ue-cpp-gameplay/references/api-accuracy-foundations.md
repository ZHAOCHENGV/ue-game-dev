# UE C++ API 准确性基础

本参考吸收 MIT 许可 `quodsoler/unreal-engine-skills` 的 API 校验思路，并按 UE Game Dev 插件风格改写。给出 C++ 代码前用它减少虚构 UE API。

## 反射检查

- 每个反射类、结构体、枚举都需要匹配的 generated include 和 `GENERATED_BODY()`。
- 只有需要反射、Blueprint、config、序列化、复制或编辑器暴露时，才使用 `UCLASS`、`USTRUCT`、`UENUM`、`UFUNCTION`、`UPROPERTY`。
- UE5 结构体优先使用 `GENERATED_BODY()`，不要引入旧式 generated body 宏。
- `AddDynamic` 绑定动态多播 delegate 时，目标函数必须是 `UFUNCTION`。
- RPC 声明需要对应 `_Implementation`；不要凭空添加 validation 签名，除非项目/引擎版本已有这种风格。

## UObject 生命周期

- 反射的 UObject 成员使用 `UPROPERTY()`，UE5 项目通常配合 `TObjectPtr<T>`。
- 非拥有缓存引用使用 `TWeakObjectPtr<T>`。
- 可选资产使用 `TSoftObjectPtr<T>`、`TSoftClassPtr<T>` 或 Primary Asset ID，避免强加载。
- 不要用 `TSharedPtr` 或 `TUniquePtr` 管理 UObject 派生类型。
- 非 UObject owner 如果必须持有 UObject 引用，需要明确 GC 引用策略，例如 `FGCObject` 或 UObject owner。

## 容器与字符串

- 反射或 gameplay-facing 数据优先使用 UE 容器：`TArray`、`TMap`、`TSet`。
- 避免在 ranged-for 中修改 `TArray`；删除元素时用索引或收集后处理。
- 稳定标识用 `FName`，可变字符串/路径用 `FString`，玩家可见文本用 `FText`。
- 项目已有 Gameplay Tags 时，玩法分类优先用 Tag，不要用字符串硬编码。

## Subsystem 访问

- `UGameInstanceSubsystem`：通过 `GetGameInstance()->GetSubsystem<T>()`，跨地图加载保留。
- `UWorldSubsystem`：通过 `GetWorld()->GetSubsystem<T>()`，作用域是 world/PIE instance。
- `ULocalPlayerSubsystem`：通过 LocalPlayer 获取，每个本地用户一份。
- `UEngineSubsystem`：通过 `GEngine->GetEngineSubsystem<T>()`，全局 engine 生命周期。

## 复制检查

- replicated property 同时需要反射 specifier 和 `GetLifetimeReplicatedProps`。
- `ReplicatedUsing` 需要匹配的 `UFUNCTION` OnRep handler。
- 把可变复制状态暴露给 Blueprint 前，先定义 owner、authority、prediction、save/load 和 UI 通知边界。

## 发送代码前

- 尽量用项目附近代码或 UE 头文件确认类名和函数名。
- 每个可能需要 `.Build.cs` 的 include/API 都说明所属模块。
- 使用 `TObjectPtr`、Enhanced Input、StateTree、Mass、PCG 等较新 API 时说明引擎版本假设。
