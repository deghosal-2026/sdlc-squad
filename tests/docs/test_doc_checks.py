"""Doc-check tests: the tooling behind `make check-links` / `make check-frontmatter`.

Each script must pass on the real repo and fail on a seeded break (I7's acceptance).

Run:  python3 tests/docs/test_doc_checks.py
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK_SCRIPT = ROOT / "scripts" / "check-links.py"
FM_SCRIPT = ROOT / "scripts" / "check-frontmatter.py"


def run(script: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script), *args],
        capture_output=True,
        text=True,
    )


class CheckLinks(unittest.TestCase):
    def test_real_repo_passes(self):
        result = run(LINK_SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_seeded_broken_link_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.md").write_text("see [missing](missing.md)\n", encoding="utf-8")
            result = run(LINK_SCRIPT, str(root))
            self.assertEqual(result.returncode, 1)
            self.assertIn("missing.md", result.stdout)

    def test_external_and_anchor_links_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.md").write_text(
                "[web](https://example.com) [top](#here) [mail](mailto:x@y.z)\n",
                encoding="utf-8",
            )
            self.assertEqual(run(LINK_SCRIPT, str(root)).returncode, 0)


class CheckFrontmatter(unittest.TestCase):
    def test_real_repo_passes(self):
        result = run(FM_SCRIPT)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_bad_status_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills" / "pmt" / "draft-prd"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: draft-prd\nrole: pmt\nstatus: bogus\n"
                "created: 2026-01-01\ndescription: x\n---\n",
                encoding="utf-8",
            )
            result = run(FM_SCRIPT, str(root))
            self.assertEqual(result.returncode, 1)
            self.assertIn("bogus", result.stdout)

    def test_name_folder_mismatch_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills" / "sdm" / "sprint-retro"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text(
                "---\nname: wrong-name\nrole: sdm\nstatus: built\n"
                "created: 2026-01-01\ndescription: x\n---\n",
                encoding="utf-8",
            )
            self.assertEqual(run(FM_SCRIPT, str(root)).returncode, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
