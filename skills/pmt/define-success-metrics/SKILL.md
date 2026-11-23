---
name: define-success-metrics
role: pmt
status: planned
created: 2026-11-22
---

# define-success-metrics — north star, guardrails, instrumentation

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A metrics block bound to `shared/output-schemas/confluence-prd-or-rfc.md` §Rollout & metrics:
north star metric, supporting metrics, guardrail metrics (what must not degrade), the
instrumentation events each needs, and post-launch evaluation criteria.

## Inputs required

- The outcome the feature serves (from the PRD)
- Existing dashboards/metrics the org already tracks
- Known guardrails: latency, cost, support load, trust

## Clarifying questions when inputs are missing

- If this shipped and nothing changed in any metric, which metric would you look at first?
- What must measurably *not* get worse?
- Which of these can you instrument from events you already emit?

## Steps (to be written)

1. (build ticket) Pick north star + guardrails → 2. Map each to an event/denominator → 3. State
the review date and the decision rule.

## Output binding

`shared/output-schemas/confluence-prd-or-rfc.md` §Rollout & metrics (PRD §8).

## Import target

Confluence — PRD §Rollout & metrics, or the launch-readiness doc.