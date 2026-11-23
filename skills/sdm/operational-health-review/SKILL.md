---
name: operational-health-review
description: Review ops health from pasted evidence: recurring bugs, toil, flaky tests, review bottlenecks; remediation tickets with DoDs.
role: sdm
status: built
created: 2026-11-22
---

# operational-health-review — ops health summary + remediation tickets

## What it produces

An ops-health artifact: recurring bugs, toil hotspots, flaky tests, and review bottlenecks —
each with its evidence (counts, examples, timestamps as supplied), its capacity cost, and
recommended remediation tickets ready for an upcoming sprint.

## RACI row

`Operational health review & remediation tickets` — **SDM A/R** (`shared/raci.md`); PMT I ·
TPM C · SDE C.

## Inputs required

- Bug/ticket history for the period (exported list or pasted rows)
- Flaky-test evidence (runs, failure counts)
- Interrupt/support log or recollection
- Review turnaround observations (as measured, not as felt)

## Clarifying questions when inputs are missing

Ask up to 3, then run with `[CONFIRM]`:

1. Which of these recurs — same signature, or same person paged?
2. How many engineer-hours did this toil cost, and how was it counted?
3. Which flaky test last blocked a merge, and how often?

## Steps

1. **Pin the period and the evidence.** Which weeks, which exports pasted. Every number
   below traces to a paste or is `[CONFIRM]`.
2. **Cluster recurring bugs by signature.** Same error, same path, same page — one cluster
   with a count. Two bugs that share nothing but a day are two clusters.
3. **Quantify toil.** Hours × frequency, arithmetic shown, from supplied numbers only.
   Toil is capacity stolen from features; the artifact says how much, in days.
4. **Name the flaky tests.** Each with failure count and the last merge it blocked (from the
   paste). A flaky test is a false alarm tax — priced like one.
5. **Measure the review bottleneck.** Turnaround as measured (timestamps from the paste),
   not as felt. If unmeasured, the row says `[CONFIRM: unmeasured]` and proposes the
   measurement first.
6. **Rank hotspots by capacity stolen**, descending — the review's own priority order.
7. **Draft remediation tickets.** `T-n` rows: scope, DoD observable by someone else, and the
   sprint bucket they enter (the debt-buffer, via `sprint-planning-and-capacity`).
8. **Read-back pass.** Every count traced; every ticket has owner-or-CONFIRM + DoD; no blame
   — hotspots, never culprits.
9. **Hand over.** Emit the review ending with its Import-target block. Answer questions.
   Wait.

## Output binding

`shared/system-conventions.md` table rules; remediation tickets follow the `T-n` task rows
of `shared/output-schemas/technical-design-doc.md`.

## Import target

Confluence — the team retro/ops doc. Jira — the maintenance tickets.

## Worked example

`tests/sdm/operational-health-review/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
