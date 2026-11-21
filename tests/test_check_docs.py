import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import check_links


class CheckDocsTests(unittest.TestCase):
    def test_accepts_existing_local_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "guide.md").write_text("# Guide\n", encoding="utf-8")
            (root / "README.md").write_text("[Guide](guide.md)\n", encoding="utf-8")

            self.assertEqual(check_links(root), [])

    def test_rejects_broken_and_empty_links(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("[Missing](missing.md) [Empty](#)\n", encoding="utf-8")

            errors = check_links(root)

            self.assertEqual(len(errors), 2)
            self.assertIn("unresolved local link", errors[0])
            self.assertIn("empty link target", errors[1])

    def test_rejects_links_outside_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            (root / "README.md").write_text("[Outside](../outside.md)\n", encoding="utf-8")

            self.assertEqual(len(check_links(root)), 1)


if __name__ == "__main__":
    unittest.main()
