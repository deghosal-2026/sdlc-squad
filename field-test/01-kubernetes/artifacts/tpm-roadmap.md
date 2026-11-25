# Program plan — In-place Update of Pod Resources (KEP-1287)

> **Field-test artifact** — the kit's `tpm/program-roadmap-and-deps` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

## Milestones

| Milestone | Target | Definition of done | Source |
|---|---|---|---|
| **Alpha** | v1.27 | Feature gate `InPlacePodVerticalScaling`; API + kubelet path behind the gate | KEP-1287 `kep.yaml` |
| **Beta** | v1.33 | API + conditions stable enough to enable by default; status fields complete | KEP-1287 `kep.yaml` |
| **Stable** | v1.35 | GA; resize API + status promoted; `Pod.Status.Resize` deprecated/removed | KEP-1287 `kep.yaml` |

## Dependency table

| ID | Depends on | Owning team | Needed by | Slack | Notes |
|---|---|---|---|---|---|
| DEP-1 | API `/resize` subresource + validation | sig-api-machinery | Alpha | [CONFIRM] | blocks US-1 |
| DEP-2 | Scheduling fit with pending resizes (`max(desired, actual, allocated)`) | sig-scheduling | Beta | [CONFIRM] | blocks US-6 |
| DEP-3 | Runtime `UpdateContainerResources` (idempotent) + container status query | containerd / CRI-O | Alpha | [CONFIRM] | blocks US-5 |
| DEP-4 | Pod-level cgroup update path (`UpdatePodSandboxResources`) | sig-node + runtimes | Beta | [CONFIRM] | — |
| DEP-5 | Autoscaler integration (VPA) | sig-autoscaling | post-stable | [CONFIRM] | participating SIG; not on the critical path |

## Critical path

**DEP-1 (API) → US-1 → US-5 (kubelet actuation) → Alpha → DEP-2 (scheduling) → Beta → Stable.**

- **Zero-slack links:** [CONFIRM: no per-link slack data was supplied — the KEP gives
  release targets, not per-dependency slack.]
- **Named risk:** the **runtime** dependency (DEP-3) is external to the core repo; a
  containerd/CRI-O slip moves the critical path.

## Program risks (feeds RAID)

| ID | Risk | Early-warning signal | Mitigation | Fallback |
|---|---|---|---|---|
| R-1 | Runtime contract (`UpdateContainerResources` idempotency / no-restart) not met | Runtime returns restart-required errors | Document the contract; runtime owners sign off | Resize marked `RestartContainer`; not in-place |
| R-2 | Scheduler race over-schedules a node during resize | `OutOfCPU`/`OutOfMemory` rejections on resize | Out of scope per KEP; documented | Reschedule the rejected Pod (KEP's accepted behavior) |
| R-3 | Memory-limit decrease triggers OOM kills | OOM kills after a resize | Best-effort usage check before decrease | Operators avoid lowering below usage |

## Import target
Confluence — the program page. Jira — dependency links on the epic.

## Handoff
- **From:** `tpm/program-roadmap-and-deps` — the program plan
- **Carried open:** `[CONFIRM: per-link slack]` · `[CONFIRM: milestone owners]`
- **Next:** `sdm/sprint-planning-and-capacity` — paste the milestones + the squad roster
