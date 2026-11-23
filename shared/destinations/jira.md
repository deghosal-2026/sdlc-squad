# Destination contract — Jira (descriptions and bulk import)

Jira has **two** distinct destinations, and a kit artifact uses one or the other — never
both in one artifact (`shared/system-conventions.md`: one artifact, one import target).

1. **Editor paste** — a ticket description or comment (a *paste destination*).
2. **Bulk import (CSV)** — an epic + story set created in bulk (`pmt/slice-mvp-and-stories`).

## 1. Editor paste (descriptions / comments)

- **Jira Cloud:** the editor supports **Markdown** for rich-text fields (headings, lists,
  code blocks, and more). Pasted Markdown converts into Jira's rich text on paste.
- **Jira Cloud stores rich text as ADF** — the Atlassian Document Format, a JSON document
  tree (`doc` root; block nodes like `heading`/`paragraph`/`bulletList`/`table`; inline
  nodes like `text`; marks like `strong`/`code`/`link`). ADF is what the API reads/writes;
  the human pastes Markdown into the editor.
- **Jira Data Center:** rich text is **wiki markup**, not Markdown — the text formatting
  notation. `[CONFIRM: Data Center paste behavior — unobserved; the G3 spot check covered
  Cloud]`.
- **Tables:** supported in ADF (`table` node) and the Cloud editor; wiki markup tables use
  its own `||header||` / `|cell|` notation. **Observed 2026-11-23 (G3, Cloud):** pasted
  pipe-tables converted into real editor tables — a 6-column table kept every column
  including empty cells (`tests/results/run-2026-11-23-g3-real-paste.md`). Data Center
  table paste remains unobserved.

### Do / Avoid (editor paste)

- Keep the kit's Markdown paste-clean: header + alignment tables, no HTML, no emoji in
  tables, fenced code blocks.
- One ticket per artifact section: paste each story's block into its ticket description.
- Don't assume ADF round-trips — what you paste is what the editor normalizes.

## 2. Bulk import (CSV) — the epic + story set

The CSV importer creates work items in bulk; the kit's `slice-mvp-and-stories` story table
is the source. As documented:

- **Column → field mapping:** after upload, each CSV column is mapped to a Jira field (or a
  new custom field); use the **Map CSV data to Jira fields** step.
- **Work types:** a column is mapped to work types (**Map column data to work types**).
- **Summary** is the required field (every work item needs one).
- **Issue Key** — set it to update an existing issue instead of creating a new one.
- **Parent/child:** parent-child relationships are not preserved by a plain column unless
  mapped explicitly; issue **links** are configured by selecting the link type in the Map
  Fields step (the link type must already exist in Admin → Issues → Issue Linking).
- **Validation:** the first 30 rows are checked against the mapping; errors surface in the
  Map step. **Observed 2026-11-23 (G3):** 3/3 rows imported clean (no errors surfaced in
  the result); the Map-step validation UX itself was not captured by the export.
- **Importer availability:** the CSV importer can be disabled by an admin. **Observed
  (G3):** available and working on the owner's Jira Cloud (Nov 2026).

### Do / Avoid (CSV)

- Header row + one row per work item; keep pipe `|` characters out of cell bodies (the
  `jira-epic-and-stories` schema already requires this).
- Map `Summary`, `Issue Type`, `Priority`, `Size`/estimate, and any dependency/link columns
  in the wizard — the kit's schema names matching columns so the mapping is mechanical.
  **Observed 2026-11-23 (G3):** `Summary`/`Issue Type`/`Description` mapped cleanly (3/3
  stories landed; descriptions and `[CONFIRM: …]` literal). Two mapping findings:
  **Priority values must match the instance's scheme** — the kit's P1/P2 landed as
  Medium (Jira Cloud defaults are Highest/High/Medium/Low/Lowest; unmatched → default);
  **Size needs a custom-field target** — with none in the scratch project it landed in
  Labels, values intact (`tests/results/run-2026-11-23-g3-real-paste.md`).
- Treat the CSV as **input to the wizard**, not a validated import file, until G3 observes a
  real import.

## Where it lands (skills)

- `pmt/slice-mvp-and-stories` → Jira epic + stories (CSV bulk import; per-ticket paste)
- `sde/technical-design-and-breakdown` → Jira sub-tasks
- `sdm/*`, `sde/generate-test-ideas-and-cases` → Jira QA checklist / backlog items

## Sources (retrieved 2026-11-23)

- Atlassian Document Format — `https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/`
- Jira Cloud — "Markdown and keyboard shortcuts"
  (`https://support.atlassian.com/jira-software-cloud/docs/markdown-and-keyboard-shortcuts/`)
- Jira Cloud CSV import — "Prepare a CSV file for import", "Import data to Jira using a CSV
  file", "Map CSV data to Jira fields", "Map column data to work types"
  (`https://support.atlassian.com/jira-software-cloud/docs/…`)
- Jira Data Center CSV import — "Importing data from CSV" (`https://confluence.atlassian.com/adminjiraserver/…`)
- Jira text formatting notation (wiki markup) — `…/WikiRendererHelpAction.jspa?section=all`
- **Open `[CONFIRM]`s:** Data Center paste behavior (the G3 spot check covered Cloud);
  whether the Priority default came from an unmapped column or unmatched vocabulary;
  the Map-step validation UX. All close with future v0.1.x pastes.
