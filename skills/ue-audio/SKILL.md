---
name: ue-audio
description: 当 Unreal Engine 任务涉及 MetaSound、Sound Cue、AudioComponent、Sound Class、Sound Mix、Sound Concurrency、Quartz、空间化、衰减、音频调试、音频性能或平台音频设置时使用。
---

# UE Audio

## 概览

这个技能负责 UE 音频系统的设计、实现和排查。先确认播放由谁拥有，再决定使用 MetaSound、Sound Cue、AudioComponent、Sound Class/Mix、Concurrency、Quartz 或平台配置。

## 使用场景

- 设计自适应音乐、脚步声、武器音效、UI 音效、环境声、空间化音源。
- 排查音频不播放、循环不停止、声音过多、衰减不对、平台 Cook 后异常。
- 用 MetaSound 做参数化音频，用 Quartz 做节拍同步，用 Sound Mix 做动态混音。

## 工作流程

1. 确认播放拥有者：Actor、Component、Subsystem、UI Widget、Anim Notify、Niagara 或 Ability。
2. 判断播放生命周期：一次性、循环、附着、池化、淡入淡出或显式 `UAudioComponent` 管理。
3. 设计参数：MetaSound exposed inputs、Sound Cue 随机/调制、Gameplay 状态和更新频率。
4. 配置混音：Sound Class、Sound Mix、Concurrency、attenuation、occlusion、spatialization。
5. 验证平台：压缩、streaming、采样率、声道数、Cook 行为和 `stat audio`。

## 规则

- 多人游戏复制 Gameplay 事件或 Cue，不复制底层音频播放状态，除非项目已有专门音频同步层。
- 高频参数更新要限流，优先事件驱动或低频 Timer。
- 循环音源使用 `UAudioComponent` 管生命周期，owner 销毁前决定停止或淡出。
- UI 音效默认非空间化并绑定本地玩家。
- 大量重复音效必须配置 Concurrency 和虚拟化行为。

## 输出

- 音频资产：MetaSound、Sound Cue、Sound Wave、Sound Class/Mix、Concurrency、Attenuation。
- 播放路径：触发方、生命周期、停止/淡出规则、网络边界。
- 性能与平台：voice 数、CPU、streaming、Cook 风险。
- 验证：编辑器、PIE、packaged build 和可听症状记录。

## 参考

- 设计和排查读取 `references/audio-checklist.md`。
