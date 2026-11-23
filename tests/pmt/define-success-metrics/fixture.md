# Fixture — pmt/define-success-metrics

Synthetic end to end.

## Input

> Goal G1 from the PRD: order-status tickets −50% in 2 months (baseline 412/month).
> Existing dashboards: a support-queue volume dashboard and a web latency dashboard
> exist. Guardrail concern: tracking page p95 latency.

## Expected artifact (skeleton)

# Success metrics — order-status self-service
## North star
- `order_status_tickets / 1,000 orders` — baseline 412 tickets/month [CONFIRM: orders/month].
## Supporting
- `self_serve_status_views / 1,000 orders` (adoption → volume → outcome).
- `guest_status_link CTR` in the order email.
## Guardrails
- Tracking p95 latency — must not rise > [CONFIRM: threshold] (dashboard exists).
- Support CSAT on order-status macro threads.
## Instrumentation events
| event | fires when | exists? |
| `status_view` | guest status rendered | needs emitting [CONFIRM: owner] |
| `queue_tag` | ticket tagged `order-status` | exists (queue export) |
## Post-launch criteria
- Review at +8 weeks: tickets < 30% below baseline → iterate self-serve flow; else keep.
- Who calls it: [CONFIRM: name].

## Checks

- [ ] North star has its denominator stated
- [ ] No guardrail without a threshold (supplied or CONFIRM)
- [ ] Every event named with exists/needs-emitting
- [ ] Post-launch rule is a decision rule with a date, not a vibe
- [ ] No invented baselines