# UE C++ 规则

## 反射与所有权

- 有意识地使用 Unreal 反射：`UCLASS`、`USTRUCT`、`UFUNCTION`、`UPROPERTY` 和 `GENERATED_BODY`。
- 反射状态保持窄而明确，只暴露设计师或 Blueprint 真正需要的内容。
- 需要被 GC 看见的 UObject 引用必须使用 `UPROPERTY`。
- UE5 中优先使用 `TObjectPtr`、`TWeakObjectPtr`、`TSoftObjectPtr`、`TSubclassOf` 和 `TSoftClassPtr`，不要随意裸持有 UObject 指针。
- 默认组件用 `CreateDefaultSubobject`，运行时 UObject 用 `NewObject`，并确认 Outer 与生命周期。

### Good

```cpp
UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Combat")
TObjectPtr<UCombatComponent> CombatComponent;
```

### Bad

```cpp
UCombatComponent* CombatComponent; // GC cannot see this reference.
```

## Blueprint 暴露

- 不要把权威可变状态粗暴暴露为 `BlueprintReadWrite`，除非设计师确实需要直接修改。
- 优先使用 `BlueprintReadOnly` 状态配合窄的 `BlueprintCallable` 命令，并在命令里做校验。
- 新增 Blueprint API 时，要说明节点搜索名、Pin、图中位置、编译检查和 PIE/Editor 验证。
- 稳定玩法契约放 C++，调参值、表现 hook 和简单组合留给 Blueprint。

### Bad

```cpp
UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Inventory")
TArray<FInventoryEntry> Items;
```

### Better

```cpp
UFUNCTION(BlueprintCallable, Category = "Inventory")
bool TryAddItem(FName ItemId, int32 Count);
```

## 头文件与模块边界

- Public 头文件保持最小；优先 forward declaration，把重 include 放到 `.cpp` 或 Private。
- Runtime 模块 Public 头不要泄漏 editor-only 类型。
- Runtime 模块不得依赖 `UnrealEd`、`Blutility`、`AssetTools` 或 editor-only UI 模块。
- Details panel、asset factory、menu extender、编辑器面板等放在 Editor 模块。

## 运行时流程

- 不需要逐帧行为时避免 Tick，优先 timer、delegate、async task 或事件驱动。
- 异步工作在写代码前先定义 ownership、取消、GameThread 回切和 UObject 生命周期。
- 修改 gameplay-critical 状态前确认 server authority、replication 和回滚/失败路径。

## UE5 注意事项

- 反射 UObject 引用优先 `TObjectPtr`，尽早处理编辑器验证警告。
- 短任务可用 `UE::Tasks` 或 Task Graph，除非明确安全，不要在后台线程访问 UObject。
- 需要数据驱动多态 struct 时可考虑 `FInstancedStruct`，避免不必要 UObject 分配。
- 物理相关示例使用 Chaos 术语和 API，不把旧 PhysX 假设混入 UE5 指南。
