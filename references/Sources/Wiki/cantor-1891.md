# Cantor -- Ueber eine elementare Frage der Mannigfaltigkeitslehre (1891)

**Summary**: Georg Cantor's 1891 paper introducing the diagonal argument, proving that for any set, the collection of all its infinite binary sequences has strictly greater cardinality -- establishing that there are different sizes of infinity and that the real numbers are uncountable.

**Sources**: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf

**Last updated**: 2026-05-11

---

## Context

The title translates to "On an elementary question of the theory of manifolds" (where "manifold" is Cantor's term for what we now call a "set"). The paper was published in the *Jahresbericht der Deutschen Mathematiker-Vereinigung*, 1:75-78, 1891. The source in this wiki is an English translation by Peter P. Jones (2019) using Google Translate and DeepL with manual edits. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

Cantor had already proved the uncountability of the reals in 1874 using a nested-intervals argument. This 1891 paper provides "a much simpler proof of that theorem, which is independent of the consideration of irrational numbers." (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## The diagonal argument

Cantor considers a collection *M* of elements *E*, where each element is an infinite sequence of two characters *m* and *w* (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf):

> E = (x1, x2, ..., xv, ...), where each coordinate is either *m* or *w*.

He then claims that *M* "does not have the power of the series 1, 2, 3, ..., v, ...." -- that is, *M* is uncountable.

**The proof**: Suppose we could list all elements of *M* as E1, E2, ..., Ev, ..., where:

- E1 = (a1,1, a1,2, ..., a1,v, ...)
- E2 = (a2,1, a2,2, ..., a2,v, ...)
- Eμ = (aμ,1, aμ,2, ..., aμ,v, ...)

Now define a new sequence b1, b2, ..., bv, ... such that bv is different from av,v. Specifically: if av,v = m, then bv = w; if av,v = w, then bv = m. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

The element E0 = (b1, b2, b3, ...) is a member of *M* (it is an infinite sequence of *m*'s and *w*'s), but it cannot equal any Eμ in the list, because it differs from Eμ at position μ. Therefore no listing can exhaust *M*. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

This is the [[diagonal-argument]]: the constructed counterexample is built by "going down the diagonal" of the listing and flipping each entry.

## The power set theorem

Cantor immediately generalizes: "the principle followed therein can be readily extended to the general proposition that the powers of well-defined manifolds have no maximum." For any set *L*, one can construct a set *M* of greater cardinality. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

He demonstrates this by letting *L* be the linear continuum (real numbers in [0,1]) and *M* the set of all functions f(x) taking only values 0 or 1 for each x in [0,1]. The power of *M* is strictly greater than that of *L*. The proof again uses a diagonal construction: define g(x) to differ from the diagonal of any proposed bijection. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## No largest infinity

Cantor states that the collection of all cardinalities ("powers"), ordered by size, forms a "well-ordered crowd" -- there is always a next greater cardinality, and the sequence never terminates. He affirms that infinite cardinal numbers "are nothing else than the actual infinite-sized cardinal numbers, and they have the same reality and certainty as those." (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## Significance for the wiki's narrative

The diagonal argument is one of the most consequential proof techniques in the history of mathematics and logic:

- **Godel's incompleteness theorems** (1931): [[godel-1931]] uses a self-referential construction closely related to diagonalization -- the Godel sentence "says" of itself that it is unprovable, mirroring Cantor's construction of an element that differs from every listed element. [[godel-numbering]] is the encoding technique that makes this self-reference possible.
- **Turing's undecidability proof** (1936): [[turing-1936]] proves the halting problem unsolvable by a direct diagonal argument -- assuming a machine *H* can decide halting for all machines, construct a machine that does the opposite of what *H* predicts for it, producing a contradiction. The structure is identical to Cantor's.
- **Russell's paradox** (1902): [[russells-paradox]] -- the set of all sets that don't contain themselves -- can also be seen as a diagonal argument applied to the membership relation.

Cantor's paper thus provides the proof technique that ultimately sets the limits on [[formal-system]]s ([[incompleteness]]) and [[computability]] ([[entscheidungsproblem]]).

## Related pages

- [[diagonal-argument]]
- [[uncountability]]
- [[godel-1931]]
- [[godel-numbering]]
- [[turing-1936]]
- [[russells-paradox]]
- [[incompleteness]]
- [[computability]]
- [[entscheidungsproblem]]
- [[formal-system]]
