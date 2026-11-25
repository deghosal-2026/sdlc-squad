# Destination profiles — mapping the kit to your instance

The kit's [`shared/destinations/`](../shared/destinations/) contracts say what each
destination renders **in general**. Your instance is specific: your priority names, your
estimate field, your formatting rules. A **profile** is a small Markdown file that records
those specifics — kept **outside** the kit, next to your `my-org.md`.

## The rule: your profile lives outside the kit

Same rule as your org glossary ([`UPGRADING.md`](UPGRADING.md)): `pip install --upgrade`
replaces the kit's files; a `git pull` conflicts with edited tracked files. A profile
**outside** the kit survives both. And, like the glossary, it holds **names and mappings
only — no credentials or tokens** (`../SECURITY.md`; [`TOOLS.md`](TOOLS.md) §Never).

Nothing loads a profile automatically: no skill, role, or CLI reads it, and `LOAD_ORDER` is
untouched. You paste it alongside your `my-org.md` at load step 2.

## What a profile maps

| What | Why it matters | Example |
|---|---|---|
| **Priority names** | Jira's P1/P2 may not exist — the G3 check saw P1/P2 coerce to **Medium** | `P1 → Blocker` |
| **Estimate unit** | Story points, t-shirt sizes, or engineering days — and whether it is a custom field or description text (the G3 check saw Size land in **Labels**) | `Size → Story Points field` |
| **Issue types** | The names your project actually uses | `Story`, `Task`, `Bug` |
| **Formatting rules** | What renders vs. breaks on paste | avoid nested tables / raw HTML |

Every value is **yours to supply**; anything you don't know stays `[CONFIRM: map …]`. The
kit never guesses an instance's scheme.

## Template — `my-jira.md`

```markdown
# My Jira profile

## Priority mapping
[CONFIRM: map each kit priority to your scheme — e.g. P1 -> Blocker, P2 -> Major]

## Estimate field
[CONFIRM: story points (custom field name), t-shirt sizes, or engineering days —
and whether it is a field or description text]

## Issue types
[CONFIRM: the issue types your project uses — Story, Task, Bug, …]

## Bulk-import notes
[CONFIRM: verify the CSV header against your instance before importing]
```

## Template — `my-confluence.md`

```markdown
# My Confluence profile

## Space
[CONFIRM: the space key artifacts land in]

## Formatting
[CONFIRM: what your editor renders — callouts, status badges, code blocks —
and what to avoid]
```

## Template — `my-github.md`

```markdown
# My GitHub profile

## Issue / PR conventions
[CONFIRM: labels, required sections, and any issue/PR templates your repo enforces]
```

## How to use it

1. Copy the templates above into files **outside** the kit (`my-jira.md`, `my-confluence.md`,
   `my-github.md` — or one `my-destinations.md`).
2. Fill what you know; leave the rest `[CONFIRM]`.
3. Paste your profile alongside your `my-org.md` at load step 2.

## Related

- [`../shared/destinations/`](../shared/destinations/) — the general contracts a profile refines
- [`UPGRADING.md`](UPGRADING.md) — the outside-the-kit rule and the ownership table
- [`EXPORTS.md`](EXPORTS.md) — getting input in, and redaction
