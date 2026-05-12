# Uncountability

**Summary**: The property of a set that cannot be placed in one-to-one correspondence with the natural numbers, first proved by Cantor in 1874 and given a simpler proof via the diagonal argument in 1891.

**Sources**: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf

**Last updated**: 2026-05-11

---

## Definition

A set is **countable** if its elements can be listed in a sequence indexed by the natural numbers 1, 2, 3, .... A set is **uncountable** if no such listing is possible -- its cardinality is strictly greater than that of the natural numbers. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## Cantor's proofs

Cantor first proved the uncountability of the real numbers in 1874 using a nested-intervals argument. In [[cantor-1891]], he provided "a much simpler proof of that theorem, which is independent of the consideration of irrational numbers." This simpler proof uses the [[diagonal-argument]]: given any proposed listing of all infinite binary sequences, a new sequence is constructed that differs from each listed sequence at the corresponding position and therefore cannot appear in the list. (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## The hierarchy of infinities

Cantor showed that uncountability is not a single phenomenon but the beginning of an unending hierarchy. For any set *L*, the set *M* of all functions from *L* to {0, 1} (equivalently, the power set of *L*) has strictly greater cardinality. This means there is no largest infinite cardinal -- the cardinalities form a "well-ordered crowd" where "in nature there is one next greater in every power, but also a next greater one follows every infinitely increasing set of powers." (source: Ueber eine elementare Frage der Mannigfaltigkeitslehre.pdf)

## Connection to computability

Uncountability has direct consequences for [[computability]]:

- The set of all [[turing-machine]]s (or programs) is countable, because each machine can be described by a finite string of symbols
- The set of all functions from natural numbers to {0, 1} is uncountable (by Cantor's theorem)
- Therefore most functions are not computable -- there are "more" problems than there are programs to solve them

This cardinality gap is the deep reason behind the undecidability results in [[turing-1936]] and the [[entscheidungsproblem]]. The [[diagonal-argument]] is the specific technique that makes this reasoning rigorous.

## Connection to the wiki's logical thread

Cantor's uncountability results (1874, 1891) precede and structurally anticipate:
- [[russells-paradox]] (1902) -- a diagonalization on set membership
- [[godel-1931]] -- a diagonalization on provability within [[formal-system]]s
- [[turing-1936]] -- a diagonalization on computability by [[turing-machine]]s

## Related pages

- [[cantor-1891]]
- [[diagonal-argument]]
- [[computability]]
- [[turing-1936]]
- [[turing-machine]]
- [[entscheidungsproblem]]
- [[godel-1931]]
- [[russells-paradox]]
- [[formal-system]]
