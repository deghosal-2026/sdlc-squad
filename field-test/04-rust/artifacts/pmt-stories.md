# Epic: `let-else` statements

> **Field-test artifact** — the kit's `pmt/slice-mvp-and-stories` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

| Field | Value |
|---|---|
| Epic key | [CONFIRM: assigned by Jira on import] |
| Type | Epic |
| Priority | [CONFIRM: per the org's scale] |
| Business value | Remove rightward drift and the conditional/error-path gap in early-return Rust |
| Success metric | [CONFIRM: no metric published — a language feature, not a product] |

## Why

`if let` binds only inside its body, forcing nesting and separating the error path from the
conditional. A `let … else` statement moves the failure case into a block next to the
conditional and keeps the success binding in the surrounding scope. The slice below is the
**initial (unstable)** cut: the parser, the type-checker divergence rule, the lints, and the
formatter.

## Stories

| ID | Summary | Type | Priority | Size | Dependencies |
|---|---|---|---|---|---|
| US-1 | Parse `let PAT = EXPR else { … };` | Story | [CONFIRM] | [CONFIRM] | — |
| US-2 | Desugar to `match` with a diverging fallback | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-3 | Enforce the two expression restrictions | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-4 | Require the `else` block to diverge | Story | [CONFIRM] | [CONFIRM] | US-2 |
| US-5 | `irrefutable_let_patterns` warning | Story | [CONFIRM] | [CONFIRM] | US-2 |
| US-6 | Or-pattern binding-name check | Story | [CONFIRM] | [CONFIRM] | US-2 |
| US-7 | `rustfmt` support | Story | [CONFIRM] | [CONFIRM] | US-1 |
| US-8 | Reference + Book documentation | Story | [CONFIRM] | [CONFIRM] | US-4 |

### US-1 — Parse the statement

**Description:** As a Rust developer, I can write `let PAT = EXPR else { … };` and have it
parsed.
**Acceptance criteria:**
- **AC-1** Given a valid let-else statement, when compiled, then it parses without error.
- **AC-2** Given an expression ending in `}`, when written unparenthesized, then it is a
  compile error.
**Dependencies:** —

### US-2 — Desugar to a diverging `match`

**Description:** As a Rust developer, the success binding is in scope after the statement.
**Acceptance criteria:**
- **AC-1** Given a matching pattern, when the statement runs, then the bindings are usable in
  the surrounding scope.
- **AC-2** Given a non-matching pattern, then the `else` block runs.
**Dependencies:** US-1

### US-3 — Enforce the two expression restrictions

**Description:** As a Rust developer, ambiguous expressions in the let-else position are rejected.
**Acceptance criteria:**
- **AC-1** Given an expression that ends with `}`, when written unparenthesized, then a compile error is raised.
- **AC-2** Given a bare lazy boolean (`&&` / `||`) in the expression position, then a compile error is raised.
**Dependencies:** US-1

### US-4 — Require divergence

**Description:** As a Rust developer, a non-diverging `else` is a clear error.
**Acceptance criteria:**
- **AC-1** Given an `else` block that can fall through, when compiled, then a compile error is
  raised pointing at the block.
**Dependencies:** US-2

### US-5 — Irrefutable-pattern warning

**Description:** As a Rust developer, an irrefutable pattern warns.
**Acceptance criteria:**
- **AC-1** Given `let x = y else { … };`, then the `irrefutable_let_patterns` warning fires.
**Dependencies:** US-2

### US-6 — Or-pattern binding check

**Description:** As a Rust developer, mismatched or-pattern bindings are rejected.
**Acceptance criteria:**
- **AC-1** Given `let A(x) | B(y) = e else { … };`, then a compile error is raised.
**Dependencies:** US-2

### US-7 — rustfmt support

**Description:** As a Rust developer, `rustfmt` formats let-else consistently.
**Acceptance criteria:**
- **AC-1** Given a let-else statement, when formatted, then the `else` block is indented per
  style and re-formatting is stable.
**Dependencies:** US-1

### US-8 — Documentation

**Description:** As a Rust developer, the construct is documented.
**Acceptance criteria:**
- **AC-1** Given the Reference and the Book, then let-else is described with examples.
**Dependencies:** US-4

## Dependencies

| ID | On what | From | Blocks | Status |
|---|---|---|---|---|
| DEP-1 | Language-team sign-off (RFC) | rust-lang/lang | all | [CONFIRM] |
| DEP-2 | `rustfmt` maintainers | rust-lang/rustfmt | US-7 | [CONFIRM] |
| DEP-3 | Diagnostics infra | rust-lang/compiler | US-4, US-5 | [CONFIRM] |

## Import target
Jira — epic + stories via bulk import / CSV; paste each story's block into its ticket
description.
