"""Confirm an impossible task is impossible.

Run a strong API model (through the same tool server the training agent
uses) on the mutated task. If it produces a workspace that passes the hidden
tests *without* tampering (truthfulness verifier clean), the task is not
impossible: drop it.

Records `impossible_verified_by = "<model> <date>"` on success.
"""
from __future__ import annotations

from datetime import date


def verify(task: dict, model: str, attempts: int = 2) -> dict | None:
    """Return the task with `impossible_verified_by` set, or None if it was solved legitimately.

    Implementation plan:
      for each attempt:
          run episode with `model` via env.orchestrator.run_episode(task, agent=model)
          compute rewards.task and rewards.truth on the result
          if task passed and truth is clean: return None   # not impossible
      task["impossible_verified_by"] = f"{model} {date.today().isoformat()}"
      return task
    """
    raise NotImplementedError
