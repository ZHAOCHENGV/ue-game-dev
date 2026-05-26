# 从 C++ 设计 Blueprint API

## 暴露方式选择

- 有副作用的动作使用 `BlueprintCallable`。
- 只有便宜、无副作用查询才使用 `BlueprintPure`。
- Blueprint 应拥有实现时使用 `BlueprintImplementableEvent`。
- C++ 提供默认实现、Blueprint 可覆盖时使用 `BlueprintNativeEvent`。
- 设计师或 Widget 需要绑定事件通知时使用 dynamic multicast delegate。

## 属性规则

- 权威状态优先使用 `BlueprintReadOnly`。
- 类默认值使用 `EditDefaultsOnly`，关卡中放置实例覆写使用 `EditInstanceOnly`。
- 类选择用 `TSubclassOf`，不应强制加载的资产用 soft reference。
- Category 要稳定且语义清晰，因为 Blueprint 用户会把它当 API 浏览入口。

## 混合模式

- C++ 拥有校验、权威、replication、save/load 和可复用逻辑。
- Blueprint 拥有默认资产、特效、简单事件响应、timeline 和设计师调参。
- 暴露小而清晰的函数，不要让 Blueprint 直接修改内部状态。

## 必须补充的 Blueprint 实现步骤

当 C++ 改动新增或变更 Blueprint-facing API 时，回复中要包含这一段：

```text
Blueprint 实现 / 调用步骤:
1. 打开: <目标 Blueprint 资产或子类>。
2. 确认父类/API: <C++ parent class, component, interface, function, event, or delegate>。
3. 添加节点: 在 <graph name> 中右键搜索 <exact node/event/function display name>。
4. 连接 exec pins: <event/caller> -> <new C++ API node> -> <next node>。
5. 连接 data pins: <parameter name> 来自 <variable/node>；<return/output> 传给 <consumer>。
6. 必要时添加保护: Is Valid、authority check、branch、cast、interface check 或 widget ownership check。
7. 编译并验证: 编译 Blueprint，运行 PIE/editor 场景，观察 <expected effect/log/UI/replication>。
```

## API 类型到 Blueprint 指引

| C++ 暴露 | 回复中应包含的 Blueprint 指引 |
| --- | --- |
| `BlueprintCallable` | 在哪里调用、由哪条 exec chain 触发、每个输入 pin 来源、预期结果或副作用。 |
| `BlueprintPure` | 在哪里读取、返回什么值、输出 pin 接给哪里，并说明它没有副作用。 |
| `BlueprintImplementableEvent` | 哪个子 Blueprint 实现事件、如何添加事件节点、事件里放哪些视觉/UI/音频/玩法反馈。 |
| `BlueprintNativeEvent` | Blueprint 是否需要 override、何时调用 parent behavior、默认 C++ 已处理什么。 |
| Dynamic multicast delegate | 哪个 Blueprint 绑定 delegate、在哪里绑定、哪个 custom event 接参数、何时解绑。 |
| `BlueprintReadOnly` / editable property | 哪个 Details panel 或 getter 使用它、设计师可调什么、不应直接改什么。 |

## 回复片段示例

对于：

```cpp
UFUNCTION(BlueprintImplementableEvent, Category = "Interaction")
void OnInteractFeedback(AActor* InstigatorActor);
```

包含：

```text
Blueprint 实现:
1. 打开这个 C++ 类的 Blueprint 子类，例如 BP_InteractableDoor。
2. 在 Event Graph 中右键搜索 "Event On Interact Feedback"。
3. 如有需要，用 InstigatorActor 读取位置、controller 或 team。
4. 在该事件中播放 Niagara、声音、动画或 UI 反馈。
5. 编译 Blueprint，在 PIE 中触发交互，确认每次交互只触发一次。
```

对于：

```cpp
UFUNCTION(BlueprintCallable, Category = "Outline")
void SetOutlineEnabled(bool bEnabled);
```

包含：

```text
Blueprint 调用:
1. 在持有该 actor/component 引用的 Blueprint 中，从引用拉线搜索 "Set Outline Enabled"。
2. 把触发 exec pin（例如 BeginPlay、clicked、hover 或 UI button event）接入 Set Outline Enabled。
3. 需要显示描边时把 bEnabled 设为 true，需要清除时设为 false。
4. 编译并运行 PIE，确认只有目标 Actor 的描边发生变化。
```
