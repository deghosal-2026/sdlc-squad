# Extending and customizing sdlc-squad

The kit is designed to be forked, trimmed, and grown. This guide covers the four ways
people change it — in the order you should do them. The standing rules first; they
govern every path below.

## Standing rules (all paths)

1. **One canonical copy of everything.** RACI lives once (`shared/raci.md`), each output
   schema once (`shared/output-schemas/`), each role's handoffs once (its role file).
   Any second copy is drift waiting to happen — extend in place, never fork a file.
2. **The mirror rule.** A change to `shared/raci.md` and the matching role file(s)
   lands in **one commit** — same for schemas and the skills that bind them.
3. **`[CONFIRM]` over invention.** Anything your org hasn't supplied stays
   `[CONFIRM: ...]` — Jira keys, dates, owner names, SLAs, benchmarks. The kit ships
   org-agnostic on purpose; your fork fills the org glossary — keep your filled copy
   **outside the kit** (`my-org.md`; see [`UPGRADING.md`](UPGRADING.md)) — not the
   skills.
4. **Statuses stay honest.** `status: planned` means skeleton; `built` means the fixture
   exists **and** the run is recorded under `tests/results/`. Never flip a status on
   intention.
5. **One role per session.** Personas blur in a shared context — when your change
   touches two roles, that's the relay, not a merged persona.

## Path 1 — Customize for your org (no new skills)

The fastest path: fill the placeholders and rename nothing.

1. **The org glossary** — copy the shipped `shared/glossary-and-org.md` to your own file
   **outside the kit** (`my-org.md`) and fill every `[CONFIRM: ...]` slot with your
   facts: Jira project key, Confluence space, sprint length, ceremonies and hours,
   on-call rotation, support expectations, escalation path, SLAs, estimate scale and
   its legend. This is the intended single customization point — skills and roles
   read it at session start and never hardcode org facts. Keeping your copy outside the
   kit is what survives upgrades ([`UPGRADING.md`](UPGRADING.md)).
2. **`shared/system-conventions.md`** — only if your tooling differs: e.g. you use
   Azure DevOps + Confluence instead of GitHub + Jira. Edit the source-of-truth table
   and the import-target language; the skills inherit.
3. **Renaming services/teams in fixtures** — don't. Fixtures are synthetic on
   purpose. Your *real* runs will name your real services; the committed kit stays
   org-neutral.

## Path 2 — Add a skill (to an existing role)

The contribution path. In one commit:

1. **Stencil it.** `cp skills/_TEMPLATE.md skills/<role>/<new-skill>/SKILL.md` — frontmatter
   (`name`, `description` — harnesses route on it, `role`, `status: planned`,
   `created`), then fill every section: what it produces, RACI row, inputs, ≤3
   clarifying questions, steps, output binding, import target.
2. **RACI first, skill second.** If the skill introduces a *new decision*, add the
   row to `shared/raci.md` (exactly one **A** — the owning role), and mirror the row
   into **all four** role files' `## Decision rights (RACI)` tables in the same commit.
   If it executes an existing row, bind to that row and skip this step. One skill may
   name two rows (`program-roadmap-and-deps` does) — but a row with no skill is a gap,
   and a skill with no row is a claim with no rights.
3. **Bind the output.** The artifact follows an existing schema in
   `shared/output-schemas/` or the table rules in `shared/system-conventions.md`.
   Genuinely new artifact shape → new schema file there, added to the README tree in
   the same commit.
4. **Route it.** Add the trigger to the role file's `## When to load this role`, the
   artifact to its `## Produces` table (and the consuming roles' `## Consumes` —
   handoffs must mirror), and a prompt to `usage/prompts-<role>.md`.
5. **Prove it.** Write `tests/<role>/<new-skill>/fixture.md` (synthetic input +
   expected artifact + the checks list), walk the playbook against it, record the run
   under `tests/results/run-<date>-<slug>.md`, then — and only then — flip
   `status: planned → built`. Add the row to the README skills table and the CHANGELOG.

## Path 3 — Add a role (say, QA Lead, Architect, Support Engineer)

Bigger: a new column, not just a row.

1. **Stencil it.** `cp roles/_TEMPLATE.md roles/<role>.md` — all 14 sections, no
   `[brackets]` left in the shipped file.
2. **Column in `shared/raci.md`.** Add the role's column; re-justify **every** existing
   row's C/I cells for the new role (a new role changes the consultation map, not just
   its own rows). Exactly one A per row, still.
3. **Mirrors.** Every other role file's `## Decision rights (RACI)` table gains the
   new column in the same commit — the mirror rule cuts both ways.
4. **Handoff mirroring.** Walk the Consumes↔Produces↔Depends-on triples across all
   five role files; every new artifact names its consumers, every consumed artifact
   names its source. `## Reviews in others' artifacts` rows move both directions too.
5. **Skills + usage.** New role gets a `skills/<role>/` tree (Path 2) and a
   `usage/prompts-<role>.md`; update `usage/USER-GUIDE.md` §"Choosing a role" and the
   README squad table.
6. **Naming.** Kebab-case role ids (`pmt`, `qa-lead`); the persona's full title in the
   H1. Keep the three-or-four-letter alias usable in frontmatter.

## Path 4 — Change a schema (artifact shape)

1. **Edit the schema file** in `shared/output-schemas/` in place — never a parallel copy.
2. **Same commit:** every skill that binds it updates its output examples; every
   fixture that exercises it updates its expected artifact; the recorded-run note
   for the change lands under `tests/results/`.
3. **Additive where possible.** A new column beats a renamed one — importers
   (Jira CSV, Confluence paste) break on renames. Deprecate with a note in the schema
   ("deprecated field, kept for import compatibility") rather than a delete.
4. **Bump sensibly.** Schema-shape changes are at least a minor version; README tree
   and CHANGELOG in the same commit.

## What not to do

- **No code, no API clients, no network.** A skill that fetches from Jira/Confluence/
  GitHub breaks the charter (`WHAT-THIS-IS.md` — "not a client for anything") and
  the offline guarantee. Import is the user's hands, by design.
- **No org facts in skills.** Your sprint length lives in
  `shared/glossary-and-org.md`, never in a playbook's step 3.
- **No merged personas.** "PMT+TPM hybrid" files are how handoffs silently disappear.
- **No score/percentage inventions.** The `[CONFIRM]` discipline is the product;
  a filled-in guess in a template is the failure the kit exists to prevent.
- **No silent status flips.** A `built` skill with no fixture and no recorded run is
  a lie the README table will happily print.

## New here? Start at

- [`usage/USER-GUIDE.md`](../usage/USER-GUIDE.md) — how a session runs
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md) — PR mechanics (one skill per PR, etc.)
- [`../ROADMAP.md`](../ROADMAP.md) — what's open
- `tests/README.md` — what a fixture and a recorded run look like