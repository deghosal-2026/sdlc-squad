---
name: generate-test-ideas-and-cases
role: sde
status: planned
created: 2026-11-22
---

# generate-test-ideas-and-cases — layered test matrix

> **Status: planned — skeleton, not yet a playbook.** Builds in v0.1.0 (core loop) per ROADMAP.

## What it produces

A test plan bound to `shared/output-schemas/test-plan-and-cases.md`: a test matrix by layer —
Unit · Integration · Contract/API · End-to-End/Smoke · Non-Functional/Failure Injection — with
Scenario, Preconditions/Input, Expected Result, and Automation/Verification type per case, plus
coverage notes stating what is deliberately not covered.

## Inputs required

- The feature/design being tested (paste or link)
- The failure modes worth inducing (from the design's §Failure Modes if run)
- The automation surface that exists: test frameworks, CI jobs
- Environment constraints (what cannot be tested end-to-end, and why)

## Clarifying questions when inputs are missing

- Which layer does your team trust for regression today?
- What breaks loudly — and what breaks silently, and which layer catches silence?
- What is too expensive/flaky to automate, and may it be listed as manual?

## RACI row

`Test plan & cases` — **SDE A/R** (`shared/raci.md`); PMT I · TPM I · SDM C.

## Steps (to be written)

1. (build ticket) Enumerate scenarios per layer → 2. Pair each happy path with failure paths →
3. Assign verification types → 4. Write coverage notes for the gaps.

## Output binding

`shared/output-schemas/test-plan-and-cases.md`.

## Import target

Jira — QA/test checklist. GitHub — PR test plan / issue body. Confluence — the test spec.