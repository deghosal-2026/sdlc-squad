# Fixture — tpm/program-status-review

Synthetic end to end.

## Input

> Monthly cadence. Last review: M1 green, M2 yellow (template unscheduled), R1
> open. This month's Jira paste: M1 done 2026-12-11 tagged `release-14`; M2 legal
> review scheduled; a new DEP-3 on translations.

## Expected artifact (skeleton)

# Program status — 2026-11-22 review
## Fixed definitions: green on-track · yellow named risk + open mitigation · red missed/no path
| Item | Owner | Status | Evidence | Δ last |
| M1 status events | Checkout | green | done 2026-12-11, tagged release-14 [paste] | yellow→green |
| M2 template | Notifications | yellow | legal review scheduled [paste]; mitigation open | yellow, persisted |
| R1 freeze slip | [CONFIRM] | yellow | signal: M1 no longer at risk; mitigation stays open | improved |
| DEP-3 translations | [CONFIRM] | new | [CONFIRM: evidence] | new |
## Deltas
M1 closed green; DEP-3 added; nothing regressed.
## Asks
| Ask: schedule DEP-3 owner | needed by: next week | cost of not deciding: M3 translation slips |

## Checks

- [ ] Every status row carries its evidence or CONFIRM
- [ ] Deltas reference the last review (not a fresh re-run)
- [ ] Asks have owner + by-when + cost-of-not-deciding
- [ ] No status greener than its reddest critical-path item