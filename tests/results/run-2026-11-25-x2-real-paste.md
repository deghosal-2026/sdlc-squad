# X2 real-paste — field-test artifacts into real destinations — 2026-11-25

> **Status: all three destinations observed** — Confluence (01, 02), Jira editor + Jira CSV
> import (01), and GitHub (01). **03/04 owner-reported fine** (not individually observed).
> Nothing projected.
>
> This is the **real-paste half of X2** (plan item **A-5**): the field-test artifacts
> (`field-test/<repo>/artifacts/`) pasted into real destinations, with the render recorded.
> It mirrors the v0.1.1 **G3** spot check (`run-2026-11-23-g3-real-paste.md`).

## Method

- **Artifact pasted:** the **PRD** (`field-test/<repo>/artifacts/pmt-prd.md`) — its import
  target is *Confluence — the PRD/RFC page for this initiative*. It is the richest surface
  (H1/H2 headings, pipe tables, bullet lists, bold, inline `code`, literal `[CONFIRM: …]`).
- **Owner:** pasted into **Confluence Cloud**, then exported the page to **PDF**.
- **Agent:** cannot read PDFs, so each export was **text-extracted** (`firecrawl parse`,
  local) and assessed. The extraction is the rendered, stored page text — which is what the
  paste produced. Extracted files live in git-ignored `.firecrawl/` (never committed).
- **Caveat (honest):** some artifacts below — split tables, stray `---`, word drift — may be
  **PDF→text extraction artifacts** rather than genuine render changes. The **styling loss**
  (bold/lists/code) is document-wide and consistent across exports, so it is treated as real.

## Confluence — OBSERVED (01, 02)

| Repo | Artifact | Headings | Paragraphs | Tables | Bold | Bullet lists | Inline `code` | Notes |
|---|---|---|---|---|---|---|---|---|
| 01-kubernetes | `pmt-prd.md` | ✅ | ✅ | ⚠️ 2 of 3 intact | ❌ lost | ❌ flattened | ❌ lost | *Edge cases* (full export) / *Open questions* (partial) split |
| 02-grafana | `pmt-prd.md` | ✅ | ✅ | ⚠️ 2 of 3 intact | ❌ lost | ❌ flattened | ❌ lost | *User journeys* split; **`$$ \mathbf{x} $$` math corruption**; *Non-goals* text scrambled |

**What survived:** all `##` section headings; all paragraph text; two of the three tables per
page; the `## Handoff` block; the field-test wrapper (when the whole file was pasted).

**What broke (consistent across both):**

1. **Bold lost** — `**immutable**`, `**stateful or batch workloads**` → plain text.
2. **Bullet / numbered lists flattened to paragraphs** — the Goals, Non-goals, and REQ-1…10
   lists lost their bullets.
3. **Inline `code` lost** — `` `/resize` ``, `` `PodResizePending` `` → plain text.
4. **A table split in two** — a header+some-rows table, then `---`, then the remaining rows
   **headerless**. (01: *Open questions* / *Edge cases*; 02: *User journeys*.)
5. **Stray `---` horizontal rules** inserted between sections.
6. **Sub-heading level promoted** — `### Functional` / `### Non-functional` → `##`.
7. **Occasional content corruption** — 02: the "**x**" in *Go back to **x*** rendered as a
   **LaTeX math block `$$ \mathbf{x} $$`**; the *Non-goals* sentence order scrambled.
8. **Possible word drift** — 01 EC-7 "resize **retried**" appeared as "retired" / "retrieved"
   in the two exports — **likely an extraction artifact** (it differed between runs).

**`[CONFIRM: …]` markers:** rendered as **literal text** (not parsed) — the discipline
survives the paste, matching the G3 finding.

## Confluence — 03, 04

**Owner-reported fine; not individually observed.** No export was supplied for
`03-deno` or `04-rust`; treated as **consistent with 01/02** `[CONFIRM: observe to confirm]`.

## Jira — EDITOR PASTE OBSERVED (01)

- **Target:** Jira issue **SCRUM-10** (type **Epic**, project **MST**) — description =
  `field-test/01-kubernetes/artifacts/pmt-stories.md` (the epic + stories). Owner ran the paste;
  the agent parsed Jira's **Word export** (`SCRUM-10.doc`), which is **HTML with a `.doc`
  extension** — so its raw tags are exactly what Jira rendered.
- **Rendered tags (counted from the export HTML):** `<h1>` × 1, `<h2>` × 5, `<h3>` × 9;
  `<b>` × 68; `<ul>` × 9, `<li>` × 20; `<table>` × 8.

| Element | Jira | Confluence (for contrast) |
|---|---|---|
| Headings | ✅ `<h1>`+`<h2>`+`<h3>` | ✅ |
| **Bold** | ✅ `<b>` × 68 | ❌ lost |
| **Bullet lists** | ✅ 9 lists / 20 items | ❌ flattened |
| **Tables** | ✅ all 3 (field, stories, dependencies) | ⚠️ some split |
| Inline `code` | ⚠️ no `<code>` tags | ❌ lost |
| `[CONFIRM: …]` literal | ✅ | ✅ |

- **Verdict: paste-clean.** Jira rendered **bold, bullet lists, headings, and every table** —
  the things Confluence dropped. The Confluence weakness is **Confluence-specific, not a kit
  defect**.
- **Note:** the issue's own **Priority** defaulted to **Medium** and its **Type** is **Epic**;
  the body's `Priority | [CONFIRM: per the org's scale]` stayed literal. G3's priority/Size
  **coercion** note applies to the **CSV import**, not the editor paste.

## Jira — CSV BULK IMPORT OBSERVED (01)

- **Source:** `output/x2/01-kubernetes-stories.csv` (git-ignored paste kit) — the `US-1…US-8`
  story table from `field-test/01-kubernetes/artifacts/pmt-stories.md`, header
  `Summary, Issue Type, Priority, Size, Dependencies`.
- **Ran:** Jira **Import issues from CSV**, project `SCRUM` — the owner ran it **twice**.
- **Result:** **8/8 stories created per run** → `SCRUM-11…18`, then `SCRUM-19…26` — **16 total**.

| CSV column | Mapped to | Result |
|---|---|---|
| Summary | Summary | ✅ |
| Issue Type | `Story` | ✅ |
| **Priority** | — | ⚠️ **left unmapped by the owner** → Jira **defaulted to `Medium`** |
| **Size** | — | ⚠️ **landed in `Labels`** (the `[CONFIRM]` value) — not Story Points |
| Dependencies | — | ⚠️ **dropped** (no matching field) |

- **Confirms G3:** `Priority` must match the instance's scheme (unmapped → the default,
  `Medium`), and `Size` lands in `Labels`. `Custom field (Story point estimate)` stayed **empty**.
- **New finding — not idempotent:** a second run of the **same** CSV **duplicated** all 8 stories
  (no dedup on Summary or key). A re-import doubles the backlog.
- **Verdict:** **structure imports cleanly (8/8); field *mapping* is the failure.** The CSV
  contract needs the instance's real priority names, a custom-field target for `Size`, and a
  re-import guard.

## GitHub — OBSERVED (01)

- **Target:** [deghosal-2026/sdlc-squad#2](https://github.com/deghosal-2026/sdlc-squad/issues/2)
  — "Design: In-place Update of Pod Resources", body = `field-test/01-kubernetes/artifacts/sde-design.md`.
  The agent fetched the **rendered public page**.
- **Rendered:** headings (every `##`); **all three tables** (affected modules, failure modes,
  sub-tasks); **bold** (`**immutable QoS class**`, `**external**`); **inline `code`**
  (`` `kube-apiserver` ``, `` `/resize` ``); bullet + numbered lists; `[CONFIRM: …]` literal.
- **Verdict: paste-clean** — GitHub renders bold, lists, tables, and inline code that Confluence
  drops.

## Verdict

**Destination-dependent — and the gap is large.** GitHub and Jira render the artifacts
**cleanly**; Confluence drops bold, bullet lists, and inline code and splits some tables.

| Element | GitHub | Jira | Confluence |
|---|---|---|---|
| Headings | ✅ | ✅ | ✅ |
| **Bold** | ✅ | ✅ | ❌ lost |
| **Bullet lists** | ✅ | ✅ | ❌ flattened |
| **Tables** | ✅ all | ✅ all | ⚠️ some split |
| Inline `code` | ✅ | ⚠️ no `<code>` | ❌ lost |
| `[CONFIRM: …]` literal | ✅ | ✅ | ✅ |

So the schemas' assumption that bold and bulleted lists survive the paste **holds on GitHub and
Jira, not on Confluence** — a **destination-contract** note, not a kit defect. The CSV import is
the one place **structure is fine but field mapping fails** (priority default, `Size` → `Labels`,
no re-import guard).

`[CONFIRM: confirm the Confluence render visually — PDF extraction may understate it.]`

## Still to do

- **03/04** — observe directly if a strict per-repo result is wanted (GitHub + Jira + Confluence
  all observed on **01**; Confluence also on **02**).
