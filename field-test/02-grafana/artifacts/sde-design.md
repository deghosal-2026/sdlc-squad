# Design: "Go back to x" navigation

> **Field-test artifact** — the kit's `sde/technical-design-and-breakdown` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Status: Draft · Author: [CONFIRM: name] · Last updated: 2026-11-25

## Affected modules / services

| Service / repo / path | Change | Risk |
|---|---|---|
| Grafana frontend — routing / URL state | Track the previous view as a back target | Medium |
| Grafana frontend — app chrome / nav | Add the "Go back to x" control | Low |
| Grafana frontend — scene/app state | Persist the back target across renders | Medium |
| Docs / UX | Document the affordance | Low |

*The issue gives no file paths; symbol-level claims are `[CONFIRM: read the implementation
PRs.]`*

## Data model & API / contract changes

- **No public API change** — a frontend navigation affordance.
- **Internal contract:** a "previous view" is tracked and exposed as a **back target**
  (a label + a route), so the control can name it (`Go back to <view>`).
- **URL stays shareable** — the back target is client state, not baked into the URL.

## Flow

1. User is on view A; the app records A as the current context.
2. User navigates to view B; the app sets the back target to A.
3. The control renders `Go back to <A>`.
4. User clicks it; the app navigates to A and clears/replaces the back target.
5. On a direct deep link (no A), the control is hidden.

## Failure modes & edge cases

| ID | Trigger | Behavior | Detection |
|---|---|---|---|
| FM-1 | Direct deep link (no previous view) | control hidden/disabled | visual / e2e |
| FM-2 | Previous view deleted/renamed | graceful message | e2e |
| FM-3 | Rapid navigation (A→B→C) | back target is the last view (B) | e2e |
| FM-4 | Back target becomes stale after reload | recompute or hide | e2e |

## Observability

- **Frontend logs / analytics** for control usage `[CONFIRM: define]`.
- **E2E coverage** for FM-1…FM-4.

## Rollback

1. Remove the control from the app chrome; routing is unchanged.
2. Revert the PR — no backend or data migration is involved.

## Sub-tasks (Jira-ready)

| ID | Task | Scope | DoD | Depends on |
|---|---|---|---|---|
| T-1 | Track the previous view | frontend state | the back target is available | — |
| T-2 | Render the "Go back to x" control | app chrome | the control names its target | T-1 |
| T-3 | Hide when no back target | app chrome | hidden on deep links | T-2 |
| T-4 | Keyboard access | app chrome | shortcut works | T-2 |
| T-5 | E2E tests | tests | FM-1…FM-4 covered | T-2 |

## Import target
Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the T-table as
sub-tasks.
