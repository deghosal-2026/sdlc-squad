---
name: sprint-planning-and-capacity
description: Plan a sprint from real capacity — per-engineer net-focus arithmetic shown, commitment split, flagged risks. Use when committing a team to a sprint.
role: sdm
status: built
created: 2026-11-22
---

# sprint-planning-and-capacity — net focus capacity + commitment

## What it produces

A sprint plan bound to `shared/output-schemas/sprint-plan-and-capacity.md`: a per-engineer
capacity table (Gross − PTO − Meetings/Ceremonies − On-call/Support/Toil = Net focus days,
arithmetic shown), a proposed commitment split into Carry-Over / Core-Milestone / Tech-Debt-
Buffer, and flagged risks.

## RACI row

`Sprint commitment (capacity-fit)` — **SDM A/R** (`shared/raci.md`); PMT I · TPM C · SDE C.

## Inputs required

- Team roster
- Sprint length and dates
- PTO/holiday calendar
- On-call rotation and support/interrupt expectations
- Known incident/review overhead this sprint
- Carry-over items
- Candidate backlog items with estimates (or the request to flag them as unestimated)

## Clarifying questions when inputs are missing

Ask up to 3, then build with `[CONFIRM]`:

1. How many focus hours does each person actually lose to ceremonies and standing meetings?
2. What carried over — and does it stay committed at its old size or re-estimate?
3. Is on-call load-bearing this sprint?

## Steps

1. **Build the capacity table.** One row per engineer: Gross days (sprint working days)
   − PTO − Meetings & ceremonies − On-call/support/toil = Net focus days. **Show every
   subtraction's input.** A cell with no traceable input is `[CONFIRM: input]`, never a
   guessed average.
2. **Sum the team's net focus.** State it. This is the ceiling — everything below it.
3. **Ring-fence carry-over first.** Carried items are committed at their old sizes, or
   explicitly re-estimated — stated either way, never silently resized.
4. **Fit the candidates.** Largest agreed value first (the backlog's own order, or PMT's
   `prioritize-asks` output). Stop at the ceiling. Committed total never exceeds net focus —
   padding capacity to fit a wish is the classic drift.
5. **Flag the unestimated.** Any candidate without a size appears in Flagged risks, not in
   the commitment.
6. **Split the buckets.** Carry-over / Core-milestone work / Debt-buffer, with the
   net-focus-days per bucket shown.
7. **Flag risks with numbers.** Over-allocated engineers (named, with their %), hidden
   dependencies, single-point-of-failure tasks (named engineer + task).
8. **Read-back pass.** Every cell traces; sums correct; no velocity claims without the
   team's own supplied history; over-allocation not smoothed.
9. **Hand over.** Emit the plan ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/output-schemas/sprint-plan-and-capacity.md`.

## Import target

Confluence — the sprint planning note. Jira — the sprint backlog after grooming.

## Worked example

`tests/sdm/sprint-planning-and-capacity/fixture.md` — full input + expected artifact
(synthetic). Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`. Condensed shape:

```markdown
Input: "6 engineers, 2-week sprint (10 working days). One on PTO Thu–Fri.
Ceremonies+meetings ~6h/wk each. Weekly on-call rotation. 3 stories carried over.
Candidates: order-status M1 (est. 8d), flaky-test fix (est. 2d)."

→ # Sprint 14 plan — Team [CONFIRM: name], 2026-12-07 → 2026-12-18
  ## Capacity — Eng A: 10 − 0 − 1.5 − 0.5 = 8 net focus days (PTO-row: Eng D 10−2−1.5−0.5=6)
  ## Commitment — Carry-over 3 stories [CONFIRM: sizes] · Core: M1 order-status · Debt: flaky fix
  ## Flagged risks — 1 candidate unestimated; Eng D at 10−... = 6d and M1-touching
  ## Import target — Confluence sprint note; Jira sprint backlog
```
