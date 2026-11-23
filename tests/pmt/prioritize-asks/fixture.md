# Fixture — pmt/prioritize-asks

Synthetic end to end.

## Input

> Pile of asks: "order-status self-serve" (support paste, 412/mo); "chatbot"
> (marketing, exec, 1 asker); "carrier deep-link" (support paste, 3 tickets);
> "dark mode" (sales, 1); plus a note: reach for order-status ≈ 2,300 tracking
> visits/month per the input paste.

## Expected artifact (skeleton)

# Ranked asks — order pipeline
## Normalized pile: 5 raw asks, deduped to 5 (sources counted).
## Framework: RICE (default) — Reach people/quarter · Impact 3/2/1/0.5/0.25 · Confidence 100/80/50% · Effort person-months.
## Scored
| ask | R | I | C | E | RICE | basis |
| order-status self-serve | 6,900/q | 1 | 80% | 1.5 | 3,680 | reach: 2,300/mo [paste]; effort [CONFIRM: SDE] |
| carrier deep-link | 690/q | 0.5 | 80% | [CONFIRM] | — | blocked: no effort estimate |
| chatbot | 690/q | 0.5 | 50% | [CONFIRM] | labeled moonshot | confidence < 50% floor |
| dark mode | 690/q | 0.25 | 50% | [CONFIRM] | labeled | — |
## Ranking basis: score, then dependency; order-status first regardless (dependency root).
## Tail (not ranked): carrier deep-link + chatbot + dark mode — need effort estimates (SDM/SDE) before ranking.

## Checks

- [ ] Framework stated with legend before scores
- [ ] Every score cell carries its basis or CONFIRM
- [ ] Confidence < 50% labeled, not silently ranked
- [ ] Tail present with reasons
- [ ] Effort numbers not invented (they are SDM/SDE's to estimate)