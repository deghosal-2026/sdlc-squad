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
- **Caveat (honest, corrected):** this run reads **PDF exports** through `firecrawl`, which
  **reconstructs `##` markers and drops inline formatting** — so it **cannot speak to Confluence's
  inline styling**. The earlier **G3** run (a careful observation,
  `run-2026-11-23-g3-real-paste.md`) flagged exactly this artifact class and found Confluence
  **converting** headings, bullet lists, and tables (no `#`/`-`/`|` markers). Treat the
  "styling" reading below as a **likely extraction artifact**, not a render defect.

## Confluence — content observed; **styling reading unreliable**

| Repo | Artifact | Headings | Paragraphs | Tables | Inline styling | Notes |
|---|---|---|---|---|---|---|
| 01-kubernetes | `pmt-prd.md` | ✅ | ✅ | ✅ *(extraction reorders cells)* | **unverified** | extraction inserted `---` / `##`; the apparent "table split" is a flattening artifact |
| 02-grafana | `pmt-prd.md` | ✅ | ✅ | ✅ | **unverified** | extraction showed `$$ \mathbf{x} $$` and reordered *Non-goals* — extraction artifacts |

**Reliable from this run:** the content is **present and complete**; `[CONFIRM: …]` renders as
**literal text**.

**Not reliable from this run:** "bold lost", "lists flattened", "inline code lost", "table
split", "stray `---`", "sub-heading promoted", "word drift" — **all extraction artifacts.** The
G3 method note warned about exactly this: flattening a rendered page to text is not the render.

**Verdict: Confluence is paste-clean** (per G3, the careful observation). This X2 export adds
**no styling evidence** either way — it should not have been read as a styling defect.

**Definitive confirmation (2026-11-25, visual):** the live page was exported and **rendered to
an image and inspected directly**. Pages 2–3 show **bold** (*immutable*, *increased*,
*stateful or batch workloads*), **bullet lists** (the Goals / Non-goals / Target-users `•`
bullets), **inline code** (`UpdateContainerResources`, monospace), headings, and the
`[CONFIRM: …]` markers — **all render correctly.** The page is clean; the "styling loss" was a
**PDF-export / extraction artifact**, not a Confluence render defect.

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
- **Verdict: paste-clean** — headings, tables, bold, lists, and inline code all render.

## Verdict

**All destinations accept the artifacts; the only real defect is the CSV import's field
mapping.** GitHub and Jira render cleanly; **Confluence's page is paste-clean (G3)** — the
apparent "styling loss" in this run is a **Confluence PDF-export / `firecrawl` extraction
artifact**, not a render defect.

| Element | GitHub | Jira | Confluence (page) |
|---|---|---|---|
| Headings | ✅ | ✅ | ✅ (G3) |
| Bold | ✅ | ✅ | ✅ (G3) — the X2 *export* dropped it |
| Bullet lists | ✅ | ✅ | ✅ (G3) |
| Tables | ✅ all | ✅ all | ✅ (G3) |
| Inline `code` | ✅ | ⚠️ no `<code>` | unverified |
| `[CONFIRM: …]` literal | ✅ | ✅ | ✅ |

The real X2 finding: the **Jira CSV import** imports structure (8/8) but **field mapping fails**
(priority → default, `Size` → `Labels`) and a **re-import duplicates**.

`[CONFIRM: confirm the Confluence PDF export vs. the page — the export may lose inline styling.]`

## Still to do

- **03/04** — observe directly if a strict per-repo result is wanted (GitHub + Jira + Confluence
  all observed on **01**; Confluence also on **02**).
