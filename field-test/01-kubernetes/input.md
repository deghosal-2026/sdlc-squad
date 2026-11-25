# Input — the raw problem (what a session would paste)

> **Source:** `kubernetes/enhancements`, KEP-1287 "In-place Update of Pod Resources" —
> *Motivation / Goals / Non-Goals*. Retrieved **2026-11-25**.
> <https://github.com/kubernetes/enhancements/blob/master/keps/sig-node/1287-in-place-update-pod-resources/README.md>
> Quoted/paraphrased; the **design and test plan are held back** in `answer-key.md`.
> Redaction: this is public project text; no personal data. `[CONFIRM: confirm license
> terms before publishing.]`

---

## Problem

Resources allocated to a Pod's container(s) can need to change:

- the load the Pod handles **increased**, and current resources are not sufficient;
- the load **decreased**, and allocated resources are unused;
- resources were simply **set improperly**.

Today, changing resource allocation requires the Pod to be **recreated**, because the
PodSpec's container `Resources` is immutable. Many stateless workloads withstand that
disruption; **stateful or batch workloads** do not — a restart means lower availability or
higher cost.

The Container Runtime Interface (CRI) also has gaps:

1. `UpdateContainerResources` takes a parameter describing resources to update for
   **Linux** containers, and may not work for Windows or future non-Linux runtimes.
2. There is **no CRI mechanism** for the kubelet to query the CPU/memory limits currently
   configured on a container.
3. The expected behavior of a runtime handling `UpdateContainerResources` is not well
   defined or documented.

## Goals

- **Primary:** allow container resource requests & limits to change **without necessarily
  restarting** the container.
- **Secondary:** allow actors (users, VPA, StatefulSet, JobController) to decide how to
  proceed if in-place resize is not possible.
- **Secondary:** allow users to specify **which containers** can be resized without a
  restart.
- **CRI:** make `UpdateContainerResources` work for Windows and other runtimes; provide a
  CRI mechanism to query a container's current CPU/memory configuration; document the
  expected runtime behavior.

## Non-goals

- Controlling the **full lifecycle** of a Pod that failed in-place resize — the initiating
  actor handles that.
- Changing a Pod's **QoS class**.
- Changing resources of **non-restartable InitContainers**.
- **Evicting** lower-priority Pods to facilitate a resize.
- Updating **extended resources**, or any type besides CPU and memory.
- CPU/memory manager policies other than the default `None`.
- Resolving **race conditions with the scheduler**.

---

*This is the input. What follows in `answer-key.md` is what the project actually built.*
