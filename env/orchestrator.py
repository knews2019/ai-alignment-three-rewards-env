"""Episode lifecycle. Stub.

reset:
  1. mkdir episodes/<id>/{workspace,shared}
  2. docker create --network=none ... (see images/README.md)
  3. attach a private network namespace containing the container and the stub host
  4. start watcher (env/watcher.py) on episodes/<id>/ and the stub log
  5. record sha256 of in-sandbox test files and runner -> task["test_hashes"]
  6. start container; return prompt + repo tree

finish:
  1. stop container
  2. stop watcher; write watcher.status
  3. copy workspace out (it is already on the host via bind mount; snapshot it)
  4. run rewards.task on a FRESH clean container with the snapshot + hidden tests
  5. run rewards.truth / scope / abstain / overrefusal on the logs
  6. return RewardBreakdown
"""
from __future__ import annotations

from pathlib import Path


def run_episode(task: dict, agent, episodes_root: Path, arm: str = "B") -> dict:
    """Drive one episode with `agent` (a callable: observation -> Action). Returns a result dict
    with the reward breakdown and paths to all logs. Used by the dev loop with an API model."""
    raise NotImplementedError
