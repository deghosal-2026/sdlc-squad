# Prompt book — SDM (Software Development Manager)

**Load first (every session):** `shared/system-conventions.md` → `shared/glossary-and-org.md`
(fill your org slots) → `roles/sdm.md` → the skill's `SKILL.md`.
**Redact personal data before pasting anything.** Every prompt below is a sample — swap in
your real facts; anything you leave out comes back as `[CONFIRM: ...]`, never invented.
The example company (Meridian Outfitters) is fictional.

## 1. sprint-planning-and-capacity — net focus capacity + commitment

**Paste with:** `skills/sdm/sprint-planning-and-capacity/SKILL.md`

```
Plan Sprint 14 (2026-12-07 → 2026-12-18, 10 working days). Roster: engineers A–F.
PTO: D is out Thu–Fri. Meetings/ceremonies: ~6h/week each. On-call: weekly
rotation, ~0.5d load. Support/interrupt buffer: 0.5d each. Carry-over: 3 stories
(2d + 2d + 1d). Candidates: order-status M1 (est. 8d), flaky-test fix (2d),
dark mode (no estimate — flag it). Show all arithmetic; commit ≤ net focus.

[PASTE: roster / PTO calendar / candidate backlog with estimates]
```

**Import target:** Confluence — the sprint planning note. Jira — the sprint backlog.

## 2. standup-execution — daily round + blocker log

**Paste with:** `skills/sdm/standup-execution/SKILL.md`

```
Run today's standup log (15 min, board order). Board: US-1 in progress;
US-3 waiting on review slot; US-4 blocked on DEP-3 translations since
yesterday. Yesterday's log attached — carry open blockers forward with
aging. Escalation norm: one working day. Park anything over 2 minutes.

[PASTE: board state / yesterday's blocker log]
```

**Import target:** Confluence — the standup page. Jira — escalated blockers as comments.

## 3. scope-cut-and-tradeoffs — ranked keep/defer/cut options

**Paste with:** `skills/sdm/scope-cut-and-tradeoffs/SKILL.md`

```
We're 3 days over capacity for Sprint 14 and the date is fixed (freeze-adjacent).
Generate cut options in exactly three moves (Must-Ship / Defer / Cut) for:
M1 order-status (8d), carrier deep-link (4d), flaky-test fix (2d), dark mode
(unknown). Cost each against customer value, technical risk, and the TPM
milestones. Rank by total damage; I decide.

[PASTE: current commitment + the capacity math]
```

**Import target:** Confluence — the decision log. Jira — the epic scope update.

## 4. operational-health-review — toil/flaky/bottleneck review

**Paste with:** `skills/sdm/operational-health-review/SKILL.md`

```
Review this quarter's ops health. Pasted: 11 reopen tickets on the status page
(same stale-cache signature), 9 in the last 6 weeks; weekly manual cache purge
(30 min × 12); flaky test test_status_guest failed 7 of 20 CI runs, blocked 2
merges; review turnaround median 2.1 days. Rank hotspots by capacity stolen;
draft remediation tickets with DoDs for the debt buffer. No blame.

[PASTE: ticket history / flaky runs / interrupt logs]
```

**Import target:** Confluence — the retro/ops doc. Jira — the maintenance tickets.

## 5. sprint-retro — last 2 sprints' done tickets → retro + action items

**Paste with:** `skills/sdm/sprint-retro/SKILL.md`

```
Run the retro for Sprints 13–14 from the attached done-ticket exports.
Sprint 13: 14 tickets, 12 closed in-sprint, 2 reopened once, 2 carried into 14.
Sprint 14: 16 done, 0 reopens, 1 carried into 15. On-call log: one Sev-2 in
Sprint 13. Went-well and hurt need receipts (ticket IDs from the paste);
action items as T-tickets with owners and DoDs; disposition the open carry.

[PASTE: Sprint 13 + Sprint 14 done-ticket exports / both sprint plans]
```

**Import target:** Confluence — the retro page. Jira — the action-item tickets.