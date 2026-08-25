#!/usr/bin/env python3
import argparse
import csv
import json
from decimal import Decimal


def dec(value):
    return Decimal(str(value)).quantize(Decimal("0.01"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--purchase", required=True)
    parser.add_argument("--usage", required=True)
    parser.add_argument("--analysis", required=True)
    parser.add_argument("--schedule", required=True)
    args = parser.parse_args()
    with open(args.purchase, encoding="utf-8") as handle:
        purchase = json.load(handle)
    with open(args.analysis, encoding="utf-8") as handle:
        analysis = json.load(handle)
    with open(args.usage, newline="", encoding="utf-8") as handle:
        usage = list(csv.DictReader(handle))
    with open(args.schedule, newline="", encoding="utf-8") as handle:
        schedule = list(csv.DictReader(handle))
    errors = []

    basis = sum((dec(item["amount"]) for item in purchase["basis_items"] if item["included"]), Decimal("0.00"))
    if basis != dec(analysis["cost_basis"]):
        errors.append("cost basis does not match included purchase items")
    miles = {row["use_type"]: dec(row["miles"]) for row in usage}
    total = sum(miles.values(), Decimal("0.00"))
    if total != dec(analysis["total_miles"]):
        errors.append("total miles do not match usage log")
    business_pct = (miles["business"] / total).quantize(Decimal("0.0001"))
    if business_pct != Decimal(str(analysis["qualified_business_use_pct"])).quantize(Decimal("0.0001")):
        errors.append("business-use percentage is wrong")
    expected_predominant = business_pct > Decimal(str(analysis["predominant_use_threshold"]))
    if expected_predominant != analysis["predominant_business_use"]:
        errors.append("predominant-use result is wrong")
    business_basis = (basis * business_pct).quantize(Decimal("0.01"))
    if business_basis != dec(analysis["depreciable_business_basis"]):
        errors.append("business basis is wrong")
    rate = Decimal(str(analysis["fixture_rate"]))
    deduction = (business_basis * rate).quantize(Decimal("0.01"))
    if deduction != dec(analysis["fixture_deduction"]):
        errors.append("fixture deduction is wrong")
    counter = analysis["counterfactual"]
    counter_basis = (basis * Decimal(str(counter["business_use_pct"]))).quantize(Decimal("0.01"))
    if counter_basis != dec(counter["depreciable_business_basis"]):
        errors.append("counterfactual basis is wrong")
    if (counter_basis * Decimal(str(counter["fixture_rate"]))).quantize(Decimal("0.01")) != dec(counter["fixture_deduction"]):
        errors.append("counterfactual deduction is wrong")
    if not counter["changed_assumption"].strip():
        errors.append("counterfactual lacks changed assumption")
    for authority in analysis["authorities"]:
        if not authority["source_url"].startswith("https://"):
            errors.append("authority URL is missing")
    if len(schedule) != 1 or dec(schedule[0]["deduction"]) != deduction:
        errors.append("schedule does not match analysis")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: basis {basis}, business use {business_pct}, deduction {deduction}")


if __name__ == "__main__":
    main()
