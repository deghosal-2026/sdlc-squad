# Fixture — sde/technical-design-and-breakdown

Synthetic end to end. Pasted code excerpts, fictional paths.

## Input

> REQ-1: status via signed link, no login. Paths pasted:
> `services/checkout/status/router.py` (route: `/status/{order_ref}`,
> session-gated), `services/checkout/status/handler.py` (renders PII when
> session present), `migrations/0431_add_state.sql` (reversible).

## Expected artifact (skeleton)

# Design: order-status self-service
> Draft · [CONFIRM: author] · 2026-11-22
## Affected modules (claims quote the paste)
| `router.py` | add signed-link branch | risk: auth-bypass (→ FM-1) |
| `handler.py` | PII redact unauthenticated | risk: leak (→ FM-2) |
## Contract
`GET /status/{order_ref}?sig=…` → 200 `{state, eta, packages[]}` — **no PII unauthenticated**;
breaking change: none (additive branch).
## Flow
1) guest opens signed link → 2) router verifies sig → 3) handler renders redacted view.
## Failure modes
| FM-1 | forged sig | 401 + rate-limit | detection: 401-spike alert |
| FM-2 | partial write → stale state | stale reads tolerated ≤ 5 min | detection: outbox-lag alert |
## Observability
`status_view` event (needs emitting) · 401-rate dashboard · outbox-lag alert [CONFIRM: link]
## Rollback
1) flag off 2) dual-read window 3) reverse 0431 4) cache purge — does NOT undo: emails sent.
## Sub-tasks
| T-1 | signed-link branch in router | DoD: curl without session → 200 redacted | — |
| T-2 | redaction + 401 alert | DoD: PII assertion in tests | T-1 |
## Import target
Confluence RFC; GitHub issue; Jira sub-tasks.

## Checks

- [ ] Every existing-code claim carries a quoted line or CONFIRM
- [ ] Breaking changes named as breaking
- [ ] Every FM has a detection path
- [ ] Rollback ordered + says what it does NOT undo
- [ ] Every T has a DoD someone else can check