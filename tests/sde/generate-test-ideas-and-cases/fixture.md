# Fixture — sde/generate-test-ideas-and-cases

Synthetic end to end.

## Input

> Design above (REQ-1, FM-1, FM-2). Automation surface: pytest (unit),
> schema contract tests in CI, playwright (E2E), Grafana alerts. Constraint:
> no production E2E environment — staging only.

## Expected artifact (skeleton)

# Test plan — order-status self-service
> In scope: REQ-1, FM-1, FM-2 · Out: carrier integrations (staged stub)
## Matrix (layers all present)
| TC-1 | Unit | malformed ref → 400 | input: bad ref | automated: pytest |
| TC-2 | Unit | sig verify rejects forged [paste: sig fn] | automated: pytest |
| TC-3 | Integration | partial write → stale tolerated ≤5m | manual+alert: outbox lag |
| TC-4 | Contract | response matches schema; PII absent | automated: CI schema test |
| TC-5 | E2E | guest link renders status, redacted | playwright, staging |
| TC-6 | E2E | logged-in link renders PII (regression guard) | playwright |
| TC-7 | Failure injection | 401-spike (FM-1) → alert fires | manual: alert runbook |
| TC-8 | Non-functional | p95 status read ≤ guardrail | [CONFIRM: threshold] → perf job |
## REQ/AC trace: REQ-1→TC-1,5,6 · REQ-2→TC-4 · FM-1→TC-2,7 · FM-2→TC-3
## Coverage notes
- No prod E2E (env constraint): staging + synthetic carrier stub in CI.
- Load: not covered [CONFIRM: perf env] — reason stated, not silent.

## Checks

- [ ] All five layer headings present; empty ones say "none + reason"
- [ ] Every happy path shadowed by ≥ 1 failure row (or a stated reason)
- [ ] Injected faults named (not "failure occurs")
- [ ] Every case typed (automated/manual/review)
- [ ] REQ/AC trace present; uncovered items listed with reasons