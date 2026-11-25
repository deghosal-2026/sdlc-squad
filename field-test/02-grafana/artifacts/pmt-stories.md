# Epic: Go back to x

> **Field-test artifact** — the kit's `pmt/slice-mvp-and-stories` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

| Field | Value |
|---|---|
| Epic key | [CONFIRM: assigned by Jira on import] |
| Type | Epic |
| Priority | [CONFIRM: per the org's scale] |
| Business value | Let users return to their previous context instead of re-navigating |
| Success metric | [CONFIRM: none published] |

## Why

Grafana users navigating between views lose their place. The team decided to build a **"Go back
to x"** button and to open a **"Show history"** epic. The slice below is the button (MVP); the
history capability is a follow-on epic.

## Stories

| ID | Summary | Type | Priority | Size | Dependencies |
|---|---|---|---|---|---|
| US-1 | "Go back to x" control that names its target | Story | [CONFIRM] | [CONFIRM] | — |
| US-2 | Remember the previous context | Story | [CONFIRM] | [CONFIRM] | — |
| US-3 | Hide/disable when there is no back target | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-4 | Keyboard-accessible | Story | [CONFIRM] | [CONFIRM] | US-1 |

### US-1 — The control

**Description:** As a Grafana user, I can click a control to return to my previous view.
**Acceptance criteria:**
- **AC-1** Given I navigated from view A to view B, when I click the control, then I return to A.
- **AC-2** Given the control, then it names the target (`Go back to <view>`).
**Dependencies:** —

### US-2 — Remember the previous context

**Description:** As a Grafana user, the app knows where I came from.
**Acceptance criteria:**
- **AC-1** Given navigation A → B, when B renders, then A is available as the back target.
**Dependencies:** —

### US-3 — No back target

**Description:** As a first-time visitor, the control doesn't mislead me.
**Acceptance criteria:**
- **AC-1** Given a direct deep link (no prior view), then the control is hidden or disabled.
**Dependencies:** US-1

### US-4 — Keyboard accessible

**Description:** As a keyboard user, I can trigger the control.
**Acceptance criteria:**
- **AC-1** Given focus, when I press the control's shortcut, then I return to the previous view.
**Dependencies:** US-1

## Companion epic (not a story)

The team also agreed to open a **"Show history"** epic (source: grafana#77704). It is a
**separate epic**, not a story in this set — recorded here so it is not lost, with its own
tracking: `[CONFIRM: the epic lives in grafana/grafana]`.

## Dependencies

| ID | On what | From | Blocks | Status |
|---|---|---|---|---|
| DEP-1 | Frontend routing (URL state) | grafana frontend platform | US-2 | [CONFIRM] |
| DEP-2 | "Show history" epic scope | grafana frontend platform | the Show history epic | [CONFIRM] |

## Import target
Jira — epic + stories via bulk import / CSV; paste each story's block into its ticket
description.
