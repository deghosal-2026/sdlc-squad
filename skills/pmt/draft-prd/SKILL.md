---
name: draft-prd
role: pmt
status: planned
created: 2026-11-22
---

# draft-prd — Confluence-ready PRD

> **Status: planned — skeleton, not yet a playbook.** The output contract and inputs below are
> committed; the step-by-step execution builds in its ROADMAP ticket (v0.1.0). Do not run as-is.

## What it produces

One PRD artifact bound to `shared/output-schemas/confluence-prd-or-rfc.md`: Problem & Context ·
Target Users · Goals & Non-Goals · User Journeys · Functional & Non-Functional Requirements ·
Edge Cases · Open Questions · Rollout & Metrics.

## Inputs required

- Problem statement or customer signal (tickets, quotes, research notes)
- Target users and their current workaround
- Business outcome sought, with any known metric
- Known constraints: dependencies, dates, compliance, cost

## Clarifying questions when inputs are missing

- Who hurts, how often, and what do they do today instead?
- What is explicitly a non-goal this phase?
- What would "worked" measure, and who checks it?

## Steps (to be written)

1. (build ticket) Elicit and pin inputs → 2. Draft per schema section order → 3. `[CONFIRM]`
every unknown → 4. Read-back pass against the schema rules.

## Output binding

`shared/output-schemas/confluence-prd-or-rfc.md` — verbatim structure, all rules.

## Import target

Confluence — the PRD page for the initiative.