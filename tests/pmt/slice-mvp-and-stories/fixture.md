# Fixture — pmt/slice-mvp-and-stories

Synthetic end to end.

## Input

> The order-status PRD (above fixture), accepted. Estimate scale: T-shirt
> (S=2d, M=5d, L=10d of one engineer). Dependency: guest-status events come
> from the Checkout service.

## Expected artifact (skeleton)

# Epic: order-status self-service
| Type | Epic · Priority | P1 · Value | cut support load on the order pipeline · Metric | status tickets −50%

## Stories
| ID | Summary | Type | Size | Dependencies |
| US-1 | Guest opens signed tracking link and sees status | Story | M | DEP-1 |
| US-2 | Support links the same guest view from macros | Story | S | US-1 |
| US-3 | Archived-order message for >90-day orders | Story | S | US-1 |
| US-4 | Chatbot (marketing ask) | — not sliced | out: non-goal this phase |

### US-1 — Guest sees order status via signed link
**AC-1** Given a signed link from the order email, when opened logged-out, then order state,
ship ETA, and package list render.
**AC-2** Given the same link, when opened, then no account PII renders.
Dependencies: DEP-1 status events from Checkout [CONFIRM: owner].

## Checks

- [ ] Every story is vertical (ships user value alone) or explicitly labeled a task
- [ ] ACs are Given/When/Then and testable as observable behavior
- [ ] Sizes only in the user's supplied scale (T-shirt legend shown)
- [ ] Dependency rows name the team or `[CONFIRM]`; non-goal (chatbot) not sliced as a story
- [ ] Pipe characters kept out of cell bodies (CSV-safe)