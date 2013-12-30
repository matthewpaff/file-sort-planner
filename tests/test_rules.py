from pathlib import Path
import tempfile
import unittest

from filename_rules_lab.core import plan
from filename_rules_lab.fixture_check import check


class RulesTests(unittest.TestCase):
    def test_mixed_extensions_and_hidden_files(self):
        result = plan(["notes.PDF", "photo.jpg", ".env", "README", "archive.tar.gz"])
        self.assertEqual([row["folder"] for row in result], ["documents", "images", "hidden", "other", "archives"])

    def test_rejects_paths_duplicates_and_invalid_names(self):
        for names in (["../a.txt"], ["a\\b"], ["C:a"], ["."], [".."], ["\x00"], [], ["   "], ["a.TXT", "A.txt"]):
            with self.subTest(names=names), self.assertRaises(ValueError):
                plan(names)

    def test_is_only_a_plan_and_preserves_order(self):
        self.assertEqual(plan(["missing.py", "missing.txt"]), [
            {"name": "missing.py", "folder": "code", "destination": "code/missing.py"},
            {"name": "missing.txt", "folder": "documents", "destination": "documents/missing.txt"}])

    def test_all_generated_fixtures(self):
        path = Path(__file__).resolve().parents[1] / "fixtures" / "cases.jsonl"
        self.assertGreaterEqual(check(path, plan), 350)

    def test_fixture_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.jsonl"
            path.write_text('{"id":"bad","input":["x.txt"],"expected":[]}\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                check(path, plan)


if __name__ == "__main__":
    unittest.main()
