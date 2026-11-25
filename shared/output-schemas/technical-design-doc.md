# Output schema — Technical design doc / RFC section

Bound by: `sde/technical-design-and-breakdown`.

## Canonical shape

```markdown
# Design: [Title]

> Status: Draft · Author: [CONFIRM: name] · Last updated: YYYY-MM-DD

## Affected modules / services
| Service / repo / path | Change | Risk |
|---|---|---|

[Every claim about existing code carries its source: the file/repo it was read from, or
CONFIRM.]

## Data model & API / contract changes
[Schema before/after; endpoint or event signatures; backwards-compatibility notes.]

## Flow
[Numbered sequence, text only: actor → step → observable state change.]

## Failure modes & edge cases
| ID | Trigger | Behavior | Detection |
|---|---|---|---|

## Observability
[What is logged/metric'd/alerted, and the query or dashboard that shows it.]

## Rollback
[Named steps, in order, back to the last good state. "Revert the PR" is a step, not a plan.]

## Sub-tasks (Jira-ready)
| ID | Task | Scope | DoD | Depends on |
|---|---|---|---|---|
| T-1 | ... | [files/services] | [observable completion] | — |

## Import target
Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the T-table
as sub-tasks.
```

## Rules

- **Cite or `[CONFIRM]` (enforced).** Every claim about existing code names a **file path and a
  symbol** (or quotes the code). An *Affected modules* row that names only a component or
  service — no path, no symbol — is **incomplete**: add the path/symbol, or mark
  `[CONFIRM: read the code]`. A design with **zero file paths and zero `[CONFIRM]`s** is a defect.
- **Detection is mandatory (enforced).** Every failure-mode row carries a **detection path** — a
  metric, condition, log, or event. A row whose *Detection* cell is `—` is an **incomplete row**:
  fill it or split the row.
- **Traceability.** Every sub-task names the **story (`US-n`)** or **requirement (`REQ-n`)** it
  serves, so `REQ-n → US-n → T-n` is followable; `[CONFIRM: source]` if none was supplied.
- Every task has a Definition of Done that is observable by someone other than its author.