# AGENTS.md — sdlc-squad

Instructions for any AI agent or assistant that can read this repository. The kit charter
([`WHAT-THIS-IS.md`](WHAT-THIS-IS.md)) overrides this file. `CONVENTIONS.md` defines file and
format standards.

## What this repo is

A private, Markdown-only kit of AI personas (roles) and work skills for the SDLC. No code runs
here. Every `SKILL.md` with `status: planned` is a skeleton — see [ROADMAP.md](ROADMAP.md) before
believing or running anything under `skills/`.

## Working WITH the kit (producing artifacts for a user)

1. Read the charter ([`WHAT-THIS-IS.md`](WHAT-THIS-IS.md)) first.
2. Identify the role the user needs: PMT, TPM, SDM, or SDE. If unclear, ask one short question —
   do not guess.
3. Load, in order: `shared/system-conventions.md`, `shared/glossary-and-org.md` (placeholders are
   `[CONFIRM]` inputs, not facts), the role file (`roles/<role>.md`), then the skill
   (`skills/<role>/<skill>/SKILL.md`).
4. Run the skill per its own steps; ask its clarifying questions when inputs are missing.
5. Emit exactly one artifact, bound to its `shared/output-schemas/` schema, ending with its
   import-target block.

## Always

- `[CONFIRM]` over invention: never invent Jira keys, epic IDs, story points, dates, owner names,
  sprint numbers, service names, or SLAs.
- ISO dates (`YYYY-MM-DD`), tables exactly per the schema's columns, plain copy-paste Markdown.
- Name the input file/repo/doc behind every claim you can; mark what you could not check.
- Stay offline: never fetch, click, open, or transmit anything.
- The user decides everything: hand over the artifact, answer questions, wait.

## Never

- Never push to, authenticate with, or call Jira, Confluence, GitHub, or any API.
- Never present a `status: planned` skill as built.
- Never invent "industry standard" numbers, benchmarks, or velocity figures.
- Never commit or push anything from an ignored output directory (user working notes).

## Working ON the kit (building it)

- Follow [ROADMAP.md](ROADMAP.md) order; one skill per ticket, its fixtures/examples written with
  it, its `status` flipped only when its acceptance is actually exercised.
- Shared files (`CONVENTIONS.md`, `shared/`) are single sources of truth — update them in the same
  change that needs them; never fork a parallel schema.
- `CHANGELOG.md` gets an entry in the same commit as the change.
- Confirm the plan with the user before restructuring anything.