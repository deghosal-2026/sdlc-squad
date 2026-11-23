# G3 spot check — real-destination paste — 2026-11-23

> **All four destinations observed, 2026-11-23.** GitHub (rendered issue fetched and
> assessed); Jira editor (owner-supplied export PDF, text-extracted); Jira CSV import
> (owner ran it; Jira's export CSV checked directly); Confluence Cloud page
> (owner-supplied export PDF, text-extracted). Nothing projected.

- **Method:** the staged synthetic sprint-plan artifact (Meridian Outfitters, from
  `tests/sdm/sprint-planning-and-capacity/fixture.md`) pasted into real destinations by
  the owner. GitHub: the agent fetched the rendered public issue. Jira: the site is
  auth-walled, so the owner supplied a PDF of Jira's issue-HTML export; the agent cannot
  read images/PDFs, so its **text was extracted (pypdf)** and assessed — the extracted
  text is the rendered, stored description, which is exactly what the paste produced.
- **Paste kit:** git-ignored `output/g3/` (bodies, CSV, checklist, results template) —
  never committed.

## GitHub — OBSERVED

**Target:** [deghosal-2026/sdlc-squad#1](https://github.com/deghosal-2026/sdlc-squad/issues/1)
— "[G3 paste test] sprint plan render check", body = `output/g3/01-github-issue-body.md`.

Assessed from the fetched rendered page:

- **Headings:** the artifact's H1 title and H2 sections rendered as headings.
- **Tables:** both tables rendered as tables — the 6-column capacity table (including the
  three empty trailing cells per row) and the 3-column commitment table with its
  `**Total committed**` footer row.
- **Bold:** rendered (`**Total committed**`, `**not committed**`, `**15.0 ≤ 39.0**`).
- **Special characters:** `−` (minus, U+2212), `≤`, and `→` all rendered correctly.
- **`[CONFIRM: …]` rendered literally** — the marker in the title line displayed as text,
  not parsed as a link or HTML. The discipline survives the paste.
- **ISO dates:** `2026-12-07 to 2026-12-18` rendered.
- **Not assessable from a markdown fetch** (owner may confirm visually): column alignment
  rendering; the outline/auto-TOC behavior.
- **Staging note (honest):** the capacity rows carry their arithmetic in the first cells
  with empty trailing cells (the fixture's 3-cell shorthand stretched across the schema's
  6-column header) — a **staging artifact, not a GitHub defect**; GitHub rendered the full
  table regardless. Any future paste body should map one value per column.

**Verdict: paste-clean** (spot check — one artifact, one issue).

## Jira — EDITOR PASTE OBSERVED (CSV below)

- **Target:** [SCRUM-5](https://deghosal.atlassian.net/browse/SCRUM-5) on the owner's
  Jira Cloud (`deghosal.atlassian.net`) — description =
  `output/g3/03-jira-issue-description.md`. (The export header shows the project as
  "MST" while the browse key is SCRUM — noted as-is, not smoothed.)
- **Jira type:** **Cloud** — `atlassian.net` domain plus the export's Cloud snapshot
  footer.
- **Observed (from the text-extracted rendered description):**
  - **Headings converted** — "Sprint 14 plan…", "Capacity", "Proposed commitment",
    "Flagged risks", "Import target" render with no `#`/`##` markers.
  - **Both tables converted into real editor tables** — no literal pipes anywhere in the
    extracted text; the 6-column capacity table kept **all** columns including the three
    empty trailing cells; the 3-column commitment table kept its footer row.
  - **Bold converted** (`**` markers consumed); the flagged-risks **bullet list
    converted** (no `-` markers).
  - **Special characters survived:** `−`, `≤`, `→`. **ISO dates intact.**
  - **`[CONFIRM: name]` rendered literally** — the discipline survives Jira's editor.
- **Not assessable from text extraction:** visual alignment/column widths, heading sizes —
  the owner can confirm visually.
- **Extraction artifacts (not Jira defects):** adjacent table cells run together in plain
  text extraction ("0.5+0.5= 7.5", "flaky-test fix2d") — a property of flattening a table
  to text, not of the rendered page.
- **CSV bulk import:** `[CONFIRM: owner — not yet run]` → **run and observed 2026-11-23**;
  see the CSV section below.

**Verdict (editor paste): paste-clean** (spot check — one artifact, one issue, Jira Cloud).

## Jira — CSV BULK IMPORT OBSERVED

- **Target:** the owner's scratch project — **key `SCRUM`, name "MST"** (this resolves the
  earlier header note: the PDF header showed the project *name*; the browse key is the
  key) — on Jira Cloud.
- **Method:** the owner ran the import with `output/g3/04-jira-bulk-import.csv`
  (3 stories) and supplied Jira's **export CSV** of the resulting issues; the agent read
  the export directly.
- **Observed (from the export):**
  - **3/3 stories landed** — SCRUM-6 (Guest opens signed tracking link…), SCRUM-7
    (Support links the same guest view…), SCRUM-8 (Archived-order message…); all created
    23/Nov/26 11:13 AM, type **Story**, status To Do.
  - **Issue Type mapping worked** — the CSV's `Issue Type` values became real Story work
    items via the work-type mapping.
  - **Descriptions survived intact, commas and all** — AC-1/AC-2 present verbatim;
    **`[CONFIRM: owner]` stayed literal** through import *and* export.
  - **Priority did not survive as written** — the CSV carried P1/P2/P2; every landed
    issue shows **Medium**. Either the column went unmapped, or P1/P2 are not in the
    instance's priority vocabulary (Jira Cloud defaults are Highest/High/Medium/Low/
    Lowest) and the default applied. `[CONFIRM: which — owner recall of the Map step]`
  - **Size landed in Labels** — the M/S/S values appear in the Labels field (the scratch
    project has no custom/story-point field for Size to map to). Values intact; not
    story points.
  - **No parent/epic link** — flat stories, exactly as the contract predicts for an
    unmapped plain column.
- **Not captured by an export:** the wizard's validation UX (any errors surfaced in the
  Map step).

**Verdict: import-clean, with two mapping findings** — priority values need the
instance's vocabulary; Size needs a custom-field target (or lands wherever mapped, here
Labels).

## Confluence — OBSERVED

**Target:** the owner's Confluence Cloud page — title *"Sprint 14 Plan: Team Capacity,
Proposed Commitment, and Flagged Risks"* — body = `output/g3/02-confluence-page.md`,
supplied as a page-export PDF (text-extracted with pypdf — the agent cannot read PDFs).

**Observed (from the text-extracted page):**

- **Headings converted** — the page title plus "Capacity", "Proposed commitment", "Flagged
  risks", "Import target" all render with no `#`/`##` markers.
- **Bullet list converted** — the flagged-risks list renders with no `-` markers.
- **Both tables converted** — **no literal pipe characters** anywhere in the extracted
  text (a raw Markdown table would show `|`); all six capacity headers ("Engineer",
  "Gross days", "− PTO", "Meetings & ceremonies", "− On-call / support / toil", "= Net
  focus days") and rows A–F are present, and the commitment table's rows plus its total.
- **`[CONFIRM: name]` rendered literally** in the H1 line — the discipline survives the
  Confluence paste too.
- **Special characters preserved:** `−`, `≤`, `→`; **ISO dates** intact (`2026-12-07 to
  2026-12-18`).
- **Extraction artifact (not a defect):** the exported PDF's text runs table cells out of
  visual order (data rows before the header row; cells wrapped mid-phrase) — a property of
  flattening a multi-column PDF to text, not of the rendered page. Visual alignment and
  column widths are the owner's to eyeball.
- **Title note:** the page title is a human-readable "*Sprint 14 Plan: Team Capacity,
  Proposed Commitment, and Flagged Risks*", distinct from the pasted H1 (`Sprint 14 plan —
  Team [CONFIRM: name], …`) — the page title was set separately from the artifact body.
- **Not observed:** code-block paste; the storage-format path (scripted page creation).

**Verdict: paste-clean** (content; spot check — one artifact, one page, Confluence Cloud).

## Verdict (so far)

| Destination | Status |
|---|---|
| GitHub | **Observed — paste-clean** |
| Jira (editor, Cloud) | **Observed — paste-clean** |
| Jira (CSV) | **Observed — import-clean w/ findings** (priority defaulted; Size → Labels) |
| Confluence | **Observed — paste-clean** |

**G3 complete — all four destinations observed.** Every finding is folded into
`shared/destinations/`; the only residue is Jira Data Center and Confluence's
storage-format path, both out of scope for manual pastes.

## Follow-ups

- All four destinations observed; only **Jira Data Center** wiki-markup behavior and
  **Confluence's storage-format path** remain unobserved (both out of scope for manual
  pastes) — future v0.1.x territory.
- Import-target wording updated (README, `usage/USER-GUIDE.md`): GitHub, the Jira editor,
  the Jira CSV import, and the Confluence page are now paste-verified; only the Data
  Center / storage-format caveats remain.
- Fix the capacity-row staging artifact in any future paste body (see GitHub note).
- Issue #1 and SCRUM-5…SCRUM-8 can be closed/deleted by the owner once this note is
  committed; the URLs above are the citations.
