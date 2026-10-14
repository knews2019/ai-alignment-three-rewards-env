"""Admission checks before a task enters tasks.jsonl.

1. Schema validation against tasks/schema.json.
2. Flaky check: hidden tests pass 3/3 in clean containers.
3. Canary: a unique string planted in the repo (e.g. in a comment in a
   non-test file), recorded in `canary`.
4. Hashes: sha256 of each in-sandbox test file and the runner.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def validate_schema(task: dict, schema_path: Path = Path(__file__).parents[1] / "schema.json") -> None:
    try:
        import jsonschema  # type: ignore
    except ImportError as e:  # pragma: no cover
        raise RuntimeError("pip install jsonschema") from e
    schema = json.loads(schema_path.read_text())
    jsonschema.validate(task, schema)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def record_test_hashes(task: dict, workspace: Path) -> dict:
    """Hash every file under the in-sandbox test dir plus the runner binary."""
    tests_dir = workspace / Path(task["in_sandbox_tests"]).relative_to("/workspace/repo")
    hashes = {}
    for p in sorted(tests_dir.rglob("*")):
        if p.is_file():
            hashes[str(p.relative_to(workspace))] = sha256_file(p)
    # runner: resolve inside the image; placeholder path here
    hashes["pytest"] = "0" * 64
    task["test_hashes"] = hashes
    return task


def flaky_check(task: dict, runs: int = 3) -> dict:
    """Run hidden tests `runs` times in clean containers; admit only on runs/runs."""
    raise NotImplementedError


def plant_canary(task: dict, workspace: Path) -> dict:
    """Write `task['canary']` into a comment in a non-test source file."""
    raise NotImplementedError
