---
name: technical-design-and-breakdown
description: Draft a technical design: affected modules quoted, contract changes, failure modes, rollback, plus Jira-ready T-tasks with DoDs.
role: sde
status: built
created: 2026-11-22
---

# technical-design-and-breakdown — RFC section + Jira-ready sub-tasks

## What it produces

A technical design bound to `shared/output-schemas/technical-design-doc.md`: Affected
Modules/Services · Data Model & API/Contract Changes · Flow · Failure Modes & Edge Cases ·
Observability · Rollback — plus a Jira-ready sub-task table (`T-n`) with scope and Definition
of Done per task.

## RACI row

`Technical design & breakdown` — **SDE A/R** (`shared/raci.md`); PMT C · TPM I · SDM C.

## Inputs required

- The requirement (PRD excerpt or story)
- Repository paths/files/services the change touches (paste or paths — unread code is `[CONFIRM]`)
- Existing contracts: API schemas, data models, event formats
- Known constraints: performance, compliance, cost

## Clarifying questions when inputs are missing

Ask up to 3, then draft with `[CONFIRM]`:

1. Which service owns this today — may I have the paths, or shall I mark them `[CONFIRM]`?
2. What breaks if this fails halfway — partial write, poison message, stuck flag?
3. What does rollback mean here, step by step?

## Steps

1. **Pin the requirement.** Restate the `REQ-n`/story being served in one line. If the
   requirement and the design disagree, that is a requirement question — flag it, never
   re-author the requirement.
2. **Read what was supplied.** Quote the pasted code/schema lines the design relies on. Every
   claim about existing behavior carries its path and symbol. Unread code is `[CONFIRM]` —
   describing a file you never saw is the classic drift.
3. **Affected modules table.** Path/service · change · risk. Each risk cell ties to a failure
   mode row below.
4. **Data model & contract changes.** Before/after shapes — schema, endpoint or event
   signatures, backwards-compatibility notes. Breaking changes are named as such.
5. **Flow.** Numbered sequence: actor → step → observable state change. Text only.
6. **Failure modes.** `FM-n` table: trigger · behavior · detection. Every success path names
   its failure paths; a failure without a detection path is an incomplete row.
7. **Observability.** What is logged/metric'd/alerted + the query or dashboard that shows
   it. "We'll notice" is not detection.
8. **Rollback.** Ordered, named steps back to the last good state — including what rollback
   does *not* undo (data written under the flag, caches, consumers). "Revert the PR" is a
   step, not a plan.
9. **Sub-tasks.** `T-n`: task · scope (files/services) · DoD observable by someone other than
   the author · depends-on. A task whose done-ness only its author can check is not
   done-defined.
10. **Read-back pass.** Every existing-code claim quoted or `[CONFIRM]`; every `FM` has
    detection; every `T` has a checkable DoD; rollback names its data effects.
11. **Hand over.** Emit the design ending with its Import-target block. Answer questions. Wait.

## Output binding

`shared/output-schemas/technical-design-doc.md`.

## Import target

Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the `T-n`
table as sub-tasks.

## Worked example

`tests/sde/technical-design-and-breakdown/fixture.md` — full input + expected artifact
(synthetic paths, pasted excerpts). Recorded run:
`tests/results/run-2026-11-22-v0.1.0.md`. Condensed shape:

```markdown
Input: "REQ-1: order status visible without login. Paths pasted:
services/checkout/status/ (router + handler), migrations/0431_add_state (reversible)."

→ # Design: order-status self-service
  ## Affected modules — services/checkout/status/router (quoted lines) · risk: auth-bypass
  ## Contract — GET /status/{order_ref} → 200 {state, eta, boxes[]} · no PII unauthenticated
  ## Failure modes — partial write → stale state · detection: outbox-lag alert
  ## Rollback — 1) flag off 2) dual-read window 3) migration 0431 reversible 4) cache purge
  ## Sub-tasks — T-1 read path (DoD: curl without session, 200) · T-2 outbox lag alert
  ## Import target — Confluence RFC; GitHub issue; Jira sub-tasks
```
