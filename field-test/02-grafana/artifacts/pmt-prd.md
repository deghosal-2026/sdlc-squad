# Go back to x — back navigation in Grafana

> **Field-test artifact** — the kit's `pmt/draft-prd` output from [`../input.md`](../input.md).
> Compare against [`../answer-key.md`](../answer-key.md) in [`../findings.md`](../findings.md).

> Status: Draft · Owner: [CONFIRM: name] · Last updated: 2026-11-25 · Reviewers: [CONFIRM: names]

## Problem & context

- `[CONFIRM: the issue records the decision, not the problem.]` Inferred: users moving between
  Grafana views **lose their place**, with no easy way to return to the previous context
  (source: grafana#77704 — decision only).
- A companion **"Show history"** need was agreed to have "a lot of potential" (source:
  grafana#77704).

## Target users

- **Grafana users** who navigate deep (dashboard → panel → Explore → another dashboard) and want
  to return to where they were. `[CONFIRM: no user research in the issue.]`

## Goals

- A **"Go back to x"** affordance that returns the user to the previous context.
- (Companion) a **"Show history"** capability to revisit prior views.

## Non-goals

- `[CONFIRM: none stated in the issue.]` Proposed: a full browser-history replacement, or
  cross-session history persistence.

## User journeys

| Step | User action | System behavior | Notes |
|---|---|---|---|
| 1 | User navigates from view A to view B | B renders; A is remembered | `[CONFIRM: mechanism]` |
| 2 | User clicks "Go back to x" | returns to A | the core ask |
| 3 | (Companion) User opens "Show history" | prior views listed | epic |

## Requirements

### Functional

- **REQ-1** A **"Go back to x"** control that returns to the previous context.
- **REQ-2** It names the target (`Go back to <view>`) — not a generic "Back".
- **REQ-3** (Companion) a **"Show history"** entry point. `[CONFIRM: scope — epic.]`

### Non-functional

- **REQ-4** Works within Grafana's SPA routing (URL stays shareable). `[CONFIRM]`
- **REQ-5** Keyboard-accessible. `[CONFIRM]`

## Edge cases

| EC | Trigger | Expected behavior |
|---|---|---|
| EC-1 | No previous view (first load) | the control is hidden or disabled |
| EC-2 | Deep link opened directly | no back target `[CONFIRM]` |
| EC-3 | Previous view was deleted/renamed | graceful message `[CONFIRM]` |

## Open questions

| # | Question | Owner | Needed by |
|---|---|---|---|
| Q-1 | What counts as "the previous context"? | [CONFIRM: grafana frontend] | [CONFIRM] |
| Q-2 | Scope of the "Show history" epic | [CONFIRM: grafana frontend] | [CONFIRM] |

## Rollout & metrics

- `[CONFIRM: no milestone, flag, or metric published in the issue.]`
- Proposed metric: reduced "navigate away and back" friction — `[CONFIRM: define]`.

## Import target
Confluence — the PRD/RFC page for this initiative.
