#!/usr/bin/env python3
"""Exact SAT check for the local C(12,5,2) degree cap used in C(13,6,3).

Claim: in a 9-block family of 5-subsets of a 12-point set covering every pair,
no point can occur in 6 or more blocks.

By point symmetry it suffices to demand degree(point 0) >= 6.  UNSAT proves
the universal cap <= 5.  The script writes a reproducible DIMACS instance and
JSON receipt; no global C(13,6,3) conclusion is made here.

Cardinality note: PySAT's incremental-totalizer RHS is used only for AT-MOST
constraints.  AT-LEAST is encoded as AT-MOST on the negated literals.  A
built-in SAT/UNSAT self-test runs before the mathematical instance.  This
repairs the earlier incorrect use of a positive RHS literal as a lower bound.
"""
from __future__ import annotations

import argparse, hashlib, itertools, json, sys, time
from pathlib import Path
from pysat.card import ITotalizer
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver

V = tuple(range(12))
BLOCKS = tuple(itertools.combinations(V, 5))
PAIRS = tuple(itertools.combinations(V, 2))


def add_at_most(cnf, vpool, lits, high):
    """Encode sum(lits) <= high using the supported totalizer direction."""
    lits = list(lits)
    if high >= len(lits):
        return
    if high < 0:
        cnf.append([])
        return
    # rhs[high] means that at least high+1 inputs are true; forbid it.
    tot = ITotalizer(lits=lits, ubound=high + 1, top_id=vpool.top)
    cnf.extend(tot.cnf.clauses)
    vpool.top = max(vpool.top, tot.top_id)
    cnf.append([-tot.rhs[high]])


def add_cardinality(cnf, vpool, lits, low=None, high=None):
    """Encode low <= sum(lits) <= high without relying on reverse RHS semantics."""
    lits = list(lits)
    assert low is not None or high is not None
    if high is not None:
        add_at_most(cnf, vpool, lits, high)
    if low is not None:
        # sum(lits) >= low  <=>  sum(not lits) <= len(lits)-low.
        add_at_most(cnf, vpool, [-lit for lit in lits], len(lits) - low)


def choose(cnf):
    for name in ("cadical195", "cadical153", "glucose4", "glucose3"):
        try:
            return name, Solver(name=name, bootstrap_with=cnf.clauses)
        except Exception:
            pass
    raise RuntimeError("no SAT solver available")


def cardinality_selftest():
    """Fail closed unless exact/lower cardinality really constrains models."""
    # Exactly 3 of 4 plus x0=false,x1=false must be UNSAT.
    vp = IDPool(start_from=1)
    xs = [vp.id(("t", i)) for i in range(4)]
    cnf = CNF()
    add_cardinality(cnf, vp, xs, low=3, high=3)
    cnf.append([-xs[0]])
    cnf.append([-xs[1]])
    _, s = choose(cnf)
    assert not s.solve(), "cardinality self-test failed: impossible exact-3 model accepted"
    s.delete()

    # Exactly 2 of 4 with 1100 fixed must be SAT.
    vp = IDPool(start_from=1)
    xs = [vp.id(("u", i)) for i in range(4)]
    cnf = CNF()
    add_cardinality(cnf, vp, xs, low=2, high=2)
    cnf.extend([[xs[0]], [xs[1]], [-xs[2]], [-xs[3]]])
    _, s = choose(cnf)
    assert s.solve(), "cardinality self-test failed: valid exact-2 model rejected"
    s.delete()

    # At least 3 of 4 plus three fixed false must be UNSAT.
    vp = IDPool(start_from=1)
    xs = [vp.id(("v", i)) for i in range(4)]
    cnf = CNF()
    add_cardinality(cnf, vp, xs, low=3)
    cnf.extend([[-xs[0]], [-xs[1]], [-xs[2]]])
    _, s = choose(cnf)
    assert not s.solve(), "cardinality self-test failed: lower bound not enforced"
    s.delete()


def build():
    vpool = IDPool(start_from=1)
    bvars = [vpool.id(("B", b)) for b in BLOCKS]
    bv = dict(zip(BLOCKS, bvars))
    cnf = CNF()
    add_cardinality(cnf, vpool, bvars, low=9, high=9)
    for p in PAIRS:
        sp = set(p)
        cnf.append([bv[b] for b in BLOCKS if sp.issubset(b)])
    # WLOG test whether some point can have degree >= 6.
    add_cardinality(cnf, vpool, [bv[b] for b in BLOCKS if 0 in b], low=6)
    return cnf, vpool, bvars


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cnf", type=Path, default=Path("c12_5_2_degree_ge6.cnf"))
    ap.add_argument("--json", type=Path, default=Path("c12_5_2_degree_cap.json"))
    args = ap.parse_args()

    cardinality_selftest()
    t0 = time.time()
    cnf, vpool, bvars = build()
    args.cnf.parent.mkdir(parents=True, exist_ok=True)
    cnf.to_file(str(args.cnf))
    digest = hashlib.sha256(args.cnf.read_bytes()).hexdigest()
    name, solver = choose(cnf)
    ts = time.time(); sat = solver.solve(); solve_s = time.time() - ts
    model = solver.get_model() if sat else None
    solver.delete()
    chosen = []
    if sat:
        pos = {x for x in model if x > 0}
        chosen = [b for b,v in zip(BLOCKS,bvars) if v in pos]
        assert len(chosen) == 9
        assert sum(0 in b for b in chosen) >= 6
        assert all(any(set(p).issubset(b) for b in chosen) for p in PAIRS)
    out = {
        "claim": "no 9-block C(12,5,2) cover has a point of degree >= 6",
        "status": "COUNTEREXAMPLE" if sat else "UNSAT",
        "solver": name,
        "cardinality_selftest": "PASS",
        "primary_block_variables": len(BLOCKS),
        "cnf_variables": vpool.top,
        "cnf_clauses": len(cnf.clauses),
        "cnf_sha256": digest,
        "build_seconds": time.time() - t0 - solve_s,
        "solve_seconds": solve_s,
        "chosen_blocks_if_sat": chosen,
    }
    args.json.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    return 10 if sat else 20

if __name__ == "__main__":
    sys.exit(main())
