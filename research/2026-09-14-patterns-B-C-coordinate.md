# C(13,6,3) — exact coordinates for the remaining degree patterns B and C

**Author:** Jared Wilder  
**Date:** 2026-09-14  
**Status:** elementary structural reductions for the two remaining hypothetical 20-cover degree patterns.

After the exhaustive Pattern-A court, a 20-block cover can survive only through

```text
B = (11,10,9^11)
C = (10,10,10,9^10).
```

This note freezes the next exact coordinates before any new search is launched.

## Universal pair-row identity

For every point `v` of global degree `d(v)`, if `r_vw` denotes the number of blocks containing the pair `{v,w}`, then

\[
\sum_{w\ne v} r_{vw}=5d(v),
\]

because each 6-block through `v` contributes five pair incidences.

Every pair occurs in at least three blocks. At a degree-9 point, its link is an optimal 9-block `C(12,5,2)` cover, so every pair incident with that degree-9 point has multiplicity at most five.

Hence every degree-9 row consists entirely of values in `{3,4,5}` and has sum 45. If `a_j` counts entries equal to `j`, then

\[
a_3+a_4+a_5=12,
\qquad
3a_3+4a_4+5a_5=45,
\]

so exactly

\[
\boxed{a_3=a_5+3},\qquad 0\le a_5\le4.
\]

This remains the local row law for every ordinary point in B and C.

---

# Pattern B: `(11,10,9^11)`

Let `H` have degree 11, let `J` have degree 10, and let the remaining eleven points have degree 9. Put

\[
x=r_{HJ}.
\]

## 1. Exact four-category block counts

Every global block lies in exactly one of four classes according to whether it contains `H` and/or `J`:

```text
contains H and J : x
contains H only  : 11-x
contains J only  : 10-x
contains neither : x-1
```

The last identity follows because there are 20 blocks in total.

The pair floor initially gives `x>=3`.

## 2. The exceptional pair cannot have multiplicity 10

Assume `x=10`. Since `J` has degree 10, every block through `J` also contains `H`.

Fix an ordinary point `y`. To cover all triples `{J,y,z}`, the blocks through the pair `{J,y}` must account for the eleven possible third points `z`. The point `H` is automatically present in every such block. A 6-block containing `J,y,H` has only three further places, so each such block can cover at most three of the remaining ten possible third points.

Therefore

\[
r_{Jy}\ge \left\lceil\frac{10}{3}\right\rceil=4.
\]

There are eleven ordinary points, hence

\[
\sum_y r_{Jy}\ge44.
\]

But the pair-row identity at `J` gives

\[
50=5d(J)=r_{JH}+\sum_y r_{Jy}=10+\sum_y r_{Jy},
\]

so the same sum is exactly 40, a contradiction.

Thus

\[
\boxed{3\le x\le9.}
\]

## 3. Marked-link conservation laws

For an ordinary degree-9 point `y`, define

\[
a_y=r_{yH},\qquad b_y=r_{yJ},\qquad c_y=\lambda_{yHJ}.
\]

Inside the optimal link at `y`, these are respectively the degrees of the two marked exceptional vertices and their pair multiplicity.

Global double counting gives

\[
\boxed{\sum_y a_y=55-x},
\]

\[
\boxed{\sum_y b_y=50-x},
\]

and, because every block containing `H,J` contains four ordinary points,

\[
\boxed{\sum_y c_y=4x}.
\]

Equivalently each ordinary point has a four-category incidence row

\[
(c_y,\ a_y-c_y,\ b_y-c_y,\ 9-a_y-b_y+c_y),
\]

counting its blocks in the categories `(HJ, H-only, J-only, neither)`.

The column sums of those eleven rows are forced to be

\[
\boxed{(4x,\ 5(11-x),\ 5(10-x),\ 6(x-1))}.
\]

This is the correct finite skeleton for Pattern B. The next search should enumerate marked optimal-link rows subject to these exact conservation laws, then apply direct local-star gluing as in Pattern A.

---

# Pattern C: `(10,10,10,9^10)`

Let the three exceptional points be `A,B,C`, all of degree 10. Write

\[
x=r_{AB},\qquad y=r_{AC},\qquad z=r_{BC},
\]

and let

\[
t=\lambda_{ABC}
\]

be the number of blocks containing all three exceptional points.

## 1. No exceptional pair has multiplicity 10

Suppose, for example, `r_AB=10`. Since `B` has degree 10, every block through `B` contains `A`.

For each ordinary point `u`, every block through `{B,u}` therefore already contains `A`. As above, it has only three remaining positions with which to cover the ten third points other than `A,B,u`. Consequently

\[
r_{Bu}\ge4
\]

for all ten ordinary `u`, so their total contribution is at least 40.

However

\[
50=5d(B)=r_{BA}+r_{BC}+\sum_u r_{Bu}
\]

and `r_BA=10`, while the pair floor gives `r_BC>=3`. Thus

\[
\sum_u r_{Bu}\le37,
\]

a contradiction.

Hence for every exceptional pair

\[
\boxed{3\le x,y,z\le9.}
\]

## 2. Exact block-count identities by number of exceptional vertices

Let `n_j` be the number of global blocks containing exactly `j` of `{A,B,C}`. Put

\[
S=x+y+z.
\]

Counting exceptional-point incidences, exceptional-pair incidences, and the triple gives

\[
n_3=t,
\]

\[
\boxed{n_2=S-3t},
\]

\[
\boxed{n_1=30-2S+3t},
\]

\[
\boxed{n_0=S-t-10}.
\]

Therefore every Pattern-C candidate must satisfy the elementary nonnegativity gates

\[
\boxed{S\ge3t},
\qquad
\boxed{S\ge t+10},
\qquad
\boxed{2S\le30+3t},
\qquad
\boxed{t\ge1}.
\]

Together with `3<=x,y,z<=9`, these are the first global exceptional-skeleton constraints.

## 3. Three-marked-link conservation laws

For each ordinary degree-9 point `u`, its optimal link contains three distinguished vertices `A,B,C`. Define local degrees

\[
a_u=r_{uA},\quad b_u=r_{uB},\quad c_u=r_{uC},
\]

pair multiplicities

\[
p_u=\lambda_{uAB},\quad q_u=\lambda_{uAC},\quad r_u=\lambda_{uBC},
\]

and the local triple multiplicity

\[
s_u=\lambda_{uABC}.
\]

The global conservation equations are

\[
\boxed{\sum_u a_u=50-x-y},
\]

\[
\boxed{\sum_u b_u=50-x-z},
\]

\[
\boxed{\sum_u c_u=50-y-z},
\]

and, because an `AB` block has four non-`A,B` positions but an `ABC` block uses one of them on `C`,

\[
\boxed{\sum_u p_u=4x-t},
\]

\[
\boxed{\sum_u q_u=4y-t},
\]

\[
\boxed{\sum_u r_u=4z-t}.
\]

Finally each block containing `A,B,C` contains exactly three ordinary points, giving

\[
\boxed{\sum_u s_u=3t}.
\]

This is the correct finite skeleton for Pattern C: ten optimal links with three marked exceptional vertices, coupled by seven exact conservation equations before any global block search.

## Close-program consequence

The next exact-close architecture is now fixed:

1. harden the Pattern-A finite elimination with a second duplicate-edge verifier;
2. enumerate the **marked-link skeletons** for Pattern B over `x=3,...,9` and kill/realize them by direct star gluing;
3. enumerate the **three-marked-link skeletons** for Pattern C over `(x,y,z,t)` satisfying the exact gates above and kill/realize them by the same first-principles gluing court;
4. only if a skeleton survives, reconstruct the complete 20-block object and verify all 286 triples independently.

No return to undifferentiated global SAT is required or justified by the current KBK state.
