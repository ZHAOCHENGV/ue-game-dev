# Chaos Physics 检查清单

## 碰撞设置

- 记录组件 Collision Enabled：No Collision、Query Only、Physics Only 或 Query and Physics。
- 确认 object type、trace channel response 和 named profile 符合玩法契约。
- 检查 `GenerateOverlapEvents`、`Simulation Generates Hit Events`、CCD、mass、damping 和 sleep threshold。
- 验证 collision complexity；movable simulated object 默认避免 complex-as-simple，除非已知成本。

## 模拟

- 识别模拟拥有者：static mesh、skeletal body、Geometry Collection、constraint chain 或 custom component。
- 决定物理状态是 gameplay-authoritative、replicated、cosmetic，还是从 save data 恢复。
- forces 和 impulses 使用正确参考系，避免多个 owner 同时驱动物理。
- 调整力大小前先验证 substepping、async physics 和 fixed timestep 假设。

## 布娃娃与约束

- 检查 Physics Asset bodies、constraints、profiles 和 mass distribution。
- 测试进入/退出：animation pose capture、collision profile 切换、禁用输入、恢复 montage 和 cleanup。
- 保持 constraint limit 稳定；大 mass ratio 和硬 angular limit 容易抖动。
- 多人项目要说明 ragdoll simulation 是本地表现还是服务器状态。

## 调试证据

- 可用 `show COLLISION`、`stat physics`、Chaos debug draw 和 collision analyzer 工具。
- 捕获最小 PIE 复现，包含对象名、期望 collision response 和实际 overlap/hit event。
- 在交接中记录修改前后的 collision profile 值。
