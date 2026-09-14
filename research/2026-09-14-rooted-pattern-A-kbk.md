# C(13,6,3) — rooted Pattern-A reduction and KBK audit

**Author:** Jared Wilder  
**Date:** 2026-09-14  
**Status:** exact structural reduction + computation-supported catalogue consequences; parent value remains `20 <= C(13,6,3) <= 21`.

This note records the strongest mathematics recovered by a second forensic pass through the 100-round close campaign. It deliberately separates exact deductions from catalogue-completeness assumptions.

## 1. Optimal-link catalogue recovered by the campaign

The campaign produced 107 pairwise nonisomorphic 9-block `C(12,5,2)` covers:

- 54 classes with maximum point degree 5;
- 53 classes with degree sequence `4^9 3^3`.

The degree-profile split over all 107 objects is

```text
53 : 4^9 3^3
46 : 5 4^7 3^4
 6 : 5^2 4^5 3^5
 2 : 5^3 4^3 3^6
```

An independent incidence-graph automorphism count on these 107 supplied objects gives total labelled mass

```text
maxdeg 4 family :  7,384,608,000
maxdeg 5 family :  6,147,187,200
all 107 classes : 13,531,795,200
```

These mass figures are consequences of the supplied catalogue. **They are not an independent proof that the catalogue is complete.** Independent completeness replay remains a live debt.

Catalogue SHA-256 in the session export:

`4b4963542117d93c942d99c11fdbe2b286ec118412ecd932aec48cf53ec4e02e`

## 2. Correction: the blanket `lambda <= 4` statement is false

A campaign summary promoted the claim that every pair in every optimal link occurs in at most four blocks. Direct audit of the 107 supplied links finds **three isomorphism classes with pair multiplicity 5**.

Therefore the blanket statement

`lambda_{yzw} <= 4 for every catalogue link`

is retracted.

This does **not** invalidate the main completion models: the actual signature code retained the multiplicity-5 bin. The defect was theorem bookkeeping, not a silent exclusion in those solver models.

## 3. Pattern A roots every ordinary link at degree 5

Pattern A has global point degrees

`(12,9^12)`.

Let `h` be the degree-12 point and let `y` be any other point. The pair-degree row at `h` has total

`12 * 5 = 60`,

so the campaign's exact row arithmetic gives

`r_{hy}=5`

for every ordinary point `y`.

Now take the link at `y`. It is an optimal 9-block `C(12,5,2)` cover. Inside that link, the distinguished point `h` has degree exactly 5.

**Consequently Pattern A never needs the 53 max-degree-4 link classes.** Only the 54 max-degree-5 classes can occur locally.

When each of those 54 unrooted classes is rooted at a degree-5 point and root orbits under the automorphism group are identified, there are only

`56 rooted isomorphism types`.

At the coarse rooted row-signature level these collapse to 27 signatures.

## 4. The correct residual coordinate

Let the eight global blocks avoiding `h` be indexed by `[8]`. Every ordinary point has global degree 9 and occurs with `h` in exactly 5 blocks, so every ordinary point occurs in exactly four `h`-avoiding blocks.

For each ordinary point `y`, define

`S_y subset [8]`

as the four avoiding blocks containing `y`.

For two ordinary points `y,z`, write

- `r_yz` for the number of global blocks containing `y,z`;
- `s_yz = lambda_hyz` for the number containing `h,y,z`;
- `a_yz = r_yz - s_yz` for the number avoiding `h` and containing `y,z`.

Then exactly

`a_yz = |S_y intersect S_z|`.

Scanning all valid degree-5-rooted catalogue types gives the stronger valid local bound

`a_yz <= 3`.

Therefore no two ordinary points can have the same `S_y`, because equal 4-subsets would intersect in 4 elements.

Hence the eight avoiding blocks are equivalently encoded by:

> **a simple 4-uniform, 6-regular hypergraph on 8 vertices with exactly 12 edges.**

The 12 hyperedges are the distinct sets `S_y`. Each has size 4 because each ordinary point lies in four avoiding blocks. Each of the 8 dual vertices has degree 6 because each avoiding global block contains six ordinary points.

This is a much smaller coordinate system than generating eight 6-subsets from the 924 possible blocks on twelve points.

## 5. Immediate KBK prune: two rooted types are impossible in Pattern A

If `a_yz=0`, then `S_z` is disjoint from `S_y`. A 4-subset of an 8-set has exactly one disjoint 4-subset: its complement.

Therefore every ordinary point `y` can have **at most one** other point `z` with `a_yz=0`.

Two of the 56 rooted catalogue types demand two such zero-intersection neighbours. Those rooted types are therefore impossible in Pattern A before any global solver is run.

So the first rooted court reduces

`56 -> 54`

possible local rooted types.

This is KBK in the intended sense: the false global `lambda <= 4` claim is removed, but the corrected rooted coordinate yields a *stronger valid* pruning statement.

## 6. Residual row arithmetic

Because the twelve `S_y` are distinct 4-subsets of `[8]`, each row has intersection counts

`(c0,c1,c2,c3)`

with

`c0+c1+c2+c3=11`

and

`c1+2c2+3c3=20`.

Also `c0` is 0 or 1. The full rooted catalogue realizes only nine of the eleven arithmetically possible profiles after the `c0<=1` court; this gives another finite local filter for a future two-anchor compatibility solver.

## 7. Next exact attack

The parent close program should no longer spend its budget on the raw Pattern-A CP-SAT model or on the old 12-point residual canonical generation.

The new exact state is:

```text
54 surviving degree-5-rooted local types
        +
12 distinct 4-subsets of an 8-set, each dual vertex degree 6
        +
symmetry r_yz = r_zy and s_yz = s_zy
        +
rooted two-anchor compatibility
```

The immediate target is to build the compatibility graph/table between rooted types and the Johnson-geometry relation `|S_y intersect S_z|`.

If that system is UNSAT with complete rooted-catalogue authority, Pattern A is eliminated. If SAT, it produces a drastically smaller exact completion state.

## Authority boundary

- Degree arithmetic and the dual-coordinate derivation are exact.
- The `a_yz<=3`, 56 rooted types, 27 coarse signatures, and labelled-mass figures are independently recomputed consequences of the supplied 107 catalogue objects.
- The statement that the 107 supplied objects are **all** optimal links still requires an independent completeness certificate/enumerator.
- No claim here changes the public bound `20 <= C(13,6,3) <= 21`.
