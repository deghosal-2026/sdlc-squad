# Test plan — Node-compatible module loader API

> **Field-test artifact** — the kit's `sde/generate-test-ideas-and-cases` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Scope: the Node loader hook surface, `require(ESM)`, invalidation, gating, and the default
> path. Out of scope: a bespoke `Deno.loader` (explicitly not built) and re-evaluation of
> already-evaluated modules (spec-forbidden).

## Test matrix

| ID | Layer | Scenario | Preconditions / input | Expected result | Verification |
|---|---|---|---|---|---|
| TC-1 | Unit | Resolve hook is invoked | a registered loader | hook called with the specifier | automated |
| TC-2 | Unit | Load hook is invoked | a registered loader | hook returns the module source | automated |
| TC-3 | Unit | No loader registered | default run | fast path; hooks not invoked | automated |
| TC-4 | Integration | `require(ESM)` | `require('./mod.mjs')` | ESM loads | automated |
| TC-5 | Integration | Invalidate + re-import | invalidate a specifier, import again | new module used; old not re-evaluated | automated |
| TC-6 | Integration | Nested imports update | a changed child module | children resolve to the update | automated |
| TC-7 | Contract / API | Node API compatibility | a Node-using project | runs under Deno without a bespoke API | automated |
| TC-8 | Contract / API | Gating off by default | no flag/permission | capability off | automated |
| TC-9 | E2E / smoke | HMR-style dev server | a minimal HMR harness | edit a file → re-import reflects it | automated |
| TC-10 | E2E / smoke | Test mocking | mock a module via the loader | the mock is used | automated |
| TC-11 | Non-functional | Default-path performance | no loader | no measurable regression | automated (bench) |
| TC-12 | Non-functional | Memory retention | repeated invalidations | growth bounded/documented | automated (bench) |
| TC-13 | Non-functional / failure injection | Loader hook throws | injected loader error | error surfaced to the tool, not swallowed | automated |

## Coverage notes

- **No re-evaluation test by design** — the ES spec forbids re-evaluating a module; the test is
  that the *old module is not re-run* (TC-5).
- **Not covered:** the bespoke `Deno.loader` fork (won't-do), V8-internal module-map behavior
  (out of Deno's public surface) — each with the reason.
- **Negative paths:** TC-3, TC-8, TC-13 cover the failure/absence side of the happy paths
  (TC-1, TC-4, TC-9).

## Import target
Jira — the QA/test checklist. GitHub — the PR test plan / issue body. Confluence — the test
spec page.
