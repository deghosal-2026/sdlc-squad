# Supported and adaptable — what works, what you change

One page for the question "will this fit our tools?" Three buckets: works out of the box,
changeable by editing Markdown, and out of scope. Every line traces to
[`EXTENDING.md`](EXTENDING.md), [`../shared/system-conventions.md`](../shared/system-conventions.md),
or a charter refusal ([`../WHAT-THIS-IS.md`](../WHAT-THIS-IS.md)).

## Works out of the box

Paste-ready Markdown artifacts, with a `## Import target` block naming where they go:

| Destination | What the kit emits |
|---|---|
| **GitHub** | Issue and PR bodies in GFM (tables, task lists, fenced code) — see [`../shared/destinations/github.md`](../shared/destinations/github.md) |
| **Jira** | Ticket descriptions (Markdown paste) and the story table that is CSV-ready for bulk import — see [`../shared/destinations/jira.md`](../shared/destinations/jira.md) |
| **Confluence** | PRD/RFC pages and status/retro pages (Markdown paste) — see [`../shared/destinations/confluence.md`](../shared/destinations/confluence.md) |

## Adaptable by editing Markdown

| What | How |
|---|---|
| **A different tracker / docs tool** (e.g., Azure DevOps + Confluence) | Edit the source-of-truth table and the import-target language in `shared/system-conventions.md`; the skills inherit (`EXTENDING.md` Path 1). |
| **Your vocabulary, ceremony hours, keys, SLAs** | Fill your own `my-org.md` glossary — kept **outside** the kit ([`UPGRADING.md`](UPGRADING.md)). |
| **A skill's steps or a schema** | Edit in place, one canonical copy, mirror rules apply (`EXTENDING.md` Paths 2–4) — a fork you then own. |

## Requires real changes (not just a glossary edit)

| What | Why |
|---|---|
| **A new artifact shape** | New schema in `shared/output-schemas/`, then bind the skill (`EXTENDING.md` Path 4). |
| **A new role** | A new RACI column, mirrored across all role files (`EXTENDING.md` Path 3). |
| **A validated Jira bulk-import CSV** | The CSV contract in [`../shared/destinations/jira.md`](../shared/destinations/jira.md) is doc-derived until a real import is observed. |

## Never (a hard boundary, not a gap)

- **API integration, auto-import, or telemetry.** Charter: "not a client for anything."
  Import is the user's hands, by design.
- **Credentials or tokens.** The kit's only "setup" is the glossary — names, not secrets.

## Related

- [`START-HERE.md`](START-HERE.md) — pick a task and skill
- [`EXTENDING.md`](EXTENDING.md) — the four customization paths
