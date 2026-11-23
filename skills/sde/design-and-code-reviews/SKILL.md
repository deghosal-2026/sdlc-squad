---
name: design-and-code-reviews
description: Produce the author gate, the reviewer pass, and the review etiquette for a PR: small diffs, self-review, nit labels, confusion as comments.
role: sde
status: built
created: 2026-11-22
---

# design-and-code-reviews — author + reviewer checklists

## What it produces

Two checklists and an etiquette page: the **author-side** pre-open gate and the
**reviewer-side** pass, plus the etiquette that keeps both humane — nits labeled `nit:`,
praise named, polish never blocks, and every "I don't understand this" becomes a comment
instead of a guess.

## RACI row

`Design & code reviews` — **SDE A/R** (`shared/raci.md`); PMT I · TPM I · SDM C.

## Inputs required

- The diff/PR paste or paths (unread code is `[CONFIRM]`)
- The design doc the change implements
- The team's review standards, if any exist (CODEOWNERS, size limits, turnaround norms)

## Clarifying questions when inputs are missing

Ask up to 3, then draft with `[CONFIRM]`:

1. How large is too large here — files, lines, or review-hours?
2. Who must review (CODEOWNERS), and who merely may?
3. What is this team's nit threshold — and who approves the style call?

## Steps — author gate (before the PR opens)

1. **Split to small reviewable diffs.** One concern per PR; a refactor PR sets the stage
   before the feature PR. The team's size norm is stated or `[CONFIRM: norm]` — a
   1,000-line PR ships unreviewed somewhere, and the artifact says so.
2. **Self-review first.** The author walks their own diff line-by-line before anyone else
   sees it — the reviewer's first read should find nothing the author could have caught.
3. **A description a stranger can follow.** What changes, why, how it was verified (tests,
   commands, outputs), what is out of scope. Self-approve only after you would approve it.
4. **Both flag states verified** — flag on, flag off restores prior behavior — and tests
   green, before open.

## Steps — reviewer pass

5. **Order: design fit → correctness → tests → complexity & naming → security.** Design
   disagreements go in comments, not hidden inside a bot failure.
6. **Every confusion is a comment.** "I don't understand this" is a real finding — it means
   the next owner won't either.
7. **Nits labeled `nit:`** — polish, not blocking. Praise named, not implied silence.
   Perfection is not the standard; the standard is what the next owner can change safely.
8. **Turnaround stated.** The team's expectation (same-day? 24h?) is in the etiquette page
   or `[CONFIRM: norm]`.
9. **Read-back pass + hand over.** Emit both checklists + etiquette ending with the
   Import-target block. Answer questions. Wait.

## Output binding

`shared/system-conventions.md` table rules.

## Import target

GitHub — the PR template / review guide. Confluence — the team review-standards page.

## Worked example

`tests/sde/design-and-code-reviews/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
