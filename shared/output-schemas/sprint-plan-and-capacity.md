# Output schema — Sprint plan and capacity

Bound by: `sdm/sprint-planning-and-capacity`. Also the export format of
`sdm/scope-cut-and-tradeoffs` when the cut lands in a sprint commitment.

## Canonical shape

```markdown
# Sprint [n] plan — [team], YYYY-MM-DD to YYYY-MM-DD

## Capacity
| Engineer | Gross days | − PTO | − Meetings & ceremonies | − On-call / support / toil | = Net focus days |
|---|---|---|---|---|---|

[Every subtraction shows the input behind it; no assumed averages.]

## Proposed commitment
| Bucket | Items | Net focus days |
|---|---|---|
| Carry-over | [items] | ... |
| Core / milestone work | [items] | ... |
| Tech debt / reliability / buffer | [items] | ... |
| **Total committed** | | [must be ≤ total net focus days] |

## Flagged risks
- [Unestimated items, hidden dependencies, single-point-of-failure tasks,
   over-allocated engineers — each with the number that flags it.]

## Import target
Confluence — the sprint planning note. Jira — the sprint backlog after grooming.
```

## Rules

- The arithmetic is shown, all of it: each capacity cell traces to an input (roster, PTO
  calendar, meeting list, on-call schedule) or is `[CONFIRM]`.
- Net focus is never padded up. Committed total never exceeds net focus total.
- Over-allocation is flagged, never smoothed over.
- No velocity claims without the user's own historical data supplied in the session.