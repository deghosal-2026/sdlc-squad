# Design: In-place Update of Pod Resources

> **Field-test artifact** — the kit's `sde/technical-design-and-breakdown` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Status: Draft · Author: [CONFIRM: name] · Last updated: 2026-11-25

## Affected modules / services

| Service / repo / path | Change | Risk |
|---|---|---|
| `kube-apiserver` — pod API + validation | New `/resize` subresource; validate resources, enforce **immutable QoS class** | High — API surface |
| `kube-apiserver` — admission (LimitRanger, ResourceQuota, PodResourceAllocation) | Support pod **updates**; order `PodResourceAllocation` before `ResourceQuota` | Medium |
| `kubelet` — status | Set `ContainerStatuses[i].Resources` (actual) + `.AllocatedResources`; manage the two conditions | High |
| `kubelet` — CRI | Idempotent `UpdateContainerResources`; new `UpdatePodSandboxResources` for pod-level cgroups | High |
| `kube-scheduler` | Fit using `max(desired, actual, allocated)` | Medium |
| Container runtimes (`containerd`, `CRI-O`) | Idempotent resize; report current resources; no deliberate restart | High — **external** |
| `kubernetes/enhancements` | KEP status + graduation | Low |

*Every claim above cites the KEP (`keps/sig-node/1287-…`); no source code was read in this
session — deeper file/symbol claims are `[CONFIRM: read the implementation PRs]`.*

## Data model & API / contract changes

- `Pod.Spec.Containers[i].Resources` → a **declaration of desired** resources.
- `Pod.Status.ContainerStatuses[i].Resources` *(new)* → the **actual** resources.
- `Pod.Status.ContainerStatuses[i].AllocatedResources` *(new)* → the **allocated** requests.
- `Pod.Spec.Containers[i].ResizePolicy[]` *(new)* → `NotRequired` | `RestartContainer`, per resource.
- New subresource **`/resize`** (Update, Patch); resources stay immutable via normal update.
- New conditions **`PodResizePending`** (`Deferred` / `Infeasible`) and **`PodResizeInProgress`**.
- **CRI:** `UpdateContainerResources` contract updated (idempotent, no deliberate restart);
  new `UpdatePodSandboxResources`.
- **Backwards-compatibility:** `Pod.Status.Resize` is deprecated and does **not** graduate
  to beta; clients must read the two conditions.

## Flow

1. **Desired** — the user/controller writes new resources via `/resize`; the API validates
   (create rules, QoS immutability, running-pod status present).
2. **Allocated** — the kubelet admits if the node can fit it (sum of others + new desired);
   checkpoints requests + limits; else sets `PodResizePending` (`Deferred`/`Infeasible`).
3. **Actuated** — the kubelet calls `UpdateContainerResources` (idempotent); on success
   records actuated resources; `PodResizeInProgress` present until allocated == actuated.
4. **Actual** — the runtime reports the applied config; the kubelet writes
   `status.containerStatuses[i].resources`; the condition clears.

Decreases before increases; pod-level cgroup limit updated first on a net increase, last on a
net decrease.

## Failure modes & edge cases

| ID | Trigger | Behavior | Detection |
|---|---|---|---|
| FM-1 | Resize exceeds node capacity | `PodResizePending` = **Infeasible** | condition + pod event |
| FM-2 | Feasible, no free capacity now | **Deferred**, re-evaluated | condition |
| FM-3 | Memory limit lowered below current usage | skip that container; `Error` reason | `PodResizeInProgress` reason/message |
| FM-4 | `UpdateContainerResources` fails | retry on next pod sync | pod event + condition |
| FM-5 | Kubelet restarts mid-resize | re-admit from checkpoint; resize retried; `LastTransitionTime` preserved | restart event + `PodResizeInProgress` re-appears |
| FM-6 | Swap enabled (burstable) | memory resize **Infeasible** (v1.35) | condition |
| FM-7 | Resize changes QoS class | rejected by validation | API error |
| FM-8 | Non-restartable InitContainer | not supported | API error |

## Observability

- **Metrics:** `kubelet_container_requested_resizes_total`, `kubelet_pod_resize_duration_seconds`,
  `kubelet_pod_infeasible_resizes_total`, `kubelet_pod_pending_resizes`,
  `kubelet_pod_in_progress_resizes`, `kubelet_pod_deferred_resize_accepted_total`.
- **Conditions + events:** `PodResizePending` / `PodResizeInProgress`; pod events at accept /
  reject / key steps.

## Rollback

1. Disable the feature gates `InPlacePodVerticalScaling` /
   `InPlacePodVerticalScalingAllocatedStatus`.
2. Revert the API + kubelet PRs; `status…resources` reverts to the allocated values.
3. Deprecated `Pod.Status.Resize` is not re-introduced — clients already on the conditions.
   *(Named steps; "revert the PR" is a step, not a plan.)*

## Sub-tasks (Jira-ready)

| ID | Task | Scope | DoD | Depends on |
|---|---|---|---|---|
| T-1 | `/resize` subresource + validation | apiserver pod API | a resize is accepted; a normal update is rejected | — |
| T-2 | Status fields (actual + allocated) | kubelet status | `status…resources` + `.allocatedResources` populated | T-1 |
| T-3 | `resizePolicy` per container | API + kubelet | restart policy honored; `Never` + non-`NotRequired` rejected | T-1 |
| T-4 | Resize conditions | kubelet | `PodResizePending`/`InProgress` set and cleared | T-2 |
| T-5 | Kubelet actuation (idempotent CRI) | kubelet CRI | resize applied; retried on failure | T-2 |
| T-6 | Scheduler + quota `max(desired, actual, allocated)` | scheduler, admission | fit + quota use the max | T-2 |
| T-7 | Memory-decrease best-effort guard | kubelet | skip + `Error` when usage > limit | T-5 |
| T-8 | Metrics | kubelet | the six metrics exposed | T-5 |

## Import target
Confluence — the RFC / tech design page. GitHub — the tracking issue. Jira — the T-table as
sub-tasks.

## Handoff
- **From:** `sde/technical-design-and-breakdown` — the design + sub-tasks
- **Carried open:** `[CONFIRM: file paths/symbols]` · `[CONFIRM: the migration owner]`
- **Next:** `sde/generate-test-ideas-and-cases` — paste this design + the test surface
