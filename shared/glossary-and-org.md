# Glossary and org placeholders

Domain vocabulary and the per-organization slots every skill needs. This file ships as a
template: every bracketed slot is an input the user fills in, never a fact the kit asserts.

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

## Org placeholders — fill before first use

| Slot | Value |
|---|---|
| Jira project key | `[CONFIRM: e.g. ABC]` |
| Jira instance / link | `[CONFIRM: URL]` |
| Confluence space key | `[CONFIRM: e.g. ENG]` |
| Primary services | `[CONFIRM: names as the org calls them]` |
| Sprint length | `[CONFIRM: e.g. 2 weeks]` |
| Ceremonies + standing meetings | `[CONFIRM: list with hours per week]` |
| On-call rotation | `[CONFIRM: rotation + expected load per engineer]` |
| Support / interrupt expectations | `[CONFIRM: hours per week per engineer]` |
| Escalation path (sev + who) | `[CONFIRM: chain]` |
| SLAs / SLOs in force | `[CONFIRM: list with targets]` |
| Estimate scale | `[CONFIRM: story points or T-shirts, with the legend]` |

## How to use this file

When a session loads the kit, ask the user once for the slots above they have real values for;
carry them for the session. Anything still empty stays `[CONFIRM: ...]` inside every artifact.
Never fill a slot with a guess.