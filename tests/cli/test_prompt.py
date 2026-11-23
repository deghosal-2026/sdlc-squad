"""G1 CLI test: `sdlc-squad prompt` output == the four canonical files, in load order.

Run:  python3 tests/cli/test_prompt.py
"""

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from sdlc_squad import cli  # noqa: E402

ORDER = (
    "shared/system-conventions.md",
    "shared/glossary-and-org.md",
    "roles/sdm.md",
    "skills/sdm/sprint-planning-and-capacity/SKILL.md",
)


class PromptAssembly(unittest.TestCase):
    def test_contains_canonical_files_in_order(self):
        out = cli.assemble("sdm", "sprint-planning-and-capacity", root=ROOT)
        positions = []
        for rel in ORDER:
            body = (ROOT / rel).read_text(encoding="utf-8").rstrip()
            self.assertIn(body, out, f"{rel} not found verbatim in the assembled load")
            positions.append(out.index(body))
        self.assertEqual(positions, sorted(positions), "files are out of load order")

    def test_all_20_skills_assemble(self):
        count = 0
        for role in cli.ROLES:
            for skill_dir in sorted((ROOT / "skills" / role).iterdir()):
                if skill_dir.is_dir():
                    cli.assemble(role, skill_dir.name, root=ROOT)
                    count += 1
        self.assertEqual(count, 20, "expected 20 skills to assemble")

    def test_missing_skill_raises(self):
        with self.assertRaises(FileNotFoundError):
            cli.assemble("sdm", "no-such-skill", root=ROOT)


if __name__ == "__main__":
    unittest.main(verbosity=2)
