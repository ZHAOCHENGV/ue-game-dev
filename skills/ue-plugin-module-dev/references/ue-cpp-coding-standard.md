# UE C++ 编码规范

## 反射

- 每个反射类型包含正确的 `GENERATED_BODY()`。
- `.generated.h` 必须是头文件最后一个 include。
- `UCLASS`、`USTRUCT`、`UENUM`、`UINTERFACE` 的 specifier 要有明确目的。
- Blueprint 暴露 API 要提供 Category、默认值、错误路径和验证。

## 头文件

- Public 头使用 forward declaration 降低耦合。
- Private 头和 `.cpp` 才 include 大型引擎/项目头。
- 不在 Public Runtime 头里 include Editor-only 类型。
- 避免把第三方库类型泄漏到大量 Public API。

## UObject 引用

- 需要 GC 可见的引用用 `UPROPERTY`。
- UE5 反射 UObject 引用优先 `TObjectPtr`。
- 临时观察引用用 `TWeakObjectPtr`，异步回调用弱引用。
- 资产引用按加载需求选择 hard reference 或 soft reference。

## 日志与错误

- 使用项目或模块 log category，不滥用 `LogTemp`。
- 失败返回 bool、enum 或 result struct，并写清日志上下文。
- `ensure` 用于可恢复异常，`check` 只用于不可继续的内部不变量。

## 构建

- `.Build.cs` 依赖保持最小。
- Editor 模块依赖不要进入 Runtime。
- 新增平台库要验证 Editor build 和 packaged build。
