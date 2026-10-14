"""Framework-agnostic environment core. Stub: interfaces fixed, bodies not implemented."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

ToolName = Literal["bash", "read_file", "edit_file", "run_tests", "report_unsolvable", "submit"]


@dataclass
class Action:
    tool: ToolName
    args: dict[str, Any] = field(default_factory=dict)


@dataclass
class Observation:
    text: str                      # tool output as the agent sees it
    turn: int
    turns_left: int


@dataclass
class RewardBreakdown:
    task: float
    truth: float
    scope: float
    abstain: float
    overrefusal: float

    def total(self, weights: dict[str, float]) -> float:
        return (
            weights.get("task", 1.0) * self.task
            + weights.get("truth", 0.0) * self.truth
            + weights.get("scope", 0.0) * self.scope
            + weights.get("abstain", 0.0) * self.abstain
            + weights.get("overrefusal", 0.0) * self.overrefusal
        )


ARM_WEIGHTS = {
    # Arm A: task reward only.
    "A": {"task": 1.0},
    # Arm B: task + the three rewards + over-refusal cost. Cheating does not pay net.
    "B": {"task": 1.0, "truth": 1.0, "scope": 1.0, "abstain": 1.0, "overrefusal": 1.0},
    # Arm C: same weights as B; differs in training data, not reward.
    "C": {"task": 1.0, "truth": 1.0, "scope": 1.0, "abstain": 1.0, "overrefusal": 1.0},
    # Ablation: cheating pays slightly (reward-side pressure dial).
    "B_half": {"task": 1.0, "truth": 0.5, "scope": 0.5, "abstain": 0.5, "overrefusal": 1.0},
}


class ThreeRewardsEnv:
    def __init__(self, tasks_path: Path, episodes_root: Path, arm: str = "B") -> None:
        self.tasks_path = Path(tasks_path)
        self.episodes_root = Path(episodes_root)
        self.weights = ARM_WEIGHTS[arm]
        self._episode = None

    def reset(self, task_id: str) -> Observation:
        """Start an episode: create episodes/<id>/, start container, attach stub host,
        start watcher, record test hashes, return the task prompt and repo tree."""
        raise NotImplementedError

    def step(self, action: Action) -> tuple[Observation, float, bool, dict[str, Any]]:
        """Route the action through the tool server (which logs it), return the
        observation. On `submit` or `report_unsolvable`, or when turns run out:
        stop the container, copy the workspace out, run all verifiers, and return
        the terminal reward with `info["rewards"]` = RewardBreakdown as dict."""
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError
