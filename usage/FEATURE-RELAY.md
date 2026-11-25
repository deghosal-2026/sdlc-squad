# The feature relay, end to end — order-status self-serve

One fictional feature — Meridian Outfitters' **order-status self-serve** — crossing all four
roles, so you can see how the artifacts connect rather than reading each skill as an isolated
template. Every fact traces to a committed sample: the prompt books
([`prompts-pmt.md`](prompts-pmt.md), [`prompts-tpm.md`](prompts-tpm.md),
[`prompts-sdm.md`](prompts-sdm.md), [`prompts-sde.md`](prompts-sde.md)) and the fixtures
under [`../tests/`](../tests/). The feature is the same across all four artifacts.

## The chain

| # | Role / skill | Artifact out | Carried to the next | Relay row |
|---|---|---|---|---|
| 1 | PMT / `draft-prd` | the PRD (Confluence) | problem, non-goals, the G1 metric, the Dec-15 freeze | PMT → TPM |
| 2 | PMT / `slice-mvp-and-stories` | epic + stories (`US-n`) | stories + sizes; deps: Checkout, Notifications | PMT → SDM |
| 3 | TPM / `program-roadmap-and-deps` | roadmap + dependency graph | milestones, critical path, zero-slack links | TPM → SDM |
| 4 | SDM / `sprint-planning-and-capacity` | sprint plan + commitment | committed scope (M1 order-status) + capacity math | SDM → SDE |
| 5 | SDE / `technical-design-and-breakdown` | RFC + sub-tasks (`T-n`) | design, rollback steps, DoD | SDE → SDM |

The relay rows come from [`RELAY.md`](RELAY.md); each hop is a **fresh session**, one role
([`../WHAT-THIS-IS.md`](../WHAT-THIS-IS.md)).

## Hop 1 — PMT drafts the PRD (`prompts-pmt.md` §1)

Raw input: support gets **~412 "where is my order?" tickets a month**; 65% of tracking-page
visits are logged-out; launch **before the Dec-15 freeze**; a chatbot is a non-goal
candidate. The PRD's success metric is **G1 — order-status tickets −50% in 2 months**.

## Handoff 1 → 2 (PMT → SDM)

```
## Handoff
- **From:** pmt/draft-prd — the order-status PRD
- **Carried open:** [CONFIRM: the exact G1 baseline from the queue export] · [CONFIRM: which non-goals are fixed]
- **Next:** pmt/slice-mvp-and-stories — paste the accepted PRD + estimate scale (T-shirt)
```

One item is **resolved** on the way (the **Dec-15 freeze** came from the input, not a
guess); one is carried **open** (the G1 baseline is only as good as the pasted export).
Never silently drop a carried `[CONFIRM]` — it is the next role's first question.

## Hop 2 — PMT slices (`prompts-pmt.md` §2)

The accepted PRD → an epic + **vertically sliced** stories, T-shirt scale (S=2d, M=5d,
L=10d), with dependencies on the **Checkout** team (guest status events) and
**Notifications** (the email template). The riskiest assumption ships first. Import: Jira.

## Hop 3 — TPM builds the program plan (`prompts-tpm.md` §1)

The PRD → milestones + a dependency graph. Teams: **Checkout** owns status events,
**Notifications** the guest email template, **Platform** launch. Launch before the Dec-15
freeze; show slack per link, name the critical path, and flag zero-slack links.

## Hop 4 — SDM plans the sprint (`prompts-sdm.md` §1)

The committed scope → a sprint plan for **Sprint 14 (2026-12-07 → 2026-12-18, 10 working
days)**, engineers A–F, all arithmetic shown, a commitment ≤ net focus. **M1 order-status**
is 8d; **dark mode** has no estimate, so it returns as a `[CONFIRM: estimate]` that blocks
the plan until SDE/SDM sizes it.

## Hop 5 — SDE designs (`prompts-sde.md` §1)

The committed item → an RFC + Jira-ready sub-tasks (`T-n`). The design touches
`services/checkout/status/router.py` and `handler.py` — the latter renders PII when a
session exists, a privacy note the design must carry. Rollback steps and the DoD cross back
to the SDM.

## Why the relay works

Each hop hands **one artifact** forward, not a mega-context — that is what keeps the roles
from blurring. The [`Handoff Block`](RELAY.md) makes the carry explicit; the
[`WALKTHROUGH.md`](WALKTHROUGH.md) shows one hop (the SDM sprint plan) in full depth.

## Related

- [`RELAY.md`](RELAY.md) — the transition table and the Handoff Block
- [`WALKTHROUGH.md`](WALKTHROUGH.md) — one hop, start to finish
- [`prompts-pmt.md`](prompts-pmt.md) · [`prompts-tpm.md`](prompts-tpm.md) ·
  [`prompts-sdm.md`](prompts-sdm.md) · [`prompts-sde.md`](prompts-sde.md) — the samples
- [`../tests/`](../tests/) — the fixtures behind each skill
