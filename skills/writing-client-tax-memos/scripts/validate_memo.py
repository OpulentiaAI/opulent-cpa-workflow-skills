#!/usr/bin/env python3
import argparse
import csv
import json
import re
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--facts", required=True)
    parser.add_argument("--memo", required=True)
    parser.add_argument("--fact-check", required=True)
    args = parser.parse_args()
    with open(args.facts, encoding="utf-8") as handle:
        facts = json.load(handle)
    with open(args.fact_check, newline="", encoding="utf-8") as handle:
        checked = list(csv.DictReader(handle))
    memo = Path(args.memo).read_text(encoding="utf-8")
    errors = []

    expected_ids = {fact["fact_id"] for fact in facts["facts"]}
    checked_ids = {row["fact_id"] for row in checked}
    if expected_ids != checked_ids:
        errors.append("fact check does not cover every approved fact")
    for row in checked:
        if row["status"] != "approved":
            errors.append(f"unapproved claim {row['fact_id']}")
        if not row["source_url"].startswith("https://") or not row["workpaper_ref"].strip():
            errors.append(f"claim lacks source or workpaper reference {row['fact_id']}")
    for fact in facts["facts"]:
        values = re.findall(r"\$?\d[\d,]*(?:\.\d+)?(?: percent)?", fact["value"])
        if not values or any(value not in memo for value in values):
            errors.append(f"memo is missing approved value for {fact['fact_id']}")
    for heading in ["What we found", "How we calculated it", "What remains open", "What to do next", "Sources"]:
        if heading not in memo:
            errors.append(f"memo is missing section {heading}")
    for term in ["benchmark", "grader", "rubric", "confidence score"]:
        if term in memo.lower():
            errors.append(f"memo contains internal term {term}")
    if "Draft for CPA approval" not in memo:
        errors.append("memo lacks CPA approval marker")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: {len(checked)} approved facts represented in client memo")


if __name__ == "__main__":
    main()
