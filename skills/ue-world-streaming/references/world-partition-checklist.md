# World Partition 与关卡流送检查清单

## 地图组织

- 确认使用 World Partition、传统 sublevel、Level Instance 还是混合方案。
- 检查 Persistent Level、Data Layers、Runtime Grid、Cell Size 和 Loading Range。
- 标记 Always Loaded Actor、spatially loaded Actor 和由 Data Layer 控制的 Actor。
- 运行时生成 Actor 要定义保存、复制、卸载和恢复策略。

## Streaming Source

- 确认 Streaming Source 来自玩家、摄像机、AI、传送点还是自定义组件。
- 验证快速移动、传送、载具和多人场景下 cell 加载是否及时。
- 不要通过把大量 Actor 设为 Always Loaded 来掩盖 streaming 问题。
- 需要预加载时，写清触发条件、加载半径和失败回退。

## Data Layers

- Data Layer 用于编辑组织、状态切换或区域内容控制。
- 不要让 Data Layer 替代核心 gameplay state 或 save schema。
- 验证 layer 激活/卸载对 AI、音频、VFX、UI prompt 和任务状态的影响。
- 对任务、剧情或开放世界状态，明确与 SaveGame/replication 的边界。

## HLOD 与性能

- 检查 HLOD layer、mesh 合并、材质替换、阴影、collision 和 Nanite 策略。
- 目标平台验证内存、IO、shader、draw call 和 HLOD 切换突变。
- NavMesh、AI、音频和物理可能需要与 streaming 同步验证。
- Large World Coordinates 相关系统要特别关注物理、动画、网络和精度。

## 验证

- Editor viewport、PIE、Standalone、packaged build 都要区分记录。
- 测试远距离移动、传送、快速回头、多人 join、地图切换和 Cook。
- 日志关注 missing package、failed to load、HLOD build、world partition runtime cell。
