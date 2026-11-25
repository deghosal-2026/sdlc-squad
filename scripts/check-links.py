#!/usr/bin/env python3
"""check-links — resolve every relative Markdown link in the repo.

Usage:  python3 scripts/check-links.py [ROOT]

Exit 0 if every relative link resolves; exit 1 otherwise, listing each broken link as
`<file>:<line>: <target>`. Absolute URLs, `mailto:`, `tel:`, and pure `#anchor` links
are ignored. Generated/vendored trees are skipped.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__",
    "dist", "build", "output", ".mypy_cache", ".pytest_cache", ".ruff_cache",
}
SKIP_PREFIXES = ("sdlc_squad/kit",)
SKIP_SUFFIXES = (".egg-info",)

# [text](target) or [text](target "title"); capture the target.
LINK_RE = re.compile(r"\[[^\]]*\]\(\s*([^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\s*\)")
EXTERNAL = ("http://", "https://", "mailto:", "tel:", "#")


def _skipped(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    if any(part in SKIP_DIRS for part in rel.parts):
        return True
    if any(part.endswith(SKIP_SUFFIXES) for part in rel.parts):
        return True
    rel_str = "/".join(rel.parts)
    return any(rel_str.startswith(p) for p in SKIP_PREFIXES)


def check(root: Path) -> list[str]:
    problems: list[str] = []
    for md in sorted(root.rglob("*.md")):
        if _skipped(md, root):
            continue
        for lineno, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for match in LINK_RE.finditer(line):
                target = match.group(1)
                if target.startswith(EXTERNAL):
                    continue
                path_part = target.split("#", 1)[0].split("?", 1)[0]
                if not path_part:
                    continue
                if path_part.startswith("/"):
                    resolved = root / path_part.lstrip("/")
                else:
                    resolved = md.parent / path_part
                if not resolved.resolve().exists():
                    problems.append(f"{md.relative_to(root)}:{lineno}: {target}")
    return problems


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    root = Path(argv[0]).resolve() if argv else Path(__file__).resolve().parents[1]
    problems = check(root)
    if problems:
        print(f"check-links: {len(problems)} broken link(s):")
        for problem in problems:
            print("  " + problem)
        return 1
    print("check-links: all relative links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
