#!/usr/bin/env python3
import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENVIRONMENTS = ROOT / "environments"
SCRATCH = ROOT / ".scratch" / "environment-validation"


def sha256(file_path):
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run(command, env):
    completed = subprocess.run(command, env=env, text=True, capture_output=True)
    return completed.returncode, completed.stdout, completed.stderr


def main():
    manifest = json.loads((ENVIRONMENTS / "manifest.json").read_text(encoding="utf-8"))
    if manifest["environment_count"] != 8:
        raise RuntimeError("expected eight skill environments")
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir(parents=True)
    failures = []
    for item in manifest["environments"]:
        task = ENVIRONMENTS / item["skill"] / item["case_id"]
        required = [
            "task.toml", "instruction.md", "provenance.json", "environment/Dockerfile",
            "tests/test.sh", "tests/grade_text.py", "tests/grader_spec.json",
            "tests/rubric.json", "solution/solve.sh", "solution/reference_answer.md"
        ]
        for relative in required:
            if not (task / relative).is_file():
                failures.append(f"{item['skill']}: missing {relative}")
        hidden_names = {"rubric.json", "grader_spec.json", "reference_answer.md"}
        leaked = [path for path in (task / "environment").rglob("*") if path.name in hidden_names]
        if leaked:
            failures.append(f"{item['skill']}: hidden grader material leaked into environment")
        provenance = json.loads((task / "provenance.json").read_text(encoding="utf-8"))
        for relative, expected in provenance["source_files"].items():
            source = task / relative
            if not source.is_file() or sha256(source) != expected:
                failures.append(f"{item['skill']}: source hash mismatch for {relative}")
            elif source.read_bytes().startswith(b"version https://git-lfs.github.com/spec/v1"):
                failures.append(f"{item['skill']}: unresolved LFS pointer in {relative}")

        scratch_task = SCRATCH / item["skill"]
        workspace = scratch_task / "workspace"
        logs = scratch_task / "logs"
        workspace.mkdir(parents=True)
        logs.mkdir(parents=True)
        env = os.environ.copy()
        env.update({
            "HARBOR_WORKSPACE": str(workspace),
            "HARBOR_TESTS_DIR": str(task / "tests"),
            "HARBOR_SOLUTION_DIR": str(task / "solution"),
            "HARBOR_VERIFIER_LOG_DIR": str(logs),
        })
        code, _, error = run([str(task / "solution" / "solve.sh")], env)
        if code:
            failures.append(f"{item['skill']}: oracle setup failed: {error.strip()}")
            continue
        code, _, error = run([str(task / "tests" / "test.sh")], env)
        reward_file = logs / "reward.json"
        reward = json.loads(reward_file.read_text(encoding="utf-8"))["reward"] if reward_file.exists() else -1
        if code or reward != 1.0:
            failures.append(f"{item['skill']}: oracle did not earn 1.0: {error.strip()}")
        (workspace / "output" / "answer.md").write_text("incomplete\n", encoding="utf-8")
        code, _, _ = run([str(task / "tests" / "test.sh")], env)
        reward = json.loads(reward_file.read_text(encoding="utf-8"))["reward"] if reward_file.exists() else 1
        if code == 0 or reward >= 1.0:
            failures.append(f"{item['skill']}: negative scenario was not rejected")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print("PASS: 8 isolated environments, 8 oracle scenarios, 8 negative scenarios, all source hashes verified")


if __name__ == "__main__":
    main()

