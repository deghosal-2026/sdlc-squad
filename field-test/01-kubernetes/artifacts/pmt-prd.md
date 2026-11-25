# In-place Update of Pod Resources

> **Field-test artifact** — the kit's `pmt/draft-prd` output from [`../input.md`](../input.md).
> Compare against [`../answer-key.md`](../answer-key.md) in [`../findings.md`](../findings.md).

> Status: Draft · Owner: [CONFIRM: name] · Last updated: 2026-11-25 · Reviewers: [CONFIRM: names]

## Problem & context

- A Pod's container resource requests & limits are **immutable**; changing them today
  requires **recreating the Pod** (source: KEP-1287 Motivation).
- Resources need to change for three reasons: load **increased** and resources are
  insufficient; load **decreased** and resources are unused; resources were **set
  improperly** (source: KEP-1287 Motivation).
- Stateless workloads withstand the disruption; **stateful or batch workloads** suffer
  lower availability or higher cost (source: KEP-1287 Motivation).
- CRI gaps: `UpdateContainerResources` is Linux-shaped; there is no way to **query** a
  container's current CPU/memory; runtime behavior is under-documented (source: KEP-1287
  Motivation).

## Target users

- Platform/SRE engineers running **stateful or batch** workloads that cannot tolerate a Pod
  restart just to change resources.
- **Autoscalers and controllers** — Vertical Pod Autoscaler, StatefulSet, JobController —
  that adjust resources on a running workload.

## Goals

- Change container resource requests & limits **without necessarily restarting** the
  container.
- Let actors (users, VPA, StatefulSet, JobController) **decide how to proceed** when an
  in-place resize is not possible.
- Let users declare **which containers** may be resized without a restart.
- Improve the **CRI** so resource updates work beyond Linux and can be queried.

## Non-goals

- Controlling the full lifecycle of a Pod whose resize failed — the initiating actor does.
- Changing a Pod's **QoS class**.
- Resizing **non-restartable InitContainers**.
- **Evicting** lower-priority Pods to make room for a resize.
- **Extended resources**, or any type besides CPU and memory.
- CPU/memory manager policies other than the default `None`.
- Resolving **scheduler race conditions**.

## User journeys

| Step | User action | System behavior | Notes |
|---|---|---|---|
| 1 | User (or VPA) changes a container's resources | API accepts it via the `/resize` subresource | resources stay immutable via normal update |
| 2 | User (or VPA) observes whether the resize was admitted | Kubelet admits, defers, or rejects | `PodResizePending` (Deferred / Infeasible) |
| 3 | User checks the applied resources | Runtime applies the limits; status updates | `PodResizeInProgress`, then `status…resources` |
| 4 | User reads the applied resources | `status.containerStatuses[i].resources` shows actual | desired ≠ actual until actuated |

## Requirements

### Functional

- **REQ-1** Resource requests & limits are mutable via a **`/resize` pod subresource**
  (Update/Patch); immutable via a normal pod update.
- **REQ-2** `Pod.Status.ContainerStatuses[i].Resources` reports the **actual** resources;
  `.AllocatedResources` reports the allocated requests.
- **REQ-3** A per-container **`resizePolicy`** (`NotRequired` | `RestartContainer`) says
  whether a restart is required to apply a resize.
- **REQ-4** Two conditions track progress: **`PodResizePending`** (Deferred/Infeasible) and
  **`PodResizeInProgress`**.
- **REQ-5** Validation: resources valid under create validation; computed **QoS class
  cannot change**; a running Pod without `status…resources` cannot be resized.
- **REQ-6** A single resize request is **atomic** across all containers, requests, and
  limits.

### Non-functional

- **REQ-7** `UpdateContainerResources` must be **idempotent**.
- **REQ-8** **Memory-limit decreases** make a **best-effort** check against current usage
  to avoid OOM kills.
- **REQ-9** Scheduler and **ResourceQuota** account for pending resizes via
  `max(desired, actual, allocated)`.
- **REQ-10** Metrics expose requested / infeasible / pending / in-progress resizes.

## Edge cases

| EC | Trigger | Expected behavior |
|---|---|---|
| EC-1 | Requested resources exceed node capacity | `PodResizePending` = **Infeasible** |
| EC-2 | Feasible, but no free capacity right now | `PodResizePending` = **Deferred**, re-evaluated |
| EC-3 | Memory limit lowered below current usage | best-effort skip + `Error` message; no guarantee |
| EC-4 | Static pod | Infeasible |
| EC-5 | Swap enabled (burstable) | memory resize Infeasible (v1.35) |
| EC-6 | Resize a terminated container | permitted ("fail open") |
| EC-7 | Kubelet restarts mid-resize | re-admit from checkpoint; resize retried |
| EC-8 | Resize would change QoS class | rejected by validation |
| EC-9 | Resize a non-restartable InitContainer | not supported |

## Open questions

| # | Question | Owner | Needed by |
|---|---|---|---|
| Q-1 | Per-release rollout / feature-gate plan | [CONFIRM: sig-node] | [CONFIRM] |
| Q-2 | Memory-manager static-policy support timeline | [CONFIRM: sig-node] | [CONFIRM] |

## Rollout & metrics

- **Staged:** alpha **v1.27** → beta **v1.33** → stable **v1.35** (source: KEP-1287
  `kep.yaml`).
- **Feature gates:** `InPlacePodVerticalScaling` (apiserver, scheduler, kubelet);
  `InPlacePodVerticalScalingAllocatedStatus` (apiserver, kubelet).
- **Metric:** resize success / deferral rate —
  `kubelet_pod_resize_duration_seconds`, `kubelet_pod_infeasible_resizes_total`
  (source: KEP-1287 Instrumentation).

## Import target
Confluence — the PRD/RFC page for this initiative.

## Handoff
- **From:** `pmt/draft-prd` — the in-place-resize PRD
- **Carried open:** `[CONFIRM: the product success metric]` · `[CONFIRM: the rollout owner]`
- **Next:** `pmt/slice-mvp-and-stories` — paste this PRD + the estimate scale
