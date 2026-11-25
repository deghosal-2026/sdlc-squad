# Epic: In-place Update of Pod Resources

> **Field-test artifact** — the kit's `pmt/slice-mvp-and-stories` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

| Field | Value |
|---|---|
| Epic key | [CONFIRM: assigned by Jira on import] |
| Type | Epic |
| Priority | [CONFIRM: per the org's scale] |
| Business value | Resize a running Pod's CPU/memory without recreating it — protecting stateful and batch availability and cost |
| Success metric | Resize deferral rate + time-to-actuate (`kubelet_pod_resize_duration_seconds`, `kubelet_pod_infeasible_resizes_total`) |

## Why

Container resources are immutable today, so a resize forces a Pod recreation — tolerable for
stateless workloads, costly for stateful and batch ones. Autoscalers and controllers need to
adjust resources on a running workload. The slice below is the **alpha** cut: the API surface
and the kubelet path that make an in-place resize possible, before autoscaler integration.

## Stories

| ID | Summary | Type | Priority | Size | Dependencies |
|---|---|---|---|---|---|
| US-1 | Mutate a Pod's resources via a `/resize` subresource | Story | [CONFIRM] | [CONFIRM] | DEP-4 |
| US-2 | Report actual + allocated resources in Pod status | Story | [CONFIRM] | [CONFIRM] | — |
| US-3 | Per-container `resizePolicy` (NotRequired / RestartContainer) | Story | [CONFIRM] | [CONFIRM] | — |
| US-4 | Track resize with `PodResizePending` / `PodResizeInProgress` conditions | Story | [CONFIRM] | [CONFIRM] | US-2 |
| US-5 | Kubelet admits and actuates a resize (idempotent CRI call) | Story | [CONFIRM] | [CONFIRM] | US-1, DEP-3 |
| US-6 | Scheduler and ResourceQuota account for pending resizes | Story | [CONFIRM] | [CONFIRM] | US-2, DEP-2 |
| US-7 | Best-effort memory-limit-decrease guard | Story | [CONFIRM] | [CONFIRM] | US-5 |
| US-8 | Emit resize metrics | Story | [CONFIRM] | [CONFIRM] | US-5 |

### US-1 — Mutate a Pod's resources via a `/resize` subresource

**Description:** As an operator (or autoscaler), I can change a running Pod's container
resource requests & limits without recreating the Pod, through a dedicated subresource.
**Acceptance criteria:**
- **AC-1** Given a running Pod, when I send an Update/Patch to `/resize` changing a
  container's CPU or memory, then the change is accepted and the spec reflects the desired
  state.
- **AC-2** Given a normal (non-`/resize`) pod update, when it changes resources, then the
  request is rejected (resources remain immutable).
**Dependencies:** DEP-4 — API machinery.

### US-2 — Report actual + allocated resources in Pod status

**Description:** As an operator, I can see the resources a Pod is actually running with,
distinct from what was requested.
**Acceptance criteria:**
- **AC-1** Given a running container, when I read the Pod status, then
  `status.containerStatuses[i].resources` shows the **actual** resources and
  `.allocatedResources` shows the allocated requests.
- **AC-2** Given a non-running container, then `status…resources` equals the allocated
  resources.
**Dependencies:** —

### US-3 — Per-container `resizePolicy`

**Description:** As a user, I can declare which containers may be resized without a restart.
**Acceptance criteria:**
- **AC-1** Given `resizePolicy[cpu]=NotRequired`, when the CPU request is resized, then the
  kubelet attempts the resize without restarting the container.
- **AC-2** Given `resizePolicy=RestartContainer`, when the resource is resized, then a
  restart is required to apply it.
- **AC-3** Given a Pod with `restartPolicy: Never`, when `resizePolicy` is not `NotRequired`,
  then validation rejects it.
**Dependencies:** —

### US-4 — Resize conditions

**Description:** As an operator, I can tell whether a resize is pending or in progress, and
why.
**Acceptance criteria:**
- **AC-1** Given a resize that cannot fit the node, when it is evaluated, then
  `PodResizePending` is set with reason **Infeasible**.
- **AC-2** Given a feasible resize with no capacity right now, then `PodResizePending` is
  **Deferred** and re-evaluated.
- **AC-3** Given a resize being actuated, then `PodResizeInProgress` is present until
  allocated == actuated.
**Dependencies:** US-2

### US-5 — Kubelet admits and actuates a resize

**Description:** As an operator, a resize I request is applied to the running container.
**Acceptance criteria:**
- **AC-1** Given an admitted resize, when the kubelet actuates it, then it calls the runtime's
  `UpdateContainerResources` and updates status on success.
- **AC-2** Given the same resize called twice, then the runtime call is idempotent.
- **AC-3** Given a failed actuation, then the resize is retried on the next pod sync.
**Dependencies:** US-1, DEP-3

### US-6 — Scheduler & quota account for pending resizes

**Description:** As a cluster operator, pending resizes are not over-scheduled.
**Acceptance criteria:**
- **AC-1** Given a pending resize, when the scheduler evaluates fit, then it uses
  `max(desired, actual, allocated)`.
- **AC-2** Given a pending resize, when ResourceQuota is evaluated, then it uses the same max.
**Dependencies:** US-2, DEP-2

### US-7 — Memory-limit-decrease guard

**Description:** As an operator, lowering a memory limit does not immediately OOM-kill a
container.
**Acceptance criteria:**
- **AC-1** Given a memory-limit decrease, when current usage exceeds the desired limit, then
  the resize is skipped with an `Error` reason and a message.
**Dependencies:** US-5

### US-8 — Resize metrics

**Description:** As an operator, I can observe resize behavior.
**Acceptance criteria:**
- **AC-1** Given resize attempts, then `kubelet_container_requested_resizes_total` and the
  pending/in-progress gauges are exposed.
**Dependencies:** US-5

## Dependencies

| ID | On what | From | Blocks | Status |
|---|---|---|---|---|
| DEP-1 | Autoscaler integration (VPA) | sig-autoscaling | future work | [CONFIRM] |
| DEP-2 | Scheduling fit with pending resizes | sig-scheduling | US-6 | [CONFIRM] |
| DEP-3 | Runtime `UpdateContainerResources` + status query | container runtimes (containerd, CRI-O) | US-5 | [CONFIRM] |
| DEP-4 | API subresource + validation | sig-api-machinery | US-1 | [CONFIRM] |

## Import target
Jira — epic + stories via bulk import / CSV; paste each story's block into its ticket
description.

## Handoff
- **From:** `pmt/slice-mvp-and-stories` — the epic + stories
- **Carried open:** `[CONFIRM: sizes]` · `[CONFIRM: which non-goals are fixed]`
- **Next:** `tpm/program-roadmap-and-deps` — paste the epic + the teams' commitments
