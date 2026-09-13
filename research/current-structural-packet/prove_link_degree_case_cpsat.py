#!/usr/bin/env python3
"""Exact CP-SAT search for one local C(12,5,2) degree case.

Select exactly nine 5-subsets of 12 points covering every pair, and force the
fixed point 0 to have exact degree d.  By symmetry, infeasibility for d=6,7,8,9
rules out every point degree >=6.  Cases d=8,9 also have independent human
counting proofs; the main computational targets are d=6,7.
"""
from __future__ import annotations

import argparse, itertools, json, os, sys, time
from ortools.sat.python import cp_model

V = tuple(range(12))
BLOCKS = tuple(itertools.combinations(V, 5))
PAIRS = tuple(itertools.combinations(V, 2))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--degree", type=int, choices=(6,7,8,9), required=True)
    ap.add_argument("--seconds", type=float, default=1800)
    args = ap.parse_args()

    model = cp_model.CpModel()
    x = [model.new_bool_var(f"b_{i}") for i in range(len(BLOCKS))]
    model.add(sum(x) == 9)
    for p in PAIRS:
        sp = set(p)
        model.add(sum(x[i] for i,b in enumerate(BLOCKS) if sp.issubset(b)) >= 1)
    model.add(sum(x[i] for i,b in enumerate(BLOCKS) if 0 in b) == args.degree)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = max(1, min(8, os.cpu_count() or 1))
    solver.parameters.random_seed = 1
    solver.parameters.max_time_in_seconds = args.seconds
    t0 = time.time()
    status = solver.solve(model)
    elapsed = time.time() - t0
    name = solver.status_name(status)

    chosen = []
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen = [b for i,b in enumerate(BLOCKS) if solver.boolean_value(x[i])]
        assert len(chosen) == 9
        assert sum(0 in b for b in chosen) == args.degree
        assert all(any(set(p).issubset(b) for b in chosen) for p in PAIRS)

    out = {
        "problem": "9-block C(12,5,2) local degree case",
        "fixed_point_degree": args.degree,
        "status": name,
        "solver": "OR-Tools CP-SAT",
        "elapsed_seconds": elapsed,
        "primary_variables": len(BLOCKS),
        "chosen_blocks_if_feasible": chosen,
    }
    path = f"c12_5_2_degree_{args.degree}.json"
    open(path, "w").write(json.dumps(out, indent=2) + "\n")
    print(json.dumps(out, indent=2))
    if status == cp_model.INFEASIBLE:
        return 0
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return 10
    return 2

if __name__ == "__main__":
    sys.exit(main())
