# Test plan — "Go back to x" navigation

> **Field-test artifact** — the kit's `sde/generate-test-ideas-and-cases` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Scope: the back-target tracking, the control, and its edge cases. Out of scope: the "Show
> history" epic (a separate epic) and browser-level history (not the ask).

## Test matrix

| ID | Layer | Scenario | Preconditions / input | Expected result | Verification |
|---|---|---|---|---|---|
| TC-1 | Unit | Back target is set on navigation | navigate A → B | back target = A | automated |
| TC-2 | Unit | Control label names the target | back target = A | label = "Go back to A" | automated |
| TC-3 | Unit | No target on first load | direct load | control hidden/disabled | automated |
| TC-4 | Integration | Click returns to previous view | on B, click control | view A renders | automated |
| TC-5 | Integration | Deep link | open B directly | no back target | automated |
| TC-6 | Integration | Rapid navigation A→B→C | three hops | back target = B | automated |
| TC-7 | Contract / API | URL stays shareable | after navigation | URL is a valid deep link | review |
| TC-8 | E2E / smoke | Panel → Explore → back | real UI | returns to the dashboard | automated (e2e) |
| TC-9 | E2E / smoke | Dashboard → dashboard → back | real UI | returns to the first dashboard | automated (e2e) |
| TC-10 | Non-functional | Keyboard access | focus + shortcut | returns to previous view | automated |
| TC-11 | Non-functional / failure injection | Previous view deleted | rename/delete target | graceful message, no crash | automated |

## Coverage notes

- **No backend layer** — a client-only change; "Integration" means the routing/state layers.
- **Not covered:** the "Show history" epic (separate), cross-session history (non-goal) — each
  with the reason.
- **Negative paths:** TC-3, TC-5, TC-11 cover the failure/absence side of the happy paths
  (TC-4, TC-8, TC-9).

## Import target
Jira — the QA/test checklist. GitHub — the PR test plan / issue body. Confluence — the test
spec page.
