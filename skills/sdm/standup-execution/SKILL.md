---
name: standup-execution
description: Run the daily standup — a board-order round plus a blocker log with aging, escalation, and carry-risk flags. Use for the daily team sync.
role: sdm
status: built
created: 2026-11-22
---

# standup-execution — daily round + blocker log

## What it produces

The standup run kit: the round format (timebox, board-order, three columns per person —
today / blocker / carry-risk), the **running blocker log** (blocker · owner · since-when ·
next step · by-when), the aging/escalation rule, and the parking-lot list for deep dives
that do not belong in the round.

## RACI row

`Standup execution & blocker log` — **SDM A/R** (`shared/raci.md`); PMT — · TPM I · SDE C.

## Inputs required

- The sprint commitment (from `sprint-planning-and-capacity`) and the current board state
- Yesterday's blocker log, for aging
- On-call/interrupt context for today
- The team's timebox and escalation norms (or the request to propose them)

## Clarifying questions when inputs are missing

Ask up to 3, then run with `[CONFIRM]`:

1. What is the round format — board order, and how many minutes?
2. At what blocker age does escalation fire (a day? two?), and to whom?
3. Which in-flight items are already trending to carry-over?

## Steps

1. **Pin the round.** Timebox (15m), order = board order (in-progress first), not people
   order — the board is the agenda. Stated at the top of the log.
2. **Three columns per person.** Today (what moves) · blocker (what is stuck, since when) ·
   carry-risk (what is trending long). **No yesterday-theater** — the board already says
   what happened; recaps are progress theater, and the log does not collect them.
3. **Capture every blocker as a row.** What · who · since when · next step · by when. A
   blocker without a next step is a complaint, not a row.
4. **Aging and escalation.** Any blocker older than the threshold (default: one working day,
   or `[CONFIRM: norm]`) escalates in the log — owner + escalation target + deadline, in
   the row. The log shows which rows are over-threshold; aging is never silent.
5. **Call the carry-risks.** Items trending to carry-over are flagged *before* the sprint's
   last days — that is the log's second job, and it feeds `sprint-retro` and the next
   `sprint-planning-and-capacity` run.
6. **Park the deep dives.** Anything > 2 minutes goes to the parking lot with its people
   and its slot ("after standup, 10:30"). The round stays the round.
7. **Read-back pass.** Blockers current (yesterday's rows carried or closed), aging visible,
   parking lot recorded, no recap theater.
8. **Hand over.** Emit the day's log ending with its Import-target block. Answer questions.
   Wait.

## Output binding

`shared/system-conventions.md` table rules; `R-n` prefix for escalated blockers that are
program-visible.

## Import target

Confluence — the team's standup page. Jira — escalated blockers as comments/tickets on the
blocked items.

## Worked example

`tests/sdm/standup-execution/fixture.md` — full input + expected artifact (synthetic).
Recorded run: `tests/results/run-2026-11-22-v0.1.0.md`.
