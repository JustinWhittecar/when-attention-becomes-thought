# On Formally Undecidable Propositions of Principia Mathematica and Related Systems (Gödel, 1931)

**Summary**: Kurt Gödel proves that any consistent formal system powerful enough to express arithmetic contains true propositions it cannot prove (first incompleteness theorem) and cannot prove its own consistency (second incompleteness theorem), ending Hilbert's program and reshaping the foundations of mathematics.

**Sources**: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf

**Last updated**: 2026-05-11

---

## Context

By 1930, David Hilbert's program aimed to establish the consistency and completeness of mathematics through finitary methods. Whitehead and Russell's [[whitehead-russell-1910]] had shown that vast tracts of mathematics could be derived from logical axioms, and Hilbert and Ackermann's [[hilbert-ackermann-1928]] had formalized the key open questions — including the [[entscheidungsproblem]]. The assumption was that a sufficiently careful formal system could, in principle, decide every mathematical question. Gödel, a 25-year-old Austrian logician, destroyed this assumption (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## Key contributions

### The first incompleteness theorem

Any consistent [[formal-system]] F that is powerful enough to express basic arithmetic contains a proposition G such that neither G nor its negation is provable in F. G is true (in the standard interpretation of arithmetic) but unprovable. The system is necessarily [[incompleteness|incomplete]] (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### The second incompleteness theorem

No consistent formal system powerful enough to express arithmetic can prove its own consistency. If F could prove "F is consistent," then F would be inconsistent. This killed Hilbert's program, which required exactly such a consistency proof (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### Gödel numbering

Gödel invented a method — [[godel-numbering]] — of encoding the symbols, formulas, and proofs of a formal system as natural numbers. Each symbol gets a number; a formula (sequence of symbols) gets a number computed from the prime factorization; a proof (sequence of formulas) gets yet another number. This allows the formal system to make statements about its own syntax using ordinary arithmetic. The self-referential proposition G effectively says "this proposition is not provable in F" — and it says so using a purely arithmetical statement about Gödel numbers (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### Recursive functions

The paper introduces the concept of **primitive recursive functions** — functions defined by base cases and rules that compute the (k+1)th value from the kth. Gödel shows that all the metamathematical concepts he needs (being a formula, being a proof, being a proof of a specific formula) can be expressed as recursive arithmetical relations. This notion of recursiveness later became central to [[computability]] theory (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## The proof strategy

1. Define a formal system P that captures the arithmetic of *Principia Mathematica*
2. Assign [[godel-numbering|Gödel numbers]] to every sign, formula, and proof-schema in P
3. Show that the metamathematical predicate "x is a proof of the formula y" corresponds to a recursive arithmetical relation on Gödel numbers
4. Construct a formula G that, via its Gödel number, asserts its own unprovability
5. Show that if P is consistent, neither G nor its negation is provable in P
6. Conclude that P is incomplete — and that this applies to any system meeting the same conditions

## Significance for the book's arc

Gödel's paper occupies a pivotal position in the chain from logic to computation:

- **Frege (1879)**: Formal logic capable of expressing mathematics ([[frege-1879]])
- **Russell's paradox (1902)**: Reveals a flaw in Frege's system ([[russell-1902]])
- **Principia (1910)**: Repairs the flaw via type theory ([[whitehead-russell-1910]])
- **Hilbert-Ackermann (1928)**: Formalizes the open questions ([[hilbert-ackermann-1928]])
- **Gödel (1931)**: Proves completeness is impossible -- **this paper**
- **Turing (1936)**: Proves decidability is impossible, inventing the computer in the process ([[turing-1936]])

Gödel's technique of encoding syntax as numbers is also a conceptual ancestor of the stored-program computer: the insight that data and instructions are the same kind of thing (numbers) reappears in von Neumann's architecture and, ultimately, in the [[universal-machine]].

## Relationship to other sources

- The paper's title explicitly references [[whitehead-russell-1910]], and Gödel's formal system P is essentially the arithmetic fragment of *Principia Mathematica*
- Braithwaite's introduction notes that Gödel's interpreted symbolism follows [[hilbert-ackermann-1928]] (the *Grundzüge der theoretischen Logik*)
- Turing's 1936 paper ([[turing-1936]]) directly responds to the questions Gödel's work left open — particularly the [[entscheidungsproblem]]
- [[russell-1902]] is the historical event that forced the type-theoretic framework Gödel worked within

## Related pages

- [[incompleteness]]
- [[godel-numbering]]
- [[entscheidungsproblem]]
- [[formal-system]]
- [[computability]]
- [[whitehead-russell-1910]]
- [[hilbert-ackermann-1928]]
- [[turing-1936]]
- [[russells-paradox]]
