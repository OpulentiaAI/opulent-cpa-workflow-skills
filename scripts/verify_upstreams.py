#!/usr/bin/env python3
import json
import os
import subprocess
import hashlib
from json import JSONDecoder
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(command, cwd, env=None):
    completed = subprocess.run(command, cwd=cwd, env=env, text=True, capture_output=True)
    if completed.returncode:
        raise RuntimeError(completed.stderr or completed.stdout)
    return completed.stdout.strip()


def json_stream(text):
    decoder = JSONDecoder()
    index = 0
    values = []
    while index < len(text):
        while index < len(text) and text[index].isspace():
            index += 1
        if index >= len(text):
            break
        value, index = decoder.raw_decode(text, index)
        values.append(value)
    return values


def resolve_apex(repo, filename):
    matches = [candidate for candidate in repo.rglob(filename) if ".git" not in candidate.parts]
    if len(matches) != 1:
        raise RuntimeError(f"APEX context file {filename!r} resolved to {len(matches)} paths")
    return matches[0]


def sha256(file_path):
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    locks = json.loads((ROOT / "upstream-lock.json").read_text(encoding="utf-8"))["repositories"]
    lfs_dir = ROOT / ".tools" / "git-lfs-3.7.1" / "extracted" / "git-lfs-3.7.1"
    git_env = os.environ.copy()
    git_env["PATH"] = f"{lfs_dir}:{git_env.get('PATH', '')}"
    for name, expected in locks.items():
        repo = ROOT / "upstream" / name
        git_marker = repo / ".git"
        if not (git_marker.is_dir() or git_marker.is_file()):
            raise RuntimeError(f"missing Git checkout: {name}")
        if run(["git", "rev-parse", "HEAD"], repo, git_env) != expected["commit"]:
            raise RuntimeError(f"commit mismatch: {name}")
        if run(["git", "remote", "get-url", "origin"], repo, git_env) != expected["remote"]:
            raise RuntimeError(f"remote mismatch: {name}")
        if run(["git", "status", "--porcelain=v1"], repo, git_env):
            raise RuntimeError(f"dirty upstream checkout: {name}")

    apex = ROOT / "upstream" / "apex-accounting"
    task_files = sorted((apex / "tasks").glob("*.json"))
    if len(task_files) != 10:
        raise RuntimeError(f"expected 10 APEX tasks, found {len(task_files)}")
    dev_values = json_stream((apex / "data" / "dev.jsonl").read_text(encoding="utf-8"))
    if len(dev_values) != 10:
        raise RuntimeError(f"expected 10 APEX dev rows, found {len(dev_values)}")
    lfs_files = [line for line in run(["git", "lfs", "ls-files"], apex, git_env).splitlines() if line]
    if len(lfs_files) != 14:
        raise RuntimeError(f"expected 14 APEX Git LFS files, found {len(lfs_files)}")
    for source in apex.rglob("*"):
        if source.is_file() and ".git" not in source.parts:
            with source.open("rb") as handle:
                if handle.read(200).startswith(b"version https://git-lfs.github.com/spec/v1"):
                    raise RuntimeError(f"unresolved Git LFS pointer: {source}")
    apex_tasks = {}
    for task_file in task_files:
        task = json.loads(task_file.read_text(encoding="utf-8"))
        apex_tasks[task["task_id"]] = task
        if not task.get("rubric") or not task.get("gold_output"):
            raise RuntimeError(f"missing APEX ground truth: {task_file.name}")
        for filename in task["context_files"]:
            source = resolve_apex(apex, filename)
            if source.read_bytes().startswith(b"version https://git-lfs.github.com/spec/v1"):
                raise RuntimeError(f"unresolved Git LFS pointer: {source}")

    suite = ROOT / "upstream" / "knowledge-work-demo-suite"
    output = run(["python3", "scripts/validate_suite.py"], suite)
    expected = "PASS: 58 tasks, 10 datasets, 688 unique source files, all hashes verified"
    if expected not in output:
        raise RuntimeError(f"unexpected suite validator result: {output}")
    apex_packets = sorted((suite / "tasks").glob("*/apex_accounting.json"))
    if len(apex_packets) != 5:
        raise RuntimeError(f"expected five APEX packets in suite, found {len(apex_packets)}")
    for packet in apex_packets:
        task_dir = packet.parent
        suite_task = json.loads((task_dir / "upstream_task.json").read_text(encoding="utf-8"))
        source_task = apex_tasks.get(suite_task["task_id"])
        if suite_task != source_task:
            raise RuntimeError(f"suite APEX task metadata drift: {task_dir.name}")
        for filename in source_task["context_files"]:
            original = resolve_apex(apex, filename)
            mirrored = task_dir / "source_docs" / filename
            if not mirrored.is_file() or sha256(original) != sha256(mirrored):
                raise RuntimeError(f"suite APEX source drift: {task_dir.name}/{filename}")
    print("PASS: 6 pinned clean checkouts, 10 complete APEX tasks, 5 byte-exact suite mirrors, and 58 verified suite tasks")


if __name__ == "__main__":
    main()
