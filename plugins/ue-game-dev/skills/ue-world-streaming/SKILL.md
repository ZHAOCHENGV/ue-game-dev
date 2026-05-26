---
name: ue-world-streaming
description: 当 Unreal Engine 任务涉及 World Partition、Data Layers、HLOD、Level Streaming、Level Streaming Volumes、Large World Coordinates、Runtime Grid、Actor 加载/卸载、开放世界性能或流送验证时使用。
---

# UE World Streaming

## 概览

这个技能负责 UE 世界流送和开放世界组织。先确认地图组织、加载边界、Data Layers、HLOD 和 runtime grid，再设计验证与性能策略。

## 使用场景

- 配置 World Partition、Data Layers、HLOD、Level Streaming 或 Streaming Volumes。
- 排查 Actor 不加载/不卸载、HLOD 异常、开放世界卡顿、Cook 后地图缺失。
- 设计大型地图、分区资源、运行时加载策略和流送性能验证。

## 工作流程

1. 确认地图类型：World Partition、传统 sublevel、Level Instance 或混合方案。
2. 识别 Streaming Source、Runtime Grid、Cell Size、Loading Range 和 Data Layer 规则。
3. 规划 Actor：Always Loaded、spatially loaded、Data Layer 控制、持久 Actor 和运行时生成 Actor。
4. 配置 HLOD、LOD、collision、navigation、lighting 和平台 memory budget。
5. 验证 Editor、PIE、packaged build、远距离移动、传送、多人和 Cook。

## 规则

- 不要把所有 Actor 都设为 Always Loaded 来规避问题。
- Data Layer 用于明确状态或编辑组织，不应替代核心 gameplay state。
- 运行时生成 Actor 需要清楚保存、复制、卸载和恢复策略。
- HLOD 和 World Partition 设置必须在目标平台验证。
- Large World Coordinates 相关系统要检查物理、动画、AI、音频和网络边界。

## 输出

- 世界组织：地图、grid、cell、Data Layer、HLOD、Streaming Source。
- Actor 策略：加载/卸载、持久化、运行时生成、网络和存档。
- 性能风险：内存、IO、HLOD、NavMesh、shader、Cook。
- 验证：Editor/PIE/packaged、平台、移动路径和日志。

## 参考

- World Partition 清单读取 `references/world-partition-checklist.md`。
