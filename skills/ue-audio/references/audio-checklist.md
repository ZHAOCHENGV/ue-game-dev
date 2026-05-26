# UE Audio 检查清单

## 播放归属

- 确认 owner：Actor、Component、Subsystem、UI Widget、Anim Notify、Niagara 事件或 Ability。
- 判断播放类型：一次性、循环、附着、池化，还是由 `UAudioComponent` 显式管理。
- 定义停止/淡出行为：owner 销毁、状态退出、地图切换、暂停和重试路径。
- 多人场景复制 gameplay event 或 cue；不要复制底层音频状态，除非项目已有音频同步层。

## MetaSound 与 Sound Cue

- MetaSound 适合程序化图、参数化自适应音频和 UE5 原生音频逻辑。
- Sound Cue 适合简单随机、调制和旧项目一致性。
- 暴露参数按玩法含义命名，例如 `EngineRpm`、`HealthRatio`、`SurfaceType`。
- 参数更新频率要受控，优先事件驱动或低频 timer，避免无意义逐帧写入。

## AudioComponent

- 循环 ambience、附着发声体、淡入淡出、参数更新和显式生命周期控制使用 AudioComponent。
- C++ 中创建组件引用时使用 `UPROPERTY` 或明确 owner 生命周期。
- 验证 `AutoActivate`、attachment socket、attenuation override 和 owner 状态切换后的存活行为。
- 如果不希望突兀截断，owner 销毁前先停止或淡出组件。

## 混音、并发和空间化

- Sound Class 管分类音量，Sound Mix 管运行时 ducking 或 mix transition。
- 高频重复音效（脚步、UI click、impact、武器、环境声）要配置 Concurrency。
- 检查 voice limit、resolution rule、retrigger time 和 virtualization。
- 世界声音验证 attenuation shape、falloff、occlusion、spatialization 和 listener position。
- UI 声音默认非空间化并绑定本地玩家。

## 平台与 Profiling

- 确认目标平台的压缩、streaming、采样率和声道数。
- 怀疑 voice 数、source 数或 CPU 成本时使用 `stat audio` 和 Audio Insights。
- codec、streaming 或 Cook 行为有风险时，必须测 packaged build。
- 交接报告记录首个可听症状、期望行为、资产路径、owner 和 runtime trigger。
