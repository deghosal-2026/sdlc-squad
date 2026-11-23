---
name: sprint-planning-and-capacity
role: sdm
status: planned
created: 2026-11-22
---

# sprint-planning-and-capacity — net focus capacity + commitment

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.1.0 (core loop) per ROADMAP.

## What it produces

A sprint plan bound to `shared/output-schemas/sprint-plan-and-capacity.md`: a per-engineer
capacity table (Gross − PTO − meetings/ceremonies − on-call/support/toil = Net focus days), a
proposed commitment split into Carry-Over / Core-Milestone / Tech-Debt-Buffer, and flagged
risks (unestimated items, hidden dependencies, single-point-of-failure tasks, over-allocated
engineers).

## Inputs required

- Team roster
- Sprint length and dates
- PTO/holiday calendar
- On-call rotation and support/interrupt expectations
- Known incident/review overhead this sprint
- Carry-over items
- Candidate backlog items with estimates (or the request to flag them as unestimated)

## Clarifying questions when inputs are missing

- How many focus hours does each person actually lose to ceremonies and standing meetings?
- What carried over, and does it stay committed at its old size or re-estimate?
- Who is on-call, and is on-call load load-bearing this sprint?

## Steps (to be written)

1. (build ticket) Build the capacity table with all arithmetic shown → 2. Ring-fence carry-over →
3. Fit candidate items to net focus, flagging every unestimated one → 4. Split the commitment
into the three buckets → 5. Flag risks with their numbers.

## Output binding

`shared/output-schemas/sprint-plan-and-capacity.md`.

## Import target

Confluence — the sprint planning note. Jira — the sprint backlog after grooming.