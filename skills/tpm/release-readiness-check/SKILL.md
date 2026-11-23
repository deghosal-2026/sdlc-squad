---
name: release-readiness-check
description: Run a go/no-go launch checklist: flags, migrations, monitoring, rollback steps, support runbook, sign-offs.
role: tpm
status: built
created: 2026-11-22
---

# release-readiness-check — go/no-go launch checklist

## What it produces

A go/no-go checklist: feature flags (default state + flip plan), backfill/migration readiness
(order + verification), monitoring/alerts (queries or dashboard links), rollback steps
(ordered, named), support runbook status, and stakeholder sign-offs with owners and dates.

## RACI row

`Launch go/no-go checklist` — **TPM A/R** (`shared/raci.md`); PMT C · SDM C · SDE C.

## Inputs required

- The release's scope and its design/test artifacts
- Migration/backfill plan if any
- Current alerting/monitoring state (as the user reports it)
- Sign-off list (who must sign, and by when)

## Clarifying questions when inputs are missing

1. What is the last safe moment to abort, and who calls it?
2. If you flip the flag and metrics scream, what is the first undo step?
3. Who is paged if this breaks at 2am, from which runbook?

## Steps

1. **Pin the launch.** What ships, to whom, on what date, behind which flag. If the flag
   state is unknown, the checklist starts `[CONFIRM]` — a launch with no named flag is a
   checklist about a different launch.
2. **Enumerate the sections, every one.** Flags · Migrations/backfill · Monitoring/alerts ·
   Rollback · Support runbook · Comms · Sign-offs. A section with nothing in it says "none —
   <reason>", never silently missing.
3. **Flags.** Per flag: default state, flip plan (who, when, percentage), removal date, and
   both-states-tested evidence from the design's §Rollback/§Observability. Flag without a
   removal date = flagged in the checklist as debt.
4. **Migrations.** Order, verification per step (row-count / checksum / canary of the data),
   and reversibility stated. A migration with no verification is a hope with a SQL file.
5. **Monitoring.** Each launch metric: dashboard or query, threshold, and the alert that
   fires. "We'll watch it" is not monitoring.
6. **Rollback.** The ordered steps, copied from the design's §Rollback verbatim (or
   `[CONFIRM]`), with the last-safe-abort moment and who calls it.
7. **Support + comms.** Runbook link/status, who staffed the launch window, what customers
   are told, when.
8. **Sign-offs.** Name · role · what they sign for · by when. Verbal sign-offs are
   `[CONFIRM: verbal → written]` until they are written.
9. **Read-back pass.** No section skipped; every row has evidence or `[CONFIRM]`; the abort
   moment named.
10. **Hand over.** Emit the checklist ending with its Import-target block. Answer
    questions. Wait.

## Output binding

`shared/system-conventions.md` table rules; smoke/verification rows reuse the `TC-n` form
of `shared/output-schemas/test-plan-and-cases.md`.

## Import target

Confluence — the launch doc. Jira — the release ticket.

## Worked example

`tests/tpm/release-readiness-check/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
