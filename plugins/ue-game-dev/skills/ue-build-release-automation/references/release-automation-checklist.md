# 发版自动化检查清单

## 前置条件

- 用户明确要求打包或发版自动化。
- `.uproject`、UE 安装路径、平台、配置、地图和输出目录已确认。
- 构建机器具备 SDK、证书、权限和磁盘空间。
- 知道会写入 `Binaries/`、`Intermediate/`、`Saved/`、StagedBuilds 和 Archive 目录。

## 命令

- 使用绝对路径。
- 明确 `-platform`、`-clientconfig` / `-serverconfig`、`-build`、`-cook`、`-stage`、`-pak`、`-archive`。
- 需要 server/client 分包时明确 target。
- 地图列表、culture、pak、IoStore、prereqs 按项目策略设置。

## 日志与产物

- 记录 UAT log、Cook log、Project log、Archive 路径。
- 上传或保存失败日志。
- 产物命名包含项目、平台、配置、版本和 commit。

## 安全

- CI secret 不进入源码。
- 证书和 keystore 使用安全存储。
- 自动化脚本不要删除未确认路径。
- 大型产物输出到明确目录，避免污染工作区。
