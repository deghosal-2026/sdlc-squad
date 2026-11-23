---
name: pr-plan-and-rollback-notes
role: sde
status: planned
created: 2026-11-22
---

# pr-plan-and-rollback-notes — GitHub PR description

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A PR description artifact: implementation checklist (ordered), verification steps (commands and
expected outputs), migration/backfill order where relevant, and rollback/recovery steps —
formatted to paste straight into a GitHub PR body.

## Inputs required

- The change being PR'd (design/diff summary)
- The verification that proves it works (commands, fixtures, dashboards)
- Migration/backfill steps if data moves
- The rollback path (from the design's §Rollback if run)

## Clarifying questions when inputs are missing

- What command shows this works, and what does its output look like when it does?
- If this must be reverted after merge, what is the first step — and what does the revert *not*
  undo (data, flags, caches)?
- What is the reviewer's shortest path to confidence?

## Steps (to be written)

1. (build ticket) Draft the checklist in merge order → 2. Write verification with real
commands → 3. State migration order → 4. Copy the rollback branch verbatim from the design (or
`[CONFIRM]` it).

## Output binding

PR body follows `shared/system-conventions.md` Markdown rules; the verification table reuses
the `TC-n` rows of `shared/output-schemas/test-plan-and-cases.md`.

## Import target

GitHub — the Pull Request description.