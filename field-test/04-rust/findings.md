# Findings — kit vs. answer key (RFC 3137 `let-else`)

> **Field test 04** — the kit's six artifacts in [`artifacts/`](artifacts/) scored against the
> real RFC in [`answer-key.md`](answer-key.md). Input: [`input.md`](input.md).

## Verdict

**Pass, with the same structural caveats as 01.** The kit reproduced the feature's shape from
the Motivation alone and refused to invent team data — but the same two failure classes
recurred: **cross-owner data duplication** and **a schema gap for the roadmap**.

## What the kit got right

| Artifact | Matched the answer key |
|---|---|
| `pmt-prd.md` | Problem (rightward drift, nesting, conditional/error gap), goals, non-goals, and the **two expression restrictions** all trace to the RFC |
| `pmt-stories.md` | The slice covers parser, desugaring, divergence, lints, rustfmt, docs — the RFC's moving parts |
| `tpm-roadmap.md` | Milestones (RFC → implementation → stabilization) and the lang/rustfmt/compiler dependencies are right |
| `sde-design.md` | The desugaring (`match` + diverging arm), the restrictions, and the `!` divergence rule match the RFC's Reference-level explanation |
| `sde-tests.md` | The matrix covers the restrictions, divergence, lints, or-patterns, and rustfmt idempotence |

## Where the kit diverged (and why it is correct)

- **Capacity, estimates, slack are all `[CONFIRM]`** — the RFC has no team data.
- **Stabilization version left `[CONFIRM]`** — the RFC does not state it; the kit did not guess.

## Review against the templates

| Artifact | Bound schema | Conformance |
|---|---|---|
| `pmt-prd.md` | `confluence-prd-or-rfc.md` | ✅ full |
| `pmt-stories.md` | `jira-epic-and-stories.md` | ⚠️ C-1 | **US-3 has a row but no block** (§7.2) |
| `tpm-roadmap.md` | *(none)* | ⚠️ loose — same gap as 01 (T-2) |
| `sdm-sprint-plan.md` | `sprint-plan-and-capacity.md` | ✅ full (all `[CONFIRM]`) |
| `sde-design.md` | `technical-design-doc.md` | ⚠️ partial — names crates, not file paths/symbols (T-1) |
| `sde-tests.md` | `test-plan-and-cases.md` | ✅ full |

## Review against the RACI

- **R-1 (recurs)** — the PRD's "Rollout" carries the **milestone sequence** (RFC → impl →
  stabilization), which is **TPM A/R**; the PRD should reference it.
- **R-2 — not present.** "Success metrics & guardrails" is **PMT A/R**, but a language feature
  has **no product metric**; the PRD says so honestly (`[CONFIRM: no metric published]`) rather
  than placing an engineering metric.
- **R-4 (recurs)** — no **REQ-n → US-n → T-n** traceability.

## New finding (04-specific)

- **A language feature has no product layer.** For an RFC, the **PMT PRD and the SDE design
  collapse into one document** even more than for the KEP — the "success metric" has no
  product meaning. This strengthens the 01 recommendation: the kit needs a **design-led mode**
  (SDE-first, PRD optional) for features that *are* specifications.

## Result

**Pass, with caveats.** Same template (T-1, T-2) and RACI (R-1, R-2, R-4) issues as 01 —
which suggests they are **systemic**, not specific to one feature. The cross-feature
recurrence is the real signal.
