# 01 — Verification: make grounding visible and checkable

> **Status (2026-11-25):** V2, V5, V7, V8, V9 in scope for 0.1.2; V1, V3, V4, V6
> are **forward-pointers to 0.2.0**. Master table: [`README`](README.md).

Theme: the review's Track 1. The kit's differentiator is anti-hallucination, but the
review's sharpest point is that it is a *prompt convention, not a check* — "weaker or
instruction-ignoring models can still invent facts or skip markers." This file splits
what a **docs-only patch** can make visible (the review's *practice* half) from what
needs **enforcement code** (a linter, schema-level blocks), which is 0.2.0.

## V1. Automated `[CONFIRM]` linter & gatekeeper — **forward to 0.2.0**

- **Review claim:** a lightweight script or pre-paste validator that scans generated
  Markdown for missing `[CONFIRM: ...]` markers on dates, owners, story points, IDs,
  and metrics, and flags suspiciously clean "zero-confirm" outputs on rough notes.
  The breakdown names it `scripts/lint_artifact.py`.
- **Why it matters:** this is the review's answer to its own W1 — turning a soft
  convention into an enforceable quality check so unverified numbers never reach a
  planning doc.
- **Classification — 0.2.0.** A new script is new behaviour, and the 0.1.1 fence drew
  exactly this line (the review's "CSV export templates" were set aside in D1 as "a
  feature"). A linter also carries a schema-level question the kit has not answered:
  *which* markers are mandatory in *which* sections — that is `shared/output-schemas/`
  work (`CONVENTIONS.md`: schema-shape work is at least a minor).
- **Docs precursor ships in 0.1.2:** the reviewer's checklist lives in V2/V7 and the
  cookbook R5 — a human can run it by eye before the script exists.
- **Where it belongs:** 0.2.0 — `scripts/lint_artifact.py`, offline, zero-dependency,
  with its own recorded run.
- **Acceptance (when built):** a local, offline checker that (a) flags zero-`[CONFIRM]`
  artifacts against raw-note input, (b) lists unresolved markers and vague
  hand-waving (`TBD`, `as needed`, `standard SLA`), and (c) reconciles capacity/estimate
  table row sums against summary totals; its behaviour is recorded under `tests/`.

## V2. Claim-to-source tagging — **0.1.2 (docs practice)**

- **Review claim:** require every non-trivial claim, estimate, or risk to carry a
  compact provenance tag — `[src: notes]`, `[src: prd-draft]`, `[src: org-glossary]`,
  or `[CONFIRM: missing from input]` — so a reviewer inspects only the claims lacking
  a valid source.
- **Anchor (zero invention):** `docs/REVIEWING-OUTPUT.md` already teaches the same
  axis as **claim-type marking** — *source-backed fact · calculation · inference ·
  open question* — and already carries the `[CONFIRM]`-resolution practice (replace
  the marker with the fact **and its source**; keep a "resolved in this revision"
  list). V2 adds the compact **tag vocabulary** and the review workflow on top.
- **Classification — 0.1.2 docs practice.** Encoding the tags into the schemas is the
  same work as the 0.1.1 forward-pointer **"artifact provenance footer"**
  ([`../0.1.1-plans/07`](../0.1.1-plans/07-scope-and-release.md), H) — deferred to
  0.2.0 there, and it stays there.
- **Acceptance:** `docs/REVIEWING-OUTPUT.md` defines the tag vocabulary and the
  review-by-exception workflow; every tag it names traces to a rule already in
  `CONVENTIONS.md` or the charter; no schema or skill file is touched.

## V3. Arithmetic & capacity self-audit block — **forward to 0.2.0**

- **Review claim:** a mandatory calculation check at the bottom of SDM/TPM outputs
  (sprint capacity, PTO deductions, story-point totals, RAID counts) that reconciles
  sub-rows against totals — because "LLMs frequently misadd numbers even when they
  format tables cleanly."
- **Classification — 0.2.0.** The capacity and estimate tables are schema-bound
  (`shared/output-schemas/sprint-plan-and-capacity.md`); adding a reconciliation block
  changes the artifact shape a skill emits — skill/schema work.
- **Docs precursor ships in 0.1.2:** V2/V7 teach the reviewer to *audit the
  arithmetic*; the SDM capacity tables are already the exemplar of shown math
  (`docs/REVIEWING-OUTPUT.md`, D3).
- **Acceptance (when built):** the SDM/TPM output schemas carry a self-audit block
  that shows sub-row sums against totals; a fixture exercises a deliberate mismatch.

## V4. Confidence & ambiguity scoring per section — **forward to 0.2.0**

- **Review claim:** tag each artifact section **High Grounding** / **Partial — needs
  confirmation** / **Assumed — draft**, with up to three high-leverage questions.
- **Classification — 0.2.0.** Per-section labels are part of the emitted artifact →
  schema/skill change. The docs-only shadow of this is V7's assumption-vs-fact
  separation, which a reviewer can apply without a schema change.
- **Acceptance (when built):** schemas define the section-confidence vocabulary; every
  playbook emits it; a fixture shows all three states.

## V5. Model behavioral profiles + 60-second benchmark — **0.1.2 (docs)**

- **Review claim:** expand `docs/MODELS.md` with concrete per-model failure notes
  (over-filling optional table cells, ignoring negative constraints, dropping
  `[CONFIRM]` brackets) plus a **60-second benchmark prompt**.
- **Anchor:** `docs/MODELS.md` already exists (D5) with the observed record
  (`GLM-5.3`), the structural-requirements note, and a five-point
  certify-your-model checklist. V5 adds the **benchmark prompt** and a
  **failure-mode table**.
- **Classification — 0.1.2 docs, with an honesty guard.** The kit forbids naming
  untested models as working, printing performance/quality scores, or stating
  benchmark numbers without the user's own data (`CONVENTIONS.md`; the D5
  classification). So the failure-mode table ships **evidence-gated**: empty (or
  `[CONFIRM: run per model]`) until a run is recorded. The 60-second prompt is a
  **user-run check** — the same evidence class as the existing checklist, which
  asserts nothing.
- **Acceptance:** MODELS.md gains a copy-paste benchmark prompt and a failure-mode
  table whose rows each cite a recorded run or carry `[CONFIRM]`; no model named as
  working without evidence; no scores.

## V6. Model regression harness — **forward to 0.2.0**

- **Review claim:** a golden set of tricky inputs (missing dates, conflicting
  priorities, over-allocated sprint capacity, subtle PII/hostnames) scored on
  refusal/flagging accuracy, schema fidelity, and low-cost-model viability.
- **Classification — 0.2.0.** A golden set is a **new class of `tests/` artifact**
  with its own expected outputs and a runner — test infrastructure, and it collides
  with the evidence rule's shape (a fixture is per-skill; a golden set is
  cross-skill and model-keyed).
- **Where it belongs:** 0.2.0, alongside the V1 linter (the harness scores what the
  linter checks).
- **Acceptance (when built):** the golden inputs and expected flag/schema outcomes are
  committed under `tests/`; a runner reports per-model refusal and schema fidelity;
  no quality score is published as a kit claim.

## V7. Assumption-vs-fact separation — **0.1.2 (docs practice)**

- **Review claim:** instead of letting assumptions hide in narrative paragraphs,
  require a dedicated **Assumptions & Open Questions (`[CONFIRM]`)** block plus inline
  markers where a guess would alter execution (target release date, dependency owner,
  DB migration lock behavior).
- **Anchor:** the playbooks already end in a **read-back step** and the schemas carry
  an open-questions/`Q-n` convention; D3 already puts the reviewer's eye on the
  fact/calculation/inference/open-question axis.
- **Classification — 0.1.2 docs practice.** A dedicated schema block is 0.2.0
  (artifact shape); the *reviewer* practice ships now.
- **Acceptance:** `docs/REVIEWING-OUTPUT.md` (or a sibling section) states the
  fact-vs-assumption split, names the high-impact guesses that must be inline-marked,
  and cites the existing read-back rule; no schema or skill file is touched.

## V8. False-positive / "legitimately clean" guidance — **0.1.2 (docs)**

- **Review claim (implicit):** "a rule saying zero `[CONFIRM]`s is a defect is a useful
  heuristic, **not a guarantee**." The plan must state the converse too, or it teaches
  reviewers to distrust good artifacts.
- **What:** `docs/REVIEWING-OUTPUT.md` states when a clean artifact is **correct** —
  every fact was supplied by the user (structured notes, an exported backlog, a prior
  artifact) — and how to tell it apart from an **unexplained** clean artifact over raw
  notes. The rule flags *unexplained* cleanliness against thin input, not cleanliness
  itself. This also fixes the future V1 linter's rule before it is written.
- **Classification — 0.1.2 docs.** Restates the existing honesty rule
  (`CONVENTIONS.md`) with its boundary; no schema/skill change.
- **Acceptance:** `REVIEWING-OUTPUT.md` names both cases and the test that separates
  them; the "zero markers on raw notes is a defect" rule is unchanged.

## V9. PII / hostname pre-paste check — **0.1.2 (docs)**

- **Review claim (implicit):** the regression harness (V6) names "subtle PII/hostnames"
  as tricky inputs — but no *reviewer* step checks for them before an artifact leaves
  the session.
- **What:** a pre-paste check in the review workflow: scan the artifact for real names,
  emails, tokens, customer identifiers, and internal hostnames/URLs, and redact per
  `docs/EXPORTS.md` §Redaction (C7). It is a **human** check — the kit detects nothing
  automatically (no network, no scanner).
- **Classification — 0.1.2 docs.** Extends the shipped redaction recipe into the
  reviewer's step list.
- **Acceptance:** `REVIEWING-OUTPUT.md` gains the pre-paste PII check, pointing at the
  redaction table; it claims no automatic detection.

## Related

- [`docs/REVIEWING-OUTPUT.md`](../REVIEWING-OUTPUT.md) — the shipped review guide V2/V7 extend
- [`docs/MODELS.md`](../MODELS.md) — the shipped model page V5 extends
- [`docs/EVIDENCE.md`](../EVIDENCE.md) — the recorded defects the cookbook (R5) will index
- [`07-scope-and-release.md`](07-scope-and-release.md) — the forward-pointer fence
