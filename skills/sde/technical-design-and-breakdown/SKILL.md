---
name: technical-design-and-breakdown
role: sde
status: planned
created: 2026-11-22
---

# technical-design-and-breakdown — RFC section + Jira-ready sub-tasks

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.1.0 (core loop) per ROADMAP.

## What it produces

A technical design bound to `shared/output-schemas/technical-design-doc.md`: Affected
Modules/Services · Data Model & API/Contract Changes · Flow · Failure Modes & Edge Cases ·
Observability · Rollback — plus a Jira-ready sub-task table (`T-n`) with scope and Definition of
Done per task.

## Inputs required

- The requirement (PRD excerpt or story)
- Repository paths/files/services the change touches (paste or paths — unread code is `[CONFIRM]`)
- Existing contracts: API schemas, data models, event formats
- Known constraints: performance, compliance, cost

## Clarifying questions when inputs are missing

- Which modules does this touch — can you paste the paths, or shall I mark them `[CONFIRM]`?
- What breaks if this fails halfway — partial write, poison message, stuck flag?
- What does rollback mean here, step by step?

## RACI row

`Technical design & breakdown` — **SDE A/R** (`shared/raci.md`); PMT C · TPM I · SDM C.

## Steps (to be written)

1. (build ticket) Read/pin the affected code (quote what was read) → 2. Draft the contract
changes → 3. Enumerate failure modes with detection → 4. Write the rollback branch → 5.
Decompose into `T-n` tasks with DoDs.

## Output binding

`shared/output-schemas/technical-design-doc.md`.

## Import target

Confluence — RFC / tech design page. GitHub — the tracking issue. Jira — the sub-tasks.