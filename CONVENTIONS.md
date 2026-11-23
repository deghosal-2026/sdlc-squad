# CONVENTIONS.md — sdlc-squad standards

The kit's file and format rules. The charter ([`WHAT-THIS-IS.md`](WHAT-THIS-IS.md)) overrides
this file. When a skill's playbook and this file disagree, the charter decides.

## Repo layout

```
roles/<role>.md                     # one persona file per role: pmt, tpm, sdm, sde
skills/<role>/<skill>/SKILL.md      # one folder per skill; SKILL.md is the playbook
shared/system-conventions.md        # tool mapping + Markdown output standards
shared/glossary-and-org.md          # domain terms + org placeholders
shared/output-schemas/<name>.md     # canonical templates; skills bind to these, never re-invent
```

- A **role** file defines perspective, priorities, decision boundaries, tone, default
  assumptions, and handoff contracts. It never contains steps.
- A **skill** file defines steps, required inputs, clarifying questions, and its output binding.
  It never redefines the persona; it inherits the role.

## Frontmatter (every content file)

```yaml
---
name: draft-prd          # kebab-case, matches the folder
role: pmt                # owning role (skills only)
status: planned          # planned | in-progress | built
created: YYYY-MM-DD
---
```

`status` is the honesty mechanism: `planned` files are skeletons and say so in the body; flipping
to `built` requires the skill's fixtures/examples to exist and to have been exercised.

## Naming

- Folders: `kebab-case`. Skills: verb-first (`draft-prd`, `slice-mvp-and-stories`).
- No spaces anywhere; no vendor product names in folder names.

## Markdown contracts (output rules)

- One artifact per skill run. The artifact ends with an **Import target** block.
- Headings, tables, and ID prefixes come from the bound schema in `shared/output-schemas/`.
- Common ID prefixes: requirements `REQ-n`, acceptance criteria `AC-n`, stories `US-n`, tasks
  `T-n`, risks `R-n`, dependencies `DEP-n`, metrics `M-n`, test cases `TC-n`.
- Acceptance criteria are Given/When/Then. Dates are ISO `YYYY-MM-DD`. Owner cells hold real
  names or `[CONFIRM: owner]` — never role titles presented as people.
- No HTML, no emoji in tables, no collapsible sections — Confluence and Jira paste must be clean.

## Honesty discipline

- `[CONFIRM: ...]` marks every unknown the artifact needed. An artifact with zero `[CONFIRM]`s and
  zero user-supplied inputs is a defect: something was invented.
- No benchmark, "industry standard," or velocity number appears without the user's own data behind
  it.
- The kit never claims an artifact is synced anywhere. Import state is the user's fact.

## Privacy

- Skills may ask for rosters, backlogs, and design context — remind the user to redact customer
  personal data before pasting.
- Generated artifacts are the user's to save; the kit keeps nothing, sends nothing.

## Testing

- Every built skill ships with fixtures: representative inputs and expected artifact shapes
  (per its output schema), stored under `tests/` when the skill is built (see ROADMAP).
- A skill without fixtures is a guess, not a skill.