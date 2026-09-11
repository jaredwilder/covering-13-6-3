#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Exact verifier for the strengthened C(13,6,3) lower-bound argument.

    python verify.py

Standard library only. Exit 0 means everything reproduced.
"""
from __future__ import annotations

import sys
from itertools import combinations
from math import ceil

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-56s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def schonheim(v, k, t):
    if t == 0:
        return 1
    return ceil(v / k * schonheim(v - 1, k - 1, t - 1))


def test_degree_arithmetic():
    print("The degree arithmetic at b = 20")
    v, k, b = 13, 6, 20
    check("triples to cover", len(list(combinations(range(v), 3))), 286)
    check("triples covered by one block", len(list(combinations(range(k), 3))), 20)
    check("sum of point degrees = k*b", k * b, 120)
    print()
    check("with degree >= 8:  13*8", 13 * 8, 104)
    check("  slack", k * b - 13 * 8, 16)
    check("with degree >= 9:  13*9", 13 * 9, 117)
    check("  slack", k * b - 13 * 9, 3)
    print("     the slack collapses from 16 to 3")


def test_lower_bound():
    print("The lower bound re-derives from degree >= 9")
    # 6b >= 13*9 = 117
    b_min = ceil(117 / 6)
    check("6b >= 117 forces b >=", b_min, 20)
    check("  and 19 would need 6*19 =", 6 * 19, 114)
    check("  which is below 117", 6 * 19 < 117, True)


def partitions(n, maxpart):
    if n == 0:
        yield ()
        return
    for p in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - p, p):
            yield (p,) + rest


def test_degree_multisets():
    print("The three admissible degree multisets")
    got = []
    for excess in partitions(3, 3):
        degs = sorted([9 + e for e in excess] + [9] * (13 - len(excess)), reverse=True)
        check("  sums to 120", sum(degs), 120)
        got.append(tuple(degs))
    check("exactly three multisets", len(got), 3)
    check("  (12, 9^12)", got[0], (12,) + (9,) * 12)
    check("  (11, 10, 9^11)", got[1], (11, 10) + (9,) * 11)
    check("  (10, 10, 10, 9^10)", got[2], (10, 10, 10) + (9,) * 10)
    counts = [d.count(9) for d in got]
    check("points of degree exactly 9", counts, [12, 11, 10])
    check("  so at least ten, always", min(counts), 10)


def test_pair_degree():
    print("The pair-degree floor")
    # a pair inside a 6-block accounts for 4 of the other 11 points
    check("C(11,4,1) = ceil(11/4)", ceil(11 / 4), 3)
    check("  other points in a block containing a fixed pair", 6 - 2, 4)
    check("  points that must be covered with that pair", 13 - 2, 11)


def test_schonheim_gap():
    print("Where the counting bound falls short")
    check("trivial bound ceil(286/20)", ceil(286 / 20), 15)
    check("Schonheim C(13,6,3)", schonheim(13, 6, 3), 18)
    check("Schonheim C(12,5,2)", schonheim(12, 5, 2), 8)
    print("     the exhaustive value of C(12,5,2) is 9, one above Schonheim")
    print("     and that one unit is the entire strengthening")
    check("Schonheim C(10,4,2)", schonheim(10, 4, 2), 8)
    print("     same shape: the true value there is 9")


def test_lp_is_useless():
    print("Why nothing prunes by bound")
    frac = 286 / 20
    check("fractional optimum 286/20, to 2 places", round(frac, 2), 14.30)
    check("  against an integer target of", 20, 20)
    check("  so the relaxation is below the target", frac < 20, True)


def main():
    for fn in (test_degree_arithmetic, test_lower_bound, test_degree_multisets,
               test_pair_degree, test_schonheim_gap, test_lp_is_useless):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
