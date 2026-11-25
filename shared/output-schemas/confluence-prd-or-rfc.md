# Output schema — Confluence PRD / RFC page

Bound by: `pmt/draft-prd` (and used as the spec half of `sde/technical-design-and-breakdown`
when a combined PRD+RFC page is requested).

## Canonical shape

```markdown
# [Title]

> Status: Draft · Owner: [CONFIRM: name] · Last updated: YYYY-MM-DD ·
> Reviewers: [CONFIRM: names]

## Problem & context
[What hurts, for whom, how often. The evidence behind the claim, each piece sourced.]

## Target users
[Who, described by behavior, not persona fluff.]

## Goals
- [Outcome-focused goals.]

## Non-goals
- [Explicitly out of scope for this phase. Phasing goes in Rollout.]

## User journeys
| Step | User action | System behavior | Notes |
|---|---|---|---|

[Every row names a **user action**. A step with no user action is a **system note** — put those
in a short **System flow** paragraph below the table, not as a journey row.]

## Requirements
### Functional
- **REQ-1** [requirement]
### Non-functional
- **REQ-n** [performance, privacy, cost, compliance...]

## Edge cases
| EC | Trigger | Expected behavior |
|---|---|---|

## Open questions
| # | Question | Owner | Needed by |
|---|---|---|---|

## Rollout & metrics
[Phasing, flags, and the **product** metric this ships against — link the metric definition.
**Milestones are owned by the TPM**: reference the program roadmap (`program-roadmap.md`); do not
assert release dates here. The **engineering** metric (latency, error rate, saturation) belongs
in the design (`technical-design-doc.md` §Observability), not here.]

## Import target
Confluence — the PRD/RFC page for this initiative.
```

## Rules

- Every number, name, and date in the body carries its source or a `[CONFIRM: ...]`.
- "Goals" name outcomes; "Non-goals" are first-class content, not a courtesy section.
- Edge cases are required, not optional: an artifact with none has not been thought through.
- **Journey rows require a user action.** A row whose *User action* cell is `—` is a system
  note — move it to a **System flow** paragraph (T-4).
- **Milestones are TPM-owned (R-1).** The Rollout section **references** the program roadmap; it
  does not assert release dates (RACI: *Program roadmap & milestone sequence* is **TPM A/R**).
- **The metric is the product outcome (R-2).** The engineering metric lives in the design's
  Observability section; the PRD carries the user/outcome metric (RACI: *Success metrics &
  guardrails* is **PMT A/R**).