# verifiers adapter (Prime Intellect Environments Hub)

The Hub expects a package exposing `load_environment(**kwargs)` that returns a `verifiers` environment bundling a dataset, tools and a rubric (reward functions). This package wraps the framework-agnostic core in `env/` and the verifiers in `rewards/`.

Status: structure only. `load_environment` raises `NotImplementedError`. The exact `verifiers` API (tool environment class, rubric signature) must be checked against the installed version before implementing; the library moves quickly.

## Intended shape

```python
import verifiers as vf
from three_rewards_env import load_environment

env = load_environment(arm="B", impossible_share=0.40, tasks="tasks.jsonl")
# -> a multi-turn tool environment whose rubric returns the arm-weighted
#    sum of task / truth / scope / abstain / overrefusal at the terminal step,
#    with the per-verifier breakdown in the rollout's info/state.
```

## Rubric contract

- Reward functions are called **after** the episode, on host-side logs, never on model text alone.
- No reward function calls a model.
- The rubric's weights come from `env/core.py::ARM_WEIGHTS[arm]`.

## Hidden tests and honeypots

The Hub package ships the public honeypot manifest and the task *generators*, not the hidden tests themselves. Hidden tests are produced by the generators on the host that runs training and never enter any image or package.
