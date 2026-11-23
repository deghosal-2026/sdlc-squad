# Prompt book — SDE (Software Development Engineer)

**Load first (every session):** `shared/system-conventions.md` → `shared/glossary-and-org.md`
(fill your org slots) → `roles/sde.md` → the skill's `SKILL.md`.
**Redact personal data before pasting anything.** Every prompt below is a sample — swap in
your real facts; anything you leave out comes back as `[CONFIRM: ...]`, never invented.
The example paths and excerpts are fictional.

## 1. technical-design-and-breakdown — RFC + Jira-ready sub-tasks

**Paste with:** `skills/sde/technical-design-and-breakdown/SKILL.md`

```
Design this change. REQ-1: order status visible via signed link, no login.
REQ-2: no PII unauthenticated. Relevant paths pasted:
services/checkout/status/router.py — route /status/{order_ref}, session-gated;
services/checkout/status/handler.py — renders PII when a session exists;
migrations/0431_add_state.sql — reversible. Quote what you read; anything not
pasted stays CONFIRM. Include failure modes with detection paths, an ordered
rollback that says what it does NOT undo, and T-tasks with DoDs.

[PASTE: real paths + file excerpts + API schemas]
```

**Import target:** Confluence — the RFC. GitHub — the tracking issue. Jira — the `T-n` sub-tasks.

## 2. generate-test-ideas-and-cases — layered test matrix

**Paste with:** `skills/sde/generate-test-ideas-and-cases/SKILL.md`

```
Build the test matrix for the attached design. Automation surface: pytest
(unit), schema contract tests in CI, playwright (E2E on staging), Grafana
alerts. Constraint: no production E2E environment. Trace every REQ and FM to
at least one case; every layer heading appears (empty ones say why); failure
injection cases name the fault.

[PASTE: the design / its failure modes / REQ-AC list]
```

**Import target:** Jira — the QA checklist. GitHub — the PR test plan. Confluence — the spec.

## 3. pr-plan-and-rollback-notes — GitHub PR description

**Paste with:** `skills/sde/pr-plan-and-rollback-notes/SKILL.md`

```
Write the PR description for this change: implementation checklist in merge
order, verification as real commands with expected outputs, migration order
(0431 pre-deploy), and rollback copied from the design — including what it
does NOT undo. Flag default off.

[PASTE: the design / diff summary / verification commands + outputs]
```

**Import target:** GitHub — the Pull Request description.

## 4. design-and-code-reviews — author gate + reviewer pass

**Paste with:** `skills/sde/design-and-code-reviews/SKILL.md`

```
Give me the review kit for this PR. Diff stats: 1,400 lines across router,
handler, and alerts, with a 40-line test file. One reviewer could not follow
_redact's session fallback. Team size norm: unknown — CONFIRM it. Include the
author gate (split order, self-review), the reviewer pass in order (design →
correctness → tests → naming → security), and the etiquette (nit: labels,
turnaround).

[PASTE: the diff / PR description / CODEOWNERS if any]
```

**Import target:** GitHub — the PR template / review guide. Confluence — team standards.

## 5. deploy-plan-and-release — canary ladder + flag ledger

**Paste with:** `skills/sde/deploy-plan-and-release/SKILL.md`

```
Write the deploy and release plan. Flag: order_status_self_serve, default off.
Migration: 0431 pre-deploy, reversible. Monitoring: queue-volume and
web-latency dashboards, outbox-lag alert (all exist). On-call: weekly
rotation. Ladder from 5% with promote criteria; rollback triggers
automatic-first, executable by on-call without me; every flag gets an owner
and a removal date.

[PASTE: the design rollback section / dashboard + alert names / TPM launch checklist]
```

**Import target:** GitHub — the release issue. Confluence — the runbook page.