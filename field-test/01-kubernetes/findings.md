# Findings — kit vs. answer key (KEP-1287)

> **Field test 01** — the kit's six artifacts in [`artifacts/`](artifacts/) scored against the
> real KEP in [`answer-key.md`](answer-key.md). Input: [`input.md`](input.md).

## Verdict

The kit reproduced the feature's **shape** faithfully — problem, goals/non-goals, the
desired→allocated→actuated→actual model, the two conditions, atomic resizes, and the memory
guard — all from the problem statement alone. It did **not** invent specifics it could not
know, and it correctly stalled where a real team input was missing.

## What the kit got right

| Artifact | Matched the answer key |
|---|---|
| `pmt-prd.md` | Problem, goals, and **non-goals** match the KEP's Motivation/Goals/Non-Goals; the rollout (alpha v1.27 → beta v1.33 → stable v1.35) and feature gates match `kep.yaml` |
| `pmt-stories.md` | The alpha slice covers the API, status, `resizePolicy`, conditions, kubelet actuation, scheduler/quota, memory guard, metrics — the KEP's affected components |
| `tpm-roadmap.md` | Milestones match the KEP's release targets; dependency table names the right SIGs (api-machinery, scheduling, autoscaling) and the runtimes |
| `sde-design.md` | The four resource states, the `/resize` subresource, `UpdatePodSandboxResources`, the decrease-before-increase ordering, and the failure modes all trace to the KEP's Design Details |
| `sde-tests.md` | Layers match the KEP's Test Plan (unit / integration / CRI contract / E2E / backward-compat + negative) |

## Where the kit diverged (and why that is correct)

- **Capacity is all `[CONFIRM]`** (`sdm-sprint-plan.md`). The KEP has no roster, PTO, on-call,
  or ceremony hours — the kit refused to invent them. This is the discipline working, but it
  also shows the **SDM hop needs a real team input** the OSS record doesn't provide.
- **No per-dependency slack** in `tpm-roadmap.md` — the KEP gives release targets, not slack;
  marked `[CONFIRM]`.
- **Estimates everywhere `[CONFIRM]`** — the KEP carries no sizes; the kit did not guess.

## Review against the templates (output schemas)

| Artifact | Bound schema | Conformance | Notes |
|---|---|---|---|
| `pmt-prd.md` | `confluence-prd-or-rfc.md` | ⚠️ T-4 | journey rows 2–3 have `—` in the User action column (§7.2) |
| `pmt-stories.md` | `jira-epic-and-stories.md` | ✅ full | AC-n in Given/When/Then; sizes `[CONFIRM]` |
| `tpm-roadmap.md` | *(none — "follows `confluence-prd-or-rfc` table standards")* | ⚠️ loose | the **only** run skill without a dedicated schema |
| `sdm-sprint-plan.md` | `sprint-plan-and-capacity.md` | ✅ full | arithmetic shown as `[CONFIRM]` — inputs absent |
| `sde-design.md` | `technical-design-doc.md` | ⚠️ T-1, T-3 | "Affected modules" lists **components, not file paths/symbols** (T-1); **FM-5's Detection cell is `—`** (T-3) |
| `sde-tests.md` | `test-plan-and-cases.md` | ✅ full | all five layers present, incl. negative paths |

**Template violations / weaknesses**
- **T-1 — `sde-design` breaks a schema rule.** `technical-design-doc.md`: *"Design sections
  cite the repository they read: file paths and symbols, quoted where it matters."* The
  artifact names components (`kube-apiserver`, `kubelet`), not paths/symbols. Marked
  `[CONFIRM: read the implementation PRs]`, so it is honest — but not conformant.
- **T-2 — the TPM roadmap has no template.** Four of the five schemas are used; the program
  roadmap "follows the PRD table standards." It is the weakest-bound artifact and the obvious
  candidate for a sixth schema.

## Review against the RACI

| Artifact | RACI row | A/R | Conformance |
|---|---|---|---|
| `pmt-prd.md` | PRD — requirements & non-goals | PMT | ⚠️ see R-1, R-2 |
| `pmt-stories.md` | Epic & story slicing | PMT | ⚠️ see R-3 |
| `tpm-roadmap.md` | Program roadmap & milestone sequence · Cross-team dependency commitments | TPM | ✅ |
| `sdm-sprint-plan.md` | Sprint commitment (capacity-fit) | SDM | ✅ |
| `sde-design.md` | Technical design & breakdown | SDE | ✅ |
| `sde-tests.md` | Test plan & cases | SDE | ✅ |

**RACI violations**
- **R-1 — milestone data asserted by two A/R owners.** The PRD's "Rollout & metrics" carries
  the release sequence (**v1.27 → v1.33 → v1.35**). The matrix assigns *"Program roadmap &
  milestone sequence"* to **TPM A/R**; PMT is only **C**. The PRD should *reference* the
  roadmap, not own its milestones. As written, PMT and TPM both assert the same data.
- **R-2 — an engineering metric on the PMT row.** *"Success metrics & guardrails"* is **PMT
  A/R**; the PRD's metric cites `kubelet_pod_resize_duration_seconds` — an SDE observability
  concern, which already appears in `sde-design` §Observability. The **product outcome**
  metric is missing from the PRD.
- **R-3 — dependency IDs collide across owners.** Stories use **DEP-1…4**; the roadmap uses
  **DEP-1…5** — same prefix, different meanings (stories' DEP-1 = autoscaler; roadmap's DEP-1
  = API subresource). *"Cross-team dependency commitments"* is **TPM A/R**; the story list
  should reference the roadmap's IDs, not mint its own.
- **R-4 — no traceability.** Nothing maps **REQ-n → US-n → T-n**. A reviewer cannot follow a
  requirement to its story to its task, which the C/I hand-offs assume.

## Gaps surfaced (candidate 0.2.0 schema work)

1. **The PMT PRD is nearly redundant with the SDE design for an infra feature.** A KEP *is* a
   design doc; the PRD restated much of it. A "design-led feature" mode (start at SDE, PRD
   optional) would avoid the duplication.
2. **No schema slot for a staged rollout as first-class content** — alpha/beta/stable lived
   inside the PRD's "Rollout" prose, but it is milestone data the TPM roadmap needs. A shared
   milestone field would connect the two.
3. **The relay assumes one squad.** A cross-SIG feature (the common case in big OSS) does not
   fit "one SDM sprint plan"; the roadmap carries the cross-team work but the sprint plan has
   no honest place to land.

## Result

**Pass, with caveats.** The kit produced usable, schema-bound artifacts from a real problem
statement, and its `[CONFIRM]` discipline held under a large, complex feature. But reviewing the
artifacts **against the templates and the RACI** — not just writing them — surfaced **2 template
gaps (T-1, T-2) and 4 RACI violations (R-1…R-4)** the first pass missed. All are candidate 0.2.0
work; none is a correctness failure in the kit.
