# Fixture — sde/pr-plan-and-rollback-notes

Synthetic end to end.

## Input

> The design above. Verification: pytest suite (all green local, paste),
> contract schema test, playwright staging run. Migration 0431 runs
> pre-deploy. Flag `order_status_self_serve`, default off.

## Expected artifact (skeleton — GitHub PR body)

# PR: order-status self-serve (REQ-1)
## Implementation checklist (merge order)
- [ ] T-1 signed-link branch (`router.py`)
- [ ] T-2 redaction + 401 alert (`handler.py`, alerts/)
- [ ] migration 0431 pre-deploy
- [ ] flag default off
## Verification
1. `pytest services/checkout/status/` → all green [paste: 47 passed]
2. contract schema test → pass [CI job CONFIRM: name]
3. playwright staging: guest link renders redacted [steps]
## Migration / backfill order
0431 → row-count parity → deploy → dual-read window → flag flip.
## Rollback
1) flag off (instant) 2) dual-read off 3) reverse 0431 4) cache purge.
**Does not undo:** emails already sent with signed links.
## Out of scope
Carrier live chat (non-goal), translations (DEP-3).

## Checks

- [ ] Checklist in merge order, not authoring order
- [ ] Verification = real commands + expected outputs, no "should work"
- [ ] Migration order explicit; rollback copied from the design
- [ ] Rollback states what it does NOT undo
- [ ] Paste-ready: no HTML, no emoji, tables only where schemas allow