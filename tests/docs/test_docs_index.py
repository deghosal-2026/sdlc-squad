"""Docs-index test: every page under docs/ is listed in docs/README.md, and every row
points at a file that exists (R7).

Run:  python3 tests/docs/test_docs_index.py
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
INDEX = DOCS / "README.md"


class DocsIndex(unittest.TestCase):
    def setUp(self):
        self.text = INDEX.read_text(encoding="utf-8")

    def test_every_docs_page_is_indexed(self):
        missing = []
        for page in sorted(DOCS.glob("*.md")):
            if page.name == "README.md":
                continue
            if page.name not in self.text:
                missing.append(page.name)
        self.assertEqual(missing, [], f"docs pages not listed in docs/README.md: {missing}")

    def test_index_rows_point_at_real_files(self):
        broken = []
        for target in re.findall(r"\]\(([^)]+)\)", self.text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            path = (DOCS / target.split("#", 1)[0]).resolve()
            if not path.exists():
                broken.append(target)
        self.assertEqual(broken, [], f"docs/README.md rows point at missing files: {broken}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
