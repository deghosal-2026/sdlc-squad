# Walkthrough — one full run, start to finish

One skill, end to end: the raw input → the load → the questions → the artifact → the
`[CONFIRM]`s resolved → where it lands. The company (**Meridian Outfitters**) and every
value below are **fictional** — they match the committed fixture
[`../tests/sdm/sprint-planning-and-capacity/fixture.md`](../tests/sdm/sprint-planning-and-capacity/fixture.md)
and its recorded run (§1.11 of
[`../tests/results/run-2026-11-22-v0.1.0.md`](../tests/results/run-2026-11-22-v0.1.0.md)).
Nothing here is invented beyond the synthetic fixture.

## 0. Before you start

```bash
pip install sdlc-squad && sdlc-squad   # prints the kit path + load order
```

## 1. The raw input

I'm an SDM planning Sprint 14 (2026-12-07 → 2026-12-18, 10 working days). Six engineers
(A–F). D is on PTO Thu–Fri. Ceremonies + standing meetings run ~6h/week each. Weekly
on-call rotation, ~0.5 day load. Support/interrupt buffer ~0.5 day each. Three stories
carried over (2d + 2d + 1d). Candidates: order-status M1 (est. 8d), flaky-test fix (2d),
dark mode (no estimate — flag it). Show all arithmetic; commit ≤ net focus.

## 2. The load (four files, in order)

`shared/system-conventions.md` → `shared/glossary-and-org.md` (or your `my-org.md`) →
`roles/sdm.md` → `skills/sdm/sprint-planning-and-capacity/SKILL.md`. *(Or one bundle:
`usage/bundles/sdm-sprint-planning-and-capacity.md` + your glossary.)*

## 3. The questions it asks (≤3)

1. **Ceremony hours per person?** → ~6h/week each (≈1.5d/sprint).
2. **Is on-call load-bearing this sprint?** → Yes, weekly rotation, ~0.5d.
3. **Do carry-overs keep their old sizes or re-estimate?** → Keep old sizes (2d+2d+1d).

## 4. The artifact

```markdown
# Sprint 14 plan — Team [CONFIRM: name], 2026-12-07 → 2026-12-18

## Capacity
| Engineer | Gross days | − PTO | − Meetings & ceremonies | − On-call / support / toil | = Net focus days |
|---|---|---|---|---|---|
| A | 10 | 0 | 1.5 | 0.5 | 8.0 |
| B | 10 | 0 | 1.5 | 0.5 | 8.0 |
| C | 10 | 0 | 1.5 | 0.5 | 8.0 |
| D | 10 | 2 | 1.5 | 0.5 | 6.0 |
| E | 10 | 0 | 1.5 | 0.5 | 8.0 |
| F | 10 | 0 | 1.5 | 0.5 | 8.0 |
[every cell trails an input, or [CONFIRM]; team net focus 46.0 days — arithmetic shown]

## Proposed commitment
| Bucket | Items | Net focus days |
|---|---|---|
| Carry-over | 3 stories (2d+2d+1d) | 5.0 |
| Core / milestone work | order-status M1 (est. 8d) | 8.0 |
| Tech debt / reliability / buffer | flaky-test fix (est. 2d) | 2.0 |
| **Total committed** | | 15.0 ≤ 46.0 |

## Flagged risks
- dark mode: unestimated → **not committed**, listed here.
- [CONFIRM: any engineer over 90% net focus — flag with the number]

## Import target
Confluence — the sprint planning note. Jira — the sprint backlog after grooming.
```

*(Numbers above mirror the fixture's shape; the fixture is the source of record for the
exact rows.)*

## 5. Resolve the `[CONFIRM]`s

- `[CONFIRM: name]` → **Meridian Outfitters** (the team is fictional; use your real team).
- dark mode → either get an estimate (then it fits the buffer) or leave it **uncommitted
  and flagged** — never a silent trim ([`../docs/REVIEWING-OUTPUT.md`](../docs/REVIEWING-OUTPUT.md)).

## 6. Where it lands

Paste the artifact into the Confluence sprint-planning note; the Jira sprint backlog after
grooming. You are the import mechanism — the kit pushes nothing.

## What to read next

[`../docs/START-HERE.md`](../docs/START-HERE.md) (task chooser) ·
[`../docs/REVIEWING-OUTPUT.md`](../docs/REVIEWING-OUTPUT.md) (the pre-paste checklist) ·
[`../docs/EVIDENCE.md`](../docs/EVIDENCE.md) (how the kit catches itself)
