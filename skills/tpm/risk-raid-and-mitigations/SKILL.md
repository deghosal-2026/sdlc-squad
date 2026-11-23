---
name: risk-raid-and-mitigations
description: Draft a RAID log — risks with early-warning signals, mitigations and fallbacks; assumptions with verification owners. Use when a program needs risk tracking.
role: tpm
status: built
created: 2026-11-22
---

# risk-raid-and-mitigations — RAID log

## What it produces

A RAID artifact: standardized tables for Risks, Assumptions, Issues, Dependencies — each risk
row with likelihood/impact rating, early-warning signal, mitigation action, fallback plan,
and owner.

## RACI row

`RAID log & risk tracking` — **TPM A/R** (`shared/raci.md`); PMT C · SDM C · SDE I.

## Inputs required

- Program context: roadmap, PRDs, prior RAID entries if any
- Known open issues and in-flight mitigations
- Owners' names

## Clarifying questions when inputs are missing

1. What signal would tell you this risk is happening *before* it costs a milestone?
2. What is the fallback if the mitigation does not land?
3. Which assumptions, if wrong, change the critical path?

## Steps

1. **Run the four tables.** Risks (might happen) · Assumptions (believed, unverified) ·
   Issues (already true) · Dependencies (needed from someone). Same ID rules — `R-n`,
   `DEP-n`; assumptions and issues numbered per the conventions. A row that is two of
   these at once is split into two rows.
2. **Rate each risk.** Likelihood × impact on fixed 3-point scales (high/med/low) — stated,
   not defended with prose. Every risk row also carries its **early-warning signal**: the
   observable that fires first. A risk you cannot detect early is a surprise with a nicer
   name — the row says so, and its owner goes to the roadmap instead.
3. **Mitigation + fallback, both.** Mitigation reduces the likelihood; fallback answers "and
   if it happens anyway?" A risk row with only a mitigation is half a row.
4. **Owners on every row.** Real names or `[CONFIRM: owner]` — a risk owned by "the team"
   is unowned.
5. **Sort by likelihood × impact**, descending. The top of the table is what this week's
   program status report carries (`program-status-review`).
6. **Assumptions get verification owners.** Each assumption names who verifies it, how, by
   when. Unverified assumptions that age are where programs die quietly.
7. **Read-back pass.** Every row has owner + signal (risks) or verifier (assumptions); no
   rating defended with adjectives alone; no invented dates or people.
8. **Hand over.** Emit the RAID ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/system-conventions.md` ID prefixes (`R-n`, `DEP-n`) and column rules.

## Import target

Confluence — the weekly program status page.

## Worked example

`tests/tpm/risk-raid-and-mitigations/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
