---
name: design-and-code-reviews
role: sde
status: planned
created: 2026-11-22
---

# design-and-code-reviews — author + reviewer checklists

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

Two checklists and an etiquette page: the **author-side** pre-open gate (split into small
reviewable diffs; self-review before anyone else sees it; a description a stranger can follow;
both flag states verified; tests green) and the **reviewer-side** pass (design fit, correctness,
tests, complexity, naming, security — in that order), plus the etiquette: nits labeled
`nit:`, praise named, polish never blocks, and every "I don't understand this" becomes a
comment instead of a guess.

## RACI row

`Design & code reviews` — **SDE A/R** (`shared/raci.md`); PMT I · TPM I · SDM C.

## Inputs required

- The diff/PR paste or paths (unread code is `[CONFIRM]`)
- The design doc the change implements
- The team's review standards, if any exist (CODEOWNERS, size limits, turnaround norms)

## Clarifying questions when inputs are missing

- How large is too large here — files, lines, or review-hours?
- Who must review (CODEOWNERS), and who merely may?
- What is this team's nit threshold — and who approves the style call?

## Steps (to be written)

1. (build ticket) Author checklist → 2. Reviewer checklist scoped to the diff → 3. Etiquette +
turnaround expectations → 4. Read-back: nothing in either checklist a stranger could not
follow.

## Output binding

`shared/system-conventions.md` table rules.

## Import target

GitHub — the PR template / review guide. Confluence — the team review-standards page.