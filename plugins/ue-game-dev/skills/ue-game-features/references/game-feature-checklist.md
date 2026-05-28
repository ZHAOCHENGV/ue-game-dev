# Game Feature 检查清单

当任务涉及 Game Feature Plugins、ModularGameplay、GameFeatureAction 资产或 Lyra 风格 Experience 时使用。

## 发现

- 定位 `.uproject`、feature `.uplugin`、feature modules、`Config/`、`Content/`、Experience 和 Action Set 资产。
- 确认插件类型、Loading Phase、启用状态，以及功能是常驻、可选择、流送加载还是 DLC 风格。
- 识别对 GameplayAbilities、EnhancedInput、CommonUI、ModularGameplay、GameFeatures、AssetManager 和项目 framework 模块的依赖。

## 激活模型

- 说明 register、load、activate、deactivate 和 error 阶段分别发生什么。
- 保证 action 幂等：不会重复添加组件、输入映射、ability spec、delegate、UI layer 或数据注册。
- 每个 activation grant 都要有对应的 deactivation cleanup。
- 区分服务器权威 gameplay grant 与客户端本地表现 grant。

## Lyra 风格 Experience 审查

- 识别 Experience、Experience Action Set、Pawn Data、Ability Set、Input Config、HUD Layout 和默认 Gameplay Tags。
- 检查 asset reference 和 bundle，确保 feature 内容可 Cook、可加载，不依赖 editor-only 路径。
- 显式记录跨 feature 依赖，避免假设另一个 feature 已经激活。

## 完成证据

- PIE 激活/停用结果。
- Game Feature 状态转换日志。
- feature-owned 内容的 Asset/Cook 证据。
- 当涉及 ability、input、pawn data 或复制状态时，提供多人验证证据。
