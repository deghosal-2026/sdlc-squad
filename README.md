# sdlc-squad

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![100% Markdown](https://img.shields.io/badge/100%25_Markdown-2ea44f)](#what-it-does)
[![Privacy](https://img.shields.io/badge/Privacy-local_only,_no_telemetry-8b5cf6)](#what-it-does)
[![Status: v0.1.1](https://img.shields.io/badge/status-v0.1.1_public-2ea44f)](#status)
[![Changelog](https://img.shields.io/badge/changelog-0.1.1-2ea44f)](CHANGELOG.md)
[![PyPI](https://img.shields.io/pypi/v/sdlc-squad)](https://pypi.org/project/sdlc-squad/)
[![Roles](https://img.shields.io/badge/roles-4-2ea44f)](#the-squad)
[![Skills](https://img.shields.io/badge/skills-20_built-2ea44f)](#skills)

![sdlc-squad — a software team in a box](docs/assets/social-preview.png)

> A software team in a box. Four AI personas — **PMT (Product Manager, Technical), TPM, SDM, SDE** —
> each with a playbook of skills, loaded into any AI chat. Each skill turns fuzzy input into one
> clean Markdown contract — a PRD, a program roadmap, a sprint capacity plan, a technical design,
> a test matrix, a PR description — copy-paste ready for **Confluence, Jira, and GitHub**.

## Status

**v0.1.1 — first-run, destinations, and paste-verified targets.** Twenty skills, each with
its fixture (`tests/<role>/<skill>/fixture.md`) and its recorded run
(`tests/results/run-2026-11-22-v0.1.0.md`). Since 0.1.0: a five-minute first run and a full
[`WALKTHROUGH`](usage/WALKTHROUGH.md), one-paste session bundles (`make bundles`), the
[`UPGRADING`](docs/UPGRADING.md) glossary discipline, the support/trust docs, per-destination
contracts (`shared/destinations/`), the `sdlc-squad prompt` CLI, and a **real-paste spot
check** — GitHub, Jira, and Confluence all observed
([`tests/results/run-2026-11-23-g3-real-paste.md`](tests/results/run-2026-11-23-g3-real-paste.md)).
Next per [ROADMAP](ROADMAP.md): v0.1.x — one real feature run end-to-end through the loop.

## What it does

GitHub holds code, Jira tracks work, Confluence stores documentation — and every AI helper wants to
be an IDE plugin. sdlc-squad is harness-agnostic instead. The files are plain Markdown, so any
runner — a CLI agent, an IDE chat, or a fully local model — loads a **role + shared context +
skill** and emits deterministic Markdown you paste where the work already lives. No server, no
daemon, no account, no API keys. Nothing leaves your machine.

## The squad

| Role | Owns | Reads | Hands off |
|---|---|---|---|
| **PMT** — Product Manager, Technical | user problem clarity, business outcomes, non-goals, acceptance criteria, phasing | customer intent, support signal, market context | PRD → TPM milestones, SDE feasibility |
| **TPM** — Technical Program Manager | cross-team dependencies, critical path, launch readiness, RAID | PRDs, design docs, team plans | program page → SDM sprint commitments |
| **SDM** — Software Development Manager | sustainable throughput, engineer capacity, scope trade-offs, operational health | roster, backlog, incident/toil history | sprint plan → committed tickets |
| **SDE** — Software Development Engineer | architecture, data/API contracts, edge cases, observability, rollback safety | PRD, designs, the actual repository code | RFC + sub-tasks + test plan + PR description |

## Quick start

1. Open any AI chat — a fully local model works.
2. Paste, in order: `shared/system-conventions.md`, `shared/glossary-and-org.md` (or your own
   `my-org.md`), the role file (`roles/sde.md`), and the skill
   (`skills/sde/technical-design-and-breakdown/SKILL.md`).
3. Give the inputs the skill asks for; answer its clarifying questions.
4. Get one Markdown contract, shaped by its output schema.
5. Paste it into Jira / Confluence / GitHub yourself. The kit never pushes anything anywhere.

Installing is optional: `pip install sdlc-squad` puts the kit on disk and `sdlc-squad` prints
its path — see [`usage/USER-GUIDE.md`](usage/USER-GUIDE.md). Cloning works the same.

## Two ways to run

1. **Any chat (paste).** Paste the four files in order — or one generated bundle
   (`make bundles`) — paste your inputs, answer ≤3 questions, get one artifact. Full
   recipe: [`usage/USER-GUIDE.md`](usage/USER-GUIDE.md), one worked run in full:
   [`usage/WALKTHROUGH.md`](usage/WALKTHROUGH.md).
2. **A repo-reading agent.** Open this repo in an agent that reads repo files (Claude Code,
   Cursor, Copilot, …) and just ask — *"run sdm sprint-planning with this input."* The
   repo's own agent files carry the load order:
   [`.github/copilot-instructions.md`](.github/copilot-instructions.md) points agents at
   [`AGENTS.md`](AGENTS.md).

## Why not just ask the chat directly?

A general chat will helpfully guess. The kit won't:

- **Unknowns are marked, never invented** — `[CONFIRM: ...]` wherever a source is missing.
- **Bound to a schema** — fixed sections, columns, ID prefixes, ISO dates.
- **One role per session** — no persona blending.
- **Ends with an import-target block** — where the artifact is meant to land.
- **Backed by evidence** — 20 fixtures, 97 recorded checks, and the defects it caught
  ([`docs/EVIDENCE.md`](docs/EVIDENCE.md)).

## The loop

```mermaid
flowchart LR
  PMT -->|PRD| TPM
  TPM -->|roadmap + dependencies| SDM
  SDM -->|sprint commitment| SDE
  SDE -->|RFC, tests, PR plan, deploy| TPM
```

One role per session; the artifact is the hand-off — see [`usage/RELAY.md`](usage/RELAY.md),
and the full chain in [`usage/FEATURE-RELAY.md`](usage/FEATURE-RELAY.md).

> **Import target = paste destination.** Artifacts name where they are meant to be pasted
> (a Jira issue, a Confluence page, a GitHub PR). GitHub and the Jira editor are
> paste-verified (spot check, Nov 2026 — `tests/results/run-2026-11-23-g3-real-paste.md`);
> Confluence and the Jira CSV import remain intended destinations until v0.1.x validates
> them ([`shared/destinations/`](shared/destinations/)).

## Layout

```
sdlc-squad/
├── README.md                        # This file
├── WHAT-THIS-IS.md                  # Charter: what it is, what it refuses
├── AGENTS.md                        # How an AI agent works in this repo
├── CONVENTIONS.md                   # File/format standards (the kit's rules)
├── ROADMAP.md                       # Build order + milestones
├── CHANGELOG.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── SUPPORT.md
├── pyproject.toml                   # pip install sdlc-squad (a file distribution)
├── PKG-README.md                    # The PyPI-facing page
├── MANIFEST.in
├── Makefile                         # build / check / upload (PyPI) · bundles / check-bundles
├── scripts/                          # Build & check scripts
│   ├── build-bundles.sh              # Generates usage/bundles/ (make bundles)
│   ├── check-links.py                # Fails on a broken relative link (make check-links)
│   └── check-frontmatter.py          # Validates roles/ + skills/ frontmatter
├── sdlc_squad/                      # The Python package: kit location CLI only
│   ├── __init__.py
│   └── cli.py                       # `sdlc-squad` prints the kit path + load order
│       (kit/ — the package copy of the kit — generated by `make sync`, gitignored)
├── usage/                            # How to run the kit
│   ├── USER-GUIDE.md                 # The 60-second run sheet + five-minute first run
│   ├── WALKTHROUGH.md                # One full run, start to finish
│   ├── RELAY.md                      # Moving an artifact role to role
│   ├── FEATURE-RELAY.md              # One feature across all four roles
│   ├── prompts-pmt.md                # Ready-to-paste prompts, all 6 PMT skills
│   ├── prompts-tpm.md                # Ready-to-paste prompts, all 4 TPM skills
│   ├── prompts-sdm.md                # Ready-to-paste prompts, all 5 SDM skills
│   ├── prompts-sde.md                # Ready-to-paste prompts, all 5 SDE skills
│   └── bundles/                      # Generated session bundles (make bundles) — do not edit
├── docs/
│   ├── README.md                     # Index of every docs/ page
│   ├── START-HERE.md                 # Find your skill by task + scenario recipes
│   ├── REVIEWING-OUTPUT.md           # Pre-paste checklist, claim tags, PII check
│   ├── ANTI-PATTERNS.md              # Failure modes + the rule that catches each
│   ├── EXPORTS.md                    # Getting input in + the redaction recipe
│   ├── TROUBLESHOOTING.md            # Recovery moves + the long-load recipe
│   ├── MODELS.md                     # Certify your model; the 60-second benchmark
│   ├── LIMITATIONS.md                # What the kit does not do
│   ├── EVIDENCE.md                   # How the kit catches itself
│   ├── EXAMPLES.md                   # All 20 fixtures + scenarios by company size
│   ├── TOOLS.md                      # Supported & adaptable matrix
│   ├── DESTINATION-PROFILES.md       # Map the kit to your Jira/Confluence/GitHub
│   ├── GITHUB-TEMPLATES.md           # Ready-to-copy PR/issue templates
│   ├── COMPANION-SKILLS.md           # Wrap other skill sets in kit conventions
│   ├── UPGRADING.md                  # Your files vs the kit's: safe upgrades
│   ├── PILOT.md                      # A 2-week, one-team trial
│   ├── EXTENDING.md                  # How to expand/customize: org, skill, role, schema
│   ├── 0.1.1-plans/                  # v0.1.1 patch plan, split by theme
│   ├── 0.1.2-plans/                  # v0.1.2 plan + implementation tracker
│   └── assets/                       # Repo social-preview card (social-preview.png + .svg)
├── field-test/                       # X2 validation: 4 real OSS repos run through the kit
│   ├── 01-kubernetes/                # kubernetes/kubernetes — platform
│   ├── 02-grafana/                   # grafana/grafana — observability
│   ├── 03-deno/                      # denoland/deno — runtime
│   └── 04-rust/                      # rust-lang/rust — language
├── LICENSE                           # MIT
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/
│   │   └── checks.yml               # CI: make gate on push/PR; release pack on a tag
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── copilot-instructions.md
├── shared/
│   ├── system-conventions.md        # Tool mapping (GitHub/Jira/Confluence), MD standards
│   ├── glossary-and-org.md          # Domain terms + org placeholders ([CONFIRM])
│   ├── glossary-and-org.EXAMPLE.md  # A filled example (fictional org) — never loaded
│   ├── raci.md                      # Decision-rights matrix (each role mirrors its column)
│   ├── destinations/                # Paste-destination contracts
│   │   ├── github.md
│   │   ├── jira.md
│   │   └── confluence.md
│   └── output-schemas/              # Canonical templates for downstream import
│       ├── confluence-prd-or-rfc.md
│       ├── jira-epic-and-stories.md
│       ├── sprint-plan-and-capacity.md
│       ├── technical-design-doc.md
│       └── test-plan-and-cases.md
├── roles/                            # Persona definitions (_TEMPLATE.md is the format)
│   ├── pmt.md
│   ├── tpm.md
│   ├── sdm.md
│   └── sde.md
├── skills/                           # One folder per skill; SKILL.md is the playbook
    ├── _TEMPLATE.md                  # The canonical skill stencil (new skills fill it)
    ├── pmt/
    │   ├── draft-prd/SKILL.md
    │   ├── slice-mvp-and-stories/SKILL.md
    │   ├── define-success-metrics/SKILL.md
    │   ├── customer-discovery-and-synthesis/SKILL.md
    │   ├── survey-design/SKILL.md
    │   └── prioritize-asks/SKILL.md
    ├── tpm/
    │   ├── program-roadmap-and-deps/SKILL.md
    │   ├── risk-raid-and-mitigations/SKILL.md
    │   ├── release-readiness-check/SKILL.md
    │   └── program-status-review/SKILL.md
    ├── sdm/
    │   ├── sprint-planning-and-capacity/SKILL.md
    │   ├── standup-execution/SKILL.md
    │   ├── scope-cut-and-tradeoffs/SKILL.md
    │   ├── operational-health-review/SKILL.md
    │   └── sprint-retro/SKILL.md
    └── sde/
        ├── technical-design-and-breakdown/SKILL.md
        ├── generate-test-ideas-and-cases/SKILL.md
        ├── pr-plan-and-rollback-notes/SKILL.md
        ├── design-and-code-reviews/SKILL.md
        └── deploy-plan-and-release/SKILL.md
└── tests/                            # Kit evidence: fixtures + recorded runs + CLI test
    ├── README.md
    ├── pmt/<skill>/fixture.md        # one fixture per skill (20 total)
    ├── tpm/<skill>/fixture.md
    ├── sdm/<skill>/fixture.md
    ├── sde/<skill>/fixture.md
    ├── cli/test_prompt.py            # the G1 CLI test
    ├── docs/                         # doc-check + docs-index tests (make test)
    └── results/                      # recorded runs: run-2026-11-22-v0.1.0.md · run-2026-11-23-g3-real-paste.md · run-2026-11-23-v0.1.1.md
```

## Skills

| Role | Skill | Produces | Import target | Status |
|---|---|---|---|---|
| PMT | [draft-prd](skills/pmt/draft-prd/SKILL.md) | PRD: problem, goals & non-goals, journeys, requirements, edge cases | Confluence PRD page | built |
| PMT | [slice-mvp-and-stories](skills/pmt/slice-mvp-and-stories/SKILL.md) | Epic summary + vertically sliced stories (Given/When/Then) | Jira bulk import | built |
| PMT | [define-success-metrics](skills/pmt/define-success-metrics/SKILL.md) | North star, supporting + guardrail metrics, instrumentation events | Confluence PRD / launch doc | built |
| PMT | [customer-discovery-and-synthesis](skills/pmt/customer-discovery-and-synthesis/SKILL.md) | Interview guide + feedback synthesis (past behavior, verbatim quotes) | Confluence research page; the user — runs the interviews | built |
| PMT | [survey-design](skills/pmt/survey-design/SKILL.md) | Bias-checked survey instrument + results read-back | the survey tool; Confluence research page | built |
| PMT | [prioritize-asks](skills/pmt/prioritize-asks/SKILL.md) | Ranked ask list on a stated framework (RICE or the org's) | Confluence decision log; Jira candidate backlog | built |
| TPM | [program-roadmap-and-deps](skills/tpm/program-roadmap-and-deps/SKILL.md) | Phases/milestones + cross-team dependency tables + critical path | Confluence program page, Jira links | built |
| TPM | [risk-raid-and-mitigations](skills/tpm/risk-raid-and-mitigations/SKILL.md) | RAID table with likelihood/impact, early warnings, fallbacks | Confluence weekly status | built |
| TPM | [release-readiness-check](skills/tpm/release-readiness-check/SKILL.md) | Go/no-go checklist: flags, migrations, alerts, rollback, sign-offs | Confluence launch doc | built |
| TPM | [program-status-review](skills/tpm/program-status-review/SKILL.md) | Bi-weekly/monthly R/Y/G rollup of all items vs objectives/Jira milestones | Confluence program status page | built |
| SDM | [sprint-planning-and-capacity](skills/sdm/sprint-planning-and-capacity/SKILL.md) | Per-engineer net focus capacity + commitment split + risk flags | Confluence sprint note, Jira backlog | built |
| SDM | [scope-cut-and-tradeoffs](skills/sdm/scope-cut-and-tradeoffs/SKILL.md) | Ranked keep/defer/cut options with impact on value, risk, milestones | Confluence decision log | built |
| SDM | [operational-health-review](skills/sdm/operational-health-review/SKILL.md) | Recurring bugs / toil / flaky-test summary + remediation tickets | Confluence retro/ops doc, Jira | built |
| SDM | [sprint-retro](skills/sdm/sprint-retro/SKILL.md) | The last 2 sprints' done tickets → went-well/hurt/change + action items | Confluence retro page; Jira action items | built |
| SDM | [standup-execution](skills/sdm/standup-execution/SKILL.md) | Daily round format + blocker log (aging, escalation, carry-risk) | Confluence standup page; Jira blockers | built |
| SDE | [technical-design-and-breakdown](skills/sde/technical-design-and-breakdown/SKILL.md) | RFC section + Jira-ready sub-tasks with Definition of Done | Confluence RFC, GitHub issue, Jira | built |
| SDE | [generate-test-ideas-and-cases](skills/sde/generate-test-ideas-and-cases/SKILL.md) | Test matrix by layer: unit → E2E → failure injection | Jira QA checklist, PR test plan | built |
| SDE | [pr-plan-and-rollback-notes](skills/sde/pr-plan-and-rollback-notes/SKILL.md) | PR checklist + verification + migration order + rollback steps | GitHub PR description | built |
| SDE | [design-and-code-reviews](skills/sde/design-and-code-reviews/SKILL.md) | Author + reviewer checklists (split small, self-review first, nit: etiquette) | GitHub PR template; Confluence review standards | built |
| SDE | [deploy-plan-and-release](skills/sde/deploy-plan-and-release/SKILL.md) | Deploy/release split, canary stages, rollback triggers, flag ledger | GitHub release issue; Confluence runbook | built |

## What it never does

- Never pushes to Jira, Confluence, or GitHub. It exports Markdown; you import it.
- Never invents ticket keys, epic IDs, dates, owner names, or sprint numbers. Unknowns are marked
  `[CONFIRM: ...]` for you to fill.
- Never fetches a URL, calls a tool, or sends telemetry. Offline by design.
- Never claims a planned skill is built. Every `SKILL.md` carries its own `status` in frontmatter.

## License

MIT — see [LICENSE](LICENSE). Public as of v0.1.0.