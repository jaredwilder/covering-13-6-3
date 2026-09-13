# C(13,6,3): two human local-link eliminations

**Author:** Jared Wilder  
**Promoted to static GitHub:** 2026-09-13

These two deductions were recovered from the release-day session report as mathematics that had not yet been promoted to a static result document.

They concern a hypothetical 20-block `C(13,6,3)` cover and its local link: a degree-9 point induces a 9-block `C(12,5,2)` cover on the other 12 points.

## Theorem 1 — local degree 9 is impossible

A 9-block `C(12,5,2)` cover cannot contain a point of degree 9.

### Proof

Assume a point `p` lies in all nine 5-blocks. Delete `p` from every block. The nine residual blocks are 4-subsets of the remaining 11 points.

Every pair of those 11 points must still be covered by at least one residual block, because every original 5-block contained `p`.

But nine 4-subsets contain at most

\[
9\binom42=9\cdot6=54
\]

pair incidences, while the 11-point ground set has

\[
\binom{11}{2}=55
\]

distinct pairs.

Contradiction. Therefore no point can have degree 9 in such a 9-block `C(12,5,2)` cover. ∎

## Theorem 2 — local degree 8 is impossible

A 9-block `C(12,5,2)` cover cannot contain a point of degree 8.

### Proof

Assume `p` has degree 8. Exactly one 5-block `B` avoids `p`. On the 11 points other than `p`, let `C` be the 6-point complement of `B`. Deleting `p` from the eight blocks through it gives 4-subsets

\[
A_1,\ldots,A_8.
\]

The block `B` already covers the 10 pairs internal to `B`. Therefore the residual 4-subsets must cover every

- cross pair in `B\times C`: `5\cdot6=30` pairs;
- pair internal to `C`: `\binom62=15` pairs.

Give each cross pair weight 2 and each pair internal to `C` weight 1. The required total weight is

\[
2\cdot30+15=75.
\]

For one residual 4-set `A`, put

\[
t=|A\cap B|,
\qquad
4-t=|A\cap C|.
\]

Its contribution to the required weighted pair universe is at most

\[
2t(4-t)+\binom{4-t}{2}.
\]

For `t=0,1,2,3,4`, these values are

\[
6,9,9,6,0,
\]

so each residual block contributes at most 9. Hence all eight together contribute at most

\[
8\cdot9=72<75,
\]

contradiction. Therefore local degree 8 is impossible. ∎

## What remains open

These two hand proofs eliminate local degrees 8 and 9 only.

The exact CP-SAT runs for local degrees 6 and 7 reached their 2400-second limits with status `UNKNOWN`; they produced neither a feasible counterexample nor an infeasibility certificate.

Therefore the stronger desired local cap

\[
\text{every point degree}\le5
\]

is **not proved**.

Any downstream Pattern-A decomposition that assumes that cap remains conditional.

## Why this matters globally

If degrees 6 and 7 were also eliminated, then in the global degree pattern `(12,9^{12})`, the degree-12 point `h` would satisfy `r_{hy}=5` for every other point `y`, forcing a very rigid decomposition into a degree-5 regular family of twelve 5-subsets through `h` and a degree-4 regular family of eight 6-subsets avoiding `h`.

That consequence is useful as a search target, but is not promoted here as an unconditional theorem.
