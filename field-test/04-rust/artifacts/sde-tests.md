# Test plan — `let-else`

> **Field-test artifact** — the kit's `sde/generate-test-ideas-and-cases` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Scope: the parser, the divergence rule, the lints, rustfmt, and diagnostics. Out of scope:
> if-let-chains (a separate feature) and fall-back assignment (a non-goal).

## Test matrix

| ID | Layer | Scenario | Preconditions / input | Expected result | Verification |
|---|---|---|---|---|---|
| TC-1 | Unit | Parser accepts a valid let-else | `let Some(x) = y else { return; };` | parses | automated |
| TC-2 | Unit | Expression ends with `}` | `let P = if a { b } else { c } else { d };` | parser error | automated |
| TC-3 | Unit | Bare lazy boolean | `let true = a && b else { return; };` | parser error | automated |
| TC-4 | Integration | Success binding in scope | matching pattern | binding usable after the statement | automated |
| TC-5 | Integration | Non-diverging `else` | `else { }` | compile error at the block | automated |
| TC-6 | Integration | Diverging forms accepted | `return` / `break` / `continue` / `loop {}` / panic | compiles | automated |
| TC-7 | Contract / API | Desugaring equivalence | let-else vs the equivalent `match` | identical semantics | review |
| TC-8 | Contract / API | Irrefutable pattern | `let x = y else { … };` | `irrefutable_let_patterns` warning | automated |
| TC-9 | Contract / API | Or-pattern same names | `let A(x) | B { x, .. } = e else { return; };` | compiles | automated |
| TC-10 | Contract / API | Or-pattern mismatched names | `let A(x) | B(y) = e else { … };` | compile error | automated |
| TC-11 | E2E / smoke | Compile a program using let-else | a small crate | builds and runs | automated |
| TC-12 | E2E / smoke | `if let p = e else { } { }` | that source | parser error | automated |
| TC-13 | Non-functional | rustfmt idempotence | a let-else file | format twice → no change | automated |
| TC-14 | Non-functional | Diagnostic clarity | each error case | message points at the right span | review |
| TC-15 | Non-functional | Compile-time cost | a large file of let-else | no measurable regression | automated (bench) |

## Coverage notes

- **No runtime layer** — a language feature has no service to smoke-test; "E2E" means *compile
  and run a program*.
- **Not covered:** if-let-chains interaction (a separate RFC), fall-back assignment (non-goal) —
  each by design.
- **Negative paths:** TC-2, TC-3, TC-5, TC-10, TC-12 cover the failure side of the happy paths
  (TC-1, TC-4, TC-6).

## Import target
Jira — the QA/test checklist. GitHub — the PR test plan / issue body. Confluence — the test
spec page.
