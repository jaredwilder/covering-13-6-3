#!/usr/bin/env python3
"""Exact SAT search for a 20-block C(13,6,3) covering.

A hypothetical 20-block covering has point degrees at least 9, total degree 120,
so (up to relabeling) its point-degree multiset is one of exactly

  A: (12,9^12)
  B: (11,10,9^11)
  C: (10,10,10,9^10).

This script solves each labeled representative exactly. A solution to any case
is a genuine 20-block covering. UNSAT for all three cases proves C(13,6,3)>=21;
together with the public 21-block witness, that gives C(13,6,3)=21.

IMPORTANT CARDINALITY NOTE
--------------------------
PySAT's incremental-totalizer RHS is used only in its documented AT-MOST
direction. AT-LEAST constraints are encoded as AT-MOST constraints on negated
literals. A SAT/UNSAT cardinality self-test runs before the mathematical case.
This repairs the first release of this script, which incorrectly treated a
positive RHS literal as an enforced lower bound; that older run is invalid and
must not be used as mathematical evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

from pysat.card import ITotalizer
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver

V = tuple(range(13))
BLOCKS = tuple(itertools.combinations(V, 6))
TRIPLES = tuple(itertools.combinations(V, 3))
PAIRS = tuple(itertools.combinations(V, 2))

PATTERNS = {
    "A": (12,) + (9,) * 12,
    "B": (11, 10) + (9,) * 11,
    "C": (10, 10, 10) + (9,) * 10,
}


def add_at_most(cnf: CNF, vpool: IDPool, lits: list[int], high: int) -> None:
    """Encode sum(lits) <= high using the supported totalizer direction."""
    lits = list(lits)
    if high >= len(lits):
        return
    if high < 0:
        cnf.append([])
        return
    # rhs[high] means at least high+1 inputs are true; forbid it.
    tot = ITotalizer(lits=lits, ubound=high + 1, top_id=vpool.top)
    cnf.extend(tot.cnf.clauses)
    vpool.top = max(vpool.top, tot.top_id)
    cnf.append([-tot.rhs[high]])


def add_cardinality(cnf: CNF, vpool: IDPool, lits: list[int], low: int | None = None,
                    high: int | None = None) -> None:
    """Encode low <= sum(lits) <= high without reverse-RHS assumptions."""
    lits = list(lits)
    assert low is not None or high is not None
    if high is not None:
        add_at_most(cnf, vpool, lits, high)
    if low is not None:
        # sum(lits) >= low iff at most len(lits)-low of the literals are false.
        add_at_most(cnf, vpool, [-lit for lit in lits], len(lits) - low)


def choose_solver(cnf: CNF, requested: str | None = None) -> tuple[str, Solver]:
    names = [requested] if requested else ["cadical195", "cadical153", "glucose4", "glucose3"]
    errors = []
    for name in names:
        if not name:
            continue
        try:
            return name, Solver(name=name, bootstrap_with=cnf.clauses)
        except Exception as exc:  # pragma: no cover - environment dependent
            errors.append(f"{name}: {exc}")
    raise RuntimeError("no requested SAT solver available: " + "; ".join(errors))


def cardinality_selftest() -> None:
    """Fail closed unless exact and lower bounds constrain primary variables."""
    # Exactly 3 of 4 plus two fixed false is impossible.
    vp = IDPool(start_from=1)
    xs = [vp.id(("t", i)) for i in range(4)]
    cnf = CNF()
    add_cardinality(cnf, vp, xs, low=3, high=3)
    cnf.extend([[-xs[0]], [-xs[1]]])
    _, s = choose_solver(cnf)
    assert not s.solve(), "cardinality self-test failed: impossible exact-3 model accepted"
    s.delete()

    # Exactly 2 of 4 with 1100 fixed is valid.
    vp = IDPool(start_from=1)
    xs = [vp.id(("u", i)) for i in range(4)]
    cnf = CNF()
    add_cardinality(cnf, vp, xs, low=2, high=2)
    cnf.extend([[xs[0]], [xs[1]], [-xs[2]], [-xs[3]]])
    _, s = choose_solver(cnf)
    assert s.solve(), "cardinality self-test failed: valid exact-2 model rejected"
    s.delete()

    # At least 3 of 4 plus three fixed false is impossible.
    vp = IDPool(start_from=1)
    xs = [vp.id(("v", i)) for i in range(4)]
    cnf = CNF()
    add_cardinality(cnf, vp, xs, low=3)
    cnf.extend([[-xs[0]], [-xs[1]], [-xs[2]]])
    _, s = choose_solver(cnf)
    assert not s.solve(), "cardinality self-test failed: lower bound not enforced"
    s.delete()


def build_case(pattern: str) -> tuple[CNF, IDPool, list[int]]:
    degs = PATTERNS[pattern]
    vpool = IDPool(start_from=1)
    block_vars = [vpool.id(("B", b)) for b in BLOCKS]
    bvar = dict(zip(BLOCKS, block_vars))
    cnf = CNF()

    # Exactly 20 blocks.
    add_cardinality(cnf, vpool, block_vars, low=20, high=20)

    # Every triple is covered.
    for t in TRIPLES:
        st = set(t)
        cnf.append([bvar[b] for b in BLOCKS if st.issubset(b)])

    # Exact labeled point degrees for this WLOG degree pattern.
    for x, d in enumerate(degs):
        lits = [bvar[b] for b in BLOCKS if x in b]
        add_cardinality(cnf, vpool, lits, low=d, high=d)

    # Redundant but strong: every pair occurs in at least 3 selected blocks.
    for p in PAIRS:
        sp = set(p)
        lits = [bvar[b] for b in BLOCKS if sp.issubset(b)]
        add_cardinality(cnf, vpool, lits, low=3)

    return cnf, vpool, block_vars


def verify_model(model: list[int], block_vars: list[int], pattern: str) -> list[tuple[int, ...]]:
    pos = set(v for v in model if v > 0)
    chosen = [b for b, v in zip(BLOCKS, block_vars) if v in pos]
    assert len(chosen) == 20
    covered = set()
    for b in chosen:
        covered.update(itertools.combinations(b, 3))
    assert len(covered) == len(TRIPLES)
    got_deg = tuple(sum(x in b for b in chosen) for x in V)
    assert got_deg == PATTERNS[pattern]
    for p in PAIRS:
        assert sum(set(p).issubset(b) for b in chosen) >= 3
    return chosen


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pattern", choices=sorted(PATTERNS))
    ap.add_argument("--solver", default=None)
    ap.add_argument("--dump-cnf", type=Path, default=None)
    ap.add_argument("--json", type=Path, default=None)
    args = ap.parse_args()

    cardinality_selftest()
    t0 = time.time()
    cnf, vpool, block_vars = build_case(args.pattern)
    build_s = time.time() - t0

    if args.dump_cnf:
        cnf.to_file(str(args.dump_cnf))
        sha = hashlib.sha256(args.dump_cnf.read_bytes()).hexdigest()
    else:
        h = hashlib.sha256()
        for c in cnf.clauses:
            h.update((" ".join(map(str, c)) + " 0\n").encode())
        sha = h.hexdigest()

    solver_name, solver = choose_solver(cnf, args.solver)
    ts = time.time()
    sat = solver.solve()
    solve_s = time.time() - ts
    model = solver.get_model() if sat else None
    solver.delete()

    selected = verify_model(model, block_vars, args.pattern) if sat else []
    result = {
        "problem": "C(13,6,3) target 20",
        "pattern": args.pattern,
        "degree_pattern": PATTERNS[args.pattern],
        "status": "SAT" if sat else "UNSAT",
        "solver": solver_name,
        "cardinality_selftest": "PASS",
        "primary_block_variables": len(BLOCKS),
        "cnf_variables": vpool.top,
        "cnf_clauses": len(cnf.clauses),
        "cnf_sha256": sha,
        "build_seconds": build_s,
        "solve_seconds": solve_s,
        "selected_blocks": selected,
    }
    text = json.dumps(result, indent=2)
    print(text)
    if args.json:
        args.json.write_text(text + "\n", encoding="utf-8")
    return 10 if sat else 20


if __name__ == "__main__":
    sys.exit(main())
