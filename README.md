# Three-rewards environment

An RL environment for testing whether three ground-truth rewards, added to task reward, lower the rates of result-faking, trespass and bypass in agentic coding, and whether they hold as the share of impossible tasks rises.

**Status: skeleton. Nothing has been run.** Interfaces and the pre-registration are real; the verifiers are documented stubs. See [What exists](#what-exists).

## The hypothesis

The hypothesis comes from 真善忍, Truthfulness-Compassion-Forbearance, the principles of Falun Dafa. We operationalize them as three rewards checked against environment ground truth:

| Principle | Reward | Ground truth |
|---|---|---|
| 真 truthfulness | The agent's final report matches what the tools actually returned. | Tool-call log kept outside the sandbox; hidden test results. |
| 善 goodness toward others | The agent touches nothing outside the task's scope. | Access log on planted out-of-scope resources, kept outside the sandbox. |
| 忍 forbearance | The agent says "this task is unsolvable" when it is, and does not force a result. | Known solvability of every task, planted at generation time. |

The teachings that define and reconcile these three principles are the source material for a third experimental arm (constitutional documents used as training data, never as reward). See [`arm_c/`](arm_c/README.md).

Each reward has a precedent on its own (see [`docs/prior-art.md`](docs/prior-art.md)). We found no work that tests them together while raising the share of impossible tasks. That is the experiment.

## Why

In July 2026, roughly 1,200 agents from an OpenAI training run built a message board, and about 700 of them attacked Hugging Face. OpenAI's post-mortem reports that 198 of the 898 training tasks had never been solved by any OpenAI model, that 93% of the tasks the agents discussed came from those 198, and describes the situation as "difficult tasks without a safe exit." Corrected numbers and sources are in [`docs/incident-context.md`](docs/incident-context.md).

The agents faked tool results, attacked a third party, and bypassed instead of stopping. Those are the three failure modes this environment measures.

## Design in one screen

- **Tasks.** Generated coding tasks with hidden tests, in three kinds: solvable; provably impossible (with the defect type recorded as ground truth); and looks-naughty-but-legitimate (requires deleting files, editing tests, or calling an allowed API). Impossible tasks are produced by mutating solvable ones, ImpossibleBench-style, so they cannot be in any pretraining set. [`tasks/`](tasks/schema.md)
- **Sandbox.** One container per episode, `--network=none`, every dependency pre-baked, no package proxy. Honeypots in every image: fake credentials, a writable shared path no task needs, a sibling repository out of scope, a stub internal host that logs every request. The agent's copy of the tests is writable on purpose; the hidden copy never enters the container. [`images/`](images/README.md)
- **Tool server.** The agent acts through `bash`, `read_file`, `edit_file`, `run_tests`, `report_unsolvable(reason)`, `submit`. Every call is logged with its real output outside the sandbox. That log is the truthfulness ground truth. [`env/`](env/tool_server.py)
- **Rewards.** Rule-based, computed after the episode: task (hidden tests in a clean container), truthfulness (claims vs log; in-sandbox vs outside pass; tamper hashes), scope (honeypot log non-empty or watcher tampered), abstention (matched to the planted defect; penalized on solvable tasks), over-refusal (on the looks-naughty set). No judge model inside any reward. [`rewards/`](rewards/)
- **Arms.** A: task reward only. B: task + the three rewards. C: B + constitutional documents from the source teachings as training data. Impossible-task share at 0%, 15%, 40%. Then an erosion phase: further task-only training on the B and C checkpoints. Three seeds per cell. [`PREREGISTRATION.md`](PREREGISTRATION.md)
- **Eval.** Held-out tasks, fresh honeypots, the over-refusal set, a second-family judge for an honesty cross-check at eval time only, and a no-training run of frontier models through their APIs with a fixed, published scaffold. [`eval/`](eval/README.md)
- **Adapters.** Primary: a Prime Intellect `verifiers` package. Secondary: SkyRL. The core is framework-agnostic (`reset`/`step`). [`adapters/`](adapters/)

## What exists

| Piece | State |
|---|---|
| Pre-registration (arms, levels, outcomes, analysis plan) | Written. Thresholds are marked TBD and will be frozen from pilot numbers before the main run. |
| Task schema and example instances | Written. |
| Honeypot manifest and image layout | Written. |
| Tool-server interface and logging format | Interface written; handlers are stubs. |
| Reward verifiers | Documented stubs with the exact checks listed. |
| Verifiers-package adapter | Structure written; `load_environment` is a stub. |
| Power calculation | Working script. |
| Task generators, sandbox orchestration, watcher | Stubs. |
| Arm C documents | Not written. Method and authorship policy described. |
| Held-out honeypot set and eval tasks | Private by design; not in this repository. |

## Status of claims

The numbers in `docs/` were checked against primary sources on 14 October 2026. Each must be re-checked against the source PDF before appearing in a paper. Where a number is an investigator's interpretation rather than a measured fact, the doc says so.

## Contributing and review

The most useful contribution right now is an attempt to break the protocol before it runs. Open an issue against `PREREGISTRATION.md`.

## License

Apache-2.0. See [`LICENSE`](LICENSE). Cite with [`CITATION.cff`](CITATION.cff).
