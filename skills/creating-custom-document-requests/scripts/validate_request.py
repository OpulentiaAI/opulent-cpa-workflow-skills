#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path


def load(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", required=True)
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--addendum", required=True)
    parser.add_argument("--traceability", required=True)
    parser.add_argument("--draft", required=True)
    args = parser.parse_args()
    with open(args.profile, encoding="utf-8") as handle:
        profile = json.load(handle)
    baseline, addendum, trace = map(load, [args.baseline, args.addendum, args.traceability])
    errors = []

    if {row["topic"] for row in baseline} != set(profile["baseline_topics"]):
        errors.append("baseline topics do not match client profile")
    if {row["cue_id"] for row in addendum} != {cue["cue_id"] for cue in profile["custom_cues"]}:
        errors.append("custom addendum does not cover every discovery cue")
    baseline_ids = {row["request_id"] for row in baseline}
    addendum_ids = {row["request_id"] for row in addendum}
    if baseline_ids & addendum_ids:
        errors.append("request IDs overlap")
    if {row["topic"] for row in baseline} & {row["topic"] for row in addendum}:
        errors.append("baseline and addendum contain duplicate topics")
    all_ids = baseline_ids | addendum_ids
    if {row["request_id"] for row in trace} != all_ids:
        errors.append("traceability does not cover every request")
    for row in baseline + addendum:
        if not row["period"].strip() or not row["reason"].strip():
            errors.append(f"missing period or reason for {row['request_id']}")
    draft = Path(args.draft).read_text(encoding="utf-8")
    if len(draft.strip()) < 200:
        errors.append("request draft is missing or too short")
    for supplied in profile["already_supplied"]:
        if supplied.lower() in draft.lower() and "already supplied" not in draft.lower():
            errors.append(f"draft appears to re-request supplied item {supplied}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: {len(baseline)} baseline and {len(addendum)} custom requests")


if __name__ == "__main__":
    main()
