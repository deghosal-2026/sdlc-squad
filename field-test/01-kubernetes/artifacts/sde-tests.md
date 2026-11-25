# Test plan — In-place Update of Pod Resources

> **Field-test artifact** — the kit's `sde/generate-test-ideas-and-cases` output from
> [`../input.md`](../input.md). Compare in [`../findings.md`](../findings.md).

> Scope: the resize API, kubelet actuation, status/conditions, scheduler + quota fit, and the
> memory-decrease guard. Out of scope: autoscaler (VPA) integration and scheduler race
> resolution — both are non-goals of the KEP.

## Test matrix

| ID | Layer | Scenario | Preconditions / input | Expected result | Verification |
|---|---|---|---|---|---|
| TC-1 | Unit | Allocation manager admits a feasible resize | node with free capacity | allocated updated; `PodResizeInProgress` | automated |
| TC-2 | Unit | Allocation manager defers / rejects | no capacity now / exceeds node | `Deferred` / `Infeasible` | automated |
| TC-3 | Unit | Memory-decrease guard | usage > desired limit | resize skipped, `Error` reason | automated |
| TC-4 | Unit | `resizePolicy` validation | `restartPolicy: Never` + `RestartContainer` | rejected | automated |
| TC-5 | Integration | API `/resize` round-trip | running pod | spec = desired; status = actual | automated |
| TC-6 | Integration | QoS class immutability | resize that would change QoS | rejected | automated |
| TC-7 | Contract / API | `UpdateContainerResources` idempotency | call twice with same config | no error, no restart | automated |
| TC-8 | Contract / API | `UpdatePodSandboxResources` | pod-level cgroup change | called after pod cgroup update; best-effort | automated |
| TC-9 | E2E / smoke | Guaranteed pod, one container, CPU up/down | E2E cluster | actual == desired after actuation | automated (E2E) |
| TC-10 | E2E / smoke | Guaranteed pod, multiple containers | E2E cluster | atomic accept across containers | automated (E2E) |
| TC-11 | E2E / smoke | Burstable pod, CPU + memory | E2E cluster | resize applied | automated (E2E) |
| TC-12 | E2E / smoke | Deferred resize retried | capacity freed later | resize eventually applied | automated (E2E) |
| TC-13 | E2E / smoke | ResourceQuota + LimitRanger on resize | namespace with quota/limits | quota/limits enforced on resize | automated (E2E) |
| TC-14 | E2E / smoke | READ + REPLACE endpoint coverage | `/resize` via both verbs | both accepted | automated (E2E) |
| TC-15 | Non-functional / failure injection | Runtime returns restart-required | injected CRI error | resize retried, not silently restarted | automated |
| TC-16 | Non-functional / failure injection | Kubelet restart mid-resize | kill kubelet during actuation | re-admit from checkpoint; resize completes | automated |
| TC-17 | Non-functional / failure injection | Memory decrease + cgroup v2 OOM risk | usage near limit | best-effort skip (TOCTOU accepted) | automated |
| TC-18 | Non-functional / backward-compat | Old client reads `Pod.Status.Resize` | pre-beta client | field absent; conditions present | review |

## Coverage notes

- **Conformance:** GA e2e must meet the conformance requirements and hold a **two-week
  flake-free window** (KEP release checklist).
- **Not covered here:** autoscaler integration (non-goal), swap-enabled resize (forbidden in
  v1.35), non-restartable InitContainers (unsupported) — each by design, with the reason.
- **Negative paths:** TC-2, TC-4, TC-6, TC-15, TC-17 cover the failure side of the happy
  paths (TC-1, TC-5, TC-9).

## Import target
Jira — the QA/test checklist. GitHub — the PR test plan / issue body. Confluence — the test
spec page.

## Handoff
- **From:** `sde/generate-test-ideas-and-cases` — the test plan
- **Carried open:** `[CONFIRM: the E2E environment]`
- **Next:** `tpm/release-readiness-check` — paste the test plan + the launch checklist
