# Fixture — sde/deploy-plan-and-release

Synthetic end to end.

## Input

> Launch: order-status self-serve. Flag `order_status_self_serve` (default
> off). Monitoring: queue-volume dashboard + web-latency dashboard + outbox
> alert exist [paste]. On-call: weekly rotation. Launch checklist (TPM)
> supplied. Migration 0431 pre-deploy, reversible.

## Expected artifact (skeleton)

# Deploy & release plan — order-status self-serve
## Deploy/release split
| deploys dark: router branch + handler redaction + 0431 | releases on flag flip |
## Pre-deploy gates
1) 0431 (verify: row-count parity; reversible: yes) 2) smoke: `smoke: checkout can
render guest status` 3) contract schema test green [CI].
## Rollout ladder
5% (24h bake — matched to outbox lag signal, the slowest that matters) → promote
criteria: zero 401-spike, p95 stable → 50% → 100%.
## Guardrails + triggers (automatic-first)
| 401-spike rate > [CONFIRM: threshold] | auto: flag to 0% | on-call notified |
| outbox lag > 5m | auto: flag hold | on-call paged |
| p95 latency > guardrail | auto: rollback to pre-deploy | [CONFIRM: threshold] |
## Flag ledger
| `order_status_self_serve` | owner [CONFIRM] | removal: +30d after 100% | both states tested [CONFIRM: evidence] |
## On-call runbook order
1) flag state 2) 401 dashboard 3) outbox alert 4) rollback steps — executable without the author.
## Post-promote
Checks: dashboard set, alert silenced false-positives reviewed, removal ticket filed.

## Checks

- [ ] Deploy vs release named per change
- [ ] Canary ladder has promote criteria + bake matched to the slowest signal
- [ ] Triggers automatic-first, executable by on-call, never the author
- [ ] Every flag has owner + removal date or is flagged as debt
- [ ] Smoke cases named by risk, not "test N"