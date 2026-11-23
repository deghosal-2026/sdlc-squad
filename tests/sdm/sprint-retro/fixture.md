# Fixture — sdm/sprint-retro

Synthetic end to end. Pulls the last 2 sprints' done tickets.

## Input

> Pastes: Sprint 13 done-ticket export (14 tickets, 12 closed in-sprint,
> 2 reopened once; 2 items carried into Sprint 14); Sprint 14 export (16 done,
> 0 reopens, 1 carried into 15). Both sprint plans supplied (commitments 13
> and 14 items). On-call log: one Sev-2 in Sprint 13.

## Expected artifact (skeleton)

# Retro — Sprints 13–14, 2026-11-07 → 2026-12-18
## What the data shows
- Sprint 13: 12/13 committed done in-sprint [paste]; 2 reopens; 2 carry-overs.
- Sprint 14: 16/14 (2 spillover absorbed) [paste]; 0 reopens; 1 carry-over.
## What went well (with receipts)
- Reopen rate 2→0 [paste counts] — the cache fix (ticket SPR-88, SPR-92 cluster).
## What hurt (with receipts)
- Sprint 13 Sev-2 during on-call [paste] — interrupt tax on M1.
- Two reopened tickets both touched stale cache [paste] — now a T-1 in the debt-buffer.
## What we change → action items
| T-3 | interrupt budget carved out of plans (not borrowed) | owner [CONFIRM] | DoD: next plan shows the buffer row |
| T-4 | carry-over naming in every standup log | owner [CONFIRM] | DoD: log rows |
## Carry-over disposition: the 1 open Sprint 14 item re-committed (not silently left).
## Import target
Confluence retro page; Jira action-item tickets.

## Checks

- [ ] Window pinned (2 sprints, dates)
- [ ] Every well/hurt names its pasted tickets
- [ ] Counts from the paste, never estimated
- [ ] Action items: owner + DoD + destination sprint
- [ ] Open items dispositioned — nothing silently dropped