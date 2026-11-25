# Examples — all 20 fixtures at a glance

Every skill ships a complete worked example (synthetic input + expected artifact + checks)
under `../tests/<role>/<skill>/fixture.md`. This is the index: what each one feeds and
where its artifact lands. The fixtures are the quality bar — inspect them without reading
test infrastructure.

| Role | Skill | Sample input | Artifact | Lands in |
|---|---|---|---|---|
| PMT | `draft-prd` | order-status self-service (support volume + tracking visits) | PRD: goals, non-goals, REQs, edge cases | Confluence |
| PMT | `slice-mvp-and-stories` | the accepted PRD + T-shirt scale | epic + vertical stories (Given/When/Then) | Jira |
| PMT | `define-success-metrics` | G1 goal + dashboards + a guardrail | north star + guardrails + events | Confluence |
| PMT | `customer-discovery-and-synthesis` | interview guide + 5 pasted notes | themes + verbatim quotes | Confluence |
| PMT | `survey-design` | one trust question + pasted results | bias-checked instrument + read-back | survey tool · Confluence |
| PMT | `prioritize-asks` | a 5-ask pile with sources | ranked list on a stated framework | Confluence · Jira |
| TPM | `program-roadmap-and-deps` | PRD + 3 teams + a freeze date | milestones + dependency table + critical path | Confluence · Jira |
| TPM | `risk-raid-and-mitigations` | a freeze-slip risk + a legal assumption | 4 tables with signals + fallbacks | Confluence |
| TPM | `release-readiness-check` | flag + migration + alerts + sign-offs | go/no-go checklist | Confluence |
| TPM | `program-status-review` | monthly cadence + Jira milestones | R/Y/G rollup with evidence | Confluence |
| SDM | `sprint-planning-and-capacity` | 6 engineers, PTO, on-call, carry-overs | capacity table + commitment + risks | Confluence · Jira |
| SDM | `scope-cut-and-tradeoffs` | a 3-day gap, fixed date, 4 items | keep/defer/cut with costs | Confluence |
| SDM | `operational-health-review` | reopen cluster + toil + flaky counts | hotspots + remediation tickets | Confluence · Jira |
| SDM | `sprint-retro` | 2 sprints' done-ticket exports | went-well/hurt/change + action items | Confluence · Jira |
| SDM | `standup-execution` | board state + yesterday's blockers | round format + blocker log | Confluence · Jira |
| SDE | `technical-design-and-breakdown` | REQ-1/REQ-2 + code excerpts | RFC + sub-tasks with DoD | Confluence · GitHub · Jira |
| SDE | `generate-test-ideas-and-cases` | the design + automation surface | test matrix by layer | Jira · PR |
| SDE | `pr-plan-and-rollback-notes` | the design + verification + migration | PR checklist + rollback steps | GitHub |
| SDE | `design-and-code-reviews` | a 1,400-line diff + team norms | author + reviewer checklists | GitHub · Confluence |
| SDE | `deploy-plan-and-release` | flag + migration + dashboards + on-call | deploy/release split + canary + flags | GitHub · Confluence |

## Scenarios by company size

The fixtures are one team's examples; these are three team **shapes**, to help you recognize
your own. All synthetic (Meridian Outfitters and neighbours — no real org data).

| Shape | What it looks like | Where to start |
|---|---|---|
| **A small startup squad** | 4–6 engineers, one PM wearing the TPM hat, no formal process | `draft-prd` → `slice-mvp-and-stories` → `sprint-planning-and-capacity` |
| **A platform / infra team** | on-call, SLOs, a shared services surface | `operational-health-review` → `technical-design-and-breakdown` → `deploy-plan-and-release` |
| **A cross-functional product squad** | PM + EM + TPM + engineers, a quarterly program | the full relay — [`../usage/FEATURE-RELAY.md`](../usage/FEATURE-RELAY.md) |

## Related

- [`START-HERE.md`](START-HERE.md) — pick by task
- [`../usage/WALKTHROUGH.md`](../usage/WALKTHROUGH.md) — one run in full
- [`../tests/README.md`](../tests/README.md) — what a fixture and a recorded run are
