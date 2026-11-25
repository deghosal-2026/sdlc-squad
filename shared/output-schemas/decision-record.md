# Output schema — Decision record (ADR)

Bound by: any role that makes a decision — a lightweight architecture/decision record.

## Canonical shape

```markdown
# Decision: [title]

> Status: Proposed · Date: YYYY-MM-DD · Owner: [CONFIRM: name] · Deciders: [CONFIRM: names]

## Context
[The forces at play — the problem, the constraints, and what forced a decision.]

## Decision
[The choice, in one or two sentences.]

## Consequences
[What becomes easier; what becomes harder; follow-ups.]

## Alternatives considered
| Option | Why not |
|---|---|

## Import target
Confluence — the decision log. The repo — `docs/adr/NNNN-<slug>.md`.
```

## Rules

- **One decision per record.** A decision to **do nothing** is still a decision — record it.
- The **Decision** is one or two sentences; the **Context** explains *why*.
- **Alternatives** each carry the reason they were not chosen. An empty table means none were
  considered — say so, don't leave it blank.
- The record captures a decision already governed by a `shared/raci.md` row; the **deciding role**
  owns the record (the RACI says who that is). This artifact adds no new decision right.
