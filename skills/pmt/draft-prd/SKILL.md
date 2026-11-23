---
name: draft-prd
description: Draft a Confluence-ready PRD from a problem statement: goals and non-goals, requirements, edge cases, rollout and metrics.
role: pmt
status: built
created: 2026-11-22
---

# draft-prd — Confluence-ready PRD

## What it produces

One PRD artifact bound to `shared/output-schemas/confluence-prd-or-rfc.md`: Problem & Context ·
Target Users · Goals & Non-Goals · User Journeys · Functional & Non-Functional Requirements ·
Edge Cases · Open Questions · Rollout & Metrics.

## RACI row

`PRD — requirements & non-goals` — **PMT A/R** (`shared/raci.md`); TPM C · SDM I · SDE C.

## Inputs required

- Problem statement or customer signal (tickets, quotes, research notes)
- Target users and their current workaround
- Business outcome sought, with any known metric
- Known constraints: dependencies, dates, compliance, cost

## Clarifying questions when inputs are missing

Ask up to 3, then draft with `[CONFIRM]`:

1. Who hurts, how often, and what do they do today instead?
2. What is explicitly a non-goal this phase?
3. What would "worked" measure, and who checks it?

## Steps

1. **Pin the decision.** From the inputs, state in one line what this PRD decides. If that line
   cannot be written, ask the clarifying questions before anything else.
2. **Problem & context — evidence only.** Quote the pasted tickets/support threads verbatim,
   with counts from the paste. Any number without a paste behind it is `[CONFIRM: source]`.
   No market claims.
3. **Target users — behavior, not persona fluff.** Name the segment and their current
   workaround (what they do today, in their words if pasted).
4. **Goals — outcomes, ≤ 5.** Each goal names a metric and a direction ("cut status
   tickets ≥ 50%", not "improve CX").
5. **Non-goals — same specificity as goals.** What is out this phase, and why it stays out.
   A courtesy non-goal ("be all things") is a defect.
6. **User journeys.** Table per schema: Step · User action · System behavior · Notes. The
   journey starts at the user's trigger, not at the feature.
7. **Requirements.** Functional `REQ-n` — each testable as an observable behavior.
   Non-functional — performance, privacy, cost, compliance — each with its source or
   `[CONFIRM]`. "Seamless" is not a requirement.
8. **Edge cases.** `EC-n` table: trigger · expected behavior. Required section: state "none
   identified yet — [CONFIRM]" only after asking, never by skipping the section.
9. **Open questions.** `Q-n`: question · owner · needed-by. Questions are deliverables, not
   apologies.
10. **Rollout & metrics.** Phasing, the flag, the metric this ships against (with baseline or
    `[CONFIRM: baseline]`), and the guardrail that must not degrade.
11. **Read-back pass.** Every number sourced or `[CONFIRM]`; every REQ testable; non-goals as
    specific as goals; no invented names/dates/companies; edge-case section present.
12. **Hand over.** Emit the artifact ending with its Import-target block. Answer questions.
    Wait. Never auto-run the next role's skill.

## Output binding

`shared/output-schemas/confluence-prd-or-rfc.md` — verbatim structure, all rules.

## Import target

Confluence — the PRD page for the initiative.

## Worked example

`tests/pmt/draft-prd/fixture.md` — full input + expected artifact (synthetic end to end:
"order-status self-service" for a fictional retailer). Recorded run:
`tests/results/run-2026-11-22-v0.1.0.md`. Condensed shape:

```markdown
Input: "Support gets ~400 where-is-my-order tickets/month. Tracking page exists,
65% of visits are logged-out. Marketing wants a chatbot."

→ # PRD: order-status self-service
  ## Problem & context — 400/month [CONFIRM: queue export]; verbatim ticket quotes
  ## Non-goals — chatbot (marketing ask, parked this phase); carrier chat
  ## Goals — G1 status tickets −50% in 2 months [baseline: 400/month]
  ## Requirements — REQ-1 status via signed link, no login · REQ-2 no PII unauthenticated
  ## Edge cases — EC-1 order > 90 days → archived message
  ## Import target — Confluence PRD page
```
