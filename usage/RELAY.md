# The relay — moving an artifact from one role to the next

One role per session (`../WHAT-THIS-IS.md`). The relay is how work crosses roles:
PMT → TPM → SDM → SDE, each handing its artifact to the next. This is the user-facing
recipe — **what to paste into the next session**, derived from the role files'
`Consumes` / `Produces` / `Depends on` tables.

## How a hand-off works

1. Finish the current role's artifact (one Markdown contract, with its `import target`).
2. Resolve the `[CONFIRM]`s the next role needs — or carry them **explicitly** as open
   (never silently drop them).
3. Start a **fresh session**. Paste the four files for the next role (or its bundle) +
   the artifact.
4. Paste the carried facts the next role's `Depends on` table lists.

## The transitions

| From → To | What to paste into the next session | Carry these glossary facts | Resolve first (or carry as open) |
|---|---|---|---|
| **PMT → TPM** | The accepted PRD | Jira project key, Confluence space, milestone cadence | Non-goals, the success metric, any fixed date |
| **PMT → SDE** | The PRD requirements (`REQ-n`) | estimate scale, services the design touches | Which requirements are in scope this phase |
| **PMT → SDM** | The accepted PRD → stories (`US-n`) | roster, sprint length, PTO, on-call, ceremony hours | Story sizes (a `[CONFIRM: SDE/SDM estimate]` blocks the plan) |
| **TPM → SDM** | The roadmap + launch checklist | team roster, sprint length, on-call/support load | Milestone dates with an owning team; the launch sprint |
| **TPM → SDE** | Dependencies + the design-relevant milestones | services, estimate scale | Which deps land before the build |
| **SDM → SDE** | The committed scope (the sprint commitment) | services, estimate scale | Which committed item goes to design first |
| **SDE → SDM** | Sub-tasks (`T-n`) with sizes + DoD | roster, sprint length | Task sizes (feeds the commitment) |
| **SDE → TPM** | The design's rollback steps + deploy plan | SLAs/SLOs, escalation path | Rollback owner; the deploy/release split |
| **SDM → TPM** | The capacity/commitment + milestone-fit rows | — | Over-allocation flags; milestone feasibility |
| **SDM → PMT** | Scope-cut options with costs | — | Which option the PMT wants (the PMT decides) |
| **PMT ↔ SDM** | The value order ↔ the cut options | — | The scope-cut loop: value order in, options out, decision back |

- The set above is derived from the role files (`roles/*.md`, `Consumes`/`Produces`);
  if a role file changes, change this table in the same commit.
- A downstream role that needs something the upstream artifact didn't capture: that is the
  cross-artifact-continuity gap, tracked as future work — for now, carry it explicitly.

## The handoff block

To make a hand-off mechanical, end each artifact with a short block the next session can
use. It is three fields, each derived from the role files' contracts:

```
## Handoff
- **From:** <role>/<skill> — <artifact name>
- **Carried open:** [CONFIRM: …] · [CONFIRM: …]   (blocking ones first)
- **Next:** <role>/<skill> — paste this artifact + <the glossary facts its Depends-on lists>
```

- **From** names the artifact and where it came from.
- **Carried open** lists the `[CONFIRM]`s the next role needs — resolved, or explicitly open;
  never silently dropped (step 2 above).
- **Next** names the recommended next role & skill and what to paste (the row above).

The block is a user's habit today; a schema-level carry field is future work (0.2.0), so
for now you append the block by hand. See it in a full chain in
[`FEATURE-RELAY.md`](FEATURE-RELAY.md).

## Cross-team features (a mode, not a different relay)

The relay above assumes **one squad**. A feature that spans multiple teams or SIGs — a
cross-cutting initiative — uses the same relay in a **cross-team mode**:

- The **TPM** owns the cross-team plan: the program roadmap
  (`../shared/output-schemas/program-roadmap.md`) — **milestones** and the **`DEP-n`** IDs.
- The **PMT PRD references** the roadmap's milestones; it does not assert release dates.
- The **SDM sprint plan is scoped to one squad**, or marked **`N/A — cross-team feature`** when no
  single squad owns the work. **Never fabricate a roster** to fill a capacity table.
- Downstream artifacts (`jira-epic-and-stories`, `technical-design-doc`) **reference** the
  roadmap's `DEP-n`; they do not mint their own.

So a cross-team feature exercises the same four roles — the TPM hop simply carries more, and the
SDM hop says `N/A` rather than inventing a team.

## Related

- [`../roles/`](../roles/) — the handoff contracts
- [`START-HERE.md`](../docs/START-HERE.md) — scenario chains built from these transitions
- [`../usage/USER-GUIDE.md`](../usage/USER-GUIDE.md) — "While you work"
