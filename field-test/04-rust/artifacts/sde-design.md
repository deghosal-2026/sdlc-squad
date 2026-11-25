# Design: `let-else` statements

> **Field-test artifact** — the kit's `sde/technical-design-and-breakdown` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Status: Draft · Author: [CONFIRM: name] · Last updated: 2026-11-25

## Affected modules / services

| Service / repo / path | Change | Risk |
|---|---|---|
| `rustc_parse` (parser) | Parse `let PAT = EXPR else { … };` | Medium |
| `rustc_ast` / AST | A let-else node (or desugar at lowering) | Medium |
| `rustc_typeck` / MIR | Enforce the `else` block's **divergence** (`!`) | High |
| `rustc_lint` | `irrefutable_let_patterns`; or-pattern binding check | Low |
| `rust-lang/rustfmt` | Format let-else | Low |
| `rust-lang/reference` + Book | Document the construct | Low |

*The RFC gives the design, not file paths; symbol-level claims are `[CONFIRM: read the
implementation PRs]`.*

## Data model & API / contract changes

- **New language surface:** the `let … else { … };` statement; sugar for `match` with a
  diverging fallback arm (per the RFC's desugaring).
- **No public library API** — a language feature, not a crate.
- **Contract:** the two expression restrictions (no trailing `}`; no bare lazy boolean) and the
  divergence requirement are part of the grammar/semantics.

## Flow

1. **Parse** — the parser accepts the statement, rejecting an expression that ends with `}` or
   is a bare `&&`/`||`.
2. **Lower** — the statement desugars to `match expr { PAT => bindings, _ => { …diverge… } }`.
3. **Type-check** — the `else` block is required to have type `!`; the bindings enter the
   surrounding scope.
4. **Lint** — an irrefutable pattern warns; mismatched or-pattern bindings error.
5. **Format** — `rustfmt` emits a stable layout.

## Failure modes & edge cases

| ID | Trigger | Behavior | Detection |
|---|---|---|---|
| FM-1 | `else` block can fall through | compile error | diagnostic at the block |
| FM-2 | Expression ends with `}` | compile error | parser diagnostic |
| FM-3 | Expression is a lazy boolean | compile error | parser diagnostic |
| FM-4 | Irrefutable pattern | warning | `irrefutable_let_patterns` |
| FM-5 | Or-pattern binds different names | compile error | name-resolution diagnostic |
| FM-6 | `if let p = e else { } { }` | not allowed | parser error |

## Observability

- **Diagnostics:** distinct error codes / messages for FM-1…FM-6 (the primary signal for a
  language feature).
- **rustfmt idempotence:** formatting is stable under re-format.

## Rollback

1. Keep the feature **behind its feature gate** (the unstable path) — no rollback needed
   pre-stabilization.
2. If stabilized and a soundness issue appears, **remove the gate removal** (re-gate) and
   revert the PRs; the desugaring is self-contained.

## Sub-tasks (Jira-ready)

| ID | Task | Scope | DoD | Depends on |
|---|---|---|---|---|
| T-1 | Parser support | `rustc_parse` | the statement parses; the two restrictions error | — |
| T-2 | Desugar to `match` | AST / lowering | success bindings in the surrounding scope | T-1 |
| T-3 | Divergence check | typeck / MIR | non-diverging `else` errors | T-2 |
| T-4 | Lints | `rustc_lint` | irrefutable warning; or-pattern check | T-2 |
| T-5 | rustfmt support | rustfmt | stable formatting | T-1 |
| T-6 | Docs | Reference + Book | the construct documented with examples | T-3 |

## Import target
Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the T-table as
sub-tasks.
