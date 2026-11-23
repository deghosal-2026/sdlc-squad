---
name: slice-mvp-and-stories
role: pmt
status: planned
created: 2026-11-22
---

# slice-mvp-and-stories — epic + vertically sliced stories

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

One epic + story set bound to `shared/output-schemas/jira-epic-and-stories.md`: epic summary
(value, metric), then vertical-slice stories — each with Summary, Type, Priority, Size, story
points or T-shirt, Description, Given/When/Then acceptance criteria, Dependencies.

## Inputs required

- A PRD or agreed goal (link or paste)
- The user's estimate scale, if any
- Known dependencies and the teams that own them

## Clarifying questions when inputs are missing

- What is the smallest slice a user would call valuable on its own?
- Which stories are enabled by others — and which only look ordered?
- What scale do you size in, and what is its legend?

## RACI row

`Epic & story slicing` — **PMT A/R** (`shared/raci.md`); TPM I · SDM C · SDE C.

## Steps (to be written)

1. (build ticket) Decompose into vertical slices → 2. Order by risk and value → 3. Write ACs
Given/When/Then → 4. CSV export on request.

## Output binding

`shared/output-schemas/jira-epic-and-stories.md`.

## Import target

Jira — bulk import / CSV, or paste each story block into its ticket description.