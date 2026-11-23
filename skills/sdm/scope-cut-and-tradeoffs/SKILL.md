---
name: scope-cut-and-tradeoffs
description: Generate ranked keep/defer/cut options when capacity misses the date, each costed on customer value, risk, and milestones. Use when a plan does not fit.
role: sdm
status: built
created: 2026-11-22
---

# scope-cut-and-tradeoffs — ranked keep/defer/cut options

## What it produces

A decision artifact: ranked scope options across three moves — **Must-Ship for the milestone** /
**Defer to next sprint** / **Cut / de-scope** — each with its impact on customer value, technical
risk, and TPM milestones, plus the capacity arithmetic that made the cut necessary.

## RACI row

`Scope-cut options & costs` — **SDM A/R** (`shared/raci.md`); PMT C · TPM C · SDE C.

## Inputs required

- The current sprint commitment or milestone scope
- The capacity math that does not fit (from `sprint-planning-and-capacity` if run)
- What is fixed: the date, the milestone, or both
- Value ordering (PMT's priorities) where it exists

## Clarifying questions when inputs are missing

Ask up to 3, then draft with `[CONFIRM]`:

1. What is actually fixed — the date, the scope, or neither?
2. Which deferral quietly breaks a dependency downstream?
3. If only one thing ships, which one keeps the promise?

## Steps

1. **Pin the fixed constraint.** Date, milestone, or both — the whole artifact bends around
   it. Stated in the header, never implied.
2. **Restate the gap in capacity days.** From the sprint plan's arithmetic, or `[CONFIRM:
   gap]` if no plan was run. A cut made without the gap stated is a guess with scissors.
3. **Generate options in exactly three moves.** Must-Ship / Defer / Cut — every candidate
   item appears in exactly one. An item in two moves is a decision made twice, silently.
4. **Cost each option.** Per item: customer value (which AC or north-star it touches),
   technical risk (half-built states, stranded migrations, what a half-run change leaves in
   the data), milestone impact (which `M-n`/`DEP-n` moves, cross-checked with the roadmap).
5. **Rank by total damage, ascending.** State the ranking basis; a rank without its basis is
   a preference.
6. **Present the package.** The recommended set, what it costs, and what survives it —
   ending in the decision the user owns. The user decides; SDM prices.
7. **Read-back pass.** No silent cuts; no "small" trim that is not in a move; every moved item
   names all three costs or says which does not apply.
8. **Hand over.** Emit the artifact ending with its Import-target block. Answer questions.
   Wait.

## Output binding

`shared/output-schemas/sprint-plan-and-capacity.md` §commitment (options as bucket rows).

## Import target

Confluence — the decision log. Jira — the epic scope update.

## Worked example

`tests/sdm/scope-cut-and-tradeoffs/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
