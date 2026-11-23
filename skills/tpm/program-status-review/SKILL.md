---
name: program-status-review
description: Produce the bi-weekly or monthly program status report — every item red/yellow/green against objectives or Jira milestones, with evidence. Use for recurring program reporting.
role: tpm
status: built
created: 2026-11-22
---

# program-status-review — R/Y/G status of all items

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

1. Which objectives or Jira milestones does this review report against?
2. What changed since the last review — and what did we promise then?
3. Which yellow needs a decision from this meeting, not just a glance?

## Steps

1. **Pin the cadence and window.** Review date, the period covered, and the objectives
   reported against. An item with no objective to roll up to is not in scope — say so.
2. **Table every item.** Per item: `M-n`/epic/`DEP-n`/`R-n` · owner (or `[CONFIRM]`) · status
   (R/Y/G per the fixed definitions above) · **evidence** (the fact that makes the status
   true — "M2 done 2026-12-11, tagged release-14") · delta since last review.
3. **Never status without evidence.** Every R/Y/G cell carries its evidence in the same row.
   A status with no evidence is written as `[CONFIRM: evidence]` and called out in the
   report's header — not smoothed to green.
4. **Deltas, not a re-run.** What changed since the last report: items that moved status,
   new items, items closed. A report that re-states last month with no deltas says so in
   its header.
5. **Write the asks.** The decisions this review must make, each with its owner and the
   cost of not deciding ("yellow M2 → needs the staff call by Fri or M3 slips").
6. **Roll up honestly.** An overall program status exists only if the org's convention asks
   for one — and it is never greener than its reddest critical-path item.
7. **Read-back pass.** Every status has evidence; every delta traces to the last report or
   `[CONFIRM]`; every ask has an owner and a by-when.
8. **Hand over.** Emit the report ending with its Import-target block. Answer questions.
   Wait.

## Output binding

`shared/system-conventions.md` table rules; `R-n`/`DEP-n` prefixes for risk/dependency rows.

## Import target

Confluence — the program status page; the review itself runs from it.

## Worked example

`tests/tpm/program-status-review/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
