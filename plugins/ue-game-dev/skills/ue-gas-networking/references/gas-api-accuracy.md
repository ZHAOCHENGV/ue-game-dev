# GAS API 准确性备注

编写或审查 Gameplay Ability System 代码前使用本参考，重点是避免看似合理但错误的 GAS API，以及不清楚的网络所有权。

## 核心类型

- `UAbilitySystemComponent` 拥有 ability spec、attribute、active gameplay effect、gameplay tag、cue 和 prediction key。
- `UGameplayAbility` 拥有激活逻辑；必须说明 authority、cost、cooldown、targeting、montage、end/cancel 行为。
- `UGameplayEffect` 是数据驱动的状态修改，不要把权威玩法状态只藏在 cosmetic Gameplay Cue 里。
- `UAttributeSet` 拥有属性与属性复制通知；属性复制需要普通 UE replication 设置和项目采用的 GAS attribute 宏/模式。
- `UGameplayCueNotify_*` 类和 cue 资产用于表现与事件反应，不是权威状态来源。

## 激活与预测

- owner/avatar 关系有效后初始化 actor info，尤其是 possession 之后。
- Client prediction 用于响应式意图，服务器必须能校验并修正。
- Ability outcome、cost、cooldown、生成 gameplay actor 和持久状态仍由服务器权威决定。
- 必须定义 cancel、blocked activation、commit 失败、montage 中断和 avatar 销毁时的行为。

## Ability Task

- 等待、targeting、montage event、gameplay event、delay 和异步 ability flow 优先使用内置 ability task。
- 自定义 ability task 必须处理 activation、delegate binding、cancellation、task end 和 avatar/ASC 生命周期。
- 不要用普通 async/threading helper 承担 ability 生命周期，除非有明确 game-thread 回切和取消模型。

## Blueprint 集成

- Blueprint ability 适合设计师编排、动画、VFX/SFX 和数据化 hook。
- C++ ability 更适合可复用 targeting、校验、authority-sensitive flow 和共享网络行为。
- GAS 交接要记录 Blueprint class、ability input binding、Gameplay Tags、GameplayEffects、GameplayCues 和验证路径。

## 调试证据

- 失败附近记录 ASC owner/avatar、local role、prediction key、ability spec handle、activation result、tags 和 active effects。
- 网络可见 ability 问题至少用服务器 + 一个客户端复现。
