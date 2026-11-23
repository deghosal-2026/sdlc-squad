# Fixture — sdm/scope-cut-and-tradeoffs

Synthetic end to end.

## Input

> From the Sprint 14 plan: capacity gap of 3 days vs. the candidate list
> (M1 8d + flaky fix 2d + carrier deep-link 4d + dark mode unknown). Fixed: the
> launch date (freeze-adjacent). Value order from PMT: M1 first.

## Expected artifact (skeleton)

# Scope decision — Sprint 14, gap = 3 days [arithmetic from plan]
## Fixed: the date (freeze-adjacent). Everything else moves.
## Moves
| Move | Item | Customer value | Technical risk | Milestone impact |
| Must-Ship | order-status M1 | G1 tickets −50% | outbox partial-write (mitigated in design) | M1→M3 chain |
| Defer | carrier deep-link | 3 tickets/mo [paste] | low — additive | none (not on critical path) |
| Defer | flaky-test fix | none direct | flake tax continues (priced 0.5d/mo) | none |
| Cut | dark mode | 1 sales ask | none | none |
## Ranking basis: total damage ascending; M1 untouchable (dependency root).
## Package: defer 2 items (deep-link, flake fix → debt-buffer next sprint), cut dark mode.
## Decision: [user's]. This artifact prices; it does not decide.

## Checks

- [ ] Gap stated in capacity days, traced
- [ ] Every item in exactly one move
- [ ] Each move names all three costs (or "does not apply" + why)
- [ ] Ranking basis stated
- [ ] No silent trims