# C(13,6,3) — current target-20 structural packet

**Author:** Jared Wilder  
**Canonical focused home:** `jaredwilder/covering-13-6-3`  
**Status:** exact 21-block witnesses + necessary structure; **no 20-block UNSAT certificate is claimed**

The current exact frontier is

\[
20\le C(13,6,3)\le21.
\]

This file promotes the stronger September structural packet that had been living under `combinatorial-records/covering-designs/C13-6-3/` into the focused subject repository.

## Two independently validated 21-block covers

### Witness A

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

### Witness B

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

Each covers all `C(13,3)=286` triples. The source audit reported the two incidence structures as non-isomorphic to one another; that observation is not promoted here into an exhaustive global classification claim.

# Necessary structure of any hypothetical 20-cover

## 1. Point degrees

Fix a point `x`. Deleting `x` from the blocks through `x` gives a `C(12,5,2)` cover. The exact finite value

\[
C(12,5,2)=9
\]

therefore gives

\[
\boxed{r_x\ge9\quad\forall x.}
\]

Since

\[
\sum_x r_x=20\cdot6=120,
\]

only three point-degree multisets are possible:

\[
\boxed{(12,9^{12})},\qquad
\boxed{(11,10,9^{11})},\qquad
\boxed{(10,10,10,9^{10})}.
\]

Thus at least ten points have degree exactly 9.

## 2. Pair multiplicity and excess

For every pair `{x,y}`,

\[
\boxed{r_{xy}\ge3}.
\]

Globally,

\[
\sum_{\{x,y\}}r_{xy}=20\binom62=300,
\]

so

\[
\boxed{\sum_{\{x,y\}}(r_{xy}-3)=66.}
\]

For each point,

\[
\boxed{\sum_{y\ne x}(r_{xy}-3)=5r_x-36.}
\]

The row excesses for point degrees `9,10,11,12` are `9,14,19,24`.

## 3. Sharp multiplicity-3 pair counts

Let

\[
e_{xy}=r_{xy}-3,
\qquad
m_3=\#\{\{x,y\}:r_{xy}=3\}.
\]

The three point-degree patterns force respectively

\[
\boxed{m_3\ge24,\quad19,\quad15.}
\]

These supersede earlier weaker public bounds.

## 4. Degree-9 points force an upper pair-multiplicity bound

If `r_x=9` and `t=r_{xy}`, then after deleting `x` from the nine incident blocks, the residual five-subsets cover all pairs on 12 points. Looking only at pairs among the 11 points other than `y`, the incidence capacity is

\[
6t+10(9-t)=90-4t.
\]

It must cover all

\[
\binom{11}{2}=55
\]

pairs. Hence `t<=8`. Together with the universal lower bound,

\[
\boxed{r_x=9\Longrightarrow3\le r_{xy}\le8\quad\forall y\ne x.}
\]

## 5. Exact local triple-excess law

Let `lambda_xyz` be the number of blocks containing `{x,y,z}`. For fixed `x`,

\[
\boxed{
\sum_{\{y,z\}\subset V\setminus\{x\}}(\lambda_{xyz}-1)=10r_x-66.
}
\]

Therefore a point of degree `9,10,11,12` lies on at least `42,32,22,12` singleton triples respectively. In particular every degree-9 point lies on at least

\[
\boxed{42}
\]

triples of multiplicity exactly one.

## 6. Exact geometry over a multiplicity-3 pair

If `r_xy=3`, delete `x,y` from the three blocks containing the pair. The resulting three 4-subsets cover all 11 remaining points and carry 12 incidences. Hence exactly one remaining point occurs twice and the other ten occur once.

Equivalently,

\[
\boxed{r_{xy}=3\Longrightarrow
\#\{z:\lambda_{xyz}=2\}=1,
\quad
\#\{z:\lambda_{xyz}=1\}=10.}
\]

So every multiplicity-3 pair has a unique doubled extension.

## 7. Global triple budget

Twenty blocks contribute

\[
20\binom63=400
\]

triple incidences to 286 triples. Therefore

\[
\boxed{\sum_T(\lambda_T-1)=114.}
\]

At most 114 triples can be nonsingletons, so

\[
\boxed{\#\{T:\lambda_T=1\}\ge172.}
\]

# New human local-link eliminations

The companion file `LOCAL-LINK-DEGREE-8-9-ELIMINATION.md` proves by hand that a 9-block `C(12,5,2)` cover cannot contain a point of local degree 8 or 9.

The corresponding local degree-6 and degree-7 CP-SAT runs reached their time limits with status `UNKNOWN`. Therefore the desired universal local cap `<=5` remains **unproved**, and any Pattern-A decomposition that assumes it is conditional.

# Exact-close program

A correct target-20 close program should now exploit the structure rather than rerunning a generic 20-block solver:

1. anchor a degree-9 point;
2. classify optimal nine-block `C(12,5,2)` links up to isomorphism;
3. lift those nine blocks through the anchor and choose eleven blocks avoiding it;
4. branch on the three exact degree multisets;
5. enforce pair-excess row sums and `m_3>=24,19,15`;
6. enforce `3<=r_xy<=8` around every degree-9 point;
7. enforce the unique doubled extension for every multiplicity-3 pair;
8. enforce local triple-excess budgets and the global excess 114 / singleton floor 172;
9. quotient by the anchored link automorphism group;
10. emit a replayable UNSAT certificate or canonical-augmentation log and replay it independently.

Until such a target-20 impossibility proof exists,

\[
\boxed{C(13,6,3)=21\text{ is not claimed}.}
\]
