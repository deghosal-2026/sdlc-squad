# Fixture — sdm/operational-health-review

Synthetic end to end.

## Input

> Pasted last-quarter ticket history: 11 reopen tickets on `status/` page
> (same stale-cache signature), 9 of them the last 6 weeks; toil: weekly manual
> cache purge, 30 min, 12 events; flaky test `test_status_guest` failed 7 of
> last 20 CI runs, blocked a merge twice; review turnaround: median 2.1 days
> [paste].

## Expected artifact (skeleton)

# Ops health — Q4 review
## Hotspots (ranked by capacity stolen)
| 1 | stale-cache reopens | 11 tickets, 9 recent [paste] | ≈ 5.5d/quarter (11 × ~0.5d) |
| 2 | cache-purge toil | 12 × 0.5h = 6h/quarter [paste: 30 min × 12] |
| 3 | flaky `test_status_guest` | 7/20 runs [paste], 2 blocked merges |
| 4 | review turnaround | median 2.1d [paste] — bottleneck row, [CONFIRM: unmeasured queue depth] |
## Remediation tickets
| T-1 | auto-cache-invalidation on status write | DoD: 90 days zero manual purges | next debt-buffer |
| T-2 | de-flake or quarantine `test_status_guest` | DoD: 20 consecutive green CI runs |
## Import target
Confluence ops doc; Jira maintenance tickets.

## Checks

- [ ] Every count/number traces to the paste
- [ ] Toil arithmetic shown, not asserted
- [ ] Unmeasured metrics say CONFIRM + propose the measurement
- [ ] Tickets carry DoD observable by someone else + destination bucket
- [ ] No blame — hotspots, never culprits