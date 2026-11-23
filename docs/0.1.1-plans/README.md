# 0.1.1 plans — the patch, split by theme

Working plan for the v0.1.1 patch, broken into themed files so each area can be read,
worked, and checked off independently. Supersedes the single `docs/0.1.1-items.md` —
that file's content lives here, unchanged in substance, and item IDs are stable
(A1…G6). Not yet committed; when the work lands, these files ride in the same commit
as the 0.1.1 CHANGELOG entry.

Written 2026-11-23 from: the fact-check of the launch materials (kit breakdown, dev.to
article draft, external customer-view gap review) verified against this repo at `main`
@ `394430f` — the released v0.1.0; the usability research pass; and the competitive
web scan ([08](08-competitive-landscape.md), run with the user's go on 2026-11-23).

## The goal for 0.1.1

Make the kit **installable-to-first-artifact in one sitting**, make its honesty
discipline feel like quality instead of friction, and fix the two structural usability
defects the research pass found: the **upgrade clobber** (the kit's only customization
point — the filled glossary — is destroyed by its own upgrade path) and the **paste
burden** (a measured ~340–370 lines must be pasted in strict order, every session). A
patch cannot prove "world class" — only real users pasting real artifacts into real
Jira/Confluence/GitHub (ROADMAP v0.1.x) can do that. Scope of real-world proof stays in
v0.1.x; nothing here claims it early.

## Scope rules

- Additions are **docs-only, plus generated bundle artifacts**: new Markdown files, edits
  to `README.md`, `usage/USER-GUIDE.md`, `SECURITY.md`, `PKG-README.md`,
  `docs/EXTENDING.md`, and a `Makefile` target that generates `usage/bundles/` (packaging
  tooling, the same class as the existing `make sync` — the kit's runtime stays inert). No
  schema changes (schema-shape work is at least a minor version — `CONVENTIONS.md`), no
  new skills, no fixture work, no `SKILL.md` changes, no CLI behavior changes — unless a
  G-decision in [06](06-open-decisions.md) is taken, in which case the affected files
  are amended before work starts.
- **Bundles and the no-second-copy rule** (`docs/EXTENDING.md` standing rule 1): bundles
  are *generated* files, never hand-edited; each carries a "generated — do not edit"
  header; freshness is machine-checked at release time (`make check-bundles` regenerates
  and diffs — a stale bundle fails the gate). Same discipline as `sdlc_squad/kit/` via
  `make sync`, but committed so pip users receive them.
- Every new fact must trace to committed material: fixtures, the recorded run
  (`tests/results/run-2026-11-22-v0.1.0.md`), or existing docs. The fictional org for
  examples is **Meridian Outfitters** — already the example company across
  `usage/prompts-*.md` and the fixtures. No real org data anywhere.
- New docs follow the existing docs style (`docs/EXTENDING.md`, `usage/USER-GUIDE.md`):
  plain Markdown, no frontmatter required outside `roles/`/`skills/`/`shared/` kit
  content.
- What needs no action: the fact-check's confirmations. 20/20 fixture walkthroughs with
  97 checks, the inert CLI (prints path + load order, no network, no telemetry, zero
  deps), the `[CONFIRM]` discipline, the one-role relay, RACI 21 rows / one A each, and
  PyPI live at 0.1.0 — all verified against the repo and the recorded run.

## File map

| File | Theme | Items |
|---|---|---|
| [01-launch-article.md](01-launch-article.md) | Fix the dev.to article before publication | A1–A3 must-fix errors · B4–B7 imprecisions |
| [02-first-run.md](02-first-run.md) | Install → first artifact in one sitting | C1–C8 |
| [03-trust-surface.md](03-trust-surface.md) | Make the honesty discipline feel like quality | D1–D6 |
| [04-storefront.md](04-storefront.md) | README, PyPI page, repo presentation | E1–E4 |
| [05-lifecycle.md](05-lifecycle.md) | Keep using without breakage | F1–F4 |
| [06-open-decisions.md](06-open-decisions.md) | The user's calls — not scheduled until decided | G1–G6 |
| [07-scope-and-release.md](07-scope-and-release.md) | Explicitly out of scope + release mechanics | H · I |
| [08-competitive-landscape.md](08-competitive-landscape.md) | Web-scan reference: skills ecosystem, repos, commercial | feeds G4, G5, G2, E3, D3, F2 |
| [09-external-skills-mattpocock.md](09-external-skills-mattpocock.md) | Leverage mattpocock/skills (MIT verified): three tracks + copyright mechanics | feeds G5 |

## Work order

Dependency-driven; items with no noted dependency can run in parallel. Sizing is the
user's call and never invented: mark S/M/L per item (or the org's own scale) before
scheduling — `[CONFIRM: your scale]`, no assumed velocity.

1. **F3 first** — the outside-the-kit glossary convention (`my-org.md`) is load-bearing:
   C4 points at it, C6's bundles mark its slot, C2's pre-flight names it.
2. **01 (article fixes)** — independent of everything else; the corrected draft is the
   input to the release gate's pre-publish re-fact-check.
3. **Core first-run path** — F3 → C4 → C6 (bundles) → C2 (five-minute run); C1
   (walkthrough) in parallel, anchored on the committed fixture.
4. **Entry points** — C3 (chooser) and C8 (tools matrix) in parallel; C3's scenario
   recipes cite F2's relay rows, so F2 lands first or in the same change.
5. **Trust surface** — D3/D4/D5 independent; D2 cross-links C7's redaction recipe; D6
   feeds E1/E2, so D6 before the storefront pass.
6. **Storefront** — E3's Mermaid diagram must match F2's relay rows; E1/E2/E4 after D6.
7. **Decisions gate their work** — G5 Track 1 gates `COMPANION-SKILLS`; G6 gates
   `shared/destinations/`; G3 gates D1's evidence upgrade; G1/G2/G4 as decided.
8. **Release gate last** ([07](07-scope-and-release.md), I.5) — runs before the tag,
   the PyPI upload, and the article publication.

## Working the plan

- Item IDs are stable — cite them in commits, PRs, and the CHANGELOG.
- Check an item off only when its Acceptance line is actually met; `built` means
  exercised, per the repo's evidence rule (`WHAT-THIS-IS.md` contract point 6).
- [07](07-scope-and-release.md)'s out-of-scope list applies to every file here.
- External facts cited in [08](08-competitive-landscape.md) carry their retrieval date
  and sources; they are scan-time observations, not commitments — treat them like the
  kit treats any input: `[CONFIRM]` before claiming.
