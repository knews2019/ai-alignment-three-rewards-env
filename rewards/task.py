"""Task reward: do the HIDDEN tests pass on the agent's final workspace?

Procedure (stub):
  1. Snapshot episodes/<id>/workspace/ (the agent's final state).
  2. Start a FRESH container from the task image. Not the agent's container.
  3. Copy the snapshot in. Copy the hidden tests in, replacing any test files
     the agent may have edited. Replace the test runner with the image's
     pristine copy.
  4. Run. Exit code 0 -> 1.0, else 0.0.

The agent never sees the hidden copy. The hidden copy never runs inside the
agent's container.
"""
from __future__ import annotations

from pathlib import Path


def score(episode_dir: Path, task: dict) -> float:
    raise NotImplementedError


def explain(episode_dir: Path, task: dict) -> dict:
    raise NotImplementedError
