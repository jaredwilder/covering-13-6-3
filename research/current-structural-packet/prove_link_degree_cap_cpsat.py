#!/usr/bin/env python3
"""Independent CP-SAT check of the C(12,5,2) degree-cap lemma.

Question: can nine 5-subsets of a 12-point set cover every pair while some
point lies in at least six selected blocks? By symmetry fix that point as 0.

INFEASIBLE certifies the local cap degree <= 5. OPTIMAL/FEASIBLE is accepted
only after the returned block family is directly rechecked.
"""
from __future__ import annotations

import itertools, json, os, sys, time
from ortools.sat.python import cp_model

V = tuple(range(12))
BLOCKS = tuple(itertools.combinations(V, 5))
PAIRS = tuple(itertools.combinations(V, 2))


def main():
    model = cp_model.CpModel()
    x = [model.new_bool_var(f"b_{i}") for i in range(len(BLOCKS))]
    model.add(sum(x) == 9)
    for p in PAIRS:
        sp = set(p)
        model.add(sum(x[i] for i,b in enumerate(BLOCKS) if sp.issubset(b)) >= 1)
    model.add(sum(x[i] for i,b in enumerate(BLOCKS) if 0 in b) >= 6)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = max(1, min(8, os.cpu_count() or 1))
    solver.parameters.random_seed = 1
    solver.parameters.max_time_in_seconds = 1200
    t0 = time.time()
    status = solver.solve(model)
    elapsed = time.time() - t0
    name = solver.status_name(status)

    chosen = []
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        chosen = [b for i,b in enumerate(BLOCKS) if solver.boolean_value(x[i])]
        assert len(chosen) == 9
        assert sum(0 in b for b in chosen) >= 6
        assert all(any(set(p).issubset(b) for b in chosen) for p in PAIRS)

    out = {
        "claim": "no 9-block C(12,5,2) cover has a point of degree >= 6",
        "solver": "OR-Tools CP-SAT",
        "status": name,
        "elapsed_seconds": elapsed,
        "primary_variables": len(BLOCKS),
        "pair_constraints": len(PAIRS),
        "chosen_blocks_if_feasible": chosen,
        "best_objective_bound": solver.best_objective_bound if status != cp_model.UNKNOWN else None,
    }
    print(json.dumps(out, indent=2))
    open("c12_5_2_degree_cap_cpsat.json", "w").write(json.dumps(out, indent=2) + "\n")
    if status == cp_model.INFEASIBLE:
        return 0
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return 10
    return 2

if __name__ == "__main__":
    sys.exit(main())
