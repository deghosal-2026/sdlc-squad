# Fixture — tpm/program-roadmap-and-deps

Synthetic end to end.

## Input

> Order-status PRD accepted. Checkout team owns status events; Notifications owns
> the guest email template; launch before the Dec-15 change freeze.

## Expected artifact (skeleton)

# Program: order-status self-service
## Milestones
| M1 | status events API | Checkout | [CONFIRM: Checkout's own date] | DoD: events emitted to bus |
| M2 | guest email template | Notifications | [CONFIRM: date] | blocks M3 |
| M3 | launch | Platform | [CONFIRM: freeze-adjacent date] |
## Dependencies
| DEP-1 | status events · from Checkout · blocks M2+ | status: in-conversation | owner [CONFIRM] |
| DEP-2 | template slot · from Notifications · blocks M3 | not-started | owner [CONFIRM] |
## Critical path
M1 → M2 → M3. Zero-slack link: M2 → M3 (freeze-adjacent) — flagged.
## Early-warning signals for top risks
- M1 date slips past Dec-1 → M3 leaves the freeze window → escalate [CONFIRM: who].

## Checks

- [ ] No date without a team behind it (or CONFIRM)
- [ ] Every DEP has owner + status; "TBD" absent
- [ ] Critical path named end-to-end; zero-slack links flagged
- [ ] No invented team names or calendar facts
- [ ] Import-target block present