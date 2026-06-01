# BuildGraph And Release Artifacts

## Release Inputs

- Project:
- Engine version:
- Platform:
- Configuration:
- Client/server targets:
- Cook maps:
- DLC/chunk rules:

## Artifact Outputs

- Packaged build:
- Symbols:
- Crash reporter symbols:
- Logs:
- Build metadata:
- AutomationTool output:
- Installer/archive:

## CI Notes

- Jenkins/Horde node labels:
- Shared DDC:
- Clean workspace policy:
- Credentials and signing:
- Archive retention:

## BuildGraph Checks

- Identify whether the project already has a BuildGraph XML or Horde template.
- Keep node names, artifact names, and archive paths stable for downstream jobs.
- Store UAT, Cook, and packaging logs as separate artifacts.
- Preserve symbols and build metadata with the packaged output.
