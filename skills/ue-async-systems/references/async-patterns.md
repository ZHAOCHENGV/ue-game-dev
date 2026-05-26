# UE 异步模式

## GameThread 回切

后台线程只处理可复制的数据、纯计算或 IO。修改 UObject、广播 Blueprint delegate、触发 Gameplay 状态前，回到 GameThread。

```cpp
Async(EAsyncExecution::ThreadPool, [WeakThis = TWeakObjectPtr<UMyService>(this), Input]()
{
    FMyResult Result = DoBlockingWork(Input);

    AsyncTask(ENamedThreads::GameThread, [WeakThis, Result]()
    {
        if (!WeakThis.IsValid())
        {
            return;
        }

        WeakThis->HandleResult(Result);
    });
});
```

## Blueprint Async Action 骨架

```cpp
UCLASS()
class UMyAsyncAction : public UBlueprintAsyncActionBase
{
    GENERATED_BODY()

public:
    UPROPERTY(BlueprintAssignable)
    FMyAsyncOutput OnSuccess;

    UPROPERTY(BlueprintAssignable)
    FMyAsyncOutput OnFailure;

    UFUNCTION(BlueprintCallable, meta=(BlueprintInternalUseOnly="true", WorldContext="WorldContextObject"))
    static UMyAsyncAction* RunAsync(UObject* WorldContextObject);

    virtual void Activate() override;

private:
    TWeakObjectPtr<UObject> WorldContext;
    bool bCancelled = false;
};
```

实现要求：

- `Activate()` 中启动工作前检查 World 和输入参数。
- 完成、失败、取消都要走同一套收尾逻辑。
- 回调到 Blueprint 前检查 node、World、owner 是否仍有效。
- 如果任务可取消，暴露取消函数或在 owner 销毁时自动取消。

## FRunnable 适用场景

- 长生命周期后台线程。
- 需要显式启动/停止/等待。
- 有持续队列、socket、外部 SDK polling 或专用 worker。

避免为短小异步工作直接使用 `FRunnable`；优先 `UE::Tasks`、`Async()`、TaskGraph 或线程池。

## ParallelFor 注意事项

- 输入数组不可在循环中改变长度。
- 每个迭代写入独立索引或使用线程安全同步。
- 不要在循环体直接访问非线程安全 UObject。
- 数据量太小时 `ParallelFor` 的调度成本可能高于收益。

## 取消与生命周期

- 保存 `TWeakObjectPtr`，不要把 UObject 强捕获进后台 lambda。
- 地图切换、PIE 停止、owner 销毁和重复触发都要能安全退出。
- 长任务要有 timeout、cancel flag 或队列清理策略。
- 日志中区分 `cancelled`、`failed` 和 `owner invalid`，便于排查。
