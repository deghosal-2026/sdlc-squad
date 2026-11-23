# 0.1.1 plans — the patch, split by theme

Working plan for the v0.1.1 patch, broken into themed files so each area can be read,
worked, and checked off independently. Supersedes the single `docs/0.1.1-items.md` —
that file's content lives here, unchanged in substance. Item IDs are stable and
**non-contiguous**: A1–A3 · B4–B7 · C1–C8 · D1–D6 · E1–E4 · F1–F4 · G1–G7.

**State:** planning docs first committed at `5d5b8de`; updated as work progresses
(decisions, build status, sizing). The 0.1.1 CHANGELOG entry lands with the release
commit (see [07](07-scope-and-release.md), I.11), not with this directory.

**Scope of this directory:** it is the **0.1.1 fence**. Everything scheduled here is
patch-able — docs-only, plus generated bundles. Any item that would change schemas,
skills, or CLI behaviour is a **forward-pointer** to 0.2.0 (listed in
[07](07-scope-and-release.md), H so it is not lost), never scheduled in this patch.

Written 2026-11-23 from: the fact-check of the launch materials (kit breakdown, dev.to
article draft, external customer-view gap review) verified against this repo at `main`
@ `394430f` — the released v0.1.0 (the baseline; the plan itself now sits on top of it
in `5d5b8de`); the usability research pass; and the competitive web scan
([08](08-competitive-landscape.md), run with the user's go on 2026-11-23).

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
- **Amended 2026-11-23** by the resolved G-decisions ([06](06-open-decisions.md)):
  `SKILL.md` **`description:`** edits are now in scope (G2 — the 20 fields only, no steps
  or fixtures); a **CLI change** is now in scope (G1 — the `sdlc-squad prompt` assembler
  plus a real test); new files join (`shared/destinations/` — G6;
  `docs/COMPANION-SKILLS.md` — G5); skills.sh publication is **declined** (G4); the
  launch article is **deferred to after ship** (G7). Everything else above stands.
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
| [06-open-decisions.md](06-open-decisions.md) | The user's calls — not scheduled until decided | G1–G7 |
| [07-scope-and-release.md](07-scope-and-release.md) | Explicitly out of scope + release mechanics | H · I |
| [08-competitive-landscape.md](08-competitive-landscape.md) | Web-scan reference: skills ecosystem, repos, commercial | feeds G4, G5, G2, E3, D3, F2 |
| [09-external-skills-mattpocock.md](09-external-skills-mattpocock.md) | Leverage mattpocock/skills (MIT verified): three tracks + copyright mechanics | feeds G5 |

## Build status (living)

Marked 2026-11-23 by the owner's instruction; update as items land. **Done** = built and
present on disk (uncommitted until told); **Not started**; **Decided** = decision recorded,
work not started; **Deferred** = intentionally after ship; **Declined** = no work by
decision.

| Item | Status |
|---|---|
| A1–A3 · B4–B7 — launch-article fixes | **Deferred** (article after ship, G7) |
| C1 walkthrough | Not started |
| C2 five-minute run | **Done** (`usage/USER-GUIDE.md`) |
| C3 chooser + recipes | Not started |
| C4 glossary example | **Done** (`shared/glossary-and-org.EXAMPLE.md`) |
| C5 two-ways-to-run | Not started |
| C6 bundles | **Done** (`usage/bundles/` ×20 · `scripts/build-bundles.sh` · `make bundles` / `make check-bundles`; prompt-book headers link it) |
| C7 exports + redaction | Not started |
| C8 tools matrix | Not started |
| D1–D6 trust surface | Not started |
| E1–E4 storefront | Not started |
| F1 feedback template | Not started |
| F2 relay recipe | Not started |
| F3 upgrade safety | **Done** (`docs/UPGRADING.md`; alignments in `docs/EXTENDING.md`, `usage/USER-GUIDE.md`, `PKG-README.md`) |
| F4 team-usage | **Done** (section in `docs/UPGRADING.md`) |
| G1 CLI prompt assembler | Decided — Not started |
| G2 description polish (20) | Decided — Not started |
| G3 real GitHub/Confluence/Jira pastes | Decided — Not started |
| G4 skills.sh publication | **Declined** |
| G5 T1 companion skills | Decided — Not started (`docs/COMPANION-SKILLS.md`); T2/T3 = 0.2.x |
| G6 destination contracts | **Done** (`shared/destinations/` — `README`, `github`, `jira`, `confluence`) |
| G7 launch article | **Deferred** (after ship) |
| I — release mechanics | Not started (runs at ship) |

## Work order

Dependency-driven; items with no noted dependency run in parallel. A **proposed** S/M/L
per item is in the sizing table below — a proposal only, never a commitment.

**Revised 2026-11-23** (per the resolved decisions, [06](06-open-decisions.md)): the
launch article moves to **after ship** (G7); skills.sh is out (G4); G6, G5 T1, G2, and
G1 add work to this patch.

1. **F3 first** — the outside-the-kit glossary convention (`my-org.md`) is load-bearing:
   C4 points at it, C6's bundles mark its slot, C2's pre-flight names it.
2. **Core first-run path** — F3 → C4 → C6 (bundles) → C2 (five-minute run); C1
   (walkthrough) in parallel, anchored on the committed fixture.
3. **Entry points** — C3 (chooser + recipes) and C8 (tools matrix) in parallel; F2 lands
   before or with C3 (the recipes cite its rows).
4. **Trust surface** — D3/D4/D5 independent (D5 now names `GLM-5.3`); D2 cross-links
   C7's redaction recipe; D6 before the storefront pass.
5. **Storefront** — E3's Mermaid diagram must match F2's relay rows; E1/E2/E4 after D6.
6. **Decision work** — G6 (fetch specs → `shared/destinations/`), G5 T1
   (`docs/COMPANION-SKILLS.md`), G2 (the 20 descriptions), G1 (CLI + test). G5 T2/T3
   are 0.2.x, not here.
7. **G3 real-paste check** — real GitHub + Confluence + Jira (+ CSV) pastes, recorded
   under `tests/results/`; feeds D1's wording and validates the G6 contracts.
8. **Release gate last** ([07](07-scope-and-release.md), I.5) — before the tag and the
   PyPI upload.
9. **Launch article (01)** — after ship (G7): apply the A/B fixes, publish, close the
   ROADMAP checkbox.

## Proposed sizing (owner to adjust — not a commitment)

Scale: **S** ≤ half a day · **M** = 1–2 days · **L** > 2 days (or your own scale).
`[CONFIRM]` until you set it.

| Item | Proposed | Note |
|---|---|---|
| C1 walkthrough | M | one full worked run |
| C2 five-minute run | S | guide section |
| C3 chooser + recipes | M | one page + three chains |
| C4 glossary example | S | one file |
| C5 two-ways-to-run | S | doc box |
| C6 bundles + script | M | generator + 20 files + gate |
| C7 exports + redaction | M | three recipes + redaction |
| C8 tools matrix | S | one page |
| D1 paste-destination wording | S | one line |
| D2 data-path (2 files) | S | USER-GUIDE + SECURITY link |
| D3 reviewing output | M | one doc |
| D4 troubleshooting | M | one doc |
| D5 model notes | S | one doc |
| D6 evidence page | S | retell of 13 defects |
| E1 PKG-README | S | links + note |
| E2 README why-not | S | ~6 lines |
| E3 presentation | S | settings + Mermaid |
| E4 examples index | S | 20 rows |
| F1 feedback template | S | one template |
| F2 relay recipe | M | derived from role files |
| F3 upgrade safety | M | convention + ownership table |
| F4 team-usage | S | pattern section |
| G1 CLI prompt + test | M | new behavior + test |
| G2 descriptions (20) | S | one field each |
| G3 real pastes | M | depends on access |
| G5 T1 companion skills | M | one doc |
| G6 destinations (3 files) | M | from fetched specs |
| G5 T2/T3 | L | 0.2.x — not this patch |
| G7 article (post-ship) | M | fixes + publish |

## Working the plan

- Item IDs are stable — cite them in commits, PRs, and the CHANGELOG.
- Check an item off only when its Acceptance line is actually met; `built` means
  exercised, per the repo's evidence rule (`WHAT-THIS-IS.md` contract point 6).
- [07](07-scope-and-release.md)'s out-of-scope list applies to every file here.
- External facts cited in [08](08-competitive-landscape.md) carry their retrieval date
  and sources; they are scan-time observations, not commitments — treat them like the
  kit treats any input: `[CONFIRM]` before claiming.
