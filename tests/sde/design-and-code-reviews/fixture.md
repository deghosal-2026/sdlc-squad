# Fixture — sde/design-and-code-reviews

Synthetic end to end.

## Input

> A 1,400-line PR touching three concerns (router, handler, alerts) with a
> 40-line test file. Team norm unknown. CODEOWNERS: [CONFIRM]. The diff is
> pasted; handler has one function a reviewer could not follow (`_redact`).

## Expected artifact (skeleton)

# Review kit — PR [CONFIRM: number]
## Author gate (before open)
- [ ] Split: 3 concerns → 3 PRs (router / handler+tests / alert) — this PR is too large;
      the split order stated.
- [ ] Self-review: line-by-line done; the two nits found are fixed before open.
- [ ] Description: what/why/verified/out-of-scope — a stranger can follow.
- [ ] Both flag states verified on; tests green before open.
## Reviewer pass (order fixed)
1. Design fit: additive branch, no breaking change [from design doc].
2. Correctness: `_redact` — **comment filed**: "I don't understand the session
   fallback here" (a confusion is a finding, not a guess).
3. Tests: 40-line test file vs 3 concerns — coverage gap comment.
4. Complexity/naming: `nit:` prefix on style points; polish never blocks.
5. Security: signed-link forge path → test exists [TC-2].
## Etiquette
- `nit:` labels; praise named ("the sig fn is clean"); turnaround [CONFIRM: norm].
- No hidden design disagreement inside bot failures.

## Checks

- [ ] Author gate before reviewer pass, both present
- [ ] The too-large PR is split with an order, not just flagged
- [ ] Confusion becomes a comment, verbatim in the kit
- [ ] Nits carry the `nit:` label; nothing polish-shaped blocks
- [ ] Turnaround norm stated or CONFIRM