# What this is — the sdlc-squad charter

sdlc-squad is a Markdown-only kit of AI personas and work skills for the software development
lifecycle. It has no code, no server, and no installer: the files are instructions, and any AI
chat — including a fully local model — runs them. This charter overrides every other file in the
repo, including `AGENTS.md` and `CONVENTIONS.md`.

## What it is

- **Four roles.** PMT (Product Manager, Technical), TPM (Technical Program Manager), SDM
  (Software Development Manager), SDE (Software Development Engineer). Each role file defines its
  persona: objective, lens, source-of-truth mapping, consumes/produces/depends-on contracts,
  decision rights (its RACI column), boundaries. One role per session — personas blur in a
  shared context.
- **Twenty skills.** PMT 6 · TPM 4 · SDM 5 · SDE 5. Each skill is a step-by-step playbook:
  required inputs, clarifying questions, execution steps, and one exact output structure bound
  to a canonical schema in `shared/output-schemas/`.
- **Markdown contracts.** Every run of a skill produces one artifact — a PRD, a roadmap, a sprint
  plan, a design, a test matrix, a PR description — formatted for its import target: a Confluence
  page, a Jira epic/story set, or a GitHub issue/PR.
- **Harness-agnostic.** Nothing assumes a particular IDE, agent, or vendor. Paste the files into
  whatever chat you already use.

## Who it is for

Engineers, PMs, program managers, and engineering managers who live in GitHub, Jira, and
Confluence, and want their AI chat to produce work products that look like their work products —
not prose, not screenshots, not vendor exports.

## What it is not

- **Not a client for anything.** It never authenticates to, pushes to, or reads from Jira,
  Confluence, or GitHub. It writes Markdown; the user imports it.
- **Not a source of truth for your org.** Team names, service names, Jira project keys, SLAs,
  escalation paths, and dates are inputs you supply. Anything missing is marked
  `[CONFIRM: ...]`, never guessed.
- **Not a code generator.** SDE skills produce designs, contracts, and task breakdowns grounded in
  your repository — not implementation.
- **Not a predictor.** No story-point or date promises without your own historical data behind
  them; capacity math is arithmetic on numbers you provide, and the assumptions are shown.

## The contract every skill keeps

1. One artifact per run, bound to its output schema.
2. Every table follows its schema's columns; every claim carries its source; every unknown is
   `[CONFIRM: ...]`.
3. Dates are ISO (`YYYY-MM-DD`); owners are real names or `[CONFIRM]`, never invented.
4. No network. Nothing is fetched, clicked, opened, or transmitted.
5. The artifact ends with its import-target block — where this Markdown is meant to be pasted.
6. `status: built` means the skill's fixture exists under `tests/` and its run is recorded under
   `tests/results/` — a status without evidence is a defect, and a `built` skill is never
   presented as planned.