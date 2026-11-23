# Glossary and org placeholders — EXAMPLE (fictional)

> **This is an example, not a template to load.** It shows what a **filled** org
> glossary looks like, using the kit's fictional company (**Meridian Outfitters**).
> Every value below is invented. Do not paste this file into a session and do not edit
> it — instead, copy the real template (`shared/glossary-and-org.md`) to your own file
> **outside the kit** (`my-org.md`) and fill it with your facts
> (see [`../docs/UPGRADING.md`](../docs/UPGRADING.md)).

Like the real glossary, this holds domain vocabulary and the per-organization slots
every skill needs — here with the slots filled.

## Roles

| Term | Meaning |
|---|---|
| **PMT** | Product Manager, Technical — problem clarity, outcomes, non-goals, phasing |
| **TPM** | Technical Program Manager — cross-team dependencies, milestones, launch readiness, RAID |
| **SDM** | Software Development Manager — team throughput, capacity, scope trade-offs, ops health |
| **SDE** | Software Development Engineer — architecture, contracts, edge cases, testability, rollback |

## Working terms

| Term | Meaning |
|---|---|
| **Epic** | A large body of work that decomposes into stories |
| **Story / US** | A user-valuable slice of work; carries acceptance criteria |
| **Vertical slice** | A story that cuts all layers (UI → API → data) and ships value alone |
| **AC** | Acceptance criteria, in Given/When/Then |
| **DoD** | Definition of Done |
| **RAID** | Risks, Assumptions, Issues, Dependencies |
| **Carry-over** | Committed work that did not finish, moving into the next sprint |
| **Toil** | Manual, repetitive, low-judgment operational work |
| **Net focus capacity** | Gross time minus PTO, meetings, ceremonies, on-call, support, toil |
| **SLO / SLA** | Service-level objective / agreement |
| **Feature flag** | Runtime switch decoupling deploy from release |
| **Backfill / migration** | Data movement or transformation shipped with a release |
| **Rollback** | The named steps to return to the last good state |

## Org placeholders — filled (fictional)

| Slot | Value |
|---|---|
| Jira project key | `MER` |
| Jira instance / link | `https://meridian-outfitters.atlassian.net` *(fictional)* |
| Confluence space key | `MERID` |
| Primary services | `checkout`, `order-status`, `catalog`, `fulfilment` |
| Sprint length | 2 weeks (10 working days) |
| Ceremonies + standing meetings | daily standup 15m · sprint planning 2h · refinement 1h · retro 1h ≈ 6h/week per engineer |
| On-call rotation | weekly, one engineer; ≈ 0.5 day load per sprint |
| Support / interrupt expectations | ≈ 0.5 day per engineer per sprint |
| Escalation path (sev + who) | Sev1 → on-call → SDM → TPM · Sev2 → team channel; Sev3 → backlog |
| SLAs / SLOs in force | `order-status` API p95 < 800 ms · availability 99.9% |
| Estimate scale | T-shirt: S = 2d · M = 5d · L = 10d |

## How to use this file

When a session loads the kit, ask the user once for the slots above they have real
values for; carry them for the session. Anything still empty stays `[CONFIRM: ...]`
inside every artifact. Never fill a slot with a guess.
