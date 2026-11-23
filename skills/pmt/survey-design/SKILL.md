---
name: survey-design
role: pmt
status: planned
created: 2026-11-22
---

# survey-design — instrument + results read-back

> **Status: planned — skeleton, not yet a playbook.** Builds with the discovery loop per ROADMAP.

## What it produces

A **survey instrument**: objectives, audience and sampling plan, typed questions
(single/multi/select-scale/open), the bias check per question, and the analysis plan. On
request, a **results read-back** from pasted data: distributions and cross-tabs as pasted,
never extrapolated.

## Inputs required

- The question the survey must answer (one, stated before any question is written)
- Audience and sample: who, reachable how, expected n
- Pasted results, for the read-back run

## Clarifying questions when inputs are missing

- What one decision does this survey inform?
- Who is sampled — and who does the sampling method silently exclude?
- How will you know if the responses are self-selected?

## RACI row

`Survey design & results read-back` — **PMT A/R** (`shared/raci.md`); TPM I · SDM I · SDE I.

## Steps (to be written)

1. (build ticket) State the objective → 2. Draft typed questions, checking each for leading
framing → 3. Write the sampling plan + bias notes → 4. Read-back run: counts and quotes from
the paste only.

## Output binding

Instrument and read-back follow the table rules in `shared/system-conventions.md`; every
result number traces to the pasted data or `[CONFIRM]`.

## Import target

Confluence — the research page; the survey tool (paste-ready).