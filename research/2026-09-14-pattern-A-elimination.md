# C(13,6,3) — Pattern A exact elimination packet

**Author:** Jared Wilder  
**Date:** 2026-09-14  
**Status:** exhaustive finite elimination of Pattern A, with one redundancy/certificate-hardening item still tracked separately.  
**Parent problem:** `20 <= C(13,6,3) <= 21` remains the full target.

This note records the next KBK layer after the rooted-link reduction. It does not use the old global 20-cover SAT route.

## Pattern A

Pattern A is the hypothetical point-degree multiset

```text
(12, 9^12).
```

Let `h` be the degree-12 point. The twelve ordinary points have degree 9, and the exact pair-row arithmetic gives `r_hy=5` for every ordinary `y`.

There are therefore exactly eight global blocks avoiding `h`. Index them by `[8]`. Every ordinary point lies in exactly four of those eight blocks, so attach to every ordinary point `y` a 4-subset

```text
S_y subset [8].
```

The prior rooted audit reduced the local geometry to a finite list of allowed four-block Venn patterns. A separate duplicate-edge court handles the possibility `S_y=S_z`; after that court the residual is a simple 4-uniform, 6-regular hypergraph with 12 edges on 8 vertices.

## Exhaustive residual classification

`patA_enum.cpp` performs canonical generation directly in the 8-vertex dual coordinate. It fixes one 4-set by symmetry, uses the exact catalogue-derived oriented Venn-pattern admissibility table, enforces dual degree 6 at each of the eight coordinates, and quotients by the stabilizer action.

Fresh replay on 2026-09-14:

```text
A=279 G=576
DONE nodes=3268358 leaves=6084 orbits=22 sec=1.83108
```

Thus the exact locally admissible residual court contains

```text
6,084 labeled residuals
22 isomorphism classes.
```

The 22 representatives are stored in `pattern-A-elimination/residual_orbits.txt`.

## Catalogue-free local completion court

The second verifier does **not** choose a local completion from the 107-link catalogue.

For a fixed residual and ordinary point `y`, its four `h`-avoiding link blocks are already determined. The verifier then works directly from the definition of a 9-block `C(12,5,2)` link: it exhaustively searches the five `h`-containing link blocks needed to cover the remaining pairs.

This gives a finite domain of all direct local stars for each of the 12 ordinary points. For every pair `y,z`, the verifier asks whether there is any pair of local stars that agrees on every global `h`-containing block involving both `y` and `z`.

Fresh replay on 2026-09-14:

```text
orbit 1  DEAD pair 0,3  domains 28,20
orbit 2  DEAD pair 0,7  domains 28,28
orbit 3  DEAD pair 3,7  domains 28,28
orbit 4  DEAD pair 0,1  domains 1,1
orbit 5  DEAD pair 0,1  domains 4,4
orbit 6  DEAD pair 0,9  domains 4,4
orbit 7  DEAD pair 0,10 domains 4,4
orbit 8  DEAD pair 0,11 domains 20,20
orbit 9  DEAD pair 0,11 domains 20,20
orbit 10 DEAD pair 0,1  domains 6,6
orbit 11 DEAD pair 0,1  domains 3,3
orbit 12 DEAD pair 0,1  domains 3,3
orbit 13 DEAD pair 0,1  domains 3,3
orbit 14 DEAD pair 0,1  domains 3,3
orbit 15 DEAD pair 0,11 domains 144,144
orbit 16 DEAD pair 0,2  domains 4,4
orbit 17 DEAD pair 0,11 domains 144,144
orbit 18 DEAD pair 0,3  domains 20,28
orbit 19 DEAD pair 0,2  domains 144,3
orbit 20 DEAD pair 0,8  domains 20,4
orbit 21 DEAD pair 0,1  domains 4,4
orbit 22 DEAD pair 0,11 domains 144,144
DONE survivors=0 sec=14.0899
```

Therefore every one of the 22 residual classes is killed already by a **pairwise star-gluing contradiction**. A full 12-variable CSP is never needed.

## Duplicate dual edge court

The residual classifier above assumes distinct `S_y`. The duplicate case is attacked separately from first principles.

Assume `S_y=S_z`. In the optimal 9-block link at `y`, the root `h` has degree 5 and `z` lies in all four root-avoiding blocks. Pair coverage forces `z` into at least one root-containing block; the independently established degree-5 cap forces exactly one such joint block. Hence the nine link blocks normalize as

```text
4 root-only blocks
4 z-only blocks
1 joint (root,z) block.
```

After fixing the three other vertices of the joint block by symmetry, the problem becomes two families `A,B` of four 4-subsets on ten vertices.

The eight 4-blocks contribute 32 point incidences. Pair coverage forces every remaining vertex to occur at least three times, so only two total degree patterns are possible:

```text
(5,3^9)
(4,4,3^8).
```

Relative to the distinguished 3-set in the joint block, these reduce to five placement cases:

```text
5C    degree-5 point inside the distinguished 3-set
5O    degree-5 point outside
44CC  both degree-4 points inside
44CO  one inside and one outside
44OO  both outside
```

All five exact binary feasibility models are UNSAT. The normalized unsplit model also replays UNSAT in about one second.

This finite duplicate court currently has an explicit exact MILP implementation. A second solver-independent verifier is retained as a redundancy/certificate-hardening requirement before the repository marks this sublemma `DOUBLE_VERIFIED`.

## Current conclusion

The finite evidence chain is now:

```text
Pattern A
 -> 8-vertex dual residual
 -> 22 exact locally admissible residual classes
 -> direct first-principles local completion domains
 -> pairwise star-gluing contradiction for all 22.
```

Accordingly Pattern A is computationally eliminated by an exhaustive finite court. The one remaining hardening task is an independent duplicate-edge verifier, not a return to the old global SAT architecture.

## Files

- `pattern-A-elimination/patA_enum.cpp` — exhaustive dual residual classifier
- `pattern-A-elimination/residual_orbits.txt` — 22 representatives
- `pattern-A-elimination/patA_direct_court.cpp` — catalogue-free direct local-completion/gluing verifier
- `pattern-A-elimination/direct_court.tsv` — per-orbit kill receipt

## No weakening

This does **not** settle `C(13,6,3)` by itself. A 20-cover could still have Pattern B `(11,10,9^11)` or Pattern C `(10,10,10,9^10)`. The next close program must eliminate or realize those two exact degree patterns using the same rooted/two-anchor machinery.
