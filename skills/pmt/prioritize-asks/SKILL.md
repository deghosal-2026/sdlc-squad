---
name: prioritize-asks
role: pmt
status: planned
created: 2026-11-22
---

# prioritize-asks — ranked ask list from any pile of requests

> **Status: planned — skeleton, not yet a playbook.** Builds with the discovery loop per ROADMAP.

## What it produces

A **ranked ask list**: the pile deduped, clustered by theme, scored on a stated framework
(reach, impact, confidence, effort — scored from user-supplied data or `[CONFIRM]`), ranked
with rationale — plus the explicit tail: what is not ranked, and why.

## Inputs required

- The raw pile: support tickets, sales requests, exec asks, survey themes, interview needs
- The ranking criteria (or the request to propose one)
- Any constraints: committed roadmap, capacity facts, deadlines

## Clarifying questions when inputs are missing

- Who asked, how often, and what did they actually say?
- Which asks are the same ask wearing three costumes?
- What does the top of this list cost the people who must build it? (→ SDM's capacity math,
  not PMT's guess)

## RACI row

`Ask intake & prioritization` — **PMT A/R** (`shared/raci.md`); TPM C · SDM C · SDE C.

## Steps (to be written)

1. (build ticket) Normalize the pile (source, ask, verbatim quote) → 2. Dedupe + cluster →
3. Score on the stated framework, arithmetic shown → 4. Rank + write the not-ranked tail.

## Output binding

Ranked table follows the table rules in `shared/system-conventions.md`; scores are arithmetic
on user-supplied inputs, shown, never vibes.

## Import target

Confluence — the decision log. Jira — the ranked asks as candidate backlog.