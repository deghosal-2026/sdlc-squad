<!--
SKILL TEMPLATE — the canonical skill format.

To add a skill: create skills/<role>/<skill-name>/SKILL.md from this file, fill
every [bracketed] slot, delete this comment block, then bind the skill to its
row(s) in shared/raci.md and add its prompt to usage/prompts-<role>.md.
A shipped skill contains no [brackets].

Standing rules for every SKILL.md:
- Frontmatter: name (kebab-case, matches the folder), description (one line:
  what one run produces — harnesses route on it), role, status, created.
- Steps live here; persona lives in roles/<role>.md. Never restate the persona.
- Output binds to a schema in shared/output-schemas/ or the table rules in
  shared/system-conventions.md — never invent a second schema.
- status flips to built only when the skill's fixture exists AND its recorded
  run is logged under tests/results/.
-->

---
name: [kebab-case-skill-name]
description: [One line: what one run produces. Harnesses route on this.]
role: [pmt | tpm | sdm | sde]
status: [planned | built]
created: YYYY-MM-DD
---

# [skill-name] — [one-line artifact name]

> **Status: [planned | built]** — planned means skeleton: contracts below are
> binding, steps are outline only.

## What it produces

[One artifact per run, named and bound. If a run could produce two, it is two
skills or two runs — say which.]

## RACI row

`[row name from shared/raci.md]` — **[ROLE] A/R** (`shared/raci.md`); [other
roles' C/I cells, verbatim from the matrix].

## Inputs required

- [Every input the skill needs before it can run; mark which are paste-shaped
  and which come from the user's own facts]

## Clarifying questions when inputs are missing

Ask up to 3, then draft anyway with `[CONFIRM]`:

1. [A question that fills the biggest gap — not a questionnaire]

## Steps

1. **[Verb.]** [One step. Each step is checkable; the read-back pass is
   always the last step before hand-over.]
[…]

## Output binding

[The exact schema file or table rules this artifact follows — verbatim
reference, never a re-invention.]

## Import target

[GitHub / Jira / Confluence — the place this Markdown is pasted, per its
schema's Import-target block.]

## Worked example

[`tests/<role>/<skill-name>/fixture.md`] — full input + expected artifact
(synthetic end to end). Recorded run:
[`tests/results/run-[date].md`].