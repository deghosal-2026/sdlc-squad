# Fixture — tpm/release-readiness-check

Synthetic end to end.

## Input

> Release: order-status self-serve behind flag `order_status_self_serve`, default off.
> Migration 0431 (reversible). Dashboards: support queue volume, web latency. Alerts:
> outbox lag. Support runbook drafted, not published. Sign-offs: PMT, SDM, legal.

## Expected artifact (skeleton)

# Go/no-go — order-status self-serve, [CONFIRM: launch date]
| Flags | `order_status_self_serve` default off · flip plan: 5% → 50% → 100% · removal [CONFIRM: date] · both states tested [CONFIRM: evidence] |
| Migrations | 0431 · order: pre-deploy · verify: row-count parity · reversible: yes |
| Monitoring | queue-volume dashboard link [CONFIRM] · outbox-lag alert · guardrail: p95 latency |
| Rollback | flag off → dual-read window → 0431 reverse → cache purge; last-safe-abort: pre-100% |
| Support | runbook drafted — publish before launch (gap, listed) |
| Comms | customer email [CONFIRM: owner] |
| Sign-offs | PMT [CONFIRM: name] · SDM [CONFIRM] · legal — written pending [CONFIRM: date] |
Every section present; gaps named as gaps.

## Checks

- [ ] All seven sections present — empty ones say "none + reason"
- [ ] Flags: default + flip plan + removal date + both-states evidence
- [ ] Migrations: order + verification + reversibility
- [ ] Rollback copied from design or CONFIRM; abort moment named
- [ ] Sign-offs with owners and by-when; verbal marked pending-written