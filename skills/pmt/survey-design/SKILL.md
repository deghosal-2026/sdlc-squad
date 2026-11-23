---
name: survey-design
description: Design a bias-checked survey instrument and read back pasted results as distributions and quotes, never extrapolated. Use when you need to measure something at scale.
role: pmt
status: built
created: 2026-11-22
---

# survey-design — instrument + results read-back

## What it produces

A **survey instrument**: objectives, audience and sampling plan, typed questions
(single/multi/select-scale/open), the bias check per question, and the analysis plan. On
request, a **results read-back** from pasted data: distributions and cross-tabs as pasted,
never extrapolated.

## RACI row

`Survey design & results read-back` — **PMT A/R** (`shared/raci.md`); TPM I · SDM I · SDE I.

## Inputs required

- The question the survey must answer (one, stated before any question is written)
- Audience and sample: who, reachable how, expected n
- Pasted results, for the read-back run

## Clarifying questions when inputs are missing

1. What one decision does this survey inform?
2. Who is sampled — and who does the method silently exclude?
3. How will you know if the responses are self-selected?

## Steps — instrument run

1. **State the objective, singular.** One question this survey answers. Two objectives →
   two surveys, run separately.
2. **Audience and sampling.** Who, how reached, expected n. Name the self-selection risk
   (who answers surveys is already an unrepresentative slice) and what offsets it.
3. **Typed questions.** Each with its type and a **bias check** line: leading framing,
   double-barrelled ("fast *and* easy" answers nothing), survivorship (asks the happy).
   Scale questions state their endpoints ("1 = never, 5 = daily").
4. **Order.** Screening first, easy before sensitive, demographics last (answers change
   once the respondent knows what the survey wants).
5. **Analysis plan.** Which cuts answer the objective; how missing data is treated. Written
   before fielding — a survey analyzed ad hoc answers whatever the cutter wanted.
6. **Read-back pass.** Every question passes its bias check; nothing double-barrelled;
   nothing leading.

## Steps — read-back run

1. **Counts from the paste only.** Distributions, cross-tabs, n — all traced. Never
   extrapolate a sample to a population; label the self-selection caveat in the artifact.
2. **Quote the open ends** verbatim, with their counts.
3. **State what the data cannot say** — the survey's limits as a labeled section, not a
   footnote.

## Output binding

`shared/system-conventions.md` table rules; every result traces to the paste or `[CONFIRM]`.

## Import target

Confluence — the research page; the survey tool (paste-ready).

## Worked example

`tests/pmt/survey-design/fixture.md` — full input + expected artifact (synthetic, both runs).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
