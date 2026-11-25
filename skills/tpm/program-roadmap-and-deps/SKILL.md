---
name: program-roadmap-and-deps
description: Build a program roadmap — milestones, a cross-team dependency table, the critical path named end to end, and slack per link. Use when multiple teams must be sequenced.
role: tpm
status: built
created: 2026-11-22
---

# program-roadmap-and-deps — program plan + dependency graph

## What it produces

A program plan bound to `shared/output-schemas/program-roadmap.md`: a **Milestones** table, a
**Dependencies** table (`DEP-n` · depends on · owning team · needed by · slack · notes), the
**critical path** named end to end, and the top **program risks**.

## RACI row

`Program roadmap & milestone sequence` + `Cross-team dependency commitments` — **TPM A/R** on
both (`shared/raci.md`); one skill, two rows.

## Inputs required

- The initiative's PRDs/designs (link or paste)
- Participating teams and their calendars/PTO windows/freeze dates
- Known dependencies, with owners and dates where they exist

## Clarifying questions when inputs are missing

Ask up to 3, then draft with `[CONFIRM]`:

1. Which teams must move before the first milestone — and who owns each move?
2. What is the slack on each link in the critical chain?
3. Which dependency is a wish today (no owner, no date)?

## Steps

1. **Pin the initiative.** Name it from the PRD; list participating teams. If teams are
   unknown, ask before drafting — the whole artifact is team-shaped.
2. **Enumerate milestones.** `M-n` from the PRD's phasing, each with: definition of done for
   the milestone, target date, and the team that owns the date. A date with no team behind it
   is `[CONFIRM: date from <team>]`.
3. **Build the dependency table.** `DEP-n`: what · from (team, named owner or `[CONFIRM]`) ·
   blocks (which `M-n`) · target date · status (`agreed / in-conversation / not-started`).
   Every row an owner or `[CONFIRM]`; "TBD" is not a status.
4. **Trace the critical path.** The longest dependent chain through the milestones. Name it
   end to end (`M1 → M2 → M3`), and say what it blocks.
5. **Compute slack per link.** For each milestone: days between its earliest-possible finish
   and its target. Zero-slack links are flagged in the plan, every time — silently accepting
   zero slack is the classic drift.
6. **Cross-check against risks.** Open risks that touch the path become `R-n` rows
   (`risk-raid-and-mitigations` is the full skill); the roadmap carries the top ones with
   their early-warning signals.
7. **Read-back pass.** No date without a team behind it; every `DEP` has an owner; every
   zero-slack link called out; no invented team names or calendar facts.
8. **Hand over.** Emit the roadmap artifact ending with its Import-target block. Answer
   questions. Wait.

## Output binding

`shared/output-schemas/program-roadmap.md` — verbatim structure, all rules. This page **owns**
the milestones and the `DEP-n` IDs; the PRD and downstream artifacts reference them.

## Import target

Confluence — the program page. Jira — dependency links on the epic issues.

## Worked example

`tests/tpm/program-roadmap-and-deps/fixture.md` — full input + expected artifact (synthetic:
the same order-status initiative). Recorded run:
`tests/results/run-2026-11-22-v0.1.0.md`. Condensed shape:

```markdown
Input: "PRD accepted. Checkout owns status events, Notifications owns the guest
email template. Launch before the Dec-15 freeze."

→ # Program: order-status self-service
  ## Milestones — M1 status events (Checkout, [CONFIRM: date]) → M2 guest email
     template (Notifications, [CONFIRM: date]) → M3 launch ([CONFIRM: freeze-adjacent])
  ## Dependencies — DEP-1 status events · from Checkout · blocks M2 · owner [CONFIRM]
  ## Critical path — M1 → M2 → M3; zero-slack link M2 → M3 — flagged
  ## Import target — Confluence program page; Jira dependency links
```
