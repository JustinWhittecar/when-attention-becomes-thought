# Principles of Mathematical Logic (Hilbert & Ackermann, 1928)

**Summary**: David Hilbert and Wilhelm Ackermann's textbook systematizes mathematical logic from propositional calculus through first-order and higher-order predicate calculus, and formally poses the *Entscheidungsproblem* — the decision problem that Turing would prove unsolvable in 1936.

**Sources**: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf

**Last updated**: 2026-05-11

---

## Context

Hilbert had been developing his program for the foundations of mathematics since the early 1900s, working with Paul Bernays and later Wilhelm Ackermann. The *Grundzüge der theoretischen Logik* (first German edition 1928, second edition 1938, English translation 1950 as *Principles of Mathematical Logic*) codifies the logical tools that Hilbert's program requires. It is the textbook that trained a generation of logicians — including, indirectly, Gödel and Turing — and it is the work that Gödel's 1931 paper ([[godel-1931]]) explicitly references for its notation and terminology (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

## Structure

The book is organized in four parts, moving from simpler to more expressive logical systems:

### I. The Sentential Calculus (propositional logic)
Covers logical connectives (AND, OR, NOT, implication), truth tables, normal forms, duality, axiomatization, and proofs of consistency, independence, and completeness of the axiom system. This is the territory of [[boolean-algebra]] (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

### II. The Calculus of Classes (monadic predicate calculus)
Reinterprets the sentential calculus using classes and predicates of a single variable. Derives the traditional Aristotelian syllogisms as a special case (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

### III. The Restricted Predicate Calculus (first-order logic)
The core of the book. Introduces quantifiers, develops the full apparatus of [[predicate-logic]], proves consistency and independence of the axioms, proves the completeness of the system (every universally valid formula is provable), and poses the **decision problem** (the [[entscheidungsproblem]]): is there a mechanical procedure to determine, for any formula of the predicate calculus, whether it is universally valid? (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

### IV. The Extended Predicate Calculus (higher-order logic)
Extends the system to predicates of predicates (second-order logic), treats the concept of number, discusses set-theoretic foundations, addresses the logical paradoxes (including [[russells-paradox]]), and introduces the predicate calculus of order omega (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

## Key contributions

### Posing the Entscheidungsproblem

The decision problem (Section III, §12) asks whether there is an algorithm that takes any formula of first-order predicate logic and determines whether it is universally valid. Hilbert believed the answer would be "yes." Turing's 1936 paper ([[turing-1936]]) proved it "no" by inventing the [[turing-machine]] and reducing the problem to the halting problem. Church independently reached the same conclusion via lambda calculus. See [[entscheidungsproblem]] (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

### Completeness of first-order logic

The book proves that the first-order predicate calculus is complete: every universally valid formula is derivable from the axioms. (Gödel later gave a sharper proof of this in his 1929 doctoral thesis — not to be confused with the 1931 *incompleteness* theorems, which concern systems powerful enough to express arithmetic.) (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

### A clean formalization of logic

The book provides a rigorous, axiom-by-axiom presentation of mathematical logic that standardized the field. Gödel adopted its notation for his 1931 paper. The editor's preface to the English translation notes that revisions incorporated Gödel's incompleteness results and the resolution of the Entscheidungsproblem (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

## Significance for the book's arc

Hilbert-Ackermann is the bridge between the foundational work of Frege, Russell, and Whitehead and the revolution that Gödel and Turing sparked:

- It **codifies** what Frege invented ([[frege-1879]]) and what Russell and Whitehead deployed ([[whitehead-russell-1910]])
- It **poses the question** (the Entscheidungsproblem) that Turing answered by inventing the computer ([[turing-1936]])
- It **provides the notation** that Gödel used to prove incompleteness ([[godel-1931]])
- Its treatment of propositional logic is the same [[boolean-algebra]] that Shannon mapped onto circuits ([[shannon-1938]])

## Related pages

- [[entscheidungsproblem]]
- [[predicate-logic]]
- [[boolean-algebra]]
- [[formal-system]]
- [[godel-1931]]
- [[turing-1936]]
- [[frege-1879]]
- [[whitehead-russell-1910]]
- [[russells-paradox]]
- [[incompleteness]]
