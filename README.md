# `C(13,6,3)` — structure of a hypothetical 20-cover

`C(13,6,3)` is the minimum number of 6-subsets of a 13-point set needed to cover every triple. The current interval is

\[
\boxed{20\le C(13,6,3)\le21}.
\]

This repository reduces the unresolved 20-block case to three degree patterns and gives a complete elimination of the first one.

## Degree-pattern reduction

The local covering value

\[
C(12,5,2)=9
\]

forces every point of a hypothetical 20-block cover to have degree at least 9. Since the total degree sum is `20×6=120`, only three point-degree multisets are possible:

```text
A: (12,9^12)
B: (11,10,9^11)
C: (10,10,10,9^10)
```

Every pair must occur in at least three blocks.

At a degree-9 point, its link is an optimal 9-block `C(12,5,2)` cover. If `#(r=j)` counts link vertices of degree `j`, then

\[
\#(r=3)=\#(r=5)+3,
\qquad
\#(r=5)\le4.
\]

## Pattern A eliminated

Let `h` be the degree-12 point. The eight blocks avoiding `h` induce a 4-uniform, 6-regular residual object on eight dual vertices.

An exhaustive C++ classification gives

```text
3,268,358 search nodes
6,084 labelled locally admissible residuals
22 residual isomorphism classes
```

A separate local-completion verifier then eliminates all

```text
22 / 22
```

classes by star-gluing contradiction. The verifier constructs the five `h`-containing blocks required at each ordinary point directly from the residual rather than selecting them from the historical link catalogue.

See:

- [`research/2026-09-14-pattern-A-elimination.md`](research/2026-09-14-pattern-A-elimination.md)
- [`research/pattern-A-elimination/`](research/pattern-A-elimination/)

## Pattern B

Let `H` have degree 11, `J` degree 10, and set `x=r_{HJ}`. Triple-coverage arithmetic gives

\[
3\le x\le9.
\]

The 20 blocks split as

```text
contain H,J   : x
H only        : 11-x
J only        : 10-x
neither       : x-1
```

For each ordinary degree-9 point `y`, define

```text
a_y = r_yH
b_y = r_yJ
c_y = λ_yHJ.
```

Then

\[
\sum a_y=55-x,
\qquad
\sum b_y=50-x,
\qquad
\sum c_y=4x.
\]

These equations are the finite coordinate system for the remaining Pattern-B search.

## Pattern C

Let the three degree-10 points be `A,B,C`, with pair multiplicities `x,y,z`, triple multiplicity `t`, and `S=x+y+z`.

For the counts `n_j` of blocks containing exactly `j` of the three high-degree points,

\[
n_3=t,
\]
\[
n_2=S-3t,
\]
\[
n_1=30-2S+3t,
\]
\[
n_0=S-t-10.
\]

Hence

\[
S\ge3t,
\qquad
S\ge t+10,
\qquad
2S\le30+3t,
\qquad
t\ge1.
\]

The ordinary degree-9 links supply additional conservation equations coupling their marked high vertices.

## Optimal-link catalogue

The historical computation produced 107 pairwise nonisomorphic optimal `C(12,5,2)` links, distributed by point-degree profile as

```text
53 : 4^9 3^3
46 : 5 4^7 3^4
 6 : 5^2 4^5 3^5
 2 : 5^3 4^3 3^6
```

Independent incidence-graph checks confirm that the supplied 107 objects are valid and mutually nonisomorphic. A previously stated pair-multiplicity-at-most-4 property is false for three of these links; the computational data itself retained the multiplicity-5 cases.

## Remaining problem

Pattern A is eliminated. Patterns B and C remain. Resolving both, together with the known 21-block construction, would determine `C(13,6,3)` exactly.

Global solver timeouts, symmetry-restricted searches, and local near-covers are not used as evidence for nonexistence.

Author: Jared Wilder. License: Apache-2.0.
