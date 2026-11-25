#!/usr/bin/env python3
"""check-frontmatter — validate the kit's frontmatter contract.

Usage:  python3 scripts/check-frontmatter.py [ROOT]

Checks `roles/<role>.md` (except `_TEMPLATE.md`) and `skills/<role>/<skill>/SKILL.md`:

- a leading `---` frontmatter block exists;
- required keys are present — `name`, `role`, `status`, `created` (skills also
  `description`);
- `status` is one of `planned` / `in-progress` / `built` (`CONVENTIONS.md`);
- `created` is ISO `YYYY-MM-DD`;
- `name` matches the folder (skills) or file stem (roles); `role` matches the role dir.

Exit 0 if clean; exit 1 otherwise, listing each violation.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

STATUSES = {"planned", "in-progress", "built"}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---"):
        return None
    fields: dict[str, str] = {}
    for line in text.splitlines()[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return None


def targets(root: Path):
    for path in sorted((root / "roles").glob("*.md")):
        if path.name != "_TEMPLATE.md":
            yield path, "role"
    for path in sorted((root / "skills").glob("*/*/SKILL.md")):
        yield path, "skill"


def check(root: Path) -> list[str]:
    problems: list[str] = []
    for path, kind in targets(root):
        rel = path.relative_to(root)
        fields = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fields is None:
            problems.append(f"{rel}: missing frontmatter block")
            continue
        required = ["name", "role", "status", "created"]
        if kind == "skill":
            required.append("description")
        for key in required:
            if not fields.get(key):
                problems.append(f"{rel}: missing '{key}'")
        status = fields.get("status")
        if status and status not in STATUSES:
            problems.append(f"{rel}: status '{status}' not in {sorted(STATUSES)}")
        created = fields.get("created", "")
        if created and not DATE_RE.match(created):
            problems.append(f"{rel}: created '{created}' is not ISO YYYY-MM-DD")
        if kind == "skill":
            folder, role_dir = path.parent.name, path.parent.parent.name
            if fields.get("name") and fields["name"] != folder:
                problems.append(f"{rel}: name '{fields['name']}' != folder '{folder}'")
            if fields.get("role") and fields["role"] != role_dir:
                problems.append(f"{rel}: role '{fields['role']}' != dir '{role_dir}'")
        else:
            if fields.get("name") and fields["name"] != path.stem:
                problems.append(f"{rel}: name '{fields['name']}' != file '{path.stem}'")
    return problems


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root = Path(argv[0]).resolve() if argv else Path(__file__).resolve().parents[1]
    problems = check(root)
    if problems:
        print(f"check-frontmatter: {len(problems)} violation(s):")
        for problem in problems:
            print("  " + problem)
        return 1
    print("check-frontmatter: roles/ and skills/ frontmatter valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
