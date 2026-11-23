# User guide — running sdlc-squad in any AI chat

No account, no API key, nothing leaves your machine. The kit is a set of Markdown files; your
chat is the runtime. Get the files either way:

```bash
pip install sdlc-squad && sdlc-squad   # prints the kit path + the load order below
# or: git clone https://github.com/deghosal-2026/sdlc-squad
```

The package is a file distribution — `pip install` only puts the Markdown on disk
([PyPI](https://pypi.org/project/sdlc-squad/)); there is no server, no runner, no telemetry.

## The 60-second version

1. Open any AI chat — including a fully local model; nothing leaves your machine.
2. Paste four files in order:
   1. `shared/system-conventions.md` — the tool mapping and output standards,
   2. `shared/glossary-and-org.md` — your org slots (Jira key, sprint length, on-call…).
      Use the shipped template for a trial, or paste your own filled copy kept **outside
      the kit** (`my-org.md` — see [`../docs/UPGRADING.md`](../docs/UPGRADING.md)) so
      upgrades never clobber it,
   3. `roles/<role>.md` — the persona (say `roles/sdm.md`),
   4. `skills/<role>/<skill>/SKILL.md` — the playbook.
3. Give the inputs the skill's **Inputs required** section asks for, and answer its clarifying
   questions (up to 3).
4. You get one Markdown artifact, ending with an **Import target** block: paste it into the
   Confluence page, Jira issue, or GitHub PR it names.

## Try it in five minutes (no real data needed)

One skill, end to end, using the fictional sample in the prompt book — the company
(Meridian Outfitters) is invented.

1. `pip install sdlc-squad && sdlc-squad` — it prints the kit path and the load order.
2. In any AI chat, paste four files in order: `shared/system-conventions.md`,
   `shared/glossary-and-org.md` (or your `my-org.md`), `roles/sdm.md`,
   `skills/sdm/sprint-planning-and-capacity/SKILL.md`.
3. Paste the sample input from [`prompts-sdm.md`](prompts-sdm.md) §1.
4. Answer the skill's ≤3 questions; you get one sprint-plan artifact.
5. Resolve its `[CONFIRM]`s with real facts before pasting it where the import-target
   block says.

**Pre-flight for real runs:** four files in order (or one bundle) · glossary state known
(template is fine to try; your `my-org.md` for real work, see
[`../docs/UPGRADING.md`](../docs/UPGRADING.md)) · inputs redacted (the redaction recipe
ships in `docs/EXPORTS.md` §Redaction, once that item lands).

## Two ways to run

1. **Any chat (paste)** — the load in "The 60-second version" above.
2. **A repo-reading agent** — open the kit repo and just ask; the repo's own agent files
   (`.github/copilot-instructions.md` → `AGENTS.md`) carry the load order.

## Data path — what leaves your machine

The kit transmits nothing and stores nothing: no network, no telemetry, no files written.
But the **runtime is the chat you choose** — if it is a hosted service, that provider's
data handling applies to whatever you paste. For sensitive input, use a fully local model,
or redact first (recipe: [`../docs/EXPORTS.md`](../docs/EXPORTS.md) §Redaction). The sample
inputs in the prompt books exist so a first run needs **no real data**. (This is the full
statement; [`../SECURITY.md`](../SECURITY.md) links here rather than repeat it.)

> **Import target = the paste destination.** The artifact names where it is meant to be
> pasted. GitHub and the Jira editor are paste-verified (spot check, Nov 2026 —
> `tests/results/run-2026-11-23-g3-real-paste.md`); Confluence and the Jira CSV import
> remain intended destinations until v0.1.x validates them.

## Copy-paste prompts for every task

[`prompts-pmt.md`](prompts-pmt.md) · [`prompts-tpm.md`](prompts-tpm.md) ·
[`prompts-sdm.md`](prompts-sdm.md) · [`prompts-sde.md`](prompts-sde.md) — one ready-to-paste
prompt per skill (all 20), with the files to load, realistic sample input, and the import
target. Start from the sample, swap in your real (redacted) facts.

## Choosing a role

- You have a fuzzy problem statement and need requirements → **PMT**.
- You have multiple teams and need a roadmap, dependency plan, RAID, status review, or launch
  checklist → **TPM**.
- You need a sprint commitment that survives PTO, on-call, and carry-over — or standups,
  retros, scope cuts, ops health → **SDM**.
- You need a design, a task breakdown, tests, a PR plan, review checklists, or a deploy
  plan → **SDE**.

Not sure? Paste [`../README.md`](../README.md) and ask the chat. It lists all four with their
ownership.

## While you work

- Redact first. Rosters, backlogs, and designs are fine to paste; customer personal data is
  not. The chat will ask you to redact, not to skip.
- Watch for `[CONFIRM: ...]` in the artifact — every one is a fact the kit needed and you
  still owe it. An artifact with no `[CONFIRM]`s and no inputs from you probably invented
  something.
- One role per session. Two personas in one context blur each other; run the relay instead —
  PMT → TPM → SDM → SDE, each handing its artifact to the next.
- The chat will not push anything anywhere. You are the import mechanism — that is the
  design.

## Saving your work

Artifacts are yours. Save them wherever your work lives; if you keep them inside a local copy
of this repo, use the git-ignored `output/` folder — its contents are never committed.

## Skill status

Every `SKILL.md` says `status` in its frontmatter. All twenty are `built` at
[`v0.1.0`](https://github.com/deghosal-2026/sdlc-squad/releases/tag/v0.1.0) — each with its
fixture under `tests/` and its recorded run under `tests/results/`.

## Extending and customizing

Filling the kit for your org, adding a skill, adding a role, or changing an artifact schema —
see [`docs/EXTENDING.md`](../docs/EXTENDING.md): the four paths, the standing rules, and the
failure modes each path is prone to.