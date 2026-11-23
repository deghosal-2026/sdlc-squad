---
name: scope-cut-and-tradeoffs
role: sdm
status: planned
created: 2026-11-22
---

# scope-cut-and-tradeoffs — ranked keep/defer/cut options

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A decision artifact: ranked scope options across three moves — **Must-Ship for the milestone** /
**Defer to next sprint** / **Cut / de-scope** — each with its impact on customer value, technical
risk, and TPM milestones, plus the capacity arithmetic that made the cut necessary.

## Inputs required

- The current sprint commitment or milestone scope
- The capacity math that does not fit (from `sprint-planning-and-capacity` if run)
- What is fixed: the date, the milestone, or both
- Value ordering (PMT's priorities) where it exists

## Clarifying questions when inputs are missing

- What is actually fixed — the date, the scope, or neither?
- Which deferral quietly breaks a dependency downstream?
- If only one thing ships, which one keeps the promise?

## RACI row

`Scope-cut options & costs` — **SDM A/R** (`shared/raci.md`); PMT C · TPM C · SDE C.

## Steps (to be written)

1. (build ticket) Restate the gap in capacity days → 2. Generate options per bucket → 3. Cost
each against value / risk / milestone → 4. Rank and present, decision left to the user.

## Output binding

`shared/output-schemas/sprint-plan-and-capacity.md` §commitment (options as bucket rows).

## Import target

Confluence — the decision log. Jira — the epic scope update.