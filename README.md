# C(13,6,3): exact structural close program

Author: Jared Wilder. First public timestamp: 2026-09-11. Latest structural court: 2026-09-14.

`C(13,6,3)` is the least number of 6-element blocks on 13 points that cover every triple. The current bound is

```text
20 <= C(13,6,3) <= 21
```

The exact close program is now reduced to the three forced degree patterns of a hypothetical 20-cover. Pattern A has undergone a complete residual/gluing court; Patterns B and C now have exact marked-link coordinates ready for the next finite attack. The repository retains every theorem, correction, obstruction and coordinate change generated on the way.

## Current frontier

The live 2026-09-14 layer is:

- [`research/2026-09-14-pattern-A-elimination.md`](research/2026-09-14-pattern-A-elimination.md) — exhaustive Pattern-A residual/gluing court
- [`research/pattern-A-elimination/`](research/pattern-A-elimination/) — executable classifier, 22 representatives, catalogue-free gluing verifier and kill receipt
- [`research/2026-09-14-patterns-B-C-coordinate.md`](research/2026-09-14-patterns-B-C-coordinate.md) — exact coordinates for the only two remaining degree patterns
- [`research/2026-09-14-rooted-pattern-A-kbk.md`](research/2026-09-14-rooted-pattern-A-kbk.md) — forensic link-catalogue audit and rooted reduction

### Pattern A: `(12,9^12)`

Let `h` be the degree-12 point. The eight blocks avoiding `h` give every ordinary point a 4-subset of `[8]`. The corrected rooted local geometry reduces the residual to a 4-uniform, 6-regular object on eight dual vertices.

The new C++ classifier exhaustively finds

```text
3,268,358 search nodes
6,084 labeled locally admissible residuals
22 residual isomorphism classes
```

and the independent direct local-completion court kills all

```text
22 / 22
```

by pairwise star-gluing contradiction. The gluing verifier does not select local completions from the 107-link catalogue: once a residual is fixed, it directly enumerates the five `h`-containing blocks needed at every ordinary point.

The remaining authority-hardening item for this pattern is a second solver-independent verifier for the duplicate-dual-edge prohibition. The normalized duplicate case already reduces to five exact degree-placement cases, all MILP-UNSAT. The close program treats this as a redundancy/certificate task, not a return to global SAT.

### Pattern B: `(11,10,9^11)`

Writing `H` for the degree-11 point, `J` for the degree-10 point and `x=r_HJ`, elementary triple-coverage arithmetic now gives

```text
3 <= x <= 9.
```

The 20 blocks split exactly into

```text
HJ        : x
H only    : 11-x
J only    : 10-x
neither   : x-1.
```

For every ordinary degree-9 point `y`, the marked optimal link supplies

```text
a_y = r_yH
b_y = r_yJ
c_y = lambda_yHJ
```

with exact global conservation laws

```text
sum a_y = 55-x
sum b_y = 50-x
sum c_y = 4x.
```

This is the next finite skeleton. The intended attack is marked-link enumeration followed by the same direct star-gluing court that eliminated A.

### Pattern C: `(10,10,10,9^10)`

Let the three high points be `A,B,C`, with pair multiplicities `x,y,z` and triple multiplicity `t`. Every high-high pair satisfies

```text
3 <= x,y,z <= 9.
```

If `S=x+y+z` and `n_j` counts blocks containing exactly `j` high points, then

```text
n3 = t
n2 = S-3t
n1 = 30-2S+3t
n0 = S-t-10.
```

Thus `S>=3t`, `S>=t+10`, `2S<=30+3t`, and `t>=1` are exact first gates.

Every ordinary point has an optimal link with three marked high vertices. Seven conservation equations couple their local marked degrees, pair multiplicities and triple multiplicity. This is now the correct finite skeleton for Pattern C.

## Structural foundation

The local covering value

```text
C(12,5,2) = 9
```

was established by exhaustive search. Therefore every point of a hypothetical 20-block cover has degree at least 9. Since the total point-degree sum is `120`, only

```text
(12,9^12)
(11,10,9^11)
(10,10,10,9^10)
```

are possible. Every pair lies in at least three blocks.

At every degree-9 point its link is an optimal 9-block `C(12,5,2)` covering. The exact row identity is

```text
#(r=3) = #(r=5) + 3,
#(r=5) <= 4.
```

## Optimal-link catalogue and correction

The campaign supplied 107 pairwise nonisomorphic optimal links:

```text
53 : 4^9 3^3
46 : 5 4^7 3^4
 6 : 5^2 4^5 3^5
 2 : 5^3 4^3 3^6
```

Independent incidence-graph checks confirm the supplied 107 objects are valid and mutually nonisomorphic. Conditional on completeness their labelled mass is `13,531,795,200`.

An intermediate campaign statement claiming every pair multiplicity in every optimal link was at most 4 was false: three supplied classes have pair multiplicity 5. That statement is retracted. The actual solver/signature code retained the multiplicity-5 bin, so the defect was theorem bookkeeping rather than a hidden exclusion.

Catalogue completeness remains an authority debt wherever a result depends on completeness. The current Pattern-A gluing verifier was deliberately made first-principles after the residual classification to reduce that dependency.

## Earlier computation and route KBK

Large global 20-cover solver branches timed out/returned UNKNOWN. Prescribed-symmetry searches proved only symmetry-restricted nonexistence. Local search reached 284/286 triples but not 286/286. None is global evidence.

The old Pattern-A 12-point residual generator grew through

```text
1, 7, 55, 1098, 22718, 243059
```

classes at levels 1--6. That explosion was not discarded: it supplied the KBK that led to the 8-vertex dual coordinate and the eventual 22-class court.

## Terminal standard

There are only two acceptable terminal outcomes:

- an explicit independently verified 20-cover, proving `C(13,6,3)=20`; or
- exhaustive elimination of Patterns A, B and C together with an independently verified 21-cover, proving `C(13,6,3)=21`.

No timeout, local optimum, symmetry-restricted UNSAT, incomplete catalogue, or weaker structural theorem substitutes for that terminal bit.

## License

Apache-2.0.
