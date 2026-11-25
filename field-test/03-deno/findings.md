# Findings — kit vs. answer key (deno #8327)

> **Field test 03** — the kit's six artifacts in [`artifacts/`](artifacts/) scored against the
> real resolution in [`answer-key.md`](answer-key.md). Input: [`input.md`](input.md).

## Verdict

**Pass, with the same systemic caveats.** The kit produced schema-shaped artifacts and refused
to invent team data — but the **decisive product decision** (adopt Node's API, no bespoke one)
is the kind of thing the loop is weakest at carrying, because it lives in a *conversation*, not
a design doc.

## What the kit got right

| Artifact | Matched the answer key |
|---|---|
| `pmt-prd.md` | The problem (no HMR, no cache invalidation, blocks mocking/ports) and the **"align to Node, not a bespoke API"** goal both trace to the thread |
| `pmt-stories.md` | The slice (Node hook surface, `require(ESM)`, gating, invalidation, fast path, docs) matches the shipped PRs |
| `tpm-roadmap.md` | Milestones (`require(ESM)` in v2.0; Node loader in 2.x) and the decision-gated critical path match the outcome |
| `sde-design.md` | Node API surface, invalidation-without-re-evaluation, and the fast path match the thread |
| `sde-tests.md` | HMR, mocking, invalidation, and the no-re-evaluation constraint are covered |

## Where the kit diverged (and why it is correct)

- **Capacity, estimates, slack `[CONFIRM]`** — no team data exists.
- **The critical path was a *decision*, not engineering.** `tpm-roadmap.md` named this
  correctly ("the decision itself"), which is a genuinely good catch from a conversation-only
  input.

## Review against the templates

| Artifact | Bound schema | Conformance |
|---|---|---|
| `pmt-prd.md` | `confluence-prd-or-rfc.md` | ✅ full |
| `pmt-stories.md` | `jira-epic-and-stories.md` | ✅ full |
| `tpm-roadmap.md` | *(none)* | ⚠️ loose — T-2 recurs |
| `sdm-sprint-plan.md` | `sprint-plan-and-capacity.md` | ✅ full (all `[CONFIRM]`) |
| `sde-design.md` | `technical-design-doc.md` | ⚠️ partial — no file paths/symbols (T-1) |
| `sde-tests.md` | `test-plan-and-cases.md` | ✅ full |

## Review against the RACI

- **R-1 (recurs)** — the PRD's "Rollout" carries the milestone sequence (**TPM A/R**).
- **R-3 — not present.** The story and roadmap **DEP IDs align** (DEP-1 = Node API, DEP-2 =
  V8/deno_core in both); the genuine collision is 01 only.
- **R-4 (recurs)** — no **REQ-n → US-n → T-n** traceability.

## New finding (03-specific)

- **A decision-only input has no artifact home.** The whole feature hinged on *"adopt Node's
  API, not a bespoke one"* — a product/architecture **decision**. The kit has no first-class
  artifact for a *decision* (an ADR); it only appears as prose inside the roadmap's risk table.
  Candidate 0.2.0: an **ADR/decision-record** artifact, or a "decision" section carried by the
  relay.

## Result

**Pass, with caveats.** Same T-1/T-2 and R-1/R-3/R-4 issues as 01 and 04 — now **three for
three**, which confirms they are **systemic** to the kit, not artifacts of one feature. New
signal: the kit needs a **decision record**.
