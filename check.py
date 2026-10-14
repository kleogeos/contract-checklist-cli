#!/usr/bin/env python3
"""Scan a freelance contract (plain text/markdown) for commonly-missing clauses.

Heuristic keyword check only — NOT legal advice, just a sanity-check reminder
before you sign or send a contract.
"""
import argparse
import sys

CHECKS = [
    ("payment terms / due date", ["payment", "due", "net 15", "net 30", "invoice"]),
    ("late payment fee / interest", ["late fee", "late payment", "interest", "overdue"]),
    ("scope of work / deliverables", ["scope", "deliverable", "in scope", "out of scope"]),
    ("revision limit", ["revision", "round of feedback", "revisions included"]),
    ("intellectual property / ownership", ["intellectual property", "copyright", "ownership", "license"]),
    ("termination clause", ["terminat", "cancel"]),
    ("confidentiality / NDA", ["confidential", "non-disclosure", "nda"]),
    ("kill fee / deposit", ["deposit", "kill fee", "upfront", "down payment"]),
    ("liability limitation", ["liability", "indemnif", "warrant"]),
    ("governing law / jurisdiction", ["governing law", "jurisdiction", "venue"]),
]


def check(text):
    low = text.lower()
    found, missing = [], []
    for label, keywords in CHECKS:
        if any(k in low for k in keywords):
            found.append(label)
        else:
            missing.append(label)
    return found, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("file", help="contract text/markdown file")
    args = ap.parse_args()

    with open(args.file, encoding="utf-8") as f:
        text = f.read()

    found, missing = check(text)

    print(f"Checked {args.file} — {len(found)}/{len(CHECKS)} common clauses detected.\n")
    if found:
        print("Found:")
        for label in found:
            print(f"  [x] {label}")
    if missing:
        print("\nPossibly missing — worth double-checking:")
        for label in missing:
            print(f"  [ ] {label}")
    print("\nKeyword heuristic only, not legal advice — read your contract yourself.")

    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main()
