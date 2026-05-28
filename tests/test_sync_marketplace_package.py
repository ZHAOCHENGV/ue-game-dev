import tempfile
import unittest
from pathlib import Path
from unittest import mock

import scripts.sync_marketplace_package as sync_marketplace_package


class SyncMarketplacePackageTests(unittest.TestCase):
    def test_copy_file_if_changed_leaves_identical_file_untouched(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source.txt"
            target = Path(tmp) / "target.txt"
            source.write_text("same\n", encoding="utf-8")
            target.write_text("same\n", encoding="utf-8")
            before = target.stat().st_mtime_ns

            sync_marketplace_package.copy_file_if_changed(source, target)

            self.assertEqual(target.read_text(encoding="utf-8"), "same\n")
            self.assertEqual(target.stat().st_mtime_ns, before)

    def test_sync_dir_removes_extra_files_and_copies_changed_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "source"
            target = Path(tmp) / "target"
            (source / "nested").mkdir(parents=True)
            target.mkdir()
            (source / "nested" / "keep.txt").write_text("source\n", encoding="utf-8")
            (target / "extra.txt").write_text("extra\n", encoding="utf-8")

            sync_marketplace_package.sync_dir(source, target)

            self.assertFalse((target / "extra.txt").exists())
            self.assertEqual((target / "nested" / "keep.txt").read_text(encoding="utf-8"), "source\n")

    def test_assert_safe_package_root_rejects_repo_root(self) -> None:
        with mock.patch.object(sync_marketplace_package, "PACKAGE_ROOT", sync_marketplace_package.ROOT):
            with self.assertRaises(RuntimeError):
                sync_marketplace_package.assert_safe_package_root()


if __name__ == "__main__":
    unittest.main()
