"""`sdlc-squad` — print the kit path and the per-session load order, or assemble one
skill's full session load.

The kit is Markdown you paste into an AI chat; this command only tells you where the
files are (and can print them concatenated for a one-paste load).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import KIT, LOAD_ORDER, __version__

ROLES = ("pmt", "tpm", "sdm", "sde")


def kit_root() -> Path:
    """The kit on disk: the packaged copy, or the repo root in a source checkout."""
    if KIT.exists():
        return KIT
    return Path(__file__).resolve().parent.parent


def load_order_paths(role: str, skill: str, root: Path) -> list[Path]:
    return [
        root / "shared/system-conventions.md",
        root / "shared/glossary-and-org.md",
        root / f"roles/{role}.md",
        root / f"skills/{role}/{skill}/SKILL.md",
    ]


def assemble(role: str, skill: str, root: Path | None = None) -> str:
    """Return one skill's full session load, concatenated in load order."""
    root = root or kit_root()
    parts = []
    for path in load_order_paths(role, skill, root):
        if not path.exists():
            raise FileNotFoundError(f"missing kit file: {path}")
        body = path.read_text(encoding="utf-8").rstrip()
        parts.append(f"<!-- {path.relative_to(root)} -->\n\n{body}")
    return "\n\n---\n\n".join(parts) + "\n"


def _default() -> int:
    print(f"sdlc-squad {__version__} — kit lives at:")
    print(f"  {kit_root().resolve()}")
    print()
    print("Paste into any AI chat, in order (fill your org slots in glossary-and-org.md):")
    for step in LOAD_ORDER:
        print(f"  {step}")
    print()
    print("Roles:", ", ".join(ROLES))
    print("Paste-ready prompt for every skill: usage/prompts-<role>.md")
    print("One paste per session: sdlc-squad prompt --role <role> --skill <skill>")
    print("Guide: usage/USER-GUIDE.md · Extend/customize: docs/EXTENDING.md")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="sdlc-squad")
    parser.add_argument("--version", action="version", version=f"sdlc-squad {__version__}")
    sub = parser.add_subparsers(dest="cmd")

    prompt = sub.add_parser("prompt", help="print one skill's full session load, concatenated")
    prompt.add_argument("--role", required=True, choices=ROLES)
    prompt.add_argument("--skill", required=True, help="a skill folder under skills/<role>/")

    args = parser.parse_args(argv)

    if args.cmd == "prompt":
        try:
            sys.stdout.write(assemble(args.role, args.skill))
        except FileNotFoundError as exc:
            print(f"sdlc-squad: {exc}", file=sys.stderr)
            return 2
        return 0

    return _default()


if __name__ == "__main__":
    raise SystemExit(main())
