---
name: deploy-plan-and-release
role: sde
status: planned
created: 2026-11-22
---

# deploy-plan-and-release — deploy plan + execution checklist

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A deploy and release plan: the deploy/release split (what ships dark behind a flag), the
rollout stages (canary percentages or cohorts), pre-deploy gates (migrations, smoke), the
guardrail metrics with thresholds and rollback triggers — automatic triggers preferred over
a human noticing — the flag ledger (owner + removal date per flag; a flag is a loan, not a
gift), the on-call runbook order, and the post-promote checks.

## RACI row

`Deploy plan & release execution` — **SDE A/R** (`shared/raci.md`); PMT I · TPM C · SDM C.

## Inputs required

- The design's rollback section and migration order
- The launch checklist (TPM), where one exists
- Monitoring/alerting state: which dashboards exist, which alerts fire
- The flag platform and its rollback mechanics
- On-call rotation: who can flip the flag at 2am

## Clarifying questions when inputs are missing

- What percentage starts the canary — and what promotes it?
- Which guardrail metric screams first — and what acts on it, automatically or human?
- What is each flag's removal date, and who owns it?

## Steps (to be written)

1. (build ticket) Deploy/release split → 2. Staged rollout with gates → 3. Rollback triggers,
automatic-first → 4. Flag ledger with removal dates → 5. On-call runbook → 6. Post-promote
checks.

## Output binding

`shared/system-conventions.md` table rules; smoke rows reuse the `TC-n` form of
`shared/output-schemas/test-plan-and-cases.md`.

## Import target

GitHub — the release issue / PR description. Confluence — the runbook page.