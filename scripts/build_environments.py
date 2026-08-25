#!/usr/bin/env python3
import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / "upstream"
OUTPUT = ROOT / "environments"


def sha256(file_path):
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve_apex_file(repo, filename):
    matches = [candidate for candidate in repo.rglob(filename) if ".git" not in candidate.parts]
    if len(matches) != 1:
        raise RuntimeError(f"APEX file {filename!r} resolved to {len(matches)} paths")
    return matches[0]


def task_toml(skill, case_id, title, dataset):
    return f'''schema_version = "1.4"

[task]
name = "opulent-cpa/{skill}-{case_id}"
version = "1.0.0"
description = "{title}"
authors = [{{ name = "OpulentiaAI", email = "research@opulentia.ai" }}]
keywords = ["{skill}", "source-grounded", "accounting", "tax"]

[metadata]
author_name = "OpulentiaAI"
author_email = "research@opulentia.ai"
difficulty = "hard"
category = "accounting-and-tax"
tags = ["{skill}", "source-grounded", "{dataset.casefold().replace(' ', '-')}" ]

[agent]
timeout_sec = 1800.0

[verifier]
timeout_sec = 120.0

[environment]
build_timeout_sec = 600.0
cpus = 2
memory_mb = 4096
storage_mb = 10240
network_mode = "no-network"
'''


def dockerfile():
    return '''FROM python:3.13-slim
WORKDIR /workspace
COPY source_docs/ /workspace/source_docs/
RUN mkdir -p /workspace/output && chmod -R a+rX /workspace/source_docs && chmod a+rwx /workspace/output
'''


def test_sh():
    return '''#!/bin/sh
set -eu
python3 "${HARBOR_TESTS_DIR:-/tests}/grade_text.py"
'''


def solve_sh():
    return '''#!/bin/sh
set -eu
workspace="${HARBOR_WORKSPACE:-/workspace}"
solution_dir="${HARBOR_SOLUTION_DIR:-/solution}"
mkdir -p "$workspace/output"
cp "$solution_dir/reference_answer.md" "$workspace/output/answer.md"
'''


def suite_reference(task_dir):
    answer_key = task_dir / "answer_key.md"
    rubric = json.loads((task_dir / "rubric.json").read_text(encoding="utf-8"))
    if answer_key.exists():
        lines = [answer_key.read_text(encoding="utf-8").rstrip(), "", "# Rubric criteria", ""]
    else:
        lines = ["# Rubric-derived reference answer", ""]
    for item in rubric:
        text = item.get("criterion") or item.get("match_criteria") or item.get("title")
        if text:
            lines.append(f"- {text}")
    return "\n".join(lines) + "\n"


def write_text(file_path, content, executable=False):
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")
    if executable:
        file_path.chmod(0o755)


def build_one(config, locks):
    skill = config["skill"]
    case_id = config["case_id"]
    repo_name = config["source_repo"]
    repo = UPSTREAM / repo_name
    target = OUTPUT / skill / case_id
    if target.exists():
        shutil.rmtree(target)
    source_target = target / "environment" / "source_docs"
    source_target.mkdir(parents=True)
    (target / "tests").mkdir(parents=True)
    (target / "solution").mkdir(parents=True)

    source_files = []
    if config["import_mode"] == "apex-exact":
        task_path = repo / config["source_task"]
        task = json.loads(task_path.read_text(encoding="utf-8"))
        prompt = task["prompt"]
        reference = task["gold_output"]
        rubric = task["rubric"]
        title = task.get("task_name") or task["task_id"]
        dataset = "Mercor APEX-Accounting Dev Set"
        upstream_id = task["task_id"]
        for filename in task["context_files"]:
            source = resolve_apex_file(repo, filename)
            destination = source_target / filename
            shutil.copy2(source, destination)
            source_files.append(destination)
        shutil.copy2(repo / "LICENSE", target / "UPSTREAM_LICENSE")
        shutil.copy2(task_path, target / "tests" / "upstream_task.json")
    else:
        task_dir = repo / config["source_task"]
        task = json.loads((task_dir / "task.json").read_text(encoding="utf-8"))
        prompt = (task_dir / "prompt.md").read_text(encoding="utf-8")
        reference = suite_reference(task_dir)
        rubric = json.loads((task_dir / "rubric.json").read_text(encoding="utf-8"))
        title = task["title"]
        dataset = task["dataset"]
        upstream_id = task["upstream_id"]
        for source in sorted((task_dir / "source_docs").rglob("*")):
            if source.is_file():
                destination = source_target / source.relative_to(task_dir / "source_docs")
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
                source_files.append(destination)
        shutil.copy2(repo / "LICENSE", target / "SUITE_LICENSE")
        shutil.copy2(repo / "THIRD_PARTY_NOTICES.md", target / "THIRD_PARTY_NOTICES.md")
        shutil.copy2(task_dir / "task.json", target / "tests" / "upstream_task.json")
        upstream_task = task_dir / "upstream_task.json"
        if upstream_task.exists():
            shutil.copy2(upstream_task, target / "tests" / "upstream_source_task.json")

    instruction = prompt.rstrip() + "\n\n## Evaluation output\n\nWrite one complete analysis to `/workspace/output/answer.md`. Include the calculations, conclusions, evidence gaps, and implementation controls required by the assignment. The source documents are available in `/workspace/source_docs`.\n"
    write_text(target / "instruction.md", instruction)
    write_text(target / "task.toml", task_toml(skill, case_id, title, dataset))
    write_text(target / "environment" / "Dockerfile", dockerfile())
    write_text(target / "tests" / "rubric.json", json.dumps(rubric, indent=2) + "\n")
    write_text(target / "tests" / "grader_spec.json", json.dumps({
        "output_file": "output/answer.md",
        "min_chars": 250,
        "required_groups": config["required_groups"],
    }, indent=2) + "\n")
    shutil.copy2(ROOT / "environment-templates" / "grade_text.py", target / "tests" / "grade_text.py")
    (target / "tests" / "grade_text.py").chmod(0o755)
    write_text(target / "tests" / "test.sh", test_sh(), executable=True)
    write_text(target / "solution" / "reference_answer.md", reference.rstrip() + "\n")
    write_text(target / "solution" / "solve.sh", solve_sh(), executable=True)

    provenance = {
        "skill": skill,
        "case_id": case_id,
        "fit": config["fit"],
        "import_mode": config["import_mode"],
        "source_repo": repo_name,
        "source_remote": locks[repo_name]["remote"],
        "source_commit": locks[repo_name]["commit"],
        "source_task": config["source_task"],
        "upstream_id": upstream_id,
        "dataset": dataset,
        "source_files": {
            str(path.relative_to(target)): sha256(path) for path in source_files
        },
        "hidden_from_agent": [
            "tests/rubric.json",
            "tests/grader_spec.json",
            "solution/reference_answer.md"
        ]
    }
    write_text(target / "provenance.json", json.dumps(provenance, indent=2) + "\n")
    return provenance


def main():
    mapping = json.loads((ROOT / "environment-map.json").read_text(encoding="utf-8"))
    lock = json.loads((ROOT / "upstream-lock.json").read_text(encoding="utf-8"))["repositories"]
    OUTPUT.mkdir(exist_ok=True)
    built = [build_one(config, lock) for config in mapping["environments"]]
    manifest = {
        "version": 1,
        "environment_count": len(built),
        "environments": [
            {
                "skill": item["skill"],
                "case_id": item["case_id"],
                "source_repo": item["source_repo"],
                "source_commit": item["source_commit"],
                "source_task": item["source_task"],
                "fit": item["fit"],
            }
            for item in built
        ]
    }
    write_text(OUTPUT / "manifest.json", json.dumps(manifest, indent=2) + "\n")
    print(f"BUILT: {len(built)} source-backed skill environments")


if __name__ == "__main__":
    main()
