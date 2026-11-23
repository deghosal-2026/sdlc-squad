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
[Phasing, flags, and the metric this ships against — link the metric definition.]

## Import target
Confluence — the PRD/RFC page for this initiative.
```

## Rules

- Every number, name, and date in the body carries its source or a `[CONFIRM: ...]`.
- "Goals" name outcomes; "Non-goals" are first-class content, not a courtesy section.
- Edge cases are required, not optional: an artifact with none has not been thought through.