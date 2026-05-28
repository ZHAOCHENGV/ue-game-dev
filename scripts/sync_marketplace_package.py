import filecmp
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
    "NOTICE",
    "README.md",
]


def assert_safe_package_root() -> None:
    package_root = PACKAGE_ROOT.resolve()
    plugins_root = (ROOT / "plugins").resolve()
    if package_root == ROOT.resolve() or plugins_root not in package_root.parents:
        raise RuntimeError(f"refusing to remove unsafe path: {package_root}")


def sync_dir(source: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)

    source_names = {child.name for child in source.iterdir()}
    for child in target.iterdir():
        if child.name not in source_names:
            remove_path(child)

    for child in source.iterdir():
        target_child = target / child.name
        if child.is_dir():
            if target_child.exists() and not target_child.is_dir():
                remove_path(target_child)
            sync_dir(child, target_child)
        else:
            copy_file_if_changed(child, target_child)


def remove_path(path: Path) -> None:
    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()


def copy_file_if_changed(source: Path, target: Path) -> None:
    if target.exists() and target.is_dir():
        shutil.rmtree(target)

    if target.exists() and filecmp.cmp(source, target, shallow=False):
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def main() -> None:
    assert_safe_package_root()
    PACKAGE_ROOT.mkdir(parents=True, exist_ok=True)

    for dirname in PACKAGE_DIRS:
        sync_dir(ROOT / dirname, PACKAGE_ROOT / dirname)

    for filename in PACKAGE_FILES:
        copy_file_if_changed(ROOT / filename, PACKAGE_ROOT / filename)

    print(f"synced marketplace package: {PACKAGE_ROOT}")


if __name__ == "__main__":
    main()
