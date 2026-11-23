---
name: operational-health-review
role: sdm
status: planned
created: 2026-11-22
---

# operational-health-review — ops health summary + remediation tickets

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

An ops-health artifact: recurring bugs, toil hotspots, flaky tests, and review bottlenecks —
each with its evidence (counts, examples, timestamps as supplied), its capacity cost story, and
recommended remediation tickets ready for an upcoming sprint.

## Inputs required

- Bug/ticket history for the period (exported list or pasted rows)
- Flaky-test evidence (runs, failure counts)
- Interrupt/support log or recollection
- Review turnaround observations (as measured, not as felt)

## Clarifying questions when inputs are missing

- Which of these recurs — same signature, or same person paged?
- How many engineer-hours did this toil cost, and how did you count it?
- Which flaky test last blocked a merge, and how often?

## RACI row

`Operational health review & remediation tickets` — **SDM A/R** (`shared/raci.md`); PMT I ·
TPM C · SDE C.

## Steps (to be written)

1. (build ticket) Cluster the evidence by hotspot → 2. Quantify with supplied numbers only →
3. Draft remediation tickets with DoD → 4. Size their capacity cost for the next sprint plan.

## Output binding

Summary tables follow `shared/system-conventions.md`; remediation tickets follow the
`T-n` task rows of `shared/output-schemas/technical-design-doc.md`.

## Import target

Confluence — the team retro/ops doc. Jira — the maintenance tickets.