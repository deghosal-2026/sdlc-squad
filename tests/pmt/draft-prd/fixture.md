# Fixture — pmt/draft-prd

Synthetic end to end. Every `[CONFIRM]` demonstrates the marking discipline.

## Input

> "Support keeps getting 'where is my order?' emails — Meridian Outfitters (fictional
> retailer). Tracking page exists but 65% of visits are logged-out. Marketing wants a
> chatbot. Support queue export pasted: 412 tickets tagged `order-status` last month."

## Expected artifact (skeleton)

# PRD: order-status self-service
> Status: Draft · Owner: [CONFIRM: name] · Last updated: 2026-11-22 · Reviewers: [CONFIRM]

## Problem & context
- 412 `order-status` tickets/month [source: pasted queue export, 2026-11]; three verbatim
  ticket quotes from the paste.

## Target users
- Guests mid-order (65% of tracking visits logged-out [source: input paste]).

## Goals
- G1: order-status tickets −50% in 2 months (baseline 412/month).

## Non-goals
- Chatbot (marketing ask — parked this phase: discovery not run on it).
- Carrier-initiated chat or SMS replies.

## User journeys
| Step | User action | System behavior | Notes |
| 1 | Opens tracking link from email | status rendered, no login | signed link |

## Requirements
- REQ-1: status visible via signed link, no login.
- REQ-2: no PII rendered unauthenticated.

## Edge cases
| EC-1 | order older than 90 days | archived message |

## Open questions
| Q1 | which locales first? | [CONFIRM: owner] | [CONFIRM: date] |

## Rollout & metrics
- Flag: `order_status_self_serve` · guardrail: p95 tracking latency [CONFIRM: baseline].

## Import target
Confluence — the PRD page for this initiative.

## Checks

- [ ] All schema sections present, in schema order
- [ ] Every number carries its paste/source or `[CONFIRM]`
- [ ] Goals ≤ 5, each metric+direction; non-goals as specific as goals
- [ ] REQs testable; edge-case section present (not skipped)
- [ ] No invented companies, names, dates, or baselines
- [ ] Import-target block present