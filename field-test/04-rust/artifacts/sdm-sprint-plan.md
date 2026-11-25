# Sprint [CONFIRM: n] plan — rustc compiler team (`let-else`), [CONFIRM: dates]

> **Field-test artifact** — the kit's `sdm/sprint-planning-and-capacity` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> **Inputs missing on purpose.** An RFC publishes the *feature*, not the *team*: no roster,
> PTO, on-call, or ceremony hours exist in the public record. Every capacity cell is `[CONFIRM]`.

## Capacity

| Engineer | Gross days | − PTO | − Meetings & ceremonies | − On-call / support / toil | = Net focus days |
|---|---|---|---|---|---|
| [CONFIRM: roster] | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] |
| **Total** | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] | **[CONFIRM]** |

No subtraction can be shown: the roster and calendars were not supplied.

## Proposed commitment

| Bucket | Items | Net focus days |
|---|---|---|
| Carry-over | [CONFIRM: prior sprint state not in the RFC] | [CONFIRM] |
| Core / milestone work | US-1 … US-8 (the initial slice) | [CONFIRM: no estimates supplied] |
| Tech debt / reliability / buffer | — | [CONFIRM] |
| **Total committed** | | **[CONFIRM]** |

## Flagged risks

- **No estimates exist.** The RFC carries no sizes; `[CONFIRM: SDE/SDM estimate]` blocks any
  commitment number.
- **A language feature is not one team's sprint.** It touches compiler, rustfmt, and the lang
  team (DEP-1…3) — the SDM hop assumes one squad.
- **Stabilization is externally gated** by the if-let-chains interaction (Q-1), which no sprint
  can schedule.

## Import target
Confluence — the sprint planning note. Jira — the sprint backlog after grooming.
