"""Environment core: framework-agnostic episode interface.

    env = ThreeRewardsEnv(tasks_path, episodes_root)
    obs = env.reset(task_id)
    while not done:
        obs, reward, done, info = env.step(action)

`reward` is 0.0 until the terminal step; `info["rewards"]` carries the
per-verifier breakdown at the terminal step. Adapters in adapters/ wrap this.
"""
from .core import ThreeRewardsEnv, Action, Observation  # noqa: F401
