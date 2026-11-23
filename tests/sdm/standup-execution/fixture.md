# Fixture — sdm/standup-execution

Synthetic end to end.

## Input

> Sprint 14, day 6. Board: US-1 in progress (engaged), US-3 waiting on the
> archived-order API review, US-4 blocked on translations [DEP-3] since
> yesterday. Yesterday's log: 2 blockers, one still open. Timebox: 15
> minutes, board order. Escalation norm: one working day.

## Expected artifact (skeleton)

# Standup log — Sprint 14, day 6 (15m, board order)
## Round
| US-1 | today: read path + tests | blocker: — | carry-risk: — |
| US-3 | today: review slot | blocker: review not scheduled, since [CONFIRM] | → parked: after-standup with reviewer |
| US-4 | — | blocker: DEP-3 translations, since yesterday | aging: 1 day = at threshold |
## Escalated (R-n if program-visible)
- US-4 blocker at escalation threshold → target [CONFIRM: DEP-3 owner], next step: translation
  owner named, by: today.
## Parking lot
- US-3 review scheduling → 10:30, [CONFIRM: names].
## No yesterday-recaps (board carries status).

## Checks

- [ ] Three columns per item; no progress theater
- [ ] Every blocker row: what/who/since/next/by
- [ ] Over-threshold aging escalated in the row, visible
- [ ] Carry-risk items flagged (feed sprint-retro + next plan)
- [ ] Deep dives parked with people + slot