---
name: deploy-plan-and-release
description: Write a deploy and release plan — deploy/release split, canary ladder with promote criteria, automatic-first rollback triggers, flag ledger. Use when a change is ready to ship.
role: sde
status: built
created: 2026-11-22
---

# deploy-plan-and-release — deploy plan + execution checklist

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

Ask up to 3, then draft with `[CONFIRM]`:

1. What percentage starts the canary — and what promotes it?
2. Which guardrail metric screams first — and what acts on it, automatically or human?
3. What is each flag's removal date, and who owns it?

## Steps

1. **Split deploy from release.** What ships in the deploy dark behind a flag; what the flag
   exposes. Deploy ≠ release — the artifact states which is which for every change.
2. **Order the pre-deploy gates.** Migrations in dependency order, each with its
   verification (row-count/checksum) and reversibility; smoke set for the canary target,
   named by risk (`smoke: checkout can start payment`, not `test 14`).
3. **Stage the rollout.** Canary percentage/cohort ladder with promote criteria between
   stages — bake time matched to the slowest signal that matters, not the fastest.
4. **Wire the rollback triggers.** Per guardrail metric: threshold, what acts, automatic
   preferred — a canary that needs a human to notice has traded a fast failure for a slow
   one. Every trigger executable by whoever is on call, without the author.
5. **Write the flag ledger.** Per flag: owner, removal date, both-states-tested evidence.
   A flag with no removal date is flagged in the plan as debt.
6. **Order the on-call runbook.** What is checked, in what order, with the links, by the
   person paged at 2am who did not write the feature.
7. **Post-promote checks.** What the promoted state must show, and the flag-removal
   reminder with its date.
8. **Read-back pass.** Every stage has criteria; every trigger has an executor; every flag
   an owner and a date; nothing requires the author at 2am.
9. **Hand over.** Emit the plan ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/system-conventions.md` table rules; smoke rows reuse the `TC-n` form of
`shared/output-schemas/test-plan-and-cases.md`.

## Import target

GitHub — the release issue / PR description. Confluence — the runbook page.

## Worked example

`tests/sde/deploy-plan-and-release/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
