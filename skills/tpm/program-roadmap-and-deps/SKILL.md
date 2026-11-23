---
name: program-roadmap-and-deps
role: tpm
status: planned
created: 2026-11-22
---

# program-roadmap-and-deps — program plan + dependency graph

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.1.0 (core loop) per ROADMAP.

## What it produces

A program plan bound to a roadmap table set: phases/milestones with dates and slack,
cross-team dependency table (Upstream/Downstream Team, Dependency Type, Target Date, Status,
Owner), and critical-path callouts naming the chain.

## Inputs required

- The initiative's PRDs/designs (link or paste)
- Participating teams and their calendars/PTO windows
- Known dependencies, with owners and dates where they exist

## Clarifying questions when inputs are missing

- Which teams must move before your first milestone — and who owns each move?
- What is the slack on each link in the critical chain?
- Which dependency is a wish (no owner, no date) today?

## RACI row

`Program roadmap & milestone sequence` + `Cross-team dependency commitments` — **TPM A/R** on
both (`shared/raci.md`); one skill, two rows.

## Steps (to be written)

1. (build ticket) Enumerate milestones → 2. Build the dependency table → 3. Trace the critical
path → 4. Flag zero-slack links and ownerless rows.

## Output binding

Roadmap tables follow `shared/output-schemas/confluence-prd-or-rfc.md` table standards; the
dependency table follows the ID/column rules in `shared/system-conventions.md`.

## Import target

Confluence — program page. Jira — dependency links on the epic issues.