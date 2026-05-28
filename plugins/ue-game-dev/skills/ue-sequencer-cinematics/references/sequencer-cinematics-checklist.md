# Sequencer / Cinematics 检查清单

当任务涉及 Level Sequence、Sequencer 轨道、过场动画、Take Recorder 或 Movie Render Queue 时使用。

## 发现

- 定位 Level Sequence、绑定 Actor、Camera Cut、Animation/Control Rig 轨道、Event Track、音频轨道和目标关卡。
- 确认 sequence 是 runtime 播放、编辑器演出、预渲染输出，还是 Gameplay 中断流程。
- 记录 spawnable/possessable 选择和对象绑定稳定性。

## 运行时播放

- 定义触发入口：Blueprint、C++、关卡脚本、Game Feature、任务系统或编辑器工具。
- 说明播放期间输入、相机、UI、暂停、跳过和恢复行为。
- Event Track 只触发表现还是改变 gameplay state，要明确 authority。
- 需要网络可见时，说明服务器和客户端分别播放什么。

## MRQ 输出

- 固定分辨率、帧率、采样、anti-aliasing、warmup、输出路径和命名。
- 检查渲染地图、关卡可见性、Data Layer、相机和后处理。
- 输出前先做短帧范围 smoke test。

## 验证

- 相机切换、动画同步、音频和事件轨道按预期执行。
- 中断/跳过后 gameplay、输入、UI 和相机恢复。
- Packaged runtime 中播放不依赖 editor-only 对象。
- MRQ 输出帧数、命名和质量设置可复现。
