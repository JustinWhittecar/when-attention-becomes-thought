# Russell's Paradox

**Summary**: The contradiction discovered by Bertrand Russell in 1901 showing that the set of all sets that do not contain themselves both must and must not contain itself -- the crisis that forced a reconstruction of logic's foundations.

**Sources**: Frege-Russell.pdf, Principia Mathematica, vol. 1 (of 3).epub

**Last updated**: 2026-05-11

---

## The paradox

Define R as the set of all sets that do not contain themselves:

> R = { x : x is not in x }

Is R a member of itself?

- If R is in R, then by the defining property, R is not in R. Contradiction.
- If R is not in R, then by the defining property, R is in R. Contradiction.

Either way, the system is inconsistent (source: Frege-Russell.pdf).

## Discovery and communication

Russell discovered the paradox in 1901 while studying Frege's *Grundgesetze der Arithmetik*. He communicated it to Frege in a letter dated June 16, 1902 (see [[russell-1902]]). In the letter, Russell formulates the paradox in terms of predicates: "Let w be the predicate: to be a predicate that cannot be predicated of itself. Can w be predicated of itself?" He also wrote to Peano, who never replied (source: Frege-Russell.pdf).

## Why it matters

### It broke Frege's system

Frege's [[frege-1879]] and *Grundgesetze* relied on Basic Law V, which allows forming a set (extension) for any predicate. Russell's paradox shows that unrestricted set formation is contradictory. In his reply, Frege acknowledged that Russell's discovery shook "not only the foundations of my arithmetic, but also the sole possible foundations of arithmetic" (source: Frege-Russell.pdf).

### It motivated the theory of types

Russell and Whitehead spent a decade constructing [[whitehead-russell-1910]] specifically to avoid this paradox. Their solution — the theory of types — arranges objects into a hierarchy (individuals, sets of individuals, sets of sets, etc.) and forbids any set from containing members of its own type. The "set of all sets that do not contain themselves" becomes an ill-formed expression that violates the type constraints (source: Principia Mathematica, vol. 1 (of 3).epub).

### It launched Hilbert's program

The foundational crisis prompted Hilbert to propose his program: prove by finitary means that mathematics is consistent. [[hilbert-ackermann-1928]] formalized the questions. [[godel-1931]] proved the program was impossible.

### It echoes in computer science

The paradox's self-referential structure reappears throughout the theory of computation:
- Gödel's [[godel-numbering]] constructs a statement that says "I am not provable" — the same self-referential pattern
- Turing's halting problem proof uses a machine that asks whether it halts on its own description — another diagonal self-reference
- Type systems in programming languages (Haskell, Rust, TypeScript) descend from Russell's type theory, designed to prevent analogous contradictions

## Related paradoxes

- **The liar paradox**: "This sentence is false" — Russell's paradox is the set-theoretic version of this ancient puzzle
- **The barber paradox**: The barber who shaves all and only those who do not shave themselves — Russell's own informal illustration
- **Cantor's paradox**: There is no set of all sets (since its power set would be larger than it) -- see [[cantor-1891]] for the [[diagonal-argument]] that proves the power set is always strictly larger

## Related pages

- [[russell-1902]]
- [[frege-1879]]
- [[whitehead-russell-1910]]
- [[formal-system]]
- [[godel-1931]]
- [[godel-numbering]]
- [[hilbert-ackermann-1928]]
- [[cantor-1891]]
- [[diagonal-argument]]
