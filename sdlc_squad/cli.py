"""`sdlc-squad` — prints the kit path and the per-session load order.

That is the entire CLI. The kit is Markdown you paste into an AI chat; this
command only tells you where the files are.
"""

from pathlib import Path

from . import KIT, LOAD_ORDER, __version__

ROLES = ("pmt", "tpm", "sdm", "sde")


def main() -> int:
    print(f"sdlc-squad {__version__} — kit lives at:")
    print(f"  {KIT.resolve()}")
    print()
    print("Paste into any AI chat, in order (fill your org slots in glossary-and-org.md):")
    for step in LOAD_ORDER:
        print(f"  {step}")
    print()
    print("Roles:", ", ".join(ROLES))
    print("Paste-ready prompt for every skill: usage/prompts-<role>.md")
    print("Guide: usage/USER-GUIDE.md · Extend/customize: docs/EXTENDING.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())