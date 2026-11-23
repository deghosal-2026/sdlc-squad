# Output schema — Jira epic and stories

Bound by: `pmt/slice-mvp-and-stories`.

## Canonical shape

```markdown
# Epic: [Summary]

| Field | Value |
|---|---|
| Epic key | [CONFIRM: assigned by Jira on import] |
| Type | Epic |
| Priority | [per the org's scale or CONFIRM] |
| Business value | [the outcome it serves, one line] |
| Success metric | [link or inline] |

## Why
[Two to four sentences from the PRD. No new claims.]

## Stories

| ID | Summary | Type | Priority | Size | Dependencies |
|---|---|---|---|---|---|
| US-1 | ... | Story | ... | [user's scale] | DEP-1 |
| US-2 | ... | Story | ... | ... | — |

### US-1 — [Summary]
**Description:** [user-valued outcome, one paragraph, no implementation.]
**Acceptance criteria:**
- **AC-1** Given [precondition] when [action] then [observable result].
**Dependencies:** DEP-1 [what and from whom]

## Dependencies
| ID | On what | From | Blocks | Status |
|---|---|---|---|---|

## Import target
Jira — epic + stories via bulk import / CSV; paste each story's block into its ticket
description.
```

## Rules

- Stories are vertical slices; a story that only changes a database column is a task, not a
  story — say so instead of dressing it up.
- Size only in the user's supplied scale (points or T-shirt); `[CONFIRM]` if none was given.
- Every dependency row names the team/person or `[CONFIRM]`.
- CSV-ready: keep pipe characters out of cell bodies, or export the story table as CSV on
  request.