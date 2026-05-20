import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT / "plugins" / "ue-game-dev"

PACKAGE_DIRS = [
    ".codex-plugin",
    "assets",
    "rules",
    "skills",
    "templates",
]

PACKAGE_FILES = [
    "CHANGELOG.md",
    "LICENSE",
    "README.md",
]


def safe_remove_package() -> None:
    package_root = PACKAGE_ROOT.resolve()
    plugins_root = (ROOT / "plugins").resolve()
    if package_root == ROOT.resolve() or plugins_root not in package_root.parents:
        raise RuntimeError(f"refusing to remove unsafe path: {package_root}")
    if PACKAGE_ROOT.exists():
        shutil.rmtree(PACKAGE_ROOT)


def main() -> None:
    safe_remove_package()
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)

    for dirname in PACKAGE_DIRS:
        shutil.copytree(ROOT / dirname, PACKAGE_ROOT / dirname)

    for filename in PACKAGE_FILES:
        shutil.copy2(ROOT / filename, PACKAGE_ROOT / filename)

    print(f"synced marketplace package: {PACKAGE_ROOT}")


if __name__ == "__main__":
    main()
