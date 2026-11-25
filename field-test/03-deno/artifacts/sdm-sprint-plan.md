# Sprint [CONFIRM: n] plan — Deno runtime team (loader API), [CONFIRM: dates]

> **Field-test artifact** — the kit's `sdm/sprint-planning-and-capacity` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> **Inputs missing on purpose.** An issue thread publishes the *feature*, not the *team*: no
> roster, PTO, on-call, or ceremony hours. Every capacity cell is `[CONFIRM]`.

## Capacity

| Engineer | Gross days | − PTO | − Meetings & ceremonies | − On-call / support / toil | = Net focus days |
|---|---|---|---|---|---|
| [CONFIRM: roster] | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] |
| **Total** | [CONFIRM] | [CONFIRM] | [CONFIRM] | [CONFIRM] | **[CONFIRM]** |

## Proposed commitment

| Bucket | Items | Net focus days |
|---|---|---|
| Carry-over | [CONFIRM: prior sprint state not in the thread] | [CONFIRM] |
| Core / milestone work | US-1 … US-6 (loader compat) | [CONFIRM: no estimates supplied] |
| Tech debt / reliability / buffer | — | [CONFIRM] |
| **Total committed** | | **[CONFIRM]** |

## Flagged risks

- **No estimates exist.** The thread carries no sizes; `[CONFIRM: SDE/SDM estimate]` blocks any
  commitment number.
- **The decision was the work.** Five years of demand and a working fork ended with *"adopt
  Node's API, no bespoke one"* — a **product/architecture decision**, not a sprint task. The
  SDM hop has nothing to schedule until that decision is made.
- **`require(ESM)` already shipped** (v2.0) and is independent of the loader work.

## Import target
Confluence — the sprint planning note. Jira — the sprint backlog after grooming.
