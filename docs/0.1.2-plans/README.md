# 0.1.2 plans — the review response, split by theme

Working plan for v0.1.2, derived from the **external review** of the launch post and
this repository at v0.1.1: the dev.to piece *"SDLC-Squad: 20 skills that write your
PRDs and sprint plans without making anything up"* plus a companion assessment, a
**20-idea** improvement list, and a deeper architectural breakdown. The review is
reproduced with its **full enumeration** in [08](08-review-input.md). Item IDs are
stable: **V1–V7** (verification) · **W1–W7** (workflow) · **I1–I5** (integrations) ·
**R1–R5** (rollout) · **X1–X3** (carry-over) · **D1–D5** (decisions).

**State:** planning docs first committed with this directory (hash in `git log`);
updated as work progresses (decisions, build status, sizing). The 0.1.2 CHANGELOG
entry lands with the release commit, not with this directory — the same rule the
0.1.1 plan followed.

**Scope of this directory:** it is the **0.1.2 fence**. By the repo's own rule
(`CONVENTIONS.md`; the same fence as
[`docs/0.1.1-plans/07`](../0.1.1-plans/07-scope-and-release.md)), a **patch** is
docs-only plus generated artifacts, and anything that changes **schemas, skills, or
CLI behaviour** is a **minor** (0.2.0). The review proposes both kinds. This plan
therefore:

- **schedules** the docs-only + generated-artifact half as **0.1.2**;
- records the enforcement/integration half as explicit **forward-pointers to 0.2.0**
  ([07](07-scope-and-release.md)) so nothing is lost;
- routes every genuine owner call to [06](06-open-decisions.md), where the owner may
  pull an item **into** 0.1.2 — exactly what the 0.1.1 plan did for its G1 CLI item.

**Written 2026-11-25 from:** the review supplied by the owner. This repo is offline
by charter (`WHAT-THIS-IS.md` contract point 4) — nothing here was fetched. The
review's own claims are reproduced as **review claims**, not repo facts; every claim
that would need a live check carries `[CONFIRM]`. Grounded against this repo at `main`
@ `9ff4f22` (the released v0.1.1).

## The goal for 0.1.2

Make the kit's honesty discipline **visible and checkable**, cut the **documented**
friction of relay and copy-paste, and give a team a **low-risk pilot path** — without
changing runtime behaviour. The review's strongest signal is that the kit's
differentiator (anti-hallucination) is a *prompt convention, not yet a check*, and
that its friction and its destination contracts are its adoption ceiling. A patch can
publish the checklists, profiles, cookbook, pilot kit, and the deferred launch
article. The enforcement half — a real linter, CLI flags, schema-level provenance,
live context — is a minor.

## Scope rules

- Additions are **docs-only, plus generated artifacts and repo presentation**: new
  Markdown under `docs/` and `usage/`, edits to `README.md` / `PKG-README.md` /
  `usage/USER-GUIDE.md` / `docs/REVIEWING-OUTPUT.md` / `docs/MODELS.md` /
  `docs/EXPORTS.md` / `shared/destinations/*`, new `.github/` templates, and — if a
  D-decision is taken — a CI workflow. No schema changes, no `SKILL.md` step changes,
  no new skills, no CLI behaviour changes (those are 0.2.0 unless a D-decision says
  otherwise).
- **Nothing in the review is adopted as-is.** Each item is classified
  (`0.1.2` / `0.2.0` / *refused*) with its reason; the classification is the plan's
  main output, because the kit's credibility rests on not shipping prompt-level claims
  as enforcement.
- Every new fact must trace to committed material: the review text ([08](08-review-input.md)),
  a fixture, a recorded run, or an existing doc. The fictional org for examples stays
  **Meridian Outfitters** (the example company across `usage/prompts-*.md` and the
  fixtures). No real org data anywhere — a review idea for "sanitized real-world
  examples" ([R3](04-adoption.md)) is satisfied with synthetic material only.
- Charter refusals are stated, not softened: **no network, no API client, no
  auto-import, no telemetry, no credentials** (`WHAT-THIS-IS.md`, `SECURITY.md`,
  `docs/TOOLS.md` §Never). Any review idea that needs one ([I2](03-integrations.md))
  is refused, not deferred.
- New docs follow the existing docs style (plain Markdown, no frontmatter outside
  `roles/`/`skills/`/`shared/` kit content).

## Legend

| Prefix | Theme | File |
|---|---|---|
| **V** | Verification & anti-hallucination | [01](01-verification.md) |
| **W** | Workflow & friction reduction | [02](02-workflow.md) |
| **I** | Integrations, tool contracts & live context | [03](03-integrations.md) |
| **R** | Team rollout & ecosystem trust | [04](04-adoption.md) |
| **X** | Carry-over: deferred 0.1.1 work + ROADMAP v0.1.x | [05](05-carry-over.md) |
| **D** | Open decisions — the owner's calls | [06](06-open-decisions.md) |
| **S** | Out-of-scope fence + release mechanics | [07](07-scope-and-release.md) |

## File map

| File | Theme | Items |
|---|---|---|
| [01-verification.md](01-verification.md) | Make grounding visible and checkable | V1–V7 |
| [02-workflow.md](02-workflow.md) | Cut the documented relay/copy-paste friction | W1–W7 |
| [03-integrations.md](03-integrations.md) | Tool contracts, instance profiles, live context | I1–I5 |
| [04-adoption.md](04-adoption.md) | Team rollout, drift checks, ecosystem trust | R1–R5 |
| [05-carry-over.md](05-carry-over.md) | The deferred launch article + ROADMAP v0.1.x | X1–X3 |
| [06-open-decisions.md](06-open-decisions.md) | The owner's calls — not scheduled until decided | D1–D5 |
| [07-scope-and-release.md](07-scope-and-release.md) | Out-of-scope forward-pointers + release mechanics | S |
| [08-review-input.md](08-review-input.md) | The review, reproduced and enumerated | reference |
| [09-gaps.md](09-gaps.md) | What the review left unnamed — the additions | V8·V9·W8·I6·I7·R6–R9·X4·D6·D7 |
| [10-implementation-plan.md](10-implementation-plan.md) | The sequenced build order, with a Done (Y/N) tracker | all 0.1.2 items |

## Build status (living)

Marked 2026-11-25 at planning time. **Done** = built and present on disk;
**Not started**; **Decided** = decision recorded, work not started; **Forward** =
classified as 0.2.0 forward-pointer; **Refused** = no work by charter.

| Item | Class | Status |
|---|---|---|
| V1 `[CONFIRM]` linter / gatekeeper | 0.2.0 | **Forward** |
| V2 claim-to-source tagging (practice) | 0.1.2 | **Done** (`docs/REVIEWING-OUTPUT.md`) |
| V3 arithmetic / capacity self-audit block | 0.2.0 | **Forward** (docs precursor in V2) |
| V4 confidence & ambiguity scoring | 0.2.0 | **Forward** |
| V5 model behavioral profiles + 60s benchmark | 0.1.2 | **Done** (`docs/MODELS.md`) |
| V6 model regression harness | 0.2.0 | **Forward** |
| V7 assumption-vs-fact separation (practice) | 0.1.2 | **Done** (`docs/REVIEWING-OUTPUT.md`) |
| V8 clean-artifact (false-positive) guidance | 0.1.2 | **Done** (`docs/REVIEWING-OUTPUT.md`) |
| V9 PII / hostname pre-paste check | 0.1.2 | **Done** (`docs/REVIEWING-OUTPUT.md`) |
| W1 `--copy` / `--out` | 0.2.0 | **Forward** (D1) |
| W2 `--context` assembly | 0.2.0 | **Forward** (D1) |
| W3 `sdlc-squad doctor` | 0.2.0 | **Forward** (D1) |
| W4 interactive intake / structured inputs | 0.2.0 | **Forward** |
| W5 diff-aware update mode | 0.2.0 | **Forward** |
| W6 end-to-end "Feature Relay" pack | 0.1.2 | **Done** (`usage/FEATURE-RELAY.md`) |
| W7 handoff block / checklist (practice) | 0.1.2 | **Done** (`usage/RELAY.md`) |
| W8 long-load / context-budget recipe | 0.1.2 | **Done** (`docs/TROUBLESHOOTING.md`) |
| I1 instance profile overlays (`my-jira.md` …) | 0.1.2 | **Done** (`docs/DESTINATION-PROFILES.md`) |
| I2 read-only context pullers | Refused | **Refused** + boundary line (`docs/EXPORTS.md`) |
| I3 Jira CSV dry-run exporter | 0.2.0 | **Forward** |
| I4 Confluence compatibility mode (docs) | 0.1.2 | **Done** (`shared/destinations/confluence.md`) |
| I5 GitHub PR/issue template pack | 0.1.2 | **Done** (`docs/GITHUB-TEMPLATES.md`) |
| I6 destination validation ledger | 0.1.2 | **Done** (`shared/destinations/README.md`) |
| I7 `make check-links` / `check-frontmatter` | 0.1.2 | **Done** (`scripts/check-links.py`, `check-frontmatter.py`, `tests/docs/`, `Makefile`) |
| R1 CI doc-to-code + bundle drift checks | 0.1.2 | **Done** (`.github/workflows/checks.yml`) |
| R2 pilot kit / 2-week rollout playbook | 0.1.2 | **Done** (`docs/PILOT.md`) |
| R3 examples across company sizes (synthetic) | 0.1.2 | **Done** (`docs/EXAMPLES.md`) |
| R4 skill maturity / verification badges | 0.2.0 | **Forward** (D3) |
| R5 anti-pattern & hallucination cookbook | 0.1.2 | **Done** (`docs/ANTI-PATTERNS.md`) |
| R6 `docs/LIMITATIONS.md` | 0.1.2 | **Done** (`docs/LIMITATIONS.md`) |
| R7 docs index / navigation | 0.1.2 | **Done** (`docs/README.md` + `tests/docs/test_docs_index.py`) |
| R8 cookbook provenance mechanism | 0.1.2 | **Done** (`docs/ANTI-PATTERNS.md`) |
| R9 `UPGRADING.md` 0.1.2 migration note | 0.1.2 | **Done** (`docs/UPGRADING.md`) |
| X1 launch article (A/B fixes) + publish | 0.1.2 | **Parked** (owner, 2026-11-25) |
| X2 ROADMAP v0.1.x end-to-end validation run | 0.1.2 / 0.2.0 | **Done** (`field-test/` + `tests/results/run-2026-11-25-x2-real-paste.md`) |
| X3 feedback / adoption analysis | v0.1.x | **Not started** |
| X4 refresh the competitive-landscape scan (optional) | 0.1.2 | **Not started** *(optional — skipped)* |
| D2·D4·D5·D6·D7 decided; D1·D3 open | — | **Decided** |
| S release mechanics | — | **Done** — v0.1.2 live on PyPI + tag `v0.1.2`; recorded run `tests/results/run-2026-11-25-v0.1.2.md` |

## Work order

Dependency-driven; items with no noted dependency run in parallel. A **proposed**
S/M/L per item is in the sizing table below — a proposal only, never a commitment.
The review's own "suggested order of attack" (trust & correctness → speed →
adoption) is honored at the *docs* level; the review's Week-1/Week-2 CLI items are
0.2.0 here ([07](07-scope-and-release.md)).

1. **Trust & correctness docs first** — V2 (claim-to-source practice) and V7
   (assumption-vs-fact practice) extend the shipped `docs/REVIEWING-OUTPUT.md`; R5
   (anti-pattern cookbook) is the same axis made concrete. These are the patch's
   differentiator and need no other item.
2. **Externalize the instance** — I1 (`my-jira.md` / `my-confluence.md` /
   `my-github.md` overlays) before I4 (Confluence compatibility mode) and I5 (GitHub
   templates), which reference the profile.
3. **Friction docs** — W6 (Feature Relay pack) and W7 (handoff block) build on the
   shipped `usage/WALKTHROUGH.md` and `usage/RELAY.md`; W7's block feeds W6's hops.
4. **Adoption** — R2 (pilot kit) and R3 (examples) after V2/V7/I1 exist to point at;
   R1 (CI) once R3 and I1 add files the drift checks must cover.
5. **Model trust** — V5 (MODELS.md benchmark + evidence-gated failure table) after the
   V-items' vocabulary is fixed.
6. **Carry-over** — X1 (launch article) after the docs land, so the article can cite
   them; X2 (validation run) last, because it feeds 0.2.0 schema work.
7. **Maintainer gaps** ([09](09-gaps.md)) — R6 (`LIMITATIONS.md`), R7 (docs index), and
   R9 (upgrade note) ship with the docs they describe; V8/V9 extend the same review
   guide as V2/V7; W8 joins the workflow docs; I6/I7 and R1 (if D2) land with the
   destination and release work.
8. **Release gate last** ([07](07-scope-and-release.md), S.3) — before the tag and the
   PyPI upload.

## Proposed sizing (owner to adjust — not a commitment)

Scale: **S** ≤ half a day · **M** = 1–2 days · **L** > 2 days (or your own scale).
`[CONFIRM]` until you set it.

| Item | Proposed | Note |
|---|---|---|
| V2 claim-to-source practice | S | extends `REVIEWING-OUTPUT.md` |
| V5 model profiles + benchmark | M | MODELS.md + an evidence-gated table |
| V7 assumption-vs-fact practice | S | one section |
| W6 feature relay pack | M | one cross-role worked example |
| W7 handoff block | M | RELAY.md + a block shape |
| I1 instance profiles | M | three overlay templates + a page |
| I4 Confluence compat mode | S | expand `shared/destinations/confluence.md` |
| I5 GitHub template pack | S | 2–3 `.github/` files |
| R1 CI drift checks | M | one workflow + a link/path check |
| R2 pilot kit | M | one playbook |
| R3 examples across sizes | M | 3 synthetic scenarios |
| R5 anti-pattern cookbook | M | catalog mapped to rules |
| X1 launch article | M | parked — A/B fixes + publish when unparked |
| X2 validation run | L | **Done** — four features, recorded |
| V8 clean-artifact guidance | S | one section |
| V9 PII pre-paste check | S | one section |
| W8 long-load recipe | S | extends TROUBLESHOOTING |
| I6 destination validation ledger | S | one table |
| I7 make check-links / check-frontmatter | M | two Makefile targets |
| R6 LIMITATIONS.md | S | one page |
| R7 docs index | S | one page |
| R8 cookbook provenance | S | a header section |
| R9 upgrade migration note | S | one section |
| X4 landscape refresh (optional) | M | owner-run web pass |

## Working the plan

- Item IDs are stable — cite them in commits, PRs, and the CHANGELOG.
- Check an item off only when its Acceptance line is actually met; `built` means
  exercised, per the repo's evidence rule (`WHAT-THIS-IS.md` contract point 6).
- [07](07-scope-and-release.md)'s out-of-scope list applies to every file here.
- The review in [08](08-review-input.md) is scan-time input, not a commitment — treat
  it like the kit treats any input: `[CONFIRM]` before claiming.
