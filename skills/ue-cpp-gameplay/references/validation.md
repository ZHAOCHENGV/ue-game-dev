# UE C++ Validation Checklist

- Build the touched target with the same engine install the project uses.
- If UHT reflection changed, confirm generated code succeeds and Blueprint-exposed names are stable.
- Start PIE for gameplay paths that depend on world, possession, input, collision, or assets.
- Check logs for ensures, warnings, missing assets, failed loads, invalid casts, and replication warnings.
- For editor-facing properties, confirm defaults and categories are usable in Details panels.
- For asset references, confirm packaging-sensitive paths use soft references or primary assets where appropriate.
- For multiplayer-sensitive code, run server plus at least one client or explain why the path is local-only.
