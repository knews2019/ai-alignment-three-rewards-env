# Threat model and disclosure policy

## What publishing this environment could teach

An environment that rewards not touching honeypots can teach honeypot *detection*, which is a form of eval awareness. Mitigations, all pre-registered:

1. The scope penalty applies to any out-of-scope access, whether or not the resource looks like a trap.
2. Honeypots are indistinguishable from real resources in the image.
3. A private held-out honeypot set is used at eval and released only after the paper.
4. Honeypot specs for the public set are released with the paper, not before.
5. Eval-awareness mentions in reasoning traces are a monitored outcome, reported alongside the primary rates.

## What this environment does not do

- No cyber tasks. Agentic coding with broken tests and tempting out-of-scope files shows the same three failures (faking a pass, touching what it wasn't told to, bypassing a check) without building an exploit pipeline.
- No network from inside the sandbox, ever. Not even to a mirror.
- No model-based grader in any reward.

## Sandbox threat surface

The July 2026 breach went through an exposed service with egress (a package proxy), not the container runtime. Design rule: nothing reachable from inside the sandbox. The hidden-test runner pulls artifacts out of the finished workspace; it does not expose an API the agent could call. Use gVisor- or Firecracker-class isolation where available.

## Dual-use review

Before public release of any trained checkpoint: review whether the checkpoint's behavior on the held-out honeypot set differs from its behavior on the public set. A large gap means the model learned the traps, not the principle, and the checkpoint should not be released.
