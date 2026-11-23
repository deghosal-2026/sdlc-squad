# sdlc-squad

[![PyPI](https://img.shields.io/pypi/v/sdlc-squad)](https://pypi.org/project/sdlc-squad/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/deghosal-2026/sdlc-squad/blob/main/LICENSE)
[![100% Markdown](https://img.shields.io/badge/100%25_Markdown-2ea44f)](https://github.com/deghosal-2026/sdlc-squad#what-it-does)
[![Privacy](https://img.shields.io/badge/Privacy-local_only,_no_telemetry-8b5cf6)](https://github.com/deghosal-2026/sdlc-squad#what-it-does)

A software team in a box. Four AI personas — **PMT (Product Manager, Technical), TPM, SDM, SDE** —
each with a playbook of skills, run in any AI chat. Each skill turns fuzzy input into one clean
Markdown contract — a PRD, a program roadmap, a sprint capacity plan, a technical design, a test
matrix, a PR description — copy-paste ready for **Confluence, Jira, and GitHub**.

## Install

```bash
pip install sdlc-squad
sdlc-squad
```

The package is a **file distribution**: `pip install` puts the whole kit on disk, and
`sdlc-squad` prints where it landed plus the per-session load order. That is the entire CLI —
no server, no code path beyond locating the files, no telemetry. Upgrade with
`pip install --upgrade sdlc-squad`, or skip the package entirely and clone the repo: the kit
is the Markdown, not the install. Upgrades replace the kit files — keep your filled org
glossary **outside** the kit (`my-org.md`; see `docs/UPGRADING.md`) so it survives.

## Run a session

1. Open any AI chat — a fully local model works.
2. Paste, in order: `shared/system-conventions.md`, `shared/glossary-and-org.md` (fill your
   org's slots), the role file (`roles/sdm.md`), then the skill (`skills/<role>/<skill>/SKILL.md`).
3. Paste the skill's inputs — redact personal data first — and answer its ≤3 clarifying questions.
4. Take the one artifact and paste it where its **Import target** block says.

`usage/prompts-<role>.md` ships a ready-to-paste prompt for **every** skill (20).
`docs/EXTENDING.md` covers customizing for your org, adding skills, roles, and schemas.

## What it never does

- Never pushes to Jira, Confluence, or GitHub — you import the Markdown.
- Never invents ticket keys, dates, or owner names — unknowns are `[CONFIRM: ...]`.
- Never fetches, calls, or transmits anything — offline by design.

20 skills · 4 roles · 21 RACI rows · MIT — [github.com/deghosal-2026/sdlc-squad](https://github.com/deghosal-2026/sdlc-squad)