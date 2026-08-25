#!/usr/bin/env python3
import argparse
import csv
from collections import defaultdict
from decimal import Decimal


def load(path):
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def amount(value):
    return Decimal(value).quantize(Decimal("0.01"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", required=True)
    parser.add_argument("--coa", required=True)
    parser.add_argument("--ledger", required=True)
    parser.add_argument("--trial-balance", required=True)
    parser.add_argument("--exceptions", required=True)
    args = parser.parse_args()
    bank, coa, ledger, tb, exceptions = map(load, [args.bank, args.coa, args.ledger, args.trial_balance, args.exceptions])
    errors = []

    bank_ids = {row["txn_id"] for row in bank}
    ledger_ids = {row["txn_id"] for row in ledger}
    if bank_ids != ledger_ids:
        errors.append("ledger transaction coverage does not match bank rows")

    accounts = {row["account_code"] for row in coa}
    for row in ledger:
        if row["account_code"] not in accounts:
            errors.append(f"unknown account {row['account_code']}")

    by_txn = defaultdict(lambda: [Decimal("0.00"), Decimal("0.00")])
    by_account = defaultdict(Decimal)
    for row in ledger:
        debit, credit = amount(row["debit"]), amount(row["credit"])
        by_txn[row["txn_id"]][0] += debit
        by_txn[row["txn_id"]][1] += credit
        by_account[row["account_code"]] += debit - credit
    for txn_id, values in by_txn.items():
        if values[0] != values[1]:
            errors.append(f"unbalanced journal entry {txn_id}")

    bank_total = sum((amount(row["amount"]) for row in bank), Decimal("0.00"))
    if by_account["1000"] != bank_total:
        errors.append("cash movement does not match signed bank activity")

    stated = {}
    for row in tb:
        net = amount(row["debit_balance"]) - amount(row["credit_balance"])
        stated[row["account_code"]] = net
    if dict(by_account) != stated:
        errors.append("trial balance does not equal ledger balances")
    tb_debits = sum((amount(row["debit_balance"]) for row in tb), Decimal("0.00"))
    tb_credits = sum((amount(row["credit_balance"]) for row in tb), Decimal("0.00"))
    if tb_debits != tb_credits:
        errors.append("trial balance debits do not equal credits")

    suspense_txns = {row["txn_id"] for row in ledger if row["account_code"] == "1999"}
    exception_txns = {row["txn_id"] for row in exceptions}
    if suspense_txns != exception_txns:
        errors.append("suspense postings do not match exceptions")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        raise SystemExit(1)
    print(f"PASS: {len(bank)} bank rows, cash {bank_total}, trial balance {tb_debits}")


if __name__ == "__main__":
    main()
