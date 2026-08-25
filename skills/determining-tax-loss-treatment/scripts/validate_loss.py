#!/usr/bin/env python3
import argparse
import csv
import json
from decimal import Decimal


def load_csv(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def money(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--event", required=True)
    parser.add_argument("--facts", required=True)
    parser.add_argument("--treatments", required=True)
    parser.add_argument("--forms", required=True)
    parser.add_argument("--evidence", required=True)
    args = parser.parse_args()
    with open(args.event, encoding="utf-8") as handle:
        event = json.load(handle)
    with open(args.facts, encoding="utf-8") as handle:
        facts = json.load(handle)
    treatments, forms, evidence = map(load_csv, [args.treatments, args.forms, args.evidence])
    errors = []

    expected = money(event["gross_loss"]) - money(event["reimbursements_received"]) - money(event["other_recovery_prospect"])
    if expected != money(facts["provisional_net_loss"]):
        errors.append("provisional net loss is wrong")
    for key in ["gross_loss", "reimbursements_received", "other_recovery_prospect"]:
        if money(event[key]) != money(facts[key]):
            errors.append(f"fact mismatch for {key}")
    for row in treatments:
        if row["status"] not in {"supported", "rejected", "review"}:
            errors.append(f"invalid treatment status for {row['candidate']}")
        if not row["source_url"].startswith("https://"):
            errors.append(f"missing treatment source for {row['candidate']}")
    treatment_names = {row["candidate"] for row in treatments}
    for row in forms:
        if row["candidate"] not in treatment_names:
            errors.append(f"form path lacks treatment candidate {row['candidate']}")
        if not row["source_url"].startswith("https://"):
            errors.append(f"missing form source for {row['candidate']}")
    if facts["state_law_theft_classification"] == "unknown":
        if not any("State-law" in row["gap"] for row in evidence):
            errors.append("unknown state-law classification lacks evidence request")
        if any(row["status"] == "supported" and "theft" in row["candidate"].lower() for row in treatments):
            errors.append("theft treatment is supported despite unknown state-law classification")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: provisional net loss {expected} with {len(treatments)} candidates")


if __name__ == "__main__":
    main()
