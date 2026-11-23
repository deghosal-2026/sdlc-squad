# Prompt book — TPM (Technical Program Manager)

**Load first (every session):** `shared/system-conventions.md` → `shared/glossary-and-org.md`
(fill your org slots) → `roles/tpm.md` → the skill's `SKILL.md`.
**Redact personal data before pasting anything.** Every prompt below is a sample — swap in
your real facts; anything you leave out comes back as `[CONFIRM: ...]`, never invented.
The example company (Meridian Outfitters) is fictional.

## 1. program-roadmap-and-deps — milestones + dependency graph

**Paste with:** `skills/tpm/program-roadmap-and-deps/SKILL.md`

```
Build the program plan for the accepted order-status PRD. Teams: Checkout owns
status events, Notifications owns the guest email template, Platform owns launch.
Launch before the Dec-15 change freeze. Show slack per link; name the critical
path end to end; flag zero-slack links.

[PASTE: the PRD / team commitments you already have]
```

**Import target:** Confluence — the program page. Jira — dependency links on the epic.

## 2. risk-raid-and-mitigations — RAID log

**Paste with:** `skills/tpm/risk-raid-and-mitigations/SKILL.md`

```
Draft a RAID log for this program. Known worries: Checkout's events API may miss
the freeze; the guest email template needs a legal review. Assumption: carrier
payload format stays stable. Open issue: legal review not yet scheduled. Every
risk needs an early-warning signal, a mitigation, AND a fallback.

[PASTE: prior RAID entries / open issues]
```

**Import target:** Confluence — the weekly program status page.

## 3. release-readiness-check — go/no-go checklist

**Paste with:** `skills/tpm/release-readiness-check/SKILL.md`

```
Run the go/no-go checklist for the order-status launch. Flag:
order_status_self_serve, default off, flip 5%→50%→100%. Migration 0431
(reversible) runs pre-deploy. Dashboards: queue volume, web latency; alert:
outbox lag. Support runbook drafted but unpublished. Sign-offs needed:
PMT, SDM, legal. Name the last safe abort moment.

[PASTE: launch checklist inputs / design rollback section]
```

**Import target:** Confluence — the launch doc. Jira — the release ticket.

## 4. program-status-review — R/Y/G status of all items (bi-weekly/monthly)

**Paste with:** `skills/tpm/program-status-review/SKILL.md`

```
Produce this month's program status report. Cadence: monthly. Report against:
the program milestones and the G1 objective. This month's Jira paste:
M1 done 2026-12-11 tagged release-14; M2 legal review scheduled; new dependency
DEP-3 on translations. Last month's report attached — show deltas, not a re-run.
No status without its evidence; every ask needs an owner and a by-when.

[PASTE: Jira milestones/epics export + last review's report + RAID changes]
```

**Import target:** Confluence — the program status page; the review runs from it.