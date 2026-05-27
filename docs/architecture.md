# UE Game Dev 架构

## 路由流程

```mermaid
graph TD
    A[用户请求] --> B[ue-game-dev-router]
    B --> C{硬规则检查}
    C -->|多 Agent| D[ue-multi-agent-workflow]
    C -->|日志或崩溃| E[ue-log-crash-triage]
    C -->|显式打包| F[ue-build-release-automation]
    C -->|阶段类请求| G[start / stage / gate / brief / plan / done]
    C -->|未命中| H{领域加权评分}
    H -->|最高分| I[领域技能]
    H -->|无匹配| J[ue-game-dev-router 兜底]
```

## 关键边界

- `skills/ue-game-dev-router/SKILL.md` 是给 Agent 阅读的人类路由契约。
- `scripts/validate_plugin.py` 用测试路由镜像这份契约，防止路由场景回退。
- 根目录插件文件是源头，`plugins/ue-game-dev/` 由 `scripts/sync_marketplace_package.py` 生成。
- 自动打包必须保持显式触发。发布准备、诊断和打包失败不能静默进入 `$ue-build-release-automation`。

## 发布检查

提交插件改动前运行：

```powershell
$env:PYTHONUTF8='1'
python scripts\sync_marketplace_package.py
python scripts\validate_plugin.py
python -m unittest discover tests
git diff --check
```
