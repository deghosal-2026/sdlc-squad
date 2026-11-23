# Fixture — sdm/sprint-planning-and-capacity

Synthetic end to end.

## Input

> 6 engineers (A–F), 2-week sprint (10 working days). D on PTO Thu–Fri (2d).
> Ceremonies+standing meetings ≈ 6h/wk each (1.5d/sprint). Weekly on-call: one
> engineer per week, ~0.5d/sprint load. Support/interrupt buffer: 0.5d each.
> Carry-over: 3 stories (sizes 2d+2d+1d). Candidates: order-status M1 est. 8d;
> flaky-test fix est. 2d; dark-mode request (no estimate).

## Expected artifact (skeleton)

# Sprint 14 plan — Team [CONFIRM: name], 2026-12-07 → 2026-12-18
## Capacity
| A | 10 − 0 − 1.5 − 0.5+0.5 | = 7.5 net focus days |
| D | 10 − 2 − 1.5 − 0.5+0.5 | = 5.5 (PTO from paste) |
| … six rows, every subtraction shows its input |
Team net focus: 39.0 days (arithmetic shown).
## Commitment
| Carry-over | 3 stories = 5d | ring-fenced first |
| Core: order-status M1 | 8d | fits: 5+8=13 ≤ 39 … |
| Debt/buffer: flaky-test fix | 2d | |
## Flagged risks
- dark-mode: unestimated → not committed, listed here.
- D at 5.5d carries an M1-touching task → over-allocation flag named.
## Import target
Confluence sprint note; Jira sprint backlog after grooming.

## Checks

- [ ] Every cell traces to an input or CONFIRM; no averaged guesses
- [ ] Committed total ≤ net focus total
- [ ] Carry-over ring-fenced first at its old sizes
- [ ] Unestimated candidates flagged, not committed
- [ ] No velocity claims (none supplied)