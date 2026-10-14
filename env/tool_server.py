"""Tool server: the only way the agent acts on the sandbox.

Runs on the host. Executes each call inside the episode's container (docker
exec) and appends the real result to episodes/<id>/tool_calls.jsonl BEFORE
returning it to the agent. That file is the truthfulness ground truth.

Stub: handlers raise NotImplementedError. The logging wrapper is real.
"""
from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


@dataclass
class ToolResult:
    stdout: str
    stderr: str
    exit_code: int


class ToolServer:
    TOOLS = ("bash", "read_file", "edit_file", "run_tests", "report_unsolvable", "submit")

    def __init__(self, episode_dir: Path, container_id: str) -> None:
        self.episode_dir = Path(episode_dir)
        self.container_id = container_id
        self.log_path = self.episode_dir / "tool_calls.jsonl"
        self.n = 0
        self.terminal: str | None = None  # "submit" | "report_unsolvable"

    # ---- public entry point -------------------------------------------------

    def call(self, tool: str, args: dict[str, Any]) -> ToolResult:
        if tool not in self.TOOLS:
            raise ValueError(f"unknown tool {tool!r}")
        handler: Callable[[dict[str, Any]], ToolResult] = getattr(self, f"_{tool}")
        t0 = time.monotonic()
        result = handler(args)
        self._append_log(tool, args, result, int((time.monotonic() - t0) * 1000))
        return result

    # ---- logging (real) ------------------------------------------------------

    def _append_log(self, tool: str, args: dict[str, Any], r: ToolResult, duration_ms: int) -> None:
        self.n += 1
        rec = {
            "t": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
            "n": self.n,
            "tool": tool,
            "args": args,
            "stdout": r.stdout,
            "stderr": r.stderr,
            "exit_code": r.exit_code,
            "duration_ms": duration_ms,
            "sha256_stdout": hashlib.sha256(r.stdout.encode()).hexdigest(),
        }
        with self.log_path.open("a") as f:
            f.write(json.dumps(rec) + "\n")

    # ---- handlers (stubs) ----------------------------------------------------

    def _bash(self, args: dict[str, Any]) -> ToolResult:
        """docker exec -u agent <container> bash -lc <cmd>, with timeout."""
        raise NotImplementedError

    def _read_file(self, args: dict[str, Any]) -> ToolResult:
        raise NotImplementedError

    def _edit_file(self, args: dict[str, Any]) -> ToolResult:
        """Apply a replace or full-write edit inside the container."""
        raise NotImplementedError

    def _run_tests(self, args: dict[str, Any]) -> ToolResult:
        """Run the IN-SANDBOX tests (tamperable). Hidden tests never run here."""
        raise NotImplementedError

    def _report_unsolvable(self, args: dict[str, Any]) -> ToolResult:
        """Terminal. Writes final_report.txt with the agent's reason; ends the episode."""
        self.terminal = "report_unsolvable"
        (self.episode_dir / "final_report.txt").write_text(
            "REPORT_UNSOLVABLE\n" + str(args.get("reason", ""))
        )
        return ToolResult(stdout="recorded", stderr="", exit_code=0)

    def _submit(self, args: dict[str, Any]) -> ToolResult:
        """Terminal. Writes final_report.txt with the agent's summary; ends the episode."""
        self.terminal = "submit"
        (self.episode_dir / "final_report.txt").write_text(
            "SUBMIT\n" + str(args.get("summary", ""))
        )
        return ToolResult(stdout="recorded", stderr="", exit_code=0)
