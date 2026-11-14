#!/usr/bin/env python3
"""Flag Units where the correct choice is too often the strictly longest one.

Usage: python3 scripts/audit_quiz_choice_length.py [unit_dir ...] [--max 0.35]
Exit 1 if any Unit exceeds the ratio. A learner who always picks the longest
choice should not beat chance by much (5 choices = 0.2).
"""
import argparse
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
ADVANCED = ["07-network-devices", "08-router-and-nat", "09-load-balancing",
            "10-vpn-and-security", "15-network-security-solutions"]


def questions(unit_dir):
    unit_md = ROOT / "units" / unit_dir / "unit.md"
    for lesson in yaml.safe_load(unit_md.read_text(encoding="utf-8").split("---")[1])["lessons"]:
        meta = yaml.safe_load((unit_md.parent / lesson["path"]).read_text(encoding="utf-8").split("---")[1]) or {}
        for page in meta.get("page_metadata") or []:
            yield from page.get("questions") or []


def longest_ratio(qs):
    hits = total = 0
    for q in qs:
        lengths = [len(c["text"]) for c in q["choices"]]
        answer = len(next(c["text"] for c in q["choices"] if c["id"] == q["answer"]))
        total += 1
        hits += answer == max(lengths) and lengths.count(answer) == 1
    return hits, total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("units", nargs="*", default=ADVANCED)
    parser.add_argument("--max", type=float, default=0.35)
    args = parser.parse_args()
    failed = False
    for unit in args.units:
        hits, total = longest_ratio(questions(unit))
        ratio = hits / total if total else 0
        flag = "FAIL" if ratio > args.max else "ok"
        failed |= flag == "FAIL"
        print(f"{flag} {unit}: {hits}/{total} correct answers are the longest choice ({ratio:.0%})")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    assert longest_ratio([{"answer": "a", "choices": [{"id": "a", "text": "long one"}, {"id": "b", "text": "x"}]}]) == (1, 1)
    assert longest_ratio([{"answer": "b", "choices": [{"id": "a", "text": "long one"}, {"id": "b", "text": "x"}]}]) == (0, 1)
    main()
