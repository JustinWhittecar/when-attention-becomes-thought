# Diagonal Argument

**Summary**: A proof technique introduced by Georg Cantor in 1891, used to show that certain sets cannot be enumerated -- foundational to the proofs of uncountability, incompleteness, and undecidability.

**Sources**: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf

**Last updated**: 2026-05-11

---

## The technique

The diagonal argument works by assuming a complete listing exists and then constructing an element that cannot be in the listing. The construction proceeds by "going down the diagonal" of the assumed enumeration and systematically differing from each listed element at the corresponding position. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## Cantor's original formulation (1891)

In [[cantor-1891]], Cantor considers infinite sequences over two characters *m* and *w*. Suppose all such sequences can be listed as E1, E2, ..., where Eμ = (aμ,1, aμ,2, ...). Define a new sequence E0 = (b1, b2, ...) by setting bv to be different from av,v (if av,v = m, set bv = w; and vice versa). Then E0 differs from every Eμ at position μ, so it cannot appear in the list. Therefore the set of all such sequences is [[uncountability|uncountable]]. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## Appearances across the wiki

The diagonal argument is the structural backbone of several of the wiki's central results:

### Russell's paradox (1902)
[[russells-paradox]] can be understood as a diagonal argument applied to the set-membership relation. Define a set R that contains exactly those sets that do not contain themselves. Does R contain itself? The self-referential contradiction mirrors Cantor's construction of an element that escapes any proposed listing. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf; see also [[russell-1902]])

### Godel's incompleteness theorems (1931)
[[godel-1931]] constructs a sentence that "says" it is unprovable within a [[formal-system]]. The construction uses [[godel-numbering]] to encode formulas as numbers, then applies a diagonalization step to produce a self-referential statement. The result: any consistent formal system rich enough to express arithmetic contains true statements it cannot prove ([[incompleteness]]). (see [[godel-1931]])

### Turing's undecidability proof (1936)
[[turing-1936]] proves the [[entscheidungsproblem]] unsolvable by direct diagonalization. Assume a [[turing-machine]] *H* can decide whether any machine halts. Construct a machine *D* that, given machine *M*, runs *H* on (M, M) and does the opposite: if *H* says *M* halts on input *M*, then *D* loops; if *H* says *M* loops, *D* halts. Running *D* on itself yields a contradiction. The structure is Cantor's argument applied to machine descriptions rather than infinite sequences. (see [[turing-1936]])

## Why it matters

The diagonal argument establishes that there are inherent limits to enumeration, formal proof, and mechanical computation. It is the thread connecting [[cantor-1891]]'s set theory to [[godel-1931]]'s metamathematics to [[turing-1936]]'s theory of computation -- the three results that collectively define the boundaries of [[formal-system]]s and [[computability]].

## Related pages

- [[cantor-1891]]
- [[uncountability]]
- [[russells-paradox]]
- [[russell-1902]]
- [[godel-1931]]
- [[godel-numbering]]
- [[incompleteness]]
- [[turing-1936]]
- [[entscheidungsproblem]]
- [[computability]]
- [[formal-system]]
