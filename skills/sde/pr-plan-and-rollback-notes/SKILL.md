---
name: pr-plan-and-rollback-notes
description: Write a GitHub PR description: merge-order checklist, verification commands with expected outputs, migration order, rollback with its limits.
role: sde
status: built
created: 2026-11-22
---

# pr-plan-and-rollback-notes — GitHub PR description

## What it produces

A PR description artifact: implementation checklist (ordered), verification steps (commands and
expected outputs), migration/backfill order where relevant, and rollback/recovery steps —
formatted to paste straight into a GitHub PR body.

## RACI row

`PR description & rollback notes` — **SDE A/R** (`shared/raci.md`); PMT — · TPM C · SDM I.

## Inputs required

- The change being PR'd (design/diff summary)
- The verification that proves it works (commands, fixtures, dashboards)
- Migration/backfill steps if data moves
- The rollback path (from the design's §Rollback if run)

## Clarifying questions when inputs are missing

1. What command shows this works, and what does its output look like when it does?
2. If this must be reverted after merge, what is the first step — and what does the revert
   *not* undo (data, flags, caches)?
3. What is the reviewer's shortest path to confidence?

## Steps

1. **Pin the change.** One line: what this PR does, which `REQ-n`/`T-n` it serves. A PR
   serving two concerns is two PRs — flagged here if so.
2. **Write the checklist in merge order,** not authoring order: migrations → code → flags →
   tests. Each item is a `T-n` from the design, checked off only as merged.
3. **Verification = real commands + expected outputs.** "Should work" is not verification.
   Each step: command, what its output looks like when the change is good (from the paste,
   or `[CONFIRM: expected output]`), and where it runs (local/CI/staging).
4. **Migration/backfill order.** If data moves: the order, the verification per step
   (row-count/checksum), and reversibility — copied from the design, never re-derived here.
   No data movement → the section says so.
5. **Rollback, copied verbatim from the design's §Rollback** (or `[CONFIRM]` if no design
   was run). Ordered, named steps — plus **what rollback does not undo**: emails sent, events
   emitted, external reads. That line is required; its absence is the classic drift.
6. **Out-of-scope block.** What this PR deliberately does not contain, so the reviewer knows
   the boundary without asking.
7. **Read-back pass.** Checklist merge-ordered; every verification a runnable command; rollback
   names its limits; paste-clean (no HTML, no emoji, tables only where schemas allow).
8. **Hand over.** Emit the description ending with its Import-target block. Answer questions.
   Wait.

## Output binding

PR body follows `shared/system-conventions.md` Markdown rules; the verification table reuses
the `TC-n` rows of `shared/output-schemas/test-plan-and-cases.md`.

## Import target

GitHub — the Pull Request description.

## Worked example

`tests/sde/pr-plan-and-rollback-notes/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
