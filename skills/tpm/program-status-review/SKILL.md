---
name: program-status-review
role: tpm
status: planned
created: 2026-11-22
---

# program-status-review — R/Y/G status of all items

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A program status report for the review cadence — bi-weekly or monthly, as the org runs it:
every item in scope (epics, milestones, dependencies, open risks) with a Red/Yellow/Green
status against its objective or Jira milestone, the evidence behind each status, deltas since
the last review, and the asks this review must answer.

## RACI row

`Program status review (bi-weekly/monthly, R/Y/G)` — **TPM A/R** (`shared/raci.md`); PMT I ·
SDM C · SDE I.

## Status definitions (fixed, not vibes)

- **Green** — on track against the baseline: milestone met, or no slip to the date.
- **Yellow** — a named risk to date or scope exists; mitigation open, owner assigned.
- **Red** — a milestone is missed, or no credible path to it exists today.

A status without its evidence is a placeholder, and the report says so.

## Inputs required

- The cadence (bi-weekly or monthly) and the review date
- Item statuses: a Jira milestones/epics paste or export
- The objectives each item rolls up to
- The last review's report (for deltas)
- RAID changes since then

## Clarifying questions when inputs are missing

- Which objectives or Jira milestones does this review report against?
- What changed since the last review — and what did we promise then?
- Which yellow needs a decision from this meeting, not just a glance?

## Steps (to be written)

1. (build ticket) Pin cadence + objectives → 2. Table every item with status + evidence →
3. Mark deltas since last review → 4. Write the asks → 5. Read-back: no status without
evidence; no green without a check.

## Output binding

`shared/system-conventions.md` table rules; `R-n`/`DEP-n` prefixes for risk/dependency rows.

## Import target

Confluence — the program status page; the review itself runs from it.