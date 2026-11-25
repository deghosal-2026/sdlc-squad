# Input — the raw problem (what a session would paste)

> **Source:** `rust-lang/rfcs`, RFC 3137 *"let-else"* — **Motivation**. Retrieved
> **2026-11-25**. <https://github.com/rust-lang/rfcs/blob/master/text/3137-let-else.md>
> Quoted/paraphrased; the **design is held back** in `answer-key.md`. Redaction: public
> project text; no personal data. `[CONFIRM: confirm license terms before publishing.]`

---

## Problem

`if let` offers a succinct syntax for matching a single pattern — useful for unwrapping
types like `Option` with a clear "success" variant but no specific "failure" variant. But an
`if let` can only create bindings **within its body**, which:

- forces **rightward drift**,
- introduces **excessive nesting**, and
- **separates the conditionals from the error paths**.

Emulating the pattern with `match` or `if let` requires intermediary bindings (usually of the
same name) and syntax boilerplate. It is especially awkward for enums that are **not**
`Option`/`Result`, which have no `ok_or()`-style helpers.

A real refactor of large `if let` blocks over `Option`s into early-return `match` expressions
was **+531 −529 lines** over a 4,111-line codebase; the largest block was 90 lines that could
have shifted left had the error case been movable to the conditional.

## Goal

Simplify the common **early-return error-handling pattern**: check error cases first, then
continue on the happy path — with the failure case in a block next to the conditional, and
the success binding in the **surrounding scope** instead of nested inside a body.

*This is the input. `answer-key.md` holds what Rust actually built.*
