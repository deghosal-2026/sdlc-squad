# Findings — kit vs. answer key (grafana #77704)

> **Field test 02** — the kit's six artifacts in [`artifacts/`](artifacts/) scored against the
> real record in [`answer-key.md`](answer-key.md). Input: [`input.md`](input.md).

## Verdict

**Pass on discipline, weak on substance — because the input was thin.** The public record is a
**decision** ("build a 'Go back to x' button"), not a design. The kit did the right thing: it
**did not invent** the design, the milestone, the metric, or the team — it marked them
`[CONFIRM]` and, in `input.md`, flagged the inferred problem as inferred.

## What the kit got right

| Artifact | Matched the answer key |
|---|---|
| `pmt-prd.md` | The **goals** match the decision (a "Go back to x" control; a companion "Show history"); the problem framing is honestly flagged `[CONFIRM]` |
| `pmt-stories.md` | US-1…US-4 are the button; US-5 is the history epic — the same split the team decided |
| `tpm-roadmap.md` | Records the consensus milestone and the two workstreams; target/team are `[CONFIRM]` |
| `sde-design.md` | A plausible frontend design (back-target tracking, hide-on-deep-link) — but it is the kit's **inference**, since no design exists |
| `sde-tests.md` | Covers the button's edge cases (deep link, deleted target) |

## Where the kit diverged (and why it is correct)

- **The whole design is `[CONFIRM]`-marked or inferred** — the kit refused to present an invented
  design as fact. `sde-design.md` is the *only* artifact here that necessarily contains the
  kit's own reasoning, and it is labeled as such.

## Review against the templates

| Artifact | Bound schema | Conformance |
|---|---|---|
| `pmt-prd.md` | `confluence-prd-or-rfc.md` | ✅ full |
| `pmt-stories.md` | `jira-epic-and-stories.md` | ⚠️ C-2, T-5 | **US-5 has a row but no block**; the row is typed `Epic` (§7.2) |
| `tpm-roadmap.md` | *(none)* | ⚠️ loose — T-2 recurs |
| `sdm-sprint-plan.md` | `sprint-plan-and-capacity.md` | ✅ full (all `[CONFIRM]`) |
| `sde-design.md` | `technical-design-doc.md` | ⚠️ partial — no file paths/symbols (T-1) |
| `sde-tests.md` | `test-plan-and-cases.md` | ✅ full |

## Review against the RACI

- **R-1 — not present.** The PRD asserts **no milestone** (`[CONFIRM: no milestone…]`), so it
  does not over-reach into the TPM row.
- **R-2 — not present.** No product metric exists; the PRD says `[CONFIRM]` rather than placing
  an engineering metric.
- **R-4 (recurs)** — no **REQ-n → US-n → T-n** traceability.

## New finding (02-specific)

- **The SDM hop finally fits.** Unlike the cross-SIG features in 01/03/04, this is one team's UI
  work — the **only** run where "one squad's sprint plan" is the right shape. So the relay's
  "one squad" assumption is **not universally wrong**; it is wrong for **cross-team** features
  specifically. That sharpens the 0.2.0 recommendation: the relay needs a **cross-team mode**,
  not a redesign.
- **Input quality is a first-class variable.** The same kit, given a *decision* instead of a
  *design*, produced mostly `[CONFIRM]` — which is correct, but means the field test should
  **record input quality per run** so results are comparable.

## Result

**Pass, with caveats.** Same T-1/T-2 and R-1/R-2/R-4 issues as 01/03/04 — **four for four**, now
confirmed **systemic**. The distinct signal from 02: the relay's one-squad assumption is right
for single-team features and wrong for cross-team ones — it needs a **mode**, not a rewrite.
