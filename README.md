# C(13,6,3): exact structural close program

Author: Jared Wilder. First public timestamp: 2026-09-11. Latest structural court: 2026-09-14.

`C(13,6,3)` is the least number of 6-element blocks on 13 points that cover every triple. The current bound is

```text
20 <= C(13,6,3) <= 21
```

and the exact value remains open. This repository records the mathematics extracted by the close campaign: exact local covering values, degree/pair constraints, optimal-link structure, route obstructions, and the current rooted Pattern-A reduction. A route that does not close the parent is retained when it creates a theorem, a falsifier, an obstruction, or a sharper search coordinate.

## Current frontier — rooted Pattern A

The latest forensic/KBK pass is here:

- [`research/2026-09-14-rooted-pattern-A-kbk.md`](research/2026-09-14-rooted-pattern-A-kbk.md)

The key new coordinate is this. In Pattern A the unique high point `h` has degree 12 and every other point has degree 9 with `r_hy=5`. Hence the link at every ordinary point is an optimal 9-block `C(12,5,2)` cover rooted at a degree-5 point.

The supplied optimal-link catalogue contains 107 pairwise nonisomorphic covers: 54 max-degree-5 classes and 53 max-degree-4 classes. Pattern A can use only the 54 max-degree-5 classes. Rooting those at degree-5 point orbits gives 56 rooted types, and a first exact residual court eliminates 2 of them.

Let the eight blocks avoiding `h` be indexed by `[8]`. Each ordinary point `y` lies in exactly four of them, giving a 4-set `S_y subset [8]`. For ordinary points `y,z`,

```text
a_yz = r_yz - lambda_hyz = |S_y intersect S_z|.
```

The rooted catalogue gives `a_yz <= 3`, so the twelve `S_y` are distinct. Therefore the Pattern-A residual is exactly a

> **simple 4-uniform, 6-regular hypergraph on 8 vertices with 12 edges.**

This dual formulation replaces the older 12-point generation from 924 candidate 6-blocks. It also yields immediate KBK: an `S_y` has only one disjoint 4-set, its complement, so any rooted type demanding two zero-intersection neighbours is impossible.

The next exact attack is rooted two-anchor compatibility in this 8-vertex Johnson geometry.

## Important correction from the catalogue audit

An intermediate campaign statement claimed every pair multiplicity in every optimal link was at most 4. Direct audit of the supplied 107-link catalogue finds three classes with pair multiplicity 5, so that blanket statement is retracted.

The actual completion/signature code retained the multiplicity-5 bin; the defect was theorem bookkeeping, not a silent exclusion from those models. The corrected Pattern-A-specific residual statement `a_yz<=3` is stronger for the live route and is recorded in the rooted KBK note.

## The structural strengthening

The local covering value

```text
C(12,5,2) = 9
```

was established by exhaustive search. This raises every point degree in a hypothetical 20-block `C(13,6,3)` cover to at least 9. Since the total point-degree sum is

```text
6 * 20 = 120,
```

only three degree multisets are possible:

```text
(12, 9^12)
(11, 10, 9^11)
(10, 10, 10, 9^10)
```

Thus at least ten points have degree exactly 9. Every pair lies in at least 3 blocks.

The same arithmetic re-derives `C(13,6,3)>=20` from `13*9<=6b`.

## Optimal-link catalogue state

The supplied 107 classes have degree-profile split

```text
53 : 4^9 3^3
46 : 5 4^7 3^4
 6 : 5^2 4^5 3^5
 2 : 5^3 4^3 3^6
```

Independent incidence-graph checking confirms the 107 supplied objects are valid and mutually nonisomorphic. Conditional on catalogue completeness, their automorphism-weighted labelled mass is

```text
max-degree-4 family :  7,384,608,000
max-degree-5 family :  6,147,187,200
all 107 classes      : 13,531,795,200
```

**Completeness of the 107-class catalogue remains a separate authority debt** and should be independently replayed before a catalogue-dependent global UNSAT is promoted to a proof.

## Earlier exact computation and calibration

The bitmask search infrastructure was calibrated in both directions on multiple covering numbers. Selected exact values include:

| value | result |
|---|---|
| `C(7,3,2)` | 7 |
| `C(8,3,2)` | 11 |
| `C(9,3,2)` | 12 |
| `C(10,4,2)` | 9 |
| `C(11,5,2)` | 7 |
| **`C(12,5,2)`** | **9** |
| `C(13,4,2)` | 13 |
| `C(8,4,3)` | 14 |
| `C(9,4,3)` | 25 |
| `C(10,4,3)` | 30 |
| `C(13,6,3)` | verified 21-block upper-bound witnesses |

The original `C(12,5,2)>=9` exhaustive run used 98,147,285 nodes and 289 seconds; the feasible side was also explicitly witnessed. A separate unrestricted belt-and-braces run did not terminate and is recorded only as an unfinished cross-check, not as additional proof.

## What the large global searches taught us

Six degree-pinned 20-cover solver branches all reached timeout/UNKNOWN rather than SAT or UNSAT. Prescribed-symmetry searches proved nonexistence only under the tested symmetry groups. Local search repeatedly reached 284/286 triples but never 286/286. None of those outcomes is promoted to global nonexistence.

Their value is diagnostic: the raw global model has weak relaxation and enormous branching. The campaign therefore moved from global solving to local-link classification, then from raw residual generation to the rooted 8-vertex dual coordinate above.

The post-transcript residual-generation receipt itself reached class counts

```text
1, 7, 55, 1098, 22718, 243059
```

through levels 1--6, confirming that continuing that old canonical-generation route would spend computation on the wrong coordinate. That explosion is KBK: it motivates the dual reduction rather than more wall-clock time.

## Existing structural packet

Earlier sources and exact scripts remain under:

- [`CURRENT-STRUCTURAL-PACKET-2026-09-13.md`](CURRENT-STRUCTURAL-PACKET-2026-09-13.md)
- [`LOCAL-LINK-DEGREE-8-9-ELIMINATION.md`](LOCAL-LINK-DEGREE-8-9-ELIMINATION.md)
- [`research/current-structural-packet/`](research/current-structural-packet/)

## Verification philosophy

Every status is typed:

- exact proof / arithmetic identity;
- independently replayed finite computation;
- catalogue-dependent consequence;
- solver UNKNOWN / diagnostic only;
- retracted statement.

A parent problem remaining open does not erase the theorems produced by the campaign, and a killed route is retained when it sharpens the next exact attack.

## License

Apache-2.0.
