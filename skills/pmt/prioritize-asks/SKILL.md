---
name: prioritize-asks
description: Rank a raw pile of asks on a stated framework (RICE default), every score traceable, plus the not-ranked tail. Use when there are more asks than capacity.
role: pmt
status: built
created: 2026-11-22
---

# prioritize-asks — ranked ask list from any pile of requests

## What it produces

A **ranked ask list**: the pile deduped, clustered by theme, scored on a stated framework
(RICE by default: Reach × Impact × Confidence ÷ Effort; or the org's own), ranked with
rationale — plus the explicit tail: what is not ranked, and why.

## RACI row

`Ask intake & prioritization` — **PMT A/R** (`shared/raci.md`); TPM C · SDM C · SDE C.

## Inputs required

- The raw pile: support tickets, sales requests, exec asks, survey themes, interview needs
- The ranking criteria (or the request to propose one)
- Any constraints: committed roadmap, capacity facts, deadlines

## Clarifying questions when inputs are missing

1. Who asked, how often, and what did they actually say?
2. Which asks are the same ask wearing three costumes?
3. What does the top of this list cost the people who must build it? (→ SDM's capacity math,
   not PMT's guess.)

## Steps

1. **Normalize the pile.** One row per raw ask: source · who asked · verbatim ask · date.
   Verbatim, not summarized — a paraphrase is PMT's opinion wearing a customer's shirt.
2. **Dedupe and cluster.** Same ask in three costumes → one ask with N sources counted.
3. **State the framework.** RICE by default — Reach (people/quarter), Impact (per-person:
   3 massive / 2 high / 1 medium / 0.5 low / 0.25 minimal), Confidence (100% high / 80%
   medium / 50% low — below that is a moonshot, labeled), Effort (person-months, minimum
   0.5). **Confidence below 50% → the ask is labeled, not ranked into silence.**
4. **Score with arithmetic shown.** Every cell of R/I/C/E carries its basis ("reach: 2,300/
   quarter from the support paste"), or `[CONFIRM]` if the pile does not carry it. Scores
   computed, never vibes.
5. **Rank — and keep the ranking honest.** A high score ranks it, not ships it: dependencies
   and table-stakes are called out as out-of-order trade-offs, explicitly, in the artifact.
   RICE is a ranking, not a verdict.
6. **Write the tail.** What is not ranked and why — too vague, needs discovery, needs SDM's
   cost estimate first. Silence here is the failure mode.
7. **Read-back pass.** Every score traceable; every quote verbatim; the tail present; no
   effort numbers invented where SDM/SDE must supply them.
8. **Hand over.** Emit the artifact ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/system-conventions.md` table rules; scores are arithmetic on user-supplied inputs,
shown, never vibes.

## Import target

Confluence — the decision log. Jira — the ranked asks as candidate backlog.

## Worked example

`tests/pmt/prioritize-asks/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
