# Destination contract — Confluence (pages)

Confluence is the kit's documentation destination: PRD/RFC pages, program pages, sprint
notes, launch checklists, retros. A kit artifact is **pasted into the page editor**.

## What a kit artifact lands as

- **Confluence Cloud pastes Markdown.** Pasting plain-text Markdown into the editor
  converts it into Confluence formatting — headings, bold, inline code, bulleted/numbered
  lists, tables. **After paste it is Confluence format**, no longer editable as Markdown.
- **The legacy editor** inserts Markdown via **Insert → Markup → Markdown** (preview, then
  Insert).
- **Under the hood** Confluence stores pages in the **storage format** — an XHTML-based XML
  (with custom elements for macros). That matters only for API/macro authors; the human
  path is editor paste. `[CONFIRM: storage format only if you later script page creation]`.
- **Markdown coverage is not full.** The Cloud editor officially supports a specific subset
  of Markdown; some constructs convert, some do not. `[CONFIRM: verify your page's tables
  and code blocks on first paste]`.

### Do / Avoid (editor paste)

- Keep the kit's paste-clean rules: header + alignment tables, **no HTML**, **no emoji in
  tables**, **no collapsible sections** (`CONVENTIONS.md`) — these are exactly the
  constructs most likely to convert poorly.
- One artifact = one page. The schema's `# Title` becomes the page title; `##` sections
  become the page's sections.
- Prefer plain Markdown tables over macro-based layouts; the schema's table columns are the
  contract.
- The `[CONFIRM: ...]` markers paste as literal text — resolve them **before** pasting, or
  keep them visible as deliberate open items (see `docs/REVIEWING-OUTPUT.md`, when it
  ships).

## Where it lands (skills)

- `pmt/draft-prd`, `pmt/define-success-metrics`, `pmt/customer-discovery-and-synthesis`,
  `pmt/survey-design`, `pmt/prioritize-asks`
- `tpm/program-roadmap-and-deps`, `tpm/risk-raid-and-mitigations`,
  `tpm/release-readiness-check`, `tpm/program-status-review`
- `sdm/*` (sprint note, decision log, ops doc, retro, standup)
- `sde/technical-design-and-breakdown` (RFC), `sde/design-and-code-reviews` (standards),
  `sde/deploy-plan-and-release` (runbook)

## Sources (retrieved 2026-11-23)

- Confluence Cloud — "Available markdown commands"
  (`https://support.atlassian.com/confluence-cloud/docs/available-markdown-commands/`)
- Confluence Cloud — "Insert Confluence wiki markup" (Markdown insert path,
  `https://support.atlassian.com/confluence-cloud/docs/insert-confluence-wiki-markup`)
- Confluence Storage Format (XHTML-based XML) — Atlassian documentation
  (`https://confluence.atlassian.com/…/Confluence+Storage+Format`; Data Center migration
  notes)
- Paste-converts-Markdown behavior — Atlassian Community threads + independent write-ups
  (2026)
- **Open `[CONFIRM]`s:** exact Markdown subset the editor converts; table fidelity on paste;
  storage format only if page creation is scripted — resolved by G3's real paste.
