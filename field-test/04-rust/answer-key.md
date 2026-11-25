# Answer key — what the project actually shipped

> **Source:** `rust-lang/rfcs` RFC 3137 (Reference-level explanation, Drawbacks,
> Alternatives) + Rust issue [#87335]. Retrieved **2026-11-25**.
> <https://github.com/rust-lang/rfcs/blob/master/text/3137-let-else.md>
> Held back from `input.md`; used to score the kit's artifacts in `findings.md`.

## The design

A new statement:

```rust
let PATTERN: TYPE = EXPRESSION else DIVERGING_BLOCK;
```

- If the pattern **matches**, its bindings are introduced **into the surrounding scope**.
- If it **does not match**, the `else` block runs and **must diverge** (return `!` —
  `return`, `break`, `continue`, `loop {}`, a diverging fn, or a panic).
- It is the counterpart of `if let`, and **syntactic sugar for `match`** where the
  non-matched arm diverges:

```rust
let Some(x) = y else { return; };
// desugars to
let x = match y {
    Some(x) => x,
    _ => { let nope: ! = { return; }; match nope {} }
};
```

### Restrictions

1. The expression may **not end with `}`** (before macro expansion) — parenthesize instead
   (prevents `… else {} else {}` ambiguity).
2. The expression may **not be just a lazy boolean expression** (`&&` / `||`) — kept open for
   future if-let-chains compatibility.
3. Any **refutable** pattern valid in `if let` is valid here.
4. An **irrefutable** pattern triggers the `irrefutable_let_patterns` warning lint.
5. **Or-patterns** (`|`) must bind the same names across variants.

### Not in scope (per the RFC)

if-let-chains, fall-back assignment, `let PATTERN = EXPR else DIVERGING_EXPR` (no block),
introducer syntax (`guard let`), renaming `else` to `otherwise`.

## Outcome

- **Rust issue:** [#87335].
- **Stabilization:** `[CONFIRM: stabilized in Rust 1.65 (2022-11) — verify the exact version.]`
- **Prior art:** Swift's `guard let … else`; the `guard!` crate; a 2015 RFC (PR #1303).

[#87335]: https://github.com/rust-lang/rust/issues/87335
