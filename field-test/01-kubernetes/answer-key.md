# Answer key — what the project actually shipped

> **Source:** `kubernetes/enhancements`, KEP-1287 — *Summary / Proposal / Design Details /
> Test Plan / kep.yaml*. Retrieved **2026-11-25**.
> <https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/1287-in-place-update-pod-resources/README.md>
> Held back from `input.md`. Used to score the kit's artifacts in `findings.md`.

## Outcome (kep.yaml)

| Field | Value |
|---|---|
| Status | `implemented` |
| Stage | **stable** |
| Alpha | v1.27 |
| Beta | v1.33 |
| Stable | v1.35 |
| Owning SIG | `sig-node` |
| Participating SIGs | `sig-autoscaling`, `sig-scheduling` |
| Feature gates | `InPlacePodVerticalScaling` (apiserver, scheduler, kubelet); `InPlacePodVerticalScalingAllocatedStatus` (apiserver, kubelet) |

## The design (Summary + Proposal)

- Container resources become a **declaration of desired state**; `Pod.Status.ContainerStatuses[i].Resources`
  reports the **actual** resources; a new `AllocatedResources` reports the allocated requests.
- Changes go through a new **`/resize` pod subresource** (Update + Patch); resources stay
  immutable via a normal pod update.
- A per-container **`resizePolicy`** (`NotRequired` default, `RestartContainer`) says whether
  a restart is needed.
- Two conditions track state: **`PodResizePending`** (`Deferred` / `Infeasible`) and
  **`PodResizeInProgress`**.
- Four resource states flow in order: **Desired → Allocated → Actuated → Actual**.
- **Atomic resizes**: all containers' requests & limits in a request are accepted or none.
- Scheduler and ResourceQuota use `max(desired, actual, allocated)`.
- **CRI**: `UpdateContainerResources` contract updated (no deliberate restarts); new
  `UpdatePodSandboxResources` API for pod-level cgroup changes.
- **Memory-limit decreases**: best-effort check against current usage to avoid OOM kills.
- **Swap** (v1.35): memory resizes of swap-enabled burstable pods are `Infeasible`.

## Affected components

Pod v1 core API · admission controllers (LimitRanger, ResourceQuota, PodResourceAllocation)
· kubelet (status, conditions, CRI calls) · scheduler (uses actual resources) · container
runtimes (containerd, CRI-O).

## Instrumentation

`kubelet_container_requested_resizes_total` · `kubelet_pod_resize_duration_seconds` ·
`kubelet_pod_infeasible_resizes_total` · `kubelet_pod_pending_resizes` ·
`kubelet_pod_in_progress_resizes` · `kubelet_pod_deferred_resize_accepted_total`.

## Test plan (as written)

Unit (Allocation Manager, Kubernetes Runtime Manager, CRI) · Integration · **Pod Resize
E2E** (Guaranteed and Burstable pods, one and multiple containers, memory-limit decrease,
patch errors, scheduler logic, retry of deferred resizes, ResourceQuota, LimitRanger, READ/
REPLACE endpoint coverage) · Backward-compatibility and negative tests. Graduation criteria
for Alpha / Beta / Stable; Upgrade/Downgrade and Version-Skew strategies.

## Implementation history

Alpha v1.27 → Beta v1.33 → Stable v1.35, with the resize-status field (`Pod.Status.Resize`)
deprecated before beta in favor of the two conditions.
