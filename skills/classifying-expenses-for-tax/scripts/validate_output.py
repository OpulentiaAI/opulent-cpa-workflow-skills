#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict
from decimal import Decimal


def rows(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def money(value):
    return Decimal(value).quantize(Decimal("0.01"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--classified", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--exceptions", required=True)
    args = parser.parse_args()

    source = rows(args.input)
    classified = rows(args.classified)
    summary = rows(args.summary)
    exceptions = rows(args.exceptions)
    errors = []

    source_ids = [row["txn_id"] for row in source]
    classified_ids = [row["txn_id"] for row in classified]
    if len(source_ids) != len(set(source_ids)):
        errors.append("source txn_id values are not unique")
    if sorted(source_ids) != sorted(classified_ids):
        errors.append("classified txn_id values do not match source exactly")

    source_by_id = {row["txn_id"]: money(row["amount"]) for row in source}
    for row in classified:
        if row["status"] not in {"accepted", "exception"}:
            errors.append(f"invalid status for {row['txn_id']}")
        if row["txn_id"] in source_by_id and money(row["amount"]) != source_by_id[row["txn_id"]]:
            errors.append(f"amount changed for {row['txn_id']}")
        if row["status"] == "accepted" and not row["source_url"].startswith("https://"):
            errors.append(f"accepted row lacks source URL for {row['txn_id']}")

    exception_ids = {row["txn_id"] for row in classified if row["status"] == "exception"}
    listed_exception_ids = {row["txn_id"] for row in exceptions}
    if exception_ids != listed_exception_ids:
        errors.append("exceptions file does not match classified exception rows")
    for row in exceptions:
        if not row["question"].strip().endswith("?"):
            errors.append(f"exception question is not direct for {row['txn_id']}")

    detail = defaultdict(lambda: [0, Decimal("0.00")])
    for row in classified:
        if row["status"] == "accepted":
            key = (row["category"], row["form"], row["line_label"])
            detail[key][0] += 1
            detail[key][1] += money(row["amount"])
    stated = {}
    for row in summary:
        key = (row["category"], row["form"], row["line_label"])
        stated[key] = [int(row["transaction_count"]), money(row["total_amount"])]
    if dict(detail) != stated:
        errors.append("summary counts or totals do not match accepted detail")

    source_total = sum(source_by_id.values(), Decimal("0.00"))
    classified_total = sum((money(row["amount"]) for row in classified), Decimal("0.00"))
    if source_total != classified_total:
        errors.append("classified total does not reconcile to source")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: {len(source)} rows and {source_total} reconciled")


if __name__ == "__main__":
    main()
