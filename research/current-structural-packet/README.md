# Covering design C(13,6,3) — two 21-block witnesses and the strengthened target-20 structure

**Estate source:** MSL Pass-2/Pass-3 + final September-2 singular synthesis  
**Point set:** `{0,1,...,12}`  
**Status:** exact witnesses + necessary structure; **no 20-block UNSAT certificate is claimed**

A `(13,6,3)` covering is a family of 6-subsets of 13 points in which every 3-subset is contained in at least one block.

The recovered estate contains two independently validated 21-block coverings. Each was checked against all

\[
\binom{13}{3}=286
\]

triples, with zero missing triples.

The September-2 source audit also reported that the two incidence structures are non-isomorphic to one another and were separated from the repository benchmark used in that audit. That is **not** promoted here to a globally exhaustive novelty/classification claim; archive-wide isomorphism classification remains a separate task.

The strongest synthesis materially improves the original target-20 reduction: the old `r_x>=8` / 16-excess package is superseded by **`r_x>=9`, three exact global point-degree multisets, sharp multiplicity-3 pair lower bounds, local triple-excess laws, and a global singleton-triple budget**.

## Witness A — `run20_C13_6_3_cover21`

```text
{0,3,4,5,7,9}
{2,5,7,8,9,10}
{1,2,4,8,9,11}
{3,4,5,6,8,11}
{0,1,2,4,6,7}
{0,2,6,8,9,12}
{0,1,2,5,11,12}
{0,1,3,5,8,12}
{1,2,3,4,8,9}
{1,5,6,7,9,12}
{2,6,9,10,11,12}
{0,1,3,9,10,11}
{3,4,6,9,10,12}
{2,3,7,10,11,12}
{0,2,3,5,6,10}
{5,7,8,9,10,11}
{0,4,7,8,10,12}
{1,3,6,7,8,10}
{0,4,8,10,11,12}
{1,2,4,5,10,12}
{0,1,4,6,7,11}
```

Independent estate validation:

```text
triples_total   = 286
triples_covered = 286
missing         = 0
PASS
```

## Witness B — `run23b_C13_6_3_cover21`

```text
{0,1,2,5,6,12}
{0,1,3,7,8,11}
{0,1,4,7,9,10}
{0,1,4,8,10,11}
{0,2,3,4,8,10}
{0,2,3,7,9,12}
{0,2,4,8,11,12}
{0,3,4,5,6,7}
{0,4,5,6,10,12}
{0,5,6,8,9,11}
{1,2,3,4,6,8}
{1,2,3,5,10,12}
{1,2,6,7,9,11}
{1,3,5,8,9,12}
{1,4,5,7,11,12}
{1,6,7,8,10,12}
{2,3,5,7,10,11}
{2,4,5,7,8,9}
{2,5,6,8,9,10}
{3,4,6,9,11,12}
{3,6,9,10,11,12}
```

Independent estate validation:

```text
triples_total   = 286
triples_covered = 286
missing         = 0
PASS
```

# Necessary structure of any hypothetical 20-block cover

## 1. Every point has degree at least 9

Fix a point `x`. Every triple `{x,y,z}` must lie in a block through `x`. Delete `x` from all blocks containing it. The resulting `r_x` five-subsets of the other 12 points cover every pair, hence form a `C(12,5,2)` cover.

Using the exact value

\[
C(12,5,2)=9,
\]

we obtain

\[
\boxed{r_x\ge9\quad\text{for every }x.}
\]

This supersedes the older pair-counting lower bound `r_x>=8`.

## 2. Only three global point-degree multisets survive

Twenty 6-blocks contain exactly

\[
\sum_x r_x=20\cdot6=120
\]

point incidences. The compulsory baseline is `13*9=117`, leaving only three excess degree units. Therefore the point-degree multiset must be exactly one of

\[
\boxed{(12,9^{12})},
\]

\[
\boxed{(11,10,9^{11})},
\]

or

\[
\boxed{(10,10,10,9^{10})}.
\]

In particular, every hypothetical 20-cover has at least **10 degree-9 points**, and each degree-9 point induces an optimal nine-block `C(12,5,2)` neighborhood.

## 3. Pair multiplicity and excess identities

Fix a pair `{x,y}`. There are 11 triples containing it, while a 6-block containing the pair covers only four choices of the third point. Thus

\[
\boxed{r_{xy}\ge3.}
\]

Globally,

\[
\sum_{\{x,y\}}r_{xy}=20\binom62=300,
\]

so

\[
\boxed{\sum_{\{x,y\}}(r_{xy}-3)=300-3\binom{13}{2}=66.}
\]

For an individual point,

\[
\boxed{\sum_{y\ne x}(r_{xy}-3)=5r_x-36,}
\]

which is `9,14,19,24` when `r_x=9,10,11,12`, respectively.

## 4. Sharp lower bounds on multiplicity-3 pairs

Write

\[
e_{xy}=r_{xy}-3
\]

and let

\[
m_3=\#\{\{x,y\}:r_{xy}=3\}
\]

be the number of zero-excess pairs.

### Pattern `(12,9^12)`

The degree-12 point has row excess 24. The twelve degree-9 vertices have total row excess `12*9=108`. Hence low-low excess is

\[
(108-24)/2=42.
\]

There are 66 low-low pairs. Since each positive-excess edge consumes at least one excess unit, at most 42 can have positive excess. Therefore

\[
\boxed{m_3\ge24.}
\]

### Pattern `(11,10,9^11)`

Let `A,B` be the degree-11 and degree-10 points and put `t=e_{AB}`. Since `r_AB<=10`, `0<=t<=7`.

The eleven degree-9 points carry total row excess 99. High-low excess is

\[
(19-t)+(14-t)=33-2t,
\]

so low-low excess is `33+t`, forcing at least `22-t` zero-excess low-low edges.

The degree-10 vertex has 11 low neighbors but only `14-t` high-low excess units, forcing at least `max(0,t-3)` zero-excess high-low edges. If `t=0`, the high-high edge itself is also zero-excess. Checking `0<=t<=7` gives

\[
\boxed{m_3\ge19.}
\]

### Pattern `(10,10,10,9^10)`

Let `T` be total excess on the three high-high edges. Low-low excess equals `24+T`, so at least `21-T` low-low edges have zero excess.

If `s_i` is the high-high excess incident to high vertex `i`, then its high-low excess is `14-s_i` over 10 edges, forcing at least `max(0,s_i-4)` zero high-low edges. Since `sum_i s_i=2T`,

\[
\sum_i\max(0,s_i-4)\ge\max(0,2T-12).
\]

Hence

\[
m_3\ge21-T+\max(0,2T-12)\ge15.
\]

Thus the three exact degree patterns force

\[
\boxed{m_3\ge24,\ 19,\ 15}
\]

respectively. This supersedes the earlier weaker public bounds `18,17,15`.

## 5. Degree-9 points force `3 <= r_xy <= 8`

Let `x` have degree 9 and fix `y!=x`. Put `t=r_xy`.

The nine residual 5-blocks on the other 12 points cover every pair. Of these nine blocks:

- `t` contain `y`; after removing `y`, each contributes at most `C(4,2)=6` pair incidences among the other 11 points;
- `9-t` avoid `y`; each contributes `C(5,2)=10` pair incidences among those 11 points.

Thus total pair-incidence capacity on the 11 points is

\[
6t+10(9-t)=90-4t.
\]

It must cover all `C(11,2)=55` pairs. Hence `90-4t>=55`, so `t<=8`. Together with the universal lower bound,

\[
\boxed{r_x=9\Longrightarrow3\le r_{xy}\le8\quad\forall y\ne x.}
\]

No pair incident to a degree-9 point can have multiplicity 9 or larger.

## 6. Exact local triple-excess law

Let `lambda_xyz` denote the number of blocks containing the triple `{x,y,z}`. For fixed `x`, the blocks through `x` contribute

\[
r_x\binom52=10r_x
\]

incidences to triples containing `x`. There are `C(12,2)=66` such triples. Therefore

\[
\boxed{
\sum_{\{y,z\}\subset V\setminus\{x\}}(\lambda_{xyz}-1)=10r_x-66.
}
\]

Hence:

| `r_x` | local triple excess | singleton triples through `x`, at least |
|---:|---:|---:|
| 9 | 24 | 42 |
| 10 | 34 | 32 |
| 11 | 44 | 22 |
| 12 | 54 | 12 |

In particular every degree-9 point lies on at least

\[
\boxed{42}
\]

triples covered exactly once. This is a local clause family, not merely a global average.

## 7. Exact geometry over a multiplicity-3 pair

Take `{x,y}` with `r_xy=3`. Delete `x,y` from the three blocks containing the pair. We obtain three 4-subsets of the remaining 11 points whose union must be all 11 points.

Those sets carry 12 incidences on 11 points. Hence exactly one point occurs twice and the other ten occur once. Equivalently:

- exactly one pair of the residual 4-sets intersects in one point;
- the other two pairwise intersections are empty;
- among the eleven triples `{x,y,z}`, exactly ten have multiplicity 1 and exactly one has multiplicity 2.

Thus every multiplicity-3 pair has a **unique doubled extension**:

\[
\boxed{r_{xy}=3\Longrightarrow\#\{z:\lambda_{xyz}=2\}=1,\quad\#\{z:\lambda_{xyz}=1\}=10.}
\]

This is stronger and more solver-useful than merely saying “one residual point repeats.”

## 8. Global triple budget

Twenty blocks contribute

\[
20\binom63=400
\]

triple incidences to the 286 triples of the 13-point ground set. Therefore

\[
\boxed{\sum_T(\lambda_T-1)=400-286=114.}
\]

Every nonsingleton triple consumes at least one unit of this excess, so at most 114 triples can have multiplicity at least two. Consequently

\[
\boxed{\#\{T:\lambda_T=1\}\ge286-114=172.}
\]

Combined with the multiplicity-3 pair law, the three degree patterns force at least `8,7,5` multiplicity-2 triples, respectively.

## Historical Lean structure receipt

An earlier formal artifact `Cover20Degree.lean` was independently recorded as `VERIFIED` (exit 0, 3.6 s) for the older pair-count / point-degree necessary conditions. That formal result is historically valid but is **superseded in strength** by the degree-9 theorem above, which uses the exact value `C(12,5,2)=9` and is not represented here as kernel-certified unless separately compiled.

# Correct exact-close program

The public frontier represented by this archive remains

\[
20\le C(13,6,3)\le21.
\]

A certified target-20 impossibility proof immediately closes the value at 21. The strengthened search should therefore:

1. anchor a degree-9 point;
2. enumerate/classify optimal nine-block `C(12,5,2)` neighborhoods up to isomorphism;
3. lift those nine local blocks to the nine 6-blocks containing the anchor;
4. choose only eleven further blocks not containing it;
5. branch immediately on the three exact point-degree multisets;
6. enforce pair multiplicity and every point-excess row sum;
7. enforce `m_3>=24,19,15` according to the degree pattern;
8. enforce `3<=r_xy<=8` around every degree-9 point;
9. for each `r_xy=3`, enforce its unique doubled extension plus ten singleton extensions;
10. enforce the local triple-excess budget `10r_x-66`, including at least 42 singleton triples through every degree-9 point;
11. enforce global triple excess 114 and at least 172 singleton triples;
12. quotient by the automorphism group of the anchored optimal `C(12,5,2)` neighborhood;
13. emit a replayable UNSAT certificate or canonical-extension log;
14. independently replay with a second checker/solver.

The archive's earlier raw MILP attempt did **not** prove infeasibility. Search failure is not a certificate. Until target 20 is actually eliminated,

\[
\boxed{C(13,6,3)=21\text{ is not claimed}.}
\]

## Reproducibility

The two block lists above are sufficient for independent checking of the upper bound: enumerate every 3-subset of `{0,...,12}` and verify that at least one displayed block contains it. No appeal to the original search procedure is needed.
