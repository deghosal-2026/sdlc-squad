# User guide — running sdlc-squad in any AI chat

No install, no account, no API key. The kit is a set of Markdown files; your chat is the runtime.

## The 60-second version

1. Open any AI chat — including a fully local model; nothing leaves your machine.
2. Paste three files in order:
   1. `shared/system-conventions.md` — the tool mapping and output standards,
   2. `roles/<role>.md` — the persona (say `roles/sdm.md`),
   3. `skills/<role>/<skill>/SKILL.md` — the playbook.
3. Give the inputs the skill's **Inputs required** section asks for, and answer its clarifying
   questions.
4. You get one Markdown artifact, ending with an **Import target** block: paste it into the
   Confluence page, Jira issue, or GitHub PR it names.

## Choosing a role

- You have a fuzzy problem statement and need requirements → **PMT**.
- You have multiple teams and need a roadmap, dependency plan, or launch checklist → **TPM**.
- You need a sprint commitment that survives PTO, on-call, and carry-over → **SDM**.
- You need a design, a task breakdown, tests, or a PR plan → **SDE**.

Not sure? Paste `README.md` and ask the chat. It lists all four with their ownership.

## While you work

- Redact first. Rosters, backlogs, and designs are fine to paste; customer personal data is not.
  The chat will ask you to redact, not to skip.
- Watch for `[CONFIRM: ...]` in the artifact — every one is a fact the kit needed and you
  still owe it. An artifact with no `[CONFIRM]`s and no inputs from you probably invented
  something.
- The chat will not push anything anywhere. You are the import mechanism — that is the design.

## Saving your work

Artifacts are yours. Save them wherever your work lives; if you keep them inside a local copy of
this repo, use the git-ignored `output/` folder — its contents are never committed.

## Skill status

Every `SKILL.md` says `status` in its frontmatter. `planned` means the skeleton exists but the
playbook is not written yet — see [`ROADMAP.md`](ROADMAP.md) for what is buildable today.