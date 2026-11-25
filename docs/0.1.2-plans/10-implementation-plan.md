# 10 — Implementation plan: working all of 0.1.2

> **Status (2026-11-25):** planning artifact — nothing built, nothing run. Every **Done**
> cell reads `N`. Tests and the release steps are **planned here**; they are authored and
> run at their own step, and the security scan + release-readiness work happens only when
> 0.1.2 is implemented and release-ready (Phase 7). Master table: [`README`](README.md).

The themed files ([01](01-verification.md)–[09](09-gaps.md)) say **what** and **why**.
This file says **in what order, touching which files, done when** — the executable form
of the 0.1.2 plan. It covers the **0.1.2-class items only**: docs-only work, generated
artifacts, repo presentation, and tooling. The enforcement half is 0.2.0
([07](07-scope-and-release.md), S1); X1 (the launch article) is drafted last.

## The sequence (done tracker)

Rows run top-to-bottom; work them in order. **Done** flips to `Y` only when the item's
Acceptance line in its plan file is actually met — `built` means exercised, per the
evidence rule (`WHAT-THIS-IS.md` contract point 6). The **Test / verify** column names
what proves the step; **new** marks a test this plan adds.

| Seq | Phase | Item | Plan | Target file(s) | Test / verify | Done |
|---|---|---|---|---|---|---|
| 0a | 0 Decide | D2 — adopt CI | [06](06-open-decisions.md) | — | — | N |
| 0b | 0 Decide | D4 — validation run placement | [06](06-open-decisions.md) | — | — | N |
| 0c | 0 Decide | D5 — context pullers refused | [06](06-open-decisions.md) | — | — | N |
| 0d | 0 Decide | D7 — overlay file type | [06](06-open-decisions.md) | — | — | N |
| 1 | 1 Trust | V2 — claim-to-source tagging | [01](01-verification.md) | `docs/REVIEWING-OUTPUT.md` | link check | N |
| 2 | 1 Trust | V7 — assumption-vs-fact split | [01](01-verification.md) | `docs/REVIEWING-OUTPUT.md` | link check | N |
| 3 | 1 Trust | V8 — clean-artifact (false-positive) rule | [01](01-verification.md) | `docs/REVIEWING-OUTPUT.md` | link check | N |
| 4 | 1 Trust | V9 — PII / hostname pre-paste check | [01](01-verification.md) | `docs/REVIEWING-OUTPUT.md` | link check | N |
| 5 | 1 Trust | R5 — anti-pattern cookbook | [04](04-adoption.md) | `docs/ANTI-PATTERNS.md` *(new)* | link check | N |
| 6 | 1 Trust | R8 — cookbook provenance header | [04](04-adoption.md) | `docs/ANTI-PATTERNS.md` | link check | N |
| 7 | 1 Trust | Phase verify | — | — | `make check-links` | N |
| 8 | 2 Instance | I1 — profile overlays | [03](03-integrations.md) | `docs/DESTINATION-PROFILES.md` *(new)* | link check | N |
| 9 | 2 Instance | I4 — Confluence compatibility mode | [03](03-integrations.md) | `shared/destinations/confluence.md` | link check | N |
| 10 | 2 Instance | I6 — destination validation ledger | [03](03-integrations.md) | `shared/destinations/README.md` | link check | N |
| 11 | 2 Instance | I5 — GitHub SDE template pack | [03](03-integrations.md) | `.github/` templates | — | N |
| 12 | 2 Instance | I7a — add `check-links` + `check-frontmatter` scripts | [03](03-integrations.md) | `scripts/check-links.py`, `scripts/check-frontmatter.py` *(new)* | — | N |
| 13 | 2 Instance | I7b — add doc-check tests | [03](03-integrations.md) | `tests/docs/test_doc_checks.py` *(new)* | **new test** (seed-break) | N |
| 14 | 2 Instance | I7c — wire Makefile targets + extend `make test` | [03](03-integrations.md) | `Makefile` | `make test` | N |
| 15 | 2 Instance | Phase verify | — | — | `make test` · `check-links` · `check-frontmatter` | N |
| 16 | 3 Friction | W7 — handoff block | [02](02-workflow.md) | `usage/RELAY.md` | link check | N |
| 17 | 3 Friction | W6 — Feature Relay pack | [02](02-workflow.md) | `usage/FEATURE-RELAY.md` *(new)* | link check | N |
| 18 | 3 Friction | W8 — long-load recipe | [02](02-workflow.md) | `docs/TROUBLESHOOTING.md` | link check | N |
| 19 | 3 Friction | Phase verify | — | — | `make check-links` | N |
| 20 | 4 Model | V5 — benchmark + evidence-gated table | [01](01-verification.md) | `docs/MODELS.md` | link check | N |
| 21 | 5 Adoption | R6 — `LIMITATIONS.md` | [04](04-adoption.md) | `docs/LIMITATIONS.md` *(new)* | link check | N |
| 22 | 5 Adoption | R7 — docs index | [04](04-adoption.md) | `docs/README.md` *(new)* | — | N |
| 23 | 5 Adoption | R7b — add docs-index completeness test | [04](04-adoption.md) | `tests/docs/test_docs_index.py` *(new)* | **new test** | N |
| 24 | 5 Adoption | R2 — pilot kit | [04](04-adoption.md) | `docs/PILOT.md` *(new)* | link check | N |
| 25 | 5 Adoption | R3 — examples across company sizes | [04](04-adoption.md) | `docs/EXAMPLES.md` | link check | N |
| 26 | 5 Adoption | R9 — upgrade migration note | [04](04-adoption.md) | `docs/UPGRADING.md` | link check | N |
| 27 | 5 Adoption | R1 — CI drift checks | [04](04-adoption.md) | `.github/workflows/checks.yml` *(new)* | CI runs the gates | N |
| 28 | 5 Adoption | I2 — puller boundary line | [03](03-integrations.md) | `docs/EXPORTS.md` | link check | N |
| 29 | 5 Adoption | Phase verify | — | — | `make test` · `make check-bundles` | N |
| 30 | 6 Carry-over | X2 — end-to-end validation run | [05](05-carry-over.md) | `tests/results/run-<date>-v0.1.x-validation.md` *(new)* | recorded run | N |
| 31 | 6 Carry-over | X4 — landscape refresh *(optional)* | [05](05-carry-over.md) | `docs/LANDSCAPE.md` *(new)* | link check | N |
| 32 | 7 Release | Security scans | [07](07-scope-and-release.md) | — | `make security` (trufflehog + gitleaks) | N |
| 33 | 7 Release | Update all relevant docs for release readiness | [07](07-scope-and-release.md) | `README.md`, `PKG-README.md`, `ROADMAP.md`, `CHANGELOG.md`, badges | `make check-links` | N |
| 34 | 7 Release | Release gate (repo rule) — all checks green | [07](07-scope-and-release.md) | — | `make test` · `check-bundles` · `check-links` · `check-frontmatter` · `twine check` | N |
| 35 | 7 Release | Post to PyPI | [07](07-scope-and-release.md) | `dist/` | verify from the index | N |
| 36 | 7 Release | Update the docs to the new release | [07](07-scope-and-release.md) | `README.md`, `PKG-README.md`, version refs | `make check-links` | N |
| 37 | 7 Release | GitHub version tag | [07](07-scope-and-release.md) | tag `v0.1.2` + release notes | tag + notes present | N |
| 38 | 7 Release | Article drafting (X1) | [05](05-carry-over.md) | `docs/launch-article.md` *(per G7)* | pre-publish re-fact-check | N |

## Scope

**In scope (0.1.2):** V2 · V5 · V7 · V8 · V9 · W6 · W7 · W8 · I1 · I4 · I5 · I6 · I7 ·
R1 · R2 · R3 · R5 · R6 · R7 · R8 · R9 · X2 · X4 · the I2 boundary line · the release
mechanics (S3).

**Out (0.2.0):** V1 · V3 · V4 · V6 · W1–W5 · I3 · R4. **Refused:** I2 (a puller script).
**Last:** X1 (launch article) — drafted after the release ships. **v0.1.x:** X3.

## Ground rules

- **The patch fence holds** (`CONVENTIONS.md`): no schema change, no `SKILL.md` step
  change, no CLI behaviour change. A new script is allowed only as **packaging/tooling**
  (I7, R1), never as kit runtime.
- **One canonical copy.** Bundles are generated (`make bundles`), never hand-edited;
  the overlays (I1) live **outside** the kit (the F3 rule, `docs/UPGRADING.md`).
- **Evidence only.** Every new fact traces to a fixture, a recorded run, or an existing
  doc. Examples stay synthetic (**Meridian Outfitters**); no real org data.
- **CHANGELOG in the same commit as the change** (repo rule); one commit per phase.
- **Honesty.** `[CONFIRM]` over invention; no scores, benchmarks, or unobserved claims
  (V5's failure table is evidence-gated).
- **Tests are added and run at their step** (Phase 2 for the doc-check tooling, Phase 5
  for the docs-index test, Phase 7 for the security scan) — never ahead of the work they
  verify.

## Phase 0 — Decisions (unblock the gated items)

| # | Decision | Default assumed | Gates |
|---|---|---|---|
| D2 | Adopt CI | **Yes** — pinned first-party actions, no secrets | R1 |
| D4 | Validation run in 0.1.2 | **Yes** — record the run; forward schema fixes to 0.2.0 | X2 |
| D5 | Context pullers | **Refused** + one boundary line in `EXPORTS.md` | I2 |
| D7 | Overlay file type | **Markdown overlays outside the kit** | I1 |

(D1, D3, D6 concern the 0.2.0 enforcement half and CI detail; they do not block 0.1.2.)

## Phase detail

### Phase 1 — Trust & correctness (no dependencies)
**Commit:** `docs: 0.1.2 trust & correctness — claim tags, assumption split, clean rule, PII check, cookbook`

- **Seq 1–4 (V2·V7·V8·V9) — one pass on `docs/REVIEWING-OUTPUT.md`.** V2 adds the tag
  vocabulary (`[src: notes]`, `[src: prd-draft]`, `[src: org-glossary]`,
  `[CONFIRM: missing from input]`) + review-by-exception; V7 adds the assumption-vs-fact
  section + high-impact inline markers; V8 adds when a clean artifact is **correct**;
  V9 adds the PII/hostname pre-paste check linking `docs/EXPORTS.md` §Redaction.
- **Seq 5–6 (R5·R8) — new `docs/ANTI-PATTERNS.md`.** Failure mode → the rule that catches
  it (cited) → a real example from `docs/EVIDENCE.md`, a fixture, or field feedback;
  header states the three sources; seed from the 13 recorded defects.
- **Seq 7 — verify:** `make check-links`.

### Phase 2 — Instance & integrations (needs D7)
**Commit:** `docs: 0.1.2 destination profiles, Confluence mode, validation ledger, GitHub templates, doc-check tooling`

- **Seq 8 (I1)** — `docs/DESTINATION-PROFILES.md`: three copy-out templates
  (`my-jira.md`, `my-confluence.md`, `my-github.md`); states the outside-the-kit rule; no
  secrets.
- **Seq 9 (I4)** — expand `shared/destinations/confluence.md` (callouts, status badges,
  code blocks); keep the storage-format path `[CONFIRM]`.
- **Seq 10 (I6)** — add the observed/unobserved ledger to `shared/destinations/README.md`.
- **Seq 11 (I5)** — audit `.github/` templates; add an SDE-aligned one (rollback, deploy/
  release split, blast radius); no duplication.
- **Seq 12 (I7a) — add the tooling:** `scripts/check-links.py` (resolve every relative
  Markdown link) and `scripts/check-frontmatter.py` (validate `roles/` + `skills/`
  frontmatter against `CONVENTIONS.md`).
- **Seq 13 (I7b) — add the tests:** `tests/docs/test_doc_checks.py` — each script must
  **pass on the real tree** and **fail on a seeded break** (a broken link; a bad `status`
  / a name-folder mismatch).
- **Seq 14 (I7c) — wire it:** Makefile targets `check-links`, `check-frontmatter`; extend
  `make test` to run the doc tests alongside the CLI test.
- **Seq 15 — verify:** `make test` · `make check-links` · `make check-frontmatter` green.

### Phase 3 — Friction (no dependencies)
**Commit:** `docs: 0.1.2 relay handoff block, feature-relay pack, long-load recipe`

- **Seq 16 (W7)** — Handoff Block in `usage/RELAY.md` (upstream sources; blocking
  `[CONFIRM]`s; next role & skill), each field traceable to a role-file contract.
- **Seq 17 (W6)** — `usage/FEATURE-RELAY.md`: one Meridian feature across
  PMT → TPM → SDM → SDE, each hop an F2 row + a fixture; one carried `[CONFIRM]` resolved,
  one open.
- **Seq 18 (W8)** — long-load recipe in `docs/TROUBLESHOOTING.md` (+ a `docs/MODELS.md`
  cross-link).
- **Seq 19 — verify:** `make check-links`.

### Phase 4 — Model trust (no dependencies)
**Commit:** `docs: 0.1.2 model benchmark prompt + evidence-gated failure table`

- **Seq 20 (V5)** — `docs/MODELS.md`: 60-second benchmark prompt + a failure-mode table
  that ships empty / `[CONFIRM: run per model]` until a run is recorded. No scores.

### Phase 5 — Adoption
**Commit:** `docs: 0.1.2 limitations, docs index, pilot kit, examples, upgrade note` (CI in its own commit)

- **Seq 21 (R6)** — `docs/LIMITATIONS.md`: the honest limits, each with its mitigation.
- **Seq 22 (R7)** — `docs/README.md`: index every `docs/` page (after seq 1–21).
- **Seq 23 (R7b)** — `tests/docs/test_docs_index.py`: every `docs/*.md` is listed in
  `docs/README.md` (no orphan pages, no dead rows).
- **Seq 24 (R2)** — `docs/PILOT.md`: 2-week, 1-squad pilot; two skills; F1 metrics; go/no-go.
- **Seq 25 (R3)** — `docs/EXAMPLES.md`: three synthetic scenarios.
- **Seq 26 (R9)** — `docs/UPGRADING.md`: 0.1.2 migration note; ownership table gains the
  I1 overlays.
- **Seq 27 (R1)** — `.github/workflows/checks.yml`: runs `make check-bundles`,
  `check-links`, `check-frontmatter`, and `test` on PRs; pinned first-party actions only.
  **Separate commit.**
- **Seq 28 (I2)** — `docs/EXPORTS.md`: the puller boundary line.
- **Seq 29 — verify:** `make test` · `make check-bundles`.

### Phase 6 — Carry-over
**Commit:** `docs: 0.1.2 recorded validation run (+ optional landscape refresh)`

- **Seq 30 (X2)** — `tests/results/run-<date>-v0.1.x-validation.md`: one real feature
  through the core loop, pasted into real targets; schema misses → 0.2.0 forward-pointers.
- **Seq 31 (X4, optional)** — `docs/LANDSCAPE.md`: owner-run, offline, with retrieval
  dates and sources.

## Phase 7 — Release (runs only when 0.1.2 is implemented and release-ready)

These steps happen at release time — **not** during Phases 0–6. Order as given:

1. **Seq 32 — Security scans.** `make security` — **trufflehog** (filesystem) + **gitleaks**
   (git history). Both must come back clean; record the pass.
2. **Seq 33 — Update all relevant docs for release readiness.** Version references,
   `README.md`, `PKG-README.md`, `ROADMAP.md`, `CHANGELOG.md`, badges, and the cross-link
   pass; `make check-links` green.
3. **Seq 34 — Release gate (repo rule, before posting).** `make test` · `make check-bundles`
   · `make check-links` · `make check-frontmatter` · `twine check` all green; README tree
   vs disk; synthetic-data check.
4. **Seq 35 — Post to PyPI.** `make sync` → `python -m build` → `twine check` → (on go)
   `twine upload`; verify the CLI + kit tree from the public index.
5. **Seq 36 — Update the docs to the new release.** Post-ship: PyPI page render check,
   version/badge references confirmed on the live pages.
6. **Seq 37 — GitHub version tag.** Tag `v0.1.2` + release notes.
7. **Seq 38 — Article drafting (X1).** Draft `docs/launch-article.md` (per G7), apply the
   A/B fixes, re-fact-check before publish.

## Testing (added where needed — authored and run at their step)

| Test | Added by | Covers | Runs via |
|---|---|---|---|
| `tests/cli/test_prompt.py` | exists (G1) | CLI assembles the four files in order | `make test` |
| `scripts/check-links.py` | I7a | every relative Markdown link resolves | `make check-links` |
| `scripts/check-frontmatter.py` | I7a | `roles/` + `skills/` frontmatter contract | `make check-frontmatter` |
| `tests/docs/test_doc_checks.py` | I7b *(new)* | both scripts pass on the real tree, fail on a seeded break | `make test` |
| `tests/docs/test_docs_index.py` | R7b *(new)* | every `docs/*.md` is listed in `docs/README.md` | `make test` |
| `scripts/build-bundles.sh` + `make check-bundles` | exists (C6) | bundles fresh vs the canonical files | `make check-bundles` |
| fixtures + recorded runs | exists (evidence rule) | each skill exercised | `tests/results/` |
| `make security` | Phase 7, Seq 32 | secrets in the tree + git history | trufflehog + gitleaks |

## File inventory

**New:** `docs/ANTI-PATTERNS.md` · `docs/DESTINATION-PROFILES.md` ·
`usage/FEATURE-RELAY.md` · `docs/LIMITATIONS.md` · `docs/README.md` · `docs/PILOT.md` ·
`docs/LANDSCAPE.md` *(optional)* · `.github/workflows/checks.yml` ·
`scripts/check-links.py` · `scripts/check-frontmatter.py` ·
`tests/docs/test_doc_checks.py` · `tests/docs/test_docs_index.py` ·
`tests/results/run-<date>-v0.1.x-validation.md` · `docs/launch-article.md` *(X1)*.

**Edited:** `docs/REVIEWING-OUTPUT.md` · `docs/MODELS.md` · `docs/TROUBLESHOOTING.md` ·
`docs/EXPORTS.md` · `docs/EXAMPLES.md` · `docs/UPGRADING.md` ·
`shared/destinations/confluence.md` · `shared/destinations/README.md` · `usage/RELAY.md` ·
`.github/` templates · `Makefile` · `README.md` · `PKG-README.md` ·
`usage/USER-GUIDE.md` · `ROADMAP.md` · `CHANGELOG.md` · `pyproject.toml` ·
`sdlc_squad/__init__.py`.

## Risks & rollbacks

| Risk | Mitigation |
|---|---|
| A 0.2.0 item leaks into the patch | The fence ([07](07-scope-and-release.md), S1); review each commit against it |
| Link rot as docs multiply | `make check-links` (I7) in the gate and CI |
| Overlays land inside the kit | State the F3 rule in I1; `docs/UPGRADING.md` ownership table (R9) |
| CI widens the supply chain | Pinned first-party actions, no secrets (D6) |
| A model claim without evidence | V5's table ships empty/`[CONFIRM]`; no scores |
| A bad upload | Yank on PyPI; revert by commit — last resort |

## Definition of done for 0.1.2

- [ ] Every 0.1.2 item's Acceptance line is met (sequence **Done** = `Y`).
- [ ] The 0.2.0 items remain forward-pointers — none shipped early.
- [ ] New tests authored and green: `make test` (CLI + doc-check + docs-index).
- [ ] Gates green: `check-bundles`, `check-links`, `check-frontmatter`, `test`.
- [ ] Security scans clean (trufflehog + gitleaks).
- [ ] Posted to PyPI; docs updated to the new release; GitHub tag `v0.1.2` cut.
- [ ] Launch article drafted (X1) — after the release.
- [ ] No charter regression (S2): `[CONFIRM]` discipline, one-role isolation, evidence
      rule, zero-runtime.

## Related

- [`README.md`](README.md) — the item list, build status, and work order
- [`07-scope-and-release.md`](07-scope-and-release.md) — the fence and release gate
- [`09-gaps.md`](09-gaps.md) — the items this plan adds
