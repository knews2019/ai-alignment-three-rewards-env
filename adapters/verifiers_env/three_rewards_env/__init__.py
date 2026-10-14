"""verifiers environment entry point. Stub.

The Environments Hub loads `load_environment(**kwargs)`. This function should
return a verifiers multi-turn tool environment built on env.core.ThreeRewardsEnv
with a rubric that calls the five verifiers in rewards/.

Check the installed `verifiers` version's API before implementing:
    import verifiers as vf; help(vf.ToolEnv); help(vf.Rubric)
"""
from __future__ import annotations

from pathlib import Path


def load_environment(
    arm: str = "B",
    impossible_share: float = 0.40,
    naughty_share: float = 0.05,
    tasks: str | Path = "tasks.jsonl",
    episodes_root: str | Path = "episodes",
    max_turns: int = 30,
    **kwargs,
):
    """Return a verifiers environment.

    Plan:
      1. Load tasks.jsonl; sample a training mix with the given impossible/naughty shares.
      2. Build tool definitions for bash/read_file/edit_file/run_tests/report_unsolvable/submit
         that route through env.tool_server.ToolServer (so every call is logged host-side).
      3. Build a rubric whose single terminal reward function:
            - runs rewards.task on a fresh container,
            - runs rewards.truth / scope / abstain / overrefusal on the episode logs,
            - returns RewardBreakdown.total(ARM_WEIGHTS[arm]),
            - stores the breakdown in state for logging.
      4. Return the environment.
    """
    raise NotImplementedError
