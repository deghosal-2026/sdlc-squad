# Fixture — tpm/risk-raid-and-mitigations

Synthetic end to end.

## Input

> Program above. Known worries: Checkout's events API may not land before the
> freeze; the guest email template has a legal review step; assume the carrier
> payload format stays stable. Open issue: legal review not scheduled.

## Expected artifact (skeleton)

# RAID — order-status program
## Risks
| R1 | events API misses freeze window | likelihood M · impact H | signal: M1 ticket slips past Dec-1 | mitigation: M1 descoped to read-only status | fallback: manual support macro | owner [CONFIRM] |
## Assumptions
| A1 | carrier payload format stable | believed: yes | verify: Checkout [CONFIRM: who/by-when] |
## Issues
| I1 | legal review of guest email template not scheduled | already true | owner [CONFIRM] | next: schedule before M2 |
## Dependencies
| DEP-1 | (from roadmap) status events · Checkout | status in-conversation |
Sort: R1 first (M×H). Top rows carried to the next program status review.

## Checks

- [ ] Four tables; a two-nature row split into two rows
- [ ] Every risk: likelihood × impact + signal + mitigation + fallback + owner
- [ ] Every assumption: verification owner + by-when
- [ ] No adjectives defending ratings; no invented people/dates