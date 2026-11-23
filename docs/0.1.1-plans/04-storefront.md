# 04 — Storefront & positioning

Theme: the surfaces where install intent forms — the README, the PyPI page, and the
repo's own presentation. All additive; the fact-check verified these surfaces are
already accurate for v0.1.0.

## E1. PKG-README pass

- **Current state:** `PKG-README.md` is current and correct for v0.1.0 — right PMT
  name, the correct four-file load order, honest "What it never does" block, clean
  install section. The 0.1.1 work is **additive**, not corrective.
- **What:** link the new docs into it (`usage/WALKTHROUGH.md` as "see a full run",
  `docs/START-HERE.md` as "find your skill", `docs/MODELS.md`, `docs/EVIDENCE.md` as
  "how the kit catches itself"); add the upgrade-safety note to the
  `pip install --upgrade` line (your `my-org.md` survives upgrades by living outside
  the kit — F3); keep the tagline consistent with the README; verify rendering on the
  PyPI page after publish (the recorded-run discipline: check the real destination,
  not just the source).
- **Why:** the PyPI page is where `pip install` intent forms; it was never reviewed by
  the gap analysis or the fact-check — now it gets the same treatment as the README.
- **Acceptance:** PKG-README carries the links and the upgrade-safety note; tagline
  matches the README; render verified on the live PyPI page post-publish.

## E2. "Why not just ask the chat directly?" — README section

- **What:** 5–8 lines showing the delta: `[CONFIRM]` over invention; canonical schema
  binding (columns, ID prefixes, ISO dates); one-role isolation; the import-target
  block; and the evidence — 20 fixtures, 97 recorded checks, 13 caught defects (link
  `docs/EVIDENCE.md`).
- **Why:** the #1 silent objection every visitor has; the launch article argues it
  narratively but the README never does, and the README is where the objection is
  formed.
- **Acceptance:** every line claims something already evidenced elsewhere in the repo;
  no new facts; no benchmarks.

## E3. Repo presentation

- **What:** social preview image (committed asset), GitHub repo description + topics,
  one tagline across README / PKG-README / article, and a **Mermaid relay diagram** in
  the README (GitHub renders Mermaid natively in Markdown files) showing the loop —
  PMT → TPM → SDM → SDE with the artifact each hand-off carries.
- **Competitive validation (from the scan, [08](08-competitive-landscape.md)):** the
  closest competitor ships a PDF of flow diagrams for exactly this purpose; a Mermaid
  diagram is the lighter, repo-native version.
- **Why:** signals a maintained project; affects click-through from GitHub search and
  external links; the loop is the product story and is currently text-only.
  Charter-safe: repo settings, one image file, one diagram — no code behavior.
- **Acceptance:** tagline identical everywhere it appears; topics set; preview renders;
  the Mermaid diagram renders on GitHub and matches the relay rows in F2.

## E4. Examples gallery — `docs/EXAMPLES.md`

- **What:** a one-line index of all 20 committed fixtures — each row: skill → the
  sample input in one phrase → the artifact it produces → where it lands. The fixtures
  already ARE complete worked examples (synthetic input + expected artifact + checks,
  per `tests/README.md`); today they live under `tests/` framed for maintainers.
- **Why:** an evaluating customer wants to inspect output quality without reading test
  infrastructure (gap P3: "make example artifacts easier to inspect"); C1 shows one
  run in depth — this shows all 20 at a glance.
- **Acceptance:** all 20 fixtures indexed; every row traceable to its fixture file;
  linked from README and PKG-README.
