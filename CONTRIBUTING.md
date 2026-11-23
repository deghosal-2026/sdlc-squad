# Contributing to sdlc-squad

sdlc-squad is a Markdown-only kit: instructions, rubrics, personas, and schemas. There is no code
to build and no test suite to run — the "tests" are fixtures, and the product is a Markdown file
that behaves the same in any AI chat.

**Adding a skill, a role, or changing a schema?** Follow
[`docs/EXTENDING.md`](docs/EXTENDING.md) — the four contribution paths, in the order to do them,
with the standing rules (mirror rule, one canonical copy, honest statuses) baked in.

## The ground rules

1. Read [`WHAT-THIS-IS.md`](WHAT-THIS-IS.md) (the charter) and [`CONVENTIONS.md`](CONVENTIONS.md)
   before proposing anything. The charter overrides all of us.
2. Skills bind to the canonical schemas in `shared/output-schemas/`. Never add a second copy of a
   schema, a table shape, or an ID prefix — extend the schema in place instead.
3. `[CONFIRM]` over invention, in the kit and in any artifact a skill produces. No invented
   ticket keys, dates, owner names, or "industry standard" numbers.
4. `status` in a `SKILL.md` frontmatter is honest: `planned` means skeleton, `built` means the
   acceptance in its ROADMAP ticket was actually exercised.

## What contributions look like

- **A new skill** — open an issue first with the role, the input, the output contract, and the
  import target. A skill without an output binding will not be accepted.
- **A schema fix** — show the artifact it broke on a real Confluence/Jira/GitHub paste.
- **A persona correction** — cite the line in the role file; personas are opinionated on purpose,
  so explain the trade-off, not just the wording.

## Mechanics

- One skill per PR. Fixtures/examples land in the same PR as the skill.
- A `CHANGELOG.md` entry in the same PR as the change.
- Markdown lint-clean: no HTML in tables, no emoji-as-icons, ISO dates.

By contributing you agree your contribution is MIT-licensed, same as the kit. See
[`LICENSE`](LICENSE) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).