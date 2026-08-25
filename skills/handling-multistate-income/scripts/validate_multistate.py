#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict
from decimal import Decimal


def load(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def money(value):
    return Decimal(value).quantize(Decimal("0.01"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--income", required=True)
    parser.add_argument("--sourcing", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--determinations", required=True)
    args = parser.parse_args()
    income, sourcing, summary, determinations = map(load, [args.income, args.sourcing, args.summary, args.determinations])
    errors = []

    gross = {row["income_id"]: money(row["gross_amount"]) for row in income}
    allocated = defaultdict(Decimal)
    by_state = defaultdict(Decimal)
    for row in sourcing:
        allocated[row["income_id"]] += money(row["allocated_amount"])
        by_state[row["state"]] += money(row["allocated_amount"])
        if not row["source_url"].startswith("https://"):
            errors.append(f"missing source URL for {row['income_id']} {row['state']}")
    if dict(allocated) != gross:
        errors.append("income allocations do not equal gross income by item")

    stated = {row["state"]: money(row["source_income"]) for row in summary}
    if dict(by_state) != stated:
        errors.append("state summary does not match sourcing detail")

    determination_states = {row["state"] for row in determinations}
    if determination_states != set(stated):
        errors.append("filing determinations do not cover each sourced state")
    for row in determinations:
        if row["status"] not in {"required", "not_required", "review"}:
            errors.append(f"invalid status for {row['state']}")
        if not row["reason"].strip() or not row["source_url"].startswith("https://"):
            errors.append(f"unsupported determination for {row['state']}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: {len(gross)} income items allocated across {len(stated)} states")


if __name__ == "__main__":
    main()
