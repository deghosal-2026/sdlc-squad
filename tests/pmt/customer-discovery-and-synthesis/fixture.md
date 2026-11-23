# Fixture — pmt/customer-discovery-and-synthesis

Synthetic end to end. Two runs: guide, then synthesis on pasted notes.

## Input (guide run)

> "We're deciding whether order-status self-serve should include live carrier chat.
> Reachable: 5 recent support-ticket submitters."

## Expected artifact — guide (skeleton)

# Discovery guide: order-status live chat?
## Decision this informs: include live carrier chat in v1 — yes/no.
## Screening: pasted `order-status` ticket submitters, last 30 days; excluded: enterprise accounts.
## Flow: open → their life → the last order-tracking episode → what it cost them → close.
## Questions (all open, past-behavior)
1. "Walk me through the last time you checked an order status."
2. "What did you do when the page didn't answer you?"
3. "What did that wait cost you — minutes, calls, anything?"
(deflects: any "would you use live chat?" — hypothetical, not in the guide)

## Input (synthesis run)

> 5 pasted interview notes. Three of five describe calling the store after the page
> staled; one proposes "an AI chatbot"; two mention checking the carrier site directly.

## Expected artifact — synthesis (skeleton)

# Synthesis: 5 interviews
## Themes
| T1 "the page staled and I called the store" | 3/5 notes | signal: specific, recent, repeated |
| T2 "I go straight to the carrier site" | 2/5 notes | signal |
| T3 "an AI chatbot" | 1/5 | anecdote: a proposed solution, recorded as words |
## Verbatim quotes: one per theme, quoted from the paste.
## Needs, not solutions: T1 → need = current-enough status; T3 → recorded, not adopted.

## Checks

- [ ] No leading/hypothetical questions in the guide
- [ ] Every theme carries a count from the paste + a verbatim quote
- [ ] Solutions-in-disguise labeled as their words, never adopted as requirements
- [ ] Signal vs. anecdote labeled