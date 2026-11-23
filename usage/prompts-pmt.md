# Prompt book — PMT (Product Manager, Technical)

**Load first (every session):** `shared/system-conventions.md` → `shared/glossary-and-org.md`
(fill your org slots) → `roles/pmt.md` → the skill's `SKILL.md`. Or paste the one generated
bundle `usage/bundles/pmt-<skill>.md` (regenerate with `make bundles`).
**Redact personal data before pasting anything.** Every prompt below is a sample — swap in
your real facts; anything you leave out comes back as `[CONFIRM: ...]`, never invented.
The example company (Meridian Outfitters) is fictional.

## 1. draft-prd — Confluence-ready PRD

**Paste with:** `skills/pmt/draft-prd/SKILL.md`

```
Draft a PRD for this. Problem: support gets ~412 "where is my order?" tickets a month
(queue export pasted below); 65% of tracking-page visits are logged-out. Target users:
guests mid-order. Outcome wanted: cut order-status support load. Constraints: launch
before the Dec-15 freeze. Known non-goal candidates: a chatbot (marketing ask).

[PASTE: ticket export rows / customer quotes / research notes]
```

**Import target:** Confluence — the PRD page for the initiative.

## 2. slice-mvp-and-stories — epic + vertical stories

**Paste with:** `skills/pmt/slice-mvp-and-stories/SKILL.md`

```
Slice the attached PRD into an epic + vertically sliced stories. Estimate scale:
T-shirt (S=2d, M=5d, L=10d, one engineer). Dependencies: guest status events come
from the Checkout team; email template from Notifications. Order the stories so the
riskiest assumption ships first.

[PASTE: the accepted PRD]
```

**Import target:** Jira — bulk import / CSV, or paste each story into its ticket.

## 3. define-success-metrics — north star + guardrails

**Paste with:** `skills/pmt/define-success-metrics/SKILL.md`

```
Define success metrics for the order-status PRD. Goal G1: order-status tickets −50%
in 2 months (baseline 412/mo). Dashboards we already have: support queue volume, web
latency. Guardrail concern: tracking p95 latency must not degrade.

[PASTE: PRD §Rollout & metrics / current dashboard names]
```

**Import target:** Confluence — PRD §Rollout & metrics, or the launch-readiness doc.

## 4. customer-discovery-and-synthesis — interview guide + synthesis

**Paste with:** `skills/pmt/customer-discovery-and-synthesis/SKILL.md`

```
(a) Draft a discovery interview guide. Decision it informs: should v1 include live
carrier chat? Reachable: 5 recent order-status ticket submitters. Mom Test rules —
past behavior only, no hypotheticals.
(b) Then synthesize these 5 interview notes into themes with verbatim quotes,
split signal vs. anecdote.

[PASTE (b): interview notes / call transcripts / support threads]
```

**Import target:** Confluence — the research page for this initiative.

## 5. survey-design — instrument + read-back

**Paste with:** `skills/pmt/survey-design/SKILL.md`

```
(a) Design a survey instrument. One objective: do guest users trust an
unauthenticated status page? Audience: recent order-email recipients, expected n≈200.
Bias-check every question.
(b) Read back these results: distributions and cross-tabs as pasted, no extrapolation.

[PASTE (b): result tables / export rows]
```

**Import target:** Confluence — the research page; the survey tool (paste-ready).

## 6. prioritize-asks — ranked ask list

**Paste with:** `skills/pmt/prioritize-asks/SKILL.md`

```
Rank this pile of asks on RICE (or tell me if another framework fits better):
- order-status self-serve (support paste, ~412 tickets/mo)
- carrier deep-link (support paste, 3 tickets)
- chatbot (marketing, one exec ask)
- dark mode (sales, one ask)
Reach figures from the pasted analytics where available; where not, mark CONFIRM.
Don't invent effort numbers — flag where engineering must estimate.

[PASTE: raw asks — tickets, sales requests, exec asks, verbatim]
```

**Import target:** Confluence — the decision log. Jira — ranked asks as candidate backlog.