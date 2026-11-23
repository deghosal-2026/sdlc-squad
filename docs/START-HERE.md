# Start here — find your skill by task

You arrive with a task, not a role. Find it below: **role → skill → minimum inputs →
needs first → import target**. Rows are reshuffled from the [README skills table](../README.md)
and each `SKILL.md`'s **Inputs required** section. Ready-to-paste prompts live in
`usage/prompts-<role>.md`.

## By task

| I need… | Role · Skill | Minimum inputs | Needs first | Lands in |
|---|---|---|---|---|
| A PRD | PMT · `draft-prd` | problem + users + outcome | — | Confluence |
| An epic + stories | PMT · `slice-mvp-and-stories` | an accepted PRD | a PRD | Jira |
| Success metrics | PMT · `define-success-metrics` | a goal + a baseline if you have one | a goal | Confluence |
| Customer interviews + synthesis | PMT · `customer-discovery-and-synthesis` | a decision to explore / pasted notes | — | Confluence |
| A survey | PMT · `survey-design` | one objective | an objective | survey tool · Confluence |
| A ranked ask list | PMT · `prioritize-asks` | a pile of asks with sources | — | Confluence · Jira |
| A program roadmap + dependencies | TPM · `program-roadmap-and-deps` | accepted PRD + owning teams | a PRD | Confluence · Jira |
| A RAID log | TPM · `risk-raid-and-mitigations` | program context + open risks | a program | Confluence |
| A launch go/no-go checklist | TPM · `release-readiness-check` | the launch + its sections | a launch | Confluence |
| A program status rollup | TPM · `program-status-review` | items + last report + cadence | a program | Confluence |
| A sprint plan that survives PTO/on-call | SDM · `sprint-planning-and-capacity` | roster, PTO, ceremonies, candidates | candidate backlog | Confluence · Jira |
| Scope-cut options | SDM · `scope-cut-and-tradeoffs` | a plan that doesn't fit + value order | a plan | Confluence |
| An ops-health review | SDM · `operational-health-review` | reopen/toil/flaky evidence | — | Confluence · Jira |
| A sprint retrospective | SDM · `sprint-retro` | last 2 sprints' done tickets | done-ticket exports | Confluence · Jira |
| A standup format + blocker log | SDM · `standup-execution` | board state | — | Confluence · Jira |
| A technical design + breakdown | SDE · `technical-design-and-breakdown` | requirements + code excerpts | requirements | Confluence · GitHub · Jira |
| Test cases | SDE · `generate-test-ideas-and-cases` | the design + automation surface | a design | Jira · PR |
| A PR plan + rollback notes | SDE · `pr-plan-and-rollback-notes` | the design + verification | a design | GitHub |
| Review checklists | SDE · `design-and-code-reviews` | a diff (or team norms) | a diff | GitHub · Confluence |
| A deploy / release plan | SDE · `deploy-plan-and-release` | flag, migration, dashboards, on-call | a change to ship | GitHub · Confluence |

## Scenario recipes

Named chains for the common jobs — read each hop's hand-off in
[`RELAY.md`](../usage/RELAY.md).

- **New feature** — `draft-prd` → `slice-mvp-and-stories` → `sprint-planning-and-capacity` →
  `technical-design-and-breakdown` → `generate-test-ideas-and-cases`
- **Release readiness** — `program-roadmap-and-deps` → `risk-raid-and-mitigations` →
  `release-readiness-check` → `deploy-plan-and-release`
- **Sprint recovery** — `operational-health-review` → `scope-cut-and-tradeoffs` → `sprint-retro`

## Not sure?

- Fuzzy problem, no requirements yet → **PMT**.
- Multiple teams, sequencing, launch → **TPM**.
- Commitments, capacity, trade-offs, ops → **SDM**.
- Design, tests, PRs, deploys → **SDE**.
- Still unsure? Load [`TOOLS.md`](../docs/TOOLS.md) and [`../README.md`](../README.md).

## Related

- [`../README.md`](../README.md) — the full skills table
- [`TOOLS.md`](../docs/TOOLS.md) — what fits your tools
- [`../docs/UPGRADING.md`](../docs/UPGRADING.md) — your glossary, upgrades
