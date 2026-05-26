# 动画性能

## 常见成本来源

- Anim Blueprint Event Graph 每帧 Cast 或查找对象。
- 过多 Skeletal Mesh、复杂骨骼、未使用 LOD 或 Update Rate Optimization。
- Control Rig、IK、Motion Matching、Pose Search、曲线和 additive layer 叠加。
- 高频 Notify、昂贵 Blueprint 逻辑和 Tick。

## 优化方向

- 缓存 owner、movement、ability 状态，不在 AnimBP 每帧查找。
- 使用 LOD、Update Rate Optimization、Visibility Based Anim Tick Option。
- 对远距离角色减少 IK、Control Rig、curve 和 montage 复杂度。
- 将复杂状态计算移到 C++、Character 或专门组件。

## 调试工具

- `stat anim`
- `showdebug animation`
- Unreal Insights
- Animation Budget Allocator
- Skeletal Mesh LOD 和 Anim Blueprint profiler

## 验证

- 对比 Editor Preview、PIE 和 packaged build。
- 记录角色数量、摄像机距离、平台、帧率和动画开销。
- 多人场景确认 simulated proxy 的动画 Tick 策略。
