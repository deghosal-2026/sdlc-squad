# Output schema — Test plan and cases

Bound by: `sde/generate-test-ideas-and-cases`. Also the test-matrix export of
`tpm/release-readiness-check`.

## Canonical shape

```markdown
# Test plan — [Feature]

> Scope: [what is in test] · Out of scope: [what is not, and why]

## Test matrix
| ID | Layer | Scenario | Preconditions / input | Expected result | Verification |
|---|---|---|---|---|---|
| TC-1 | Unit | ... | ... | ... | automated / manual / review |
| TC-n | Integration | ... | ... | ... | ... |
| | Contract / API | ... | ... | ... | ... |
| | End-to-end / smoke | ... | ... | ... | ... |
| | Non-functional / failure injection | ... | ... | ... | ... |

[One row per case. Every layer heading appears even when empty, with "none" and the reason.]

## Coverage notes
[What the matrix does not cover, each with the reason: cost, flakiness, environment.]

## Import target
Jira — the QA/test checklist. GitHub — the PR test plan / issue body. Confluence — the test
spec page.
```

## Rules

- Layers are fixed: Unit · Integration · Contract/API · End-to-End/Smoke ·
  Non-Functional/Failure Injection.
- A case states its verification type. "Manual" and "review" are allowed; "hopefully" is not.
- Failure injection cases name the injected fault (timeout, 5xx, partial write, poison
  message).
- Negative paths are not optional: every happy-path row implies at least one failure-path row,
  or a stated reason.