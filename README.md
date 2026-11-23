# sdlc-squad

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![100% Markdown](https://img.shields.io/badge/100%25_Markdown-2ea44f)](#what-it-does)
[![Privacy](https://img.shields.io/badge/Privacy-local_only,_no_telemetry-8b5cf6)](#what-it-does)
[![Status: private scaffold](https://img.shields.io/badge/status-private_scaffold-8b5cf6)](#status)
[![Roles](https://img.shields.io/badge/roles-4-2ea44f)](#the-squad)
[![Skills](https://img.shields.io/badge/skills-12_scaffolded-2ea44f)](#skills)

> A software team in a box. Four AI personas — **PMT (Product Manager, Technical), TPM, SDM, SDE** —
> each with a playbook of skills, loaded into any AI chat. Each skill turns fuzzy input into one
> clean Markdown contract — a PRD, a program roadmap, a sprint capacity plan, a technical design,
> a test matrix, a PR description — copy-paste ready for **Confluence, Jira, and GitHub**.

## Status

**Private scaffold** — created 2026-11-22. In place: the repo, the four role personas
(`roles/`), the shared conventions and glossary, and the five canonical output schemas
(`shared/output-schemas/`). The twelve skills exist as reviewed skeletons (`status: planned` in
each `SKILL.md` frontmatter). The kit builds in the order its [charter](WHAT-THIS-IS.md) sets —
core loop first, a real feature run end-to-end, then the remaining skills. A public OSS release is
planned; the community files (LICENSE, CONTRIBUTING, SECURITY, SUPPORT, CODE_OF_CONDUCT) are
already in place. Build order and milestones: [ROADMAP.md](ROADMAP.md).

## What it does

GitHub holds code, Jira tracks work, Confluence stores documentation — and every AI helper wants to
be an IDE plugin. sdlc-squad is harness-agnostic instead. The files are plain Markdown, so any
runner — a CLI agent, an IDE chat, or a fully local model — loads a **role + shared context +
skill** and emits deterministic Markdown you paste where the work already lives. No install, no
account, no API keys. Nothing leaves your machine.

## The squad

| Role | Owns | Reads | Hands off |
|---|---|---|---|
| **PMT** — Product Manager, Technical | user problem clarity, business outcomes, non-goals, acceptance criteria, phasing | customer intent, support signal, market context | PRD → TPM milestones, SDE feasibility |
| **TPM** — Technical Program Manager | cross-team dependencies, critical path, launch readiness, RAID | PRDs, design docs, team plans | program page → SDM sprint commitments |
| **SDM** — Software Development Manager | sustainable throughput, engineer capacity, scope trade-offs, operational health | roster, backlog, incident/toil history | sprint plan → committed tickets |
| **SDE** — Software Development Engineer | architecture, data/API contracts, edge cases, observability, rollback safety | PRD, designs, the actual repository code | RFC + sub-tasks + test plan + PR description |

## Quick start

1. Open any AI chat — a fully local model works.
2. Paste, in order: `shared/system-conventions.md`, the role file (`roles/sde.md`), and the skill
   (`skills/sde/technical-design-and-breakdown/SKILL.md`).
3. Give the inputs the skill asks for; answer its clarifying questions.
4. Get one Markdown contract, shaped by its output schema.
5. Paste it into Jira / Confluence / GitHub yourself. The kit never pushes anything anywhere.

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
├── USER-GUIDE.md
├── LICENSE                           # MIT
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── copilot-instructions.md
├── shared/
│   ├── system-conventions.md        # Tool mapping (GitHub/Jira/Confluence), MD standards
│   ├── glossary-and-org.md          # Domain terms + org placeholders ([CONFIRM])
│   └── output-schemas/              # Canonical templates for downstream import
│       ├── confluence-prd-or-rfc.md
│       ├── jira-epic-and-stories.md
│       ├── sprint-plan-and-capacity.md
│       ├── technical-design-doc.md
│       └── test-plan-and-cases.md
├── roles/                            # Persona definitions
│   ├── pmt.md
│   ├── tpm.md
│   ├── sdm.md
│   └── sde.md
└── skills/                           # One folder per skill; SKILL.md is the playbook
    ├── pmt/
    │   ├── draft-prd/SKILL.md
    │   ├── slice-mvp-and-stories/SKILL.md
    │   └── define-success-metrics/SKILL.md
    ├── tpm/
    │   ├── program-roadmap-and-deps/SKILL.md
    │   ├── risk-raid-and-mitigations/SKILL.md
    │   └── release-readiness-check/SKILL.md
    ├── sdm/
    │   ├── sprint-planning-and-capacity/SKILL.md
    │   ├── scope-cut-and-tradeoffs/SKILL.md
    │   └── operational-health-review/SKILL.md
    └── sde/
        ├── technical-design-and-breakdown/SKILL.md
        ├── generate-test-ideas-and-cases/SKILL.md
        └── pr-plan-and-rollback-notes/SKILL.md
```

## Skills

| Role | Skill | Produces | Import target | Status |
|---|---|---|---|---|
| PMT | [draft-prd](skills/pmt/draft-prd/SKILL.md) | PRD: problem, goals & non-goals, journeys, requirements, edge cases | Confluence PRD page | planned |
| PMT | [slice-mvp-and-stories](skills/pmt/slice-mvp-and-stories/SKILL.md) | Epic summary + vertically sliced stories (Given/When/Then) | Jira bulk import | planned |
| PMT | [define-success-metrics](skills/pmt/define-success-metrics/SKILL.md) | North star, supporting + guardrail metrics, instrumentation events | Confluence PRD / launch doc | planned |
| TPM | [program-roadmap-and-deps](skills/tpm/program-roadmap-and-deps/SKILL.md) | Phases/milestones + cross-team dependency tables + critical path | Confluence program page, Jira links | planned |
| TPM | [risk-raid-and-mitigations](skills/tpm/risk-raid-and-mitigations/SKILL.md) | RAID table with likelihood/impact, early warnings, fallbacks | Confluence weekly status | planned |
| TPM | [release-readiness-check](skills/tpm/release-readiness-check/SKILL.md) | Go/no-go checklist: flags, migrations, alerts, rollback, sign-offs | Confluence launch doc | planned |
| SDM | [sprint-planning-and-capacity](skills/sdm/sprint-planning-and-capacity/SKILL.md) | Per-engineer net focus capacity + commitment split + risk flags | Confluence sprint note, Jira backlog | planned |
| SDM | [scope-cut-and-tradeoffs](skills/sdm/scope-cut-and-tradeoffs/SKILL.md) | Ranked keep/defer/cut options with impact on value, risk, milestones | Confluence decision log | planned |
| SDM | [operational-health-review](skills/sdm/operational-health-review/SKILL.md) | Recurring bugs / toil / flaky-test summary + remediation tickets | Confluence retro/ops doc, Jira | planned |
| SDE | [technical-design-and-breakdown](skills/sde/technical-design-and-breakdown/SKILL.md) | RFC section + Jira-ready sub-tasks with Definition of Done | Confluence RFC, GitHub issue, Jira | planned |
| SDE | [generate-test-ideas-and-cases](skills/sde/generate-test-ideas-and-cases/SKILL.md) | Test matrix by layer: unit → E2E → failure injection | Jira QA checklist, PR test plan | planned |
| SDE | [pr-plan-and-rollback-notes](skills/sde/pr-plan-and-rollback-notes/SKILL.md) | PR checklist + verification + migration order + rollback steps | GitHub PR description | planned |

## What it never does

- Never pushes to Jira, Confluence, or GitHub. It exports Markdown; you import it.
- Never invents ticket keys, epic IDs, dates, owner names, or sprint numbers. Unknowns are marked
  `[CONFIRM: ...]` for you to fill.
- Never fetches a URL, calls a tool, or sends telemetry. Offline by design.
- Never claims a planned skill is built. Every `SKILL.md` carries its own `status` in frontmatter.

## License

MIT — see [LICENSE](LICENSE). Private today; public OSS release planned ([roadmap](ROADMAP.md)).