---
name: release-readiness-check
role: tpm
status: planned
created: 2026-11-22
---

# release-readiness-check — go/no-go launch checklist

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A go/no-go checklist: feature flags (default state + flip plan), backfill/migration readiness
(order + verification), monitoring/alerts (queries or dashboard links), rollback steps
(ordered, named), support runbook status, and stakeholder sign-offs with owners and dates.

## Inputs required

- The release's scope and its design/test artifacts
- Migration/backfill plan if any
- Current alerting/monitoring state (as the user reports it)
- Sign-off list (who must sign, and by when)

## Clarifying questions when inputs are missing

- What is the last safe moment to abort, and who calls it?
- If you flip the flag and metrics scream, what is the first undo step?
- Who is paged if this breaks at 2am, from which runbook?

## RACI row

`Launch go/no-go checklist` — **TPM A/R** (`shared/raci.md`); PMT C · SDM C · SDE C.

## Steps (to be written)

1. (build ticket) Enumerate checklist sections → 2. Pair each item with its evidence or
`[CONFIRM]` → 3. Draft the abort/rollback branch → 4. Collect sign-off rows.

## Output binding

Checklist tables follow `shared/system-conventions.md` column rules; the test rows reuse
`shared/output-schemas/test-plan-and-cases.md` layer names.

## Import target

Confluence — the launch doc. Jira — the release ticket.