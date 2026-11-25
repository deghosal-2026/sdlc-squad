# Sprint [CONFIRM: n] plan — sig-node (KEP-1287), [CONFIRM: dates]

> **Field-test artifact** — the kit's `sdm/sprint-planning-and-capacity` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> **Inputs missing on purpose.** The KEP publishes the *feature*, not the *team*: no roster,
> PTO, on-call, or ceremony hours exist in the public record. Every capacity cell is therefore
> `[CONFIRM]` — the kit refuses to invent them. A real squad would supply these and the
> arithmetic would fill in.

## Capacity

| Engineer | Gross days | − PTO | − Meetings & ceremonies | − On-call / support / toil | = Net focus days |
|---|---|---|---|---|---|
| [CONFIRM: roster] | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] |
| **Total** | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] | **[CONFIRM]** |

No subtraction can be shown: the roster, PTO calendar, ceremony list, and on-call schedule
were not supplied (they are not in the KEP).

## Synthetic team (to exercise the SDM hop)

The OSS record has no roster, so the capacity table above cannot fill. To **exercise the SDM
hop** end-to-end, here is a **synthetic** squad — clearly fictional; `[CONFIRM: replace with a
real roster]`:

| Engineer | Gross days | − PTO | − Meetings & ceremonies | − On-call / support / toil | = Net focus days |
|---|---|---|---|---|---|
| PERSON-A | 10 | 0 | 1.5 | 0.5 | 8 |
| PERSON-B | 10 | 2 | 1.5 | 0 | 6.5 |
| PERSON-C | 10 | 0 | 1.5 | 1 | 7.5 |
| PERSON-D | 10 | 1 | 1.5 | 0 | 7.5 |
| **Total** | 40 | 3 | 6 | 1.5 | **29.5** |

Arithmetic: `40 − 3 − 6 − 1.5 = 29.5` net focus days. The commitment below must be ≤ 29.5 — but
with no story estimates it still cannot be sized (`[CONFIRM: SDE/SDM estimate]`).

## Proposed commitment

| Bucket | Items | Net focus days |
|---|---|---|
| Carry-over | [CONFIRM: prior sprint state not in the KEP] | [CONFIRM] |
| Core / milestone work | US-1 … US-8 (the alpha slice) | [CONFIRM: no estimates supplied] |
| Tech debt / reliability / buffer | — | [CONFIRM] |
| **Total committed** | | **[CONFIRM]** |

## Flagged risks

- **No estimates exist.** The KEP carries no sizes; `[CONFIRM: SDE/SDM estimate]` blocks any
  commitment number.
- **External dependency on the critical path** — the runtime contract (DEP-3) is owned
  outside sig-node; a slip moves the whole sprint.
- **No roster** — capacity cannot be computed, so over-allocation cannot be assessed yet.
- **Cross-SIG work** (scheduling, API machinery) is not one team's sprint — the relay's SDM
  hop assumes a single squad; here the work spans SIGs.

## Import target
Confluence — the sprint planning note. Jira — the sprint backlog after grooming.

## Handoff
- **From:** `sdm/sprint-planning-and-capacity` — the sprint plan
- **Carried open:** `[CONFIRM: story estimates]` · `[CONFIRM: the real roster]`
- **Next:** `sde/technical-design-and-breakdown` — paste the committed item + the services it touches
