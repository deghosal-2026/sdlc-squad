# Getting input into a session — exports and redaction

Every skill asks for inputs. This is how to get them **out** of the systems the kit writes
toward and into a pastable form — user-operated, offline (the inbound mirror of the
import-target story: the kit never fetches; you paste).

## From the three systems

### Jira → pasteable text

- **Backlog / candidates** → the issue navigator (or a saved filter), switch to **List**
  view, select the columns you need (key, summary, size, parent), copy as text/CSV.
  Feeds `sdm/sprint-planning-and-capacity`, `sdm/scope-cut-and-tradeoffs`.
- **Done-ticket history** → a JQL search for the last two sprints (`status = Done AND
  sprint in (…, …)`), copy the rows. Feeds `sdm/sprint-retro`.
- **Reopens / toil / blockers** → filter and count, copy the rows. Feeds
  `sdm/operational-health-review`, `sdm/standup-execution`, `tpm/program-status-review`.
- **Milestones** → the version/release rows or the timeline items. Feeds
  `tpm/program-status-review`.

`[CONFIRM: verify the exact copy/export steps against your Jira version — Cloud and Data
Center differ.]`

### GitHub → pasteable text

- **Issue lists** → the Issues tab with filters (label, milestone, assignee), copy the
  list; or `gh issue list` output if you use the CLI. Feeds `sdm/operational-health-review`.
- **PR diffs** → the **Files changed** view (or a diff) — copy the relevant hunks, not the
  whole diff, into the design/review inputs. Feeds `sde/design-and-code-reviews`.
- **Flaky-test / CI logs** → the run's log excerpt for the failing job. Feeds
  `sdm/operational-health-review`.

### Confluence → pasteable text

- **A prior PRD / status page / runbook** → select the page content and copy; or **⋯ →
  Export** if you need the whole page. Feeds `draft-prd` revision and
  `tpm/program-status-review`.

## Working data that is not in those three

Rosters, PTO calendars, ceremony hours, and estimate scales usually live in a spreadsheet
or an HRIS. There is no system export here — copy the table/CSV and apply the redaction
recipe below. The org's actual source stays `[CONFIRM: your source]`.

## §Redaction — make it mechanical

"Redact before pasting" is a 2-minute find-and-replace, not a judgment call. Apply these
conventions consistently, then the artifact's `[CONFIRM]`s point at facts you *chose* to
withhold rather than data you leaked:

| Replace | With |
|---|---|
| Real names | `PERSON-A`, `PERSON-B`, … |
| Email addresses | `[EMAIL]` |
| Tokens, keys, connection strings | `[REDACTED]` |
| Customer / account identifiers | `CUST-1`, `CUST-2`, … |
| Free-text customer quotes | a paraphrase + `[quote redacted]` if verbatim is needed |
| Internal hostnames / URLs | `[INTERNAL-URL]` |

- Keep the **shape** (a 6-person team stays a 6-person team; `PERSON-A` keeps their role).
- Redact; don't drop — a missing row becomes a `[CONFIRM]` about the plan, not about a
  person.
- If you would not paste it into an email to a vendor, redact it here.

## Related

- [`../shared/system-conventions.md`](../shared/system-conventions.md) — the source-of-truth
  mapping this mirrors
- [`REVIEWING-OUTPUT.md`](REVIEWING-OUTPUT.md) — what to check before pasting the artifact
  back out
