---
name: define-success-metrics
description: Define north-star, supporting, and guardrail metrics with the instrumentation events each needs. Use when a product goal needs measurable success and guardrails.
role: pmt
status: built
created: 2026-11-22
---

# define-success-metrics — north star, guardrails, instrumentation

## What it produces

A metrics block bound to `shared/output-schemas/confluence-prd-or-rfc.md` §Rollout & metrics:
north star metric, supporting metrics, guardrail metrics (what must not degrade), the
instrumentation events each needs, and post-launch evaluation criteria.

## RACI row

`Success metrics & guardrails` — **PMT A/R** (`shared/raci.md`); TPM C · SDM I · SDE C.

## Inputs required

- The outcome the feature serves (from the PRD)
- Existing dashboards/metrics the org already tracks
- Known guardrails: latency, cost, support load, trust

## Clarifying questions when inputs are missing

1. If this shipped and nothing changed in any metric, which would you look at first?
2. What must measurably *not* get worse?
3. Which of these can you instrument from events you already emit?

## Steps

1. **Pin the outcome.** Restate the PRD goal the metric serves — a metric without an outcome
   behind it is a vanity number waiting to happen.
2. **Pick the north star.** One metric, its denominator stated ("status tickets per 1,000
   orders", not bare counts), its baseline `[CONFIRM: baseline]` if not supplied.
3. **Supporting metrics.** ≤ 3, each named with the north-star relationship it explains
   (adoption → volume → outcome). Same denominators rule.
4. **Guardrails.** What must not degrade: latency, error rate, cost, support load, trust
   signals. Each with a threshold the user supplies or `[CONFIRM: threshold]` — a guardrail
   with no threshold is a hope.
5. **Instrumentation events.** Per metric: the event name, when it fires, what it carries,
   whether it exists today or needs emitting. This table is the SDE handoff — the design doc's
   observability section starts here.
6. **Post-launch criteria.** The review date, the decision rule ("if status tickets < 30%
   below baseline after 8 weeks → iterate on the self-serve flow"), and who calls it.
7. **Read-back pass.** No metric without its denominator; no guardrail without a threshold;
   no invented baselines; events named for existence-check.
8. **Hand over.** Emit the block ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/output-schemas/confluence-prd-or-rfc.md` §Rollout & metrics.

## Import target

Confluence — PRD §Rollout & metrics, or the launch-readiness doc.

## Worked example

`tests/pmt/define-success-metrics/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
