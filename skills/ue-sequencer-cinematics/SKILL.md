---
name: ue-sequencer-cinematics
description: 当 Unreal Engine 请求涉及 Sequencer、Level Sequence、Movie Render Queue、MRQ、过场动画、镜头轨道、事件轨道、Take Recorder、剧情演出或渲染输出流水线时使用。
---

# UE Sequencer Cinematics

这个技能处理 Sequencer、Level Sequence 和 Movie Render Queue。重点是把镜头/轨道、运行时触发、事件边界、资产引用和渲染输出可重复性说清楚。

## 工作流程

1. 读取 Level Sequence、绑定 Actor、Camera Cut、Control Rig/Animation 轨道、Event Track、关卡和渲染配置。
2. 判断用途：过场动画、Gameplay 内演出、预渲染影片、Take Recorder 捕捉，还是 MRQ 批量输出。
3. 梳理触发方式：关卡启动、Blueprint、C++、Game Feature、任务系统或编辑器工具。
4. 确认边界：哪些轨道驱动 gameplay，哪些只是表现；事件轨道是否需要 authority 或只在本地播放。
5. 定义验证：绑定稳定性、相机切换、动画同步、音频、跳过/中断、packaged runtime 和 MRQ 输出。

## 设计规则

- Level Sequence 资产要避免隐藏依赖临时关卡对象；绑定和 spawnable/possessable 选择要明确。
- Gameplay 关键状态不要只靠 Event Track 的表现事件驱动，必要时由 gameplay system 拥有状态。
- 运行时播放要定义输入锁定、UI 遮罩、相机切换、跳过和恢复。
- MRQ 输出要固定分辨率、帧率、anti-aliasing、warmup、路径和命名。
- 与 Control Rig、Animation Blueprint、root motion 或角色移动交叉时，要明确谁拥有最终姿态。

## 跨域交接

- 动画蓝图、Montage、Control Rig 和姿态同步进入 `$ue-animation`。
- UI 遮罩、字幕、跳过按钮或 CommonUI 流程进入 `$ue-client-ui`。
- 渲染质量、材质、后处理或性能进入 `$ue-render-vfx` 或 `$ue-performance-packaging`。

## 参考

- 添加 Sequencer 演出、事件轨道或 MRQ 输出流水线前读取 `references/sequencer-cinematics-checklist.md`。
