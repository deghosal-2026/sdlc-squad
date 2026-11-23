# User guide — running sdlc-squad in any AI chat

No install, no account, no API key. The kit is a set of Markdown files; your chat is the runtime.

## The 60-second version

1. Open any AI chat — including a fully local model; nothing leaves your machine.
2. Paste three or four files in order:
   1. `shared/system-conventions.md` — the tool mapping and output standards,
   2. `shared/glossary-and-org.md` — fill your org slots (Jira key, sprint length, on-call…),
   3. `roles/<role>.md` — the persona (say `roles/sdm.md`),
   4. `skills/<role>/<skill>/SKILL.md` — the playbook.
3. Give the inputs the skill's **Inputs required** section asks for, and answer its clarifying
   questions (up to 3).
4. You get one Markdown artifact, ending with an **Import target** block: paste it into the
   Confluence page, Jira issue, or GitHub PR it names.

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