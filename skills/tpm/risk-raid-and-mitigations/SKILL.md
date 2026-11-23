---
name: risk-raid-and-mitigations
role: tpm
status: planned
created: 2026-11-22
---

# risk-raid-and-mitigations — RAID log

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.2.0 per ROADMAP.

## What it produces

A RAID artifact: standardized tables for Risks, Assumptions, Issues, Dependencies — each risk row
with likelihood/impact rating, early-warning signal, mitigation action, fallback plan, and owner.

## Inputs required

- Program context: roadmap, PRDs, prior RAID entries if any
- Known open issues and in-flight mitigations
- Owners' names

## Clarifying questions when inputs are missing

- What signal would tell you this risk is happening *before* it costs a milestone?
- What is the fallback if the mitigation does not land?
- Which assumptions, if wrong, change the critical path?

## Steps (to be written)

1. (build ticket) Elicit per category → 2. Rate and pair signals → 3. Assign owners or
`[CONFIRM]` → 4. Sort by likelihood × impact.

## Output binding

RAID tables follow the ID prefixes (`R-n`, `DEP-n`) and column rules in
`shared/system-conventions.md`.

## Import target

Confluence — the weekly program status page.