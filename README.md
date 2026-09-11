# C(13,6,3): the lower bound, strengthened

Author: Jared Wilder. First public timestamp: 2026-09-11.

`C(13,6,3)` is the least number of 6-element blocks from a 13-point set such that every one of the
286 triples lies in some block. It is known to satisfy `20 <= C(13,6,3) <= 21`, and whether 20 is
achievable is open.

**This did not close it.** What it did is strengthen the structural bound enough that the remaining
search space is small and sharply described, and measure exactly why more solver time will not
finish the job.

---

## The strengthening

The structural fact previously on record was **every point of a hypothetical 20-block cover has
degree at least 8**, resting on `C(12,5,2) >= 8`, the Schönheim bound.

**`C(12,5,2) = 9`, proved here by exhaustive search** — 98,147,285 nodes, 289 seconds, infeasible at
8 and feasible at 9. That raises the point-degree floor to 9, and the consequences are large:

```
sum of point degrees = 6 * 20 = 120

with degree >= 8    13 * 8 = 104     slack 16
with degree >= 9    13 * 9 = 117     slack  3
```

**The slack collapses from 16 to 3.** Two things follow immediately.

**The lower bound re-derives itself.** `6b >= 13 * 9 = 117` gives `b >= 19.5`, hence
**`C(13,6,3) >= 20`** without appealing to anything else.

**The degree multiset is pinned to three possibilities.** Three units of excess over thirteen points
leaves only:

```
(12, 9^12)          12 points of degree exactly 9
(11, 10, 9^11)      11 points of degree exactly 9
(10, 10, 10, 9^10)  10 points of degree exactly 9
```

So **at least ten points have degree exactly 9** in any 20-block cover.

Alongside it, a pair-degree floor: every pair lies in at least `C(11,4,1) = 3` blocks, since a pair
inside a 6-block accounts for only 4 of the other 11 points.

**Both bounds are tight, so neither cut excludes anything real.** All four verified 21-covers found
here have minimum degree exactly 9 and minimum pair-degree exactly 3.

## Why the counting bound could not have done this

```
trivial bound   ceil(286 / 20) = 15
Schönheim       C(13,6,3) >= 18,   C(12,5,2) >= 8
exhaustive      C(12,5,2)  =  9
```

The Schönheim bound gives 8 where the truth is 9. **The exhaustive searcher decides a value the
counting bound cannot**, and that one unit is the whole strengthening.

The same point shows up in calibration: `C(10,4,2) = 9` while Schönheim gives only 8 there, and the
searcher settles it both ways.

---

## Calibration, both directions

Every value below was proved infeasible at `b-1` and feasible at `b` by a dedicated exhaustive
bitmask search, before anything was trusted at 20.

| value | at b−1 | at b |
|---|---|---|
| C(7,3,2) = 7 | infeasible | feasible, 25 nodes |
| C(8,3,2) = 11 | infeasible | feasible, 40 |
| C(9,3,2) = 12 | infeasible | feasible, 146 |
| **C(10,4,2) = 9** | infeasible, 2,440 nodes | feasible, 34,879 |
| C(11,5,2) = 7 | infeasible | feasible, 50,976 |
| **C(12,5,2) = 9** | **infeasible, 98,147,285 nodes, 289 s** | feasible, 8,894,174 |
| C(13,4,2) = 13 | infeasible | feasible, 532 |
| C(8,4,3) = 14 | infeasible | feasible, 56/56 verified |
| **C(9,4,3) = 25** | infeasible | feasible, 84/84 verified |
| C(10,4,3) = 30 | infeasible | feasible |
| C(13,6,3) <= 21 | — | **286/286 verified** |

Isomorphism machinery was validated separately: the Fano plane, STS(9) and PG(2,3) each return
exactly one class.

---

## What was run at 20, and what it returned

**An exhaustive six-case split with the degree vector fully pinned** — relabelling only, no
prescribed group, so all six returning infeasible would have closed the problem. All six returned
**unknown at 5,400 seconds each**, roughly 36 CPU-hours:

```
branches    5.3M   48.6M   43.4M   95.1M   38.7M   37.4M
conflicts   292k    166k    158k    352k    1.50M   1.46M
```

**Prescribed-symmetry search over 23 groups: zero covers found**, and **13 groups proved to admit no
invariant 20-cover** — including one of order 2,520. That is non-existence *under those symmetries*
and never non-existence, which is how it is recorded.

**Local search, seven independent runs: best 284 of 286 triples, two uncovered, never zero.** The
same code finds a 21-cover in about a second, and at known-optimum-minus-one it stalls at 1, 1 and 4
uncovered on three other designs. Suggestive of infeasibility. Not evidence.

## The measured bottleneck

**The linear relaxation is worthless here.** Its fractional optimum is about `286/20 = 14.3` against
an integer target of 20, so no bound-based pruning is available at all and the entire burden falls on
combinatorial search.

The signature in the pinned cases says the rest plainly: roughly `10^7` to `10^8` branches against
only `10^5` to `10^6` conflicts, about **one learned clause per 30 to 300 branches**. One case burned
95.1 million branches for 352 thousand conflicts.

**More solver time will not close this.**

## The step that would

Every 20-cover has at least ten points of degree exactly 9, and the link of such a point is an
**optimal (12,5,2) covering**. Enumerating those links up to isomorphism reduces the problem to an
11-block completion inside 12 points — 924 candidates at depth 11 rather than depth 20.

The isomorph-rejection machinery for this was built and validated. The link enumeration itself
exceeded `3.7 x 10^8` nodes without finishing, because it needs **canonical augmentation**, rejecting
isomorphs *during* generation rather than after. That, not a larger solver, is what would settle it.

## Also incomplete

A belt-and-braces re-check of `C(12,5,2) >= 9` without the level-2 relabelling restriction reached
`3.76 x 10^9` nodes in 7,892 seconds without completing. The restriction it removes was validated
independently on five designs, so the value stands — but **that particular run did not finish**, and
it is recorded as unfinished rather than as a confirmation.

## Bounds after this work

```
20 <= C(13,6,3) <= 21        unchanged
```

## Verification

```bash
python verify.py
```

Standard library only. Recomputes the degree arithmetic, the three admissible degree multisets, the
pair-degree floor, and the gap between the Schönheim bound and the exhaustive value.

## License

Apache-2.0.
