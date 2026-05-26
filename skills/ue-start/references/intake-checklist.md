# UE 入口检查清单

## 必要上下文

- `.uproject` 路径。
- UE 版本。
- 目标平台。
- 当前阶段：旧项目接手、需求、计划、实现、调试、验证、性能、打包。
- 相关系统：C++、Blueprint、UI、GAS、Input、AI、Animation、Render、Save、Services。

## 判断问题

- 用户是要先理解项目，还是直接改功能？
- 需求是否足够清楚，可以进入实施计划？
- 是否有日志、崩溃或错误输出？
- 是否明确要求运行或生成打包自动化？
- 是否需要保存项目记忆？

## 路由

- 旧项目接手：`$ue-project-onboarding`
- 项目阶段：`$ue-stage-detect`
- 需求澄清：`$ue-feature-brief`
- 实施计划：`$ue-implementation-plan`
- 日志/崩溃：`$ue-log-crash-triage`
- 行为调试：`$ue-debug-validation`
- 完成验收：`$ue-feature-done`
