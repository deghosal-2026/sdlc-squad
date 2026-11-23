"""sdlc-squad — a file distribution: locate the kit, print the load order.

No behavior, no network, no telemetry. The package's only job is putting the
Markdown kit on disk and telling you where it landed.
"""

__version__ = "0.1.0"

from pathlib import Path

KIT = Path(__file__).parent / "kit"

LOAD_ORDER = [
    "shared/system-conventions.md",
    "shared/glossary-and-org.md",
    "roles/<role>.md",
    "skills/<role>/<skill>/SKILL.md",
]