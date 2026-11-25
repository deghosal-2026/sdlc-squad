# Destination contracts — GitHub · Jira · Confluence

The **paste-destination** contracts behind every skill's `## Import target` block: what
each destination renders, what the kit's Markdown artifacts do when they land there, and
what to keep out. This is the "compatible format" half of the kit's native-compatibility
story.

## Status (honesty first)

- **Derived from vendor specifications**, retrieved 2026-11-23, not from a live paste.
- **Not yet instance-validated.** Behavior varies by plan, editor, and admin configuration
  — the version-specific parts carry `[CONFIRM: verify against your instance]`, exactly as
  the kit marks any unknown. The first real paste (decision **G3** in the 0.1.1 plan)
  upgrades these from doc-derived to observed.
- **Binding is deferred.** The output schemas stay canonical; skills begin *emitting
  per-contract* (for example, `slice-mvp-and-stories` emitting a CSV block shaped by
  `jira.md`) only in a later minor — schema-shape work is at least a minor version
  (`CONVENTIONS.md`).

## What is observed — the validation ledger

Which paths have been pasted for real, and which are still doc-derived. Every *observed*
row cites the recorded paste; every *unobserved* row is a `[CONFIRM]` until it is.

| Destination path | State | Evidence |
|---|---|---|
| GitHub issue body (GFM) | **Observed** | [`../../tests/results/run-2026-11-23-g3-real-paste.md`](../../tests/results/run-2026-11-23-g3-real-paste.md) |
| Jira Cloud editor paste | **Observed** | same run |
| Jira CSV bulk import | **Observed** (G3: 3/3 stories, priority P1/P2 → Medium; **X2: 8/8 but priority → default and `Size` → `Labels`; a re-import duplicates**) | G3 + X2 |
| Confluence Cloud page paste | **Observed** (headings, paragraphs, tables; **bold, bullet lists, and inline code are dropped**) | G3 + X2 |
| Jira Data Center | Unobserved | `[CONFIRM: verify on your instance]` |
| Confluence storage format (scripted pages) | Unobserved | `[CONFIRM: out of scope for a manual paste]` |
| Confluence code-block paste | Unobserved | `[CONFIRM: verify on your instance]` |

A row moves from *unobserved* to *observed* only when a real paste is recorded under
[`../../tests/results/`](../../tests/results/) — never on a doc read. The **X2** run
([`run-2026-11-25-x2-real-paste.md`](../../tests/results/run-2026-11-25-x2-real-paste.md))
re-observed GitHub, Jira (editor + CSV), and Confluence on the field-test artifacts, adding the
**styling** finding: **GitHub and Jira render bold, bullet lists, and inline code; Confluence
does not.**

## The files

| File | Destination | Covers |
|---|---|---|
| [`github.md`](github.md) | GitHub | Issue and PR bodies (GFM) |
| [`jira.md`](jira.md) | Jira | Ticket descriptions (editor) and bulk import (CSV) |
| [`confluence.md`](confluence.md) | Confluence | Pages (editor paste; storage format) |

## How these relate to the schemas

- `shared/output-schemas/*` define **what** an artifact contains (sections, columns, ID
  prefixes).
- `shared/destinations/*` define **how the destination renders it** (what converts, what
  breaks).
- They must agree. A schema change that alters a table or heading should be checked against
  the destination contract for the skills bound to it.

## Whoever pastes is the importer

The kit never pushes anywhere (`WHAT-THIS-IS.md`). These contracts exist so the **user's**
paste is predictable — and so the kit never claims a compatibility it has not observed.
