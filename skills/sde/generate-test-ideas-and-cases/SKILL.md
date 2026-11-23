---
name: generate-test-ideas-and-cases
description: Build a layered test matrix — unit, integration, contract, E2E, failure injection — with a requirement trace and coverage notes. Use when a design needs a test plan.
role: sde
status: built
created: 2026-11-22
---

# generate-test-ideas-and-cases — layered test matrix

## What it produces

A test plan bound to `shared/output-schemas/test-plan-and-cases.md`: a test matrix by layer —
Unit · Integration · Contract/API · End-to-End/Smoke · Non-Functional/Failure Injection — with
Scenario, Preconditions/Input, Expected Result, and Verification type per case, plus coverage
notes stating what is deliberately not covered.

## RACI row

`Test plan & cases` — **SDE A/R** (`shared/raci.md`); PMT I · TPM I · SDM C.

## Inputs required

- The feature/design being tested (paste or link)
- The failure modes worth inducing (from the design's §Failure Modes if run)
- The automation surface that exists: test frameworks, CI jobs
- Environment constraints (what cannot be tested end-to-end, and why)

## Clarifying questions when inputs are missing

Ask up to 3, then draft with `[CONFIRM]`:

1. Which layer does your team trust for regression today?
2. What breaks loudly — and what breaks silently, and which layer catches silence?
3. What is too expensive/flaky to automate — and may it be listed as manual?

## Steps

1. **Pin the scope.** Feature + design revision + what is explicitly out of test (with the
   reason — cost, flake, environment).
2. **Enumerate per layer.** Rows in the fixed layers — Unit, Integration, Contract/API,
   E2E/Smoke, Non-Functional/Failure Injection. Every layer heading appears even when empty:
   "none — <reason>", never a silent gap.
3. **Happy paths first, then their shadows.** Every happy-path `TC-n` implies at least one
   failure-path row, or a stated reason why not. Negative paths are not optional.
4. **Name the injected fault.** Failure-injection cases name the fault: timeout, 5xx,
   partial write, poison message, flag flipped mid-read. "Failure occurs" is not a case.
5. **Assign verification.** Automated (framework + job) / manual (steps) / review (who).
   Each case states its type — "hopefully" is not a type.
6. **Trace to requirements.** Every `REQ-n`/`AC-n` from the input maps to ≥ 1 `TC-n`, or is
   listed in coverage notes as uncovered (with the reason).
7. **Coverage notes.** What is not covered and why: cost, flake risk, environment. Silence
   here is the failure mode.
8. **Read-back pass.** Layers all present; every happy path shadowed or excused; every case
   typed; no case asserting a number the inputs never supplied.
9. **Hand over.** Emit the matrix ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/output-schemas/test-plan-and-cases.md`.

## Import target

Jira — the QA/test checklist. GitHub — the PR test plan / issue body. Confluence — the test
spec page.

## Worked example

`tests/sde/generate-test-ideas-and-cases/fixture.md` — full input + expected artifact
(synthetic). Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`. Condensed shape:

```markdown
Input: "Design: GET /status/{order_ref}, signed link, no PII unauthenticated.
Unit: pytest. Contract: schema tests in CI. E2E: playwright. Alerts: Grafana."

→ # Test plan — order-status self-service
  ## Matrix — TC-1 Unit: ref parse rejects malformed → 400 [automated]
     TC-4 Contract: response matches schema, PII absent [automated]
     TC-7 E2E: guest link → status renders [playwright]
     TC-9 Failure injection: outbox poison → stale-state alert fires [manual+alert]
  ## Coverage notes — no prod E2E (env): carrier stub in CI instead
  ## Import target — Jira QA checklist; PR test plan; Confluence spec
```
