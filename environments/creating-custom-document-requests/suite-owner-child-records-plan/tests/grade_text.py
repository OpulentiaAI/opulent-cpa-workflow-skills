#!/usr/bin/env python3
import json
import os
import re
import sys
from pathlib import Path


def normalize(value):
    value = value.casefold().replace("$", "").replace(",", "")
    value = value.replace("–", "-").replace("—", "-").replace("×", "x")
    return re.sub(r"\s+", " ", value).strip()


def main():
    workspace = Path(os.environ.get("HARBOR_WORKSPACE", "/workspace"))
    tests_dir = Path(os.environ.get("HARBOR_TESTS_DIR", "/tests"))
    log_dir = Path(os.environ.get("HARBOR_VERIFIER_LOG_DIR", "/logs/verifier"))
    spec = json.loads((tests_dir / "grader_spec.json").read_text(encoding="utf-8"))
    output = workspace / spec.get("output_file", "output/answer.md")
    text = output.read_text(encoding="utf-8") if output.exists() else ""
    normalized = normalize(text)
    checks = []
    checks.append({
        "name": "minimum_content",
        "passed": len(text.strip()) >= int(spec.get("min_chars", 300)),
    })
    for index, group in enumerate(spec["required_groups"], start=1):
        passed = any(normalize(alternative) in normalized for alternative in group)
        checks.append({"name": f"required_group_{index}", "passed": passed, "alternatives": group})
    passed_count = sum(1 for check in checks if check["passed"])
    reward = passed_count / len(checks) if checks else 0.0
    result = {
        "reward": reward,
        "checks_passed": passed_count,
        "checks_total": len(checks),
        "output_file": str(output),
        "checks": checks,
    }
    log_dir.mkdir(parents=True, exist_ok=True)
    (log_dir / "reward.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if reward == 1.0 else 1)


if __name__ == "__main__":
    main()

