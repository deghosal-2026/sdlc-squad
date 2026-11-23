---
name: sprint-retro
description: Run a retrospective from the last two sprints' done-ticket exports — went-well, hurt, and change with receipts, plus action items. Use at the end of a sprint.
role: sdm
status: built
created: 2026-11-22
---

# sprint-retro — last 2 sprints' done tickets → retro + action items

## What it produces

A retrospective bound to the sprint-plan table rules: what went well / what hurt / what we
change — **grounded in the last two sprints' completed tickets** (past), plus action items as
`T-n` remediation tickets with owners and DoD that feed the next sprint plan (future).

## RACI row

`Sprint retrospective & action items` — **SDM A/R** (`shared/raci.md`); PMT C · TPM I · SDE C.

## Inputs required

- The last 2 sprints' **done** tickets (paste or export from Jira) — ticket ID, summary, size,
  sprint, and reopen/escaped-defect flags where the export carries them
- The 2 sprint plans (commitments) those tickets landed against, if available
- Who was on-call / what interrupted, if the team tracked it

## Clarifying questions when inputs are missing

Ask up to 3, then run with `[CONFIRM]`:

1. May I have the done-ticket export for the last two sprints — ID, summary, size, sprint?
2. Which completions slipped into the next sprint (carry-over history), if the export shows it?
3. What interrupted the team that neither sprint plan predicted?

## Steps

1. **Pin the retro window.** Name the two sprints (numbers + dates). Everything in the retro
   cites a ticket from inside this window, or it is an opinion — say which.
2. **Read the tickets.** Cluster the pasted done tickets: by epic/theme, by size, by reopen
   or escaped-defect flag. Counts come from the paste, never estimated.
3. **State what the data shows.** Completion vs. commitment per sprint (from the plans, if
   supplied); carry-over count at each boundary; reopen rate; the biggest and smallest items
   shipped. Numbers first, narrative after — every number traceable to the paste.
4. **What went well — with receipts.** Each item names the tickets behind it ("flag flip with
   zero rollbacks — SPR-210, SPR-211"). No praise without a pasted ticket.
5. **What hurt — with receipts.** Same discipline: interruptions, reopen clusters, items that
   slipped twice, unplanned work the export shows. No blame — history is input, not verdict.
6. **What we change.** Each change maps to a hurt item it addresses, and lands as a `T-n`
   action item: owner (real name or `[CONFIRM]`), DoD observable by someone else, and the
   sprint it enters (next debt-buffer bucket, via `sprint-planning-and-capacity`).
7. **Carry-over disposition.** Anything still open from these two sprints is named here —
   re-committed, deferred with reason, or dropped with reason — never silently left.
8. **Read-back pass.** Every count traces to a paste; every action item has owner + DoD +
   destination sprint; no invented tickets, names, or dates.
9. **Hand over.** Emit the retro ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/system-conventions.md` table rules; `T-n` rows per
`shared/output-schemas/technical-design-doc.md`.

## Import target

Confluence — the team retro page. Jira — the `T-n` action items as tickets.

## Worked example

`tests/sdm/sprint-retro/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
