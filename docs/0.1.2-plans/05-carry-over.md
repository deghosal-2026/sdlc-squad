# 05 — Carry-over: the deferred launch article + ROADMAP v0.1.x

> **Status (2026-11-25):** X1, X4 in scope for 0.1.2; X2 splits across 0.1.2/0.2.0
> (D4); X3 stays in v0.1.x. Master table: [`README`](README.md).

Theme: work that predates the review and is still open — the launch article the 0.1.1
plan deferred to "after ship," the ROADMAP's v0.1.x validation milestone, and a
landscape refresh. None of it is in the review, but all of it is in the repo's own
open list.

## X1. Launch article (A/B fixes) + publish — **0.1.2**

- **Carried from 0.1.1:** the must-fix errors **A1–A3** (PMT expansion; the load order
  is four files not three; the false "no vendor-specific tool schemas") and the
  imprecisions **B4–B7** ("no installer"; single-role rule attribution; "zero
  configuration"; RACI "just edit"). Deferred to after ship under **G7**; 0.1.1 has
  shipped, so it is now doable.
- **Anchor:** the exact fixes live in
  [`../0.1.1-plans/01-launch-article.md`](../0.1.1-plans/01-launch-article.md); G7
  recommends the corrected draft live at `docs/launch-article.md` (so the CHANGELOG can
  cite it and the pre-publish re-fact-check has one addressable file).
- **Classification — 0.1.2 docs + publish** (closes the ROADMAP "Launch article — dev.to"
  checkbox).
- **Acceptance:** zero occurrences of "Technical Product Manager"; the article's load
  order matches the CLI's printed `LOAD_ORDER` (four entries, glossary included); no
  claim of "no vendor schemas"; the B imprecisions fixed; **published** (the ROADMAP item
  closes on publication).

## X2. ROADMAP v0.1.x end-to-end validation run — **0.1.2 (record) / 0.2.0 (schema, D4)**

- **ROADMAP open:** "Run one real feature/initiative through the core loop (PRD →
  roadmap → sprint plan → design → tests), inspect every artifact against its import
  target (real Confluence page, real Jira issue, real GitHub PR), and refine the schemas
  where they miss."
- **Classification — split.** The **run itself** is evidence and changes no behaviour,
  so it can be **recorded in 0.1.2**; the **schema refinements** it surfaces are
  0.2.0 (`CONVENTIONS.md`: schema-shape work is at least a minor).
  [D4](06-open-decisions.md) decides whether to record it here or leave the whole
  milestone to 0.2.0.
- **Why it belongs near this plan:** it is the same "test against your real instance"
  the review's takeaways urge, and its findings feed I6 (the validation ledger) and the
  0.2.0 destination-binding work.
- **Field test (2026-11-25):** the four-repo run lives in
  [`field-test/`](../../field-test/README.md) at the repo root — Kubernetes · Grafana ·
  Deno · Rust, one feature each; raw input in, the project's own design held back as the
  answer key.
- **Acceptance:** the run recorded under `tests/results/`; every artifact pasted into
  its real target; schema misses either fixed (owner's call) or listed as 0.2.0
  forward-pointers in [07](07-scope-and-release.md).

## X3. Feedback / adoption analysis — **v0.1.x (not 0.1.2)**

- The F1 `field-feedback` template ships (0.1.1); **analyzing** its results needs real
  users first, so it stays in v0.1.x. It is the evidence inlet for R2 and R5/R8.
- **Acceptance (in v0.1.x):** findings summarized from real feedback; feeds R2's pilot
  and R5's cookbook; nothing collected automatically.

## X4. Refresh the competitive-landscape scan — **0.1.2 (docs, optional)**

- **Gap:** the only scan on file is dated 2026-11-23
  ([`../0.1.1-plans/08-competitive-landscape.md`](../0.1.1-plans/08-competitive-landscape.md));
  the review is a fresh external input, and the ecosystem moves fast.
- **Classification — 0.1.2 docs** (a new reference file), **optional** — the review is
  already reproduced in [08](08-review-input.md), so this is a *nice-to-have*, not a
  blocker. **Offline constraint:** the repo fetches nothing by charter, so a refresh is
  an owner-run web pass, recorded with retrieval dates and sources, exactly like the
  0.1.1 scan.
- **Acceptance:** every row carries a retrieval date and a source; it feeds
  candidate-skill and positioning decisions; it claims nothing unverified.

## Related

- [`../0.1.1-plans/01-launch-article.md`](../0.1.1-plans/01-launch-article.md) — the A/B fixes (X1)
- [`../../ROADMAP.md`](../../ROADMAP.md) — the open v0.1.x and launch-article items
- [`../0.1.1-plans/08-competitive-landscape.md`](../0.1.1-plans/08-competitive-landscape.md) — the prior scan (X4)
- [`../../tests/results/run-2026-11-23-g3-real-paste.md`](../../tests/results/run-2026-11-23-g3-real-paste.md) — the observed pastes X2 extends
