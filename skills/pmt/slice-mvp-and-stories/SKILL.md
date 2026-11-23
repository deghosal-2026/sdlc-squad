---
name: slice-mvp-and-stories
description: Slice an accepted PRD into a Jira-ready epic plus vertically sliced user stories with Given/When/Then acceptance criteria. Use when requirements are agreed and work must be planned.
role: pmt
status: built
created: 2026-11-22
---

# slice-mvp-and-stories — epic + vertically sliced stories

## What it produces

One epic + story set bound to `shared/output-schemas/jira-epic-and-stories.md`: epic summary
(value, metric), then vertical-slice stories — each with Summary, Type, Priority, Size, story
points or T-shirt, Description, Given/When/Then acceptance criteria, Dependencies.

## RACI row

`Epic & story slicing` — **PMT A/R** (`shared/raci.md`); TPM I · SDM C · SDE C.

## Inputs required

- A PRD or agreed goal (link or paste)
- The user's estimate scale, if any
- Known dependencies and the teams that own them

## Clarifying questions when inputs are missing

1. What is the smallest slice a user would call valuable on its own?
2. Which stories are enabled by others — and which only look ordered?
3. What scale do you size in, and what is its legend?

## Steps

1. **Pin the epic.** Summary table first: type Epic, priority per the org's scale,
   business value in one line, the success metric it serves (from the PRD).
2. **Slice vertically.** Every story cuts UI → API → data and ships user value alone. A
   story that only changes a schema layer is a task — say so and put it behind a story that
   needs it, never dressed up as a story.
3. **Order by risk and value.** The scariest assumption in the earliest slice (same lens as
   the PRD); the highest-value thin slice first. Say the ordering logic out loud in the
   artifact.
4. **Write the ACs.** `AC-n` Given/When/Then per story, testable as observable behavior —
   same standard as `REQ-n` in the PRD.
5. **Size honestly.** In the user's supplied scale only; `[CONFIRM: scale legend]` if none
   was given. An epic with no sizes shown is a defect, not a plan.
6. **Dependency rows.** `DEP-n`: on what, from which team, blocks which `US-n`. Every row a
   named owner or `[CONFIRM]`.
7. **Read-back pass.** Every story vertical or explicitly labeled a task; ACs Given/When/Then;
   sizes in the user's scale or CONFIRM; pipes kept out of cell bodies (CSV-ready).
8. **Hand over.** Emit the artifact ending with its Import-target block. CSV of the story
   table on request. Wait.

## Output binding

`shared/output-schemas/jira-epic-and-stories.md`.

## Import target

Jira — bulk import / CSV, or paste each story block into its ticket description.

## Worked example

`tests/pmt/slice-mvp-and-stories/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
