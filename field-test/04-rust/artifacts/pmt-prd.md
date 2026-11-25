# let-else — a `let` with a diverging `else`

> **Field-test artifact** — the kit's `pmt/draft-prd` output from [`../input.md`](../input.md).
> Compare against [`../answer-key.md`](../answer-key.md) in [`../findings.md`](../findings.md).

> Status: Draft · Owner: [CONFIRM: name] · Last updated: 2026-11-25 · Reviewers: [CONFIRM: names]

## Problem & context

- `if let` can only bind **inside its body**, forcing **rightward drift**, **nesting**, and a
  **gap between the conditional and the error path** (source: RFC 3137 Motivation).
- Emulating early-return with `match`/`ok_or_else` adds boilerplate and intermediary bindings,
  and does **not** work for enums that aren't `Option`/`Result` (source: RFC 3137 Motivation).
- A real refactor was **+531 −529** lines over 4,111 lines; the largest block was 90 lines
  that could have shifted left (source: RFC 3137 Motivation).

## Target users

- **Rust developers** writing early-return error handling — especially with custom enums whose
  "success" variant is contextual and which have no `Option`/`Result` helpers.

## Goals

- Let the **success** binding land in the **surrounding scope**, not nested in a body.
- Put the **failure** case in a block **next to** the conditional (reduces drift/nesting).
- Work for **any refutable pattern** `if let` accepts, including non-`Option`/`Result` enums.

## Non-goals

- `if let` chains (a separate, unimplemented feature).
- Fall-back assignment (assigning from the `else` block).
- Any new **negation** pattern-matching rules.
- A new keyword (`otherwise`) or introducer syntax (`guard let`).

## User journeys

| Step | User action | System behavior | Notes |
|---|---|---|---|
| 1 | Write `let PAT = expr else { … };` | Parser accepts the statement | subject to the two expression restrictions |
| 2 | The pattern matches | bindings enter the surrounding scope | like a normal `let` |
| 3 | The pattern does not match | the `else` block runs and must diverge | `!`-typed |
| 4 | The `else` block can't diverge | compile error | the outer context can't continue soundly |

## Requirements

### Functional

- **REQ-1** A `let PATTERN = EXPRESSION else { … };` statement is parsed as sugar for `match`
  with a diverging fallback arm.
- **REQ-2** On match, bindings are introduced into the **surrounding scope**.
- **REQ-3** The `else` block **must diverge** (`!`); otherwise a compile error.
- **REQ-4** The expression may **not end with `}`**, and may **not** be a bare lazy boolean
  (`&&`/`||`).
- **REQ-5** Any refutable pattern valid in `if let` is valid; an irrefutable one warns
  (`irrefutable_let_patterns`).
- **REQ-6** Or-patterns must bind the same names across variants.

### Non-functional

- **REQ-7** `rustfmt` formats let-else consistently; the trailing `else` is not mis-indented.
- **REQ-8** Diagnostics point at the non-diverging `else` block with a clear message.
- **REQ-9** Documentation (the Reference + the Book) covers the construct.

## Edge cases

| EC | Trigger | Expected behavior |
|---|---|---|
| EC-1 | `else` block does not diverge | compile error |
| EC-2 | Expression ends with `}` | compile error; require parentheses |
| EC-3 | Expression is a lazy boolean | compile error (future if-let-chains) |
| EC-4 | Irrefutable pattern | `irrefutable_let_patterns` warning |
| EC-5 | Or-pattern with mismatched bindings | compile error |
| EC-6 | `if let p = e else { } { }` | not allowed; use `if let p = e { } else { }` |

## Open questions

| # | Question | Owner | Needed by |
|---|---|---|---|
| Q-1 | Conflict with the if-let-chains RFC | [CONFIRM: lang team] | [CONFIRM] |
| Q-2 | Grammar clarifications for the two restrictions | [CONFIRM: lang team] | [CONFIRM] |

## Rollout & metrics

- **Staged:** RFC accepted → implementation behind a feature gate → **stabilization**
  (source: RFC 3137; `[CONFIRM: stabilization version]`).
- **Metric:** adoption in crates.io code — `[CONFIRM: no metric published in the RFC]`.

## Import target
Confluence — the PRD/RFC page for this initiative.
