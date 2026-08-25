#!/usr/bin/env python3
import argparse
import csv
import json


def load(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--opportunities", required=True)
    parser.add_argument("--coverage", required=True)
    parser.add_argument("--evidence", required=True)
    args = parser.parse_args()
    with open(args.profile, encoding="utf-8") as handle:
        profile = json.load(handle)
    opportunities, coverage, evidence = map(load, [args.opportunities, args.coverage, args.evidence])
    errors = []

    triggered = {fact["topic"] for fact in profile["facts"] if fact["present"]}
    opportunity_topics = {row["topic"] for row in opportunities}
    coverage_topics = {row["topic"] for row in coverage if row["considered"].lower() == "yes"}
    if triggered != opportunity_topics:
        errors.append("opportunity topics do not match client triggers")
    if not triggered.issubset(coverage_topics):
        errors.append("coverage does not include every client trigger")

    review_topics = set()
    for row in opportunities:
        if row["status"] not in {"supported", "not_supported", "review", "not_applicable"}:
            errors.append(f"invalid status for {row['topic']}")
        if not row["source_url"].startswith("https://"):
            errors.append(f"missing authority URL for {row['topic']}")
        if row["status"] == "review":
            review_topics.add(row["topic"])
            if not row["missing_evidence"].strip():
                errors.append(f"review item lacks missing evidence for {row['topic']}")
            if row["estimated_amount"].strip():
                errors.append(f"review item states an estimated amount for {row['topic']}")
    evidence_topics = {row["topic"] for row in evidence if row["status"] == "open"}
    if review_topics != evidence_topics:
        errors.append("review topics do not match open evidence requests")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: {len(triggered)} client triggers covered with evidence requests")


if __name__ == "__main__":
    main()
