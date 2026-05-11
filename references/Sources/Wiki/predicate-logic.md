# Predicate Logic

**Summary**: The branch of formal logic that extends propositional logic with quantifiers ("for all," "there exists") and predicates, allowing the expression of statements about objects and their properties.

**Sources**: Begriffsschrift.pdf, Principia Mathematica, vol. 1 (of 3).epub, 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf

**Last updated**: 2026-05-11

---

## Definition

Predicate logic (also called first-order logic) enriches propositional logic with:

- **Predicates**: expressions like P(x) that assert a property of an object x, or R(x, y) that assert a relation between objects
- **Quantifiers**: ∀x ("for all x") and ∃x ("there exists an x")
- **Variables** that range over a domain of objects
- **Functions** that map objects to objects

This allows expressing statements that [[boolean-algebra]] (propositional logic) cannot, such as "every even number greater than 2 is the sum of two primes" or "there exists a number that is its own square."

## Origins

Gottlob Frege invented predicate logic in his *Begriffsschrift* (1879; see [[frege-1879]]). He introduced the universal quantifier and showed that the existential quantifier could be defined via negation: ∃x P(x) ≡ ¬∀x ¬P(x). He also replaced the Aristotelian subject-predicate analysis of propositions with a function-argument analysis, treating "Socrates is mortal" as the function "is mortal" applied to the argument "Socrates" (source: Begriffsschrift.pdf).

## Role in the foundations of mathematics

Russell and Whitehead's *Principia Mathematica* (1910; see [[whitehead-russell-1910]]) used predicate logic as the basis for deriving all of mathematics from logical axioms. Their system added the theory of types to avoid [[russells-paradox]], which arose from unrestricted predicate formation (see [[russell-1902]]). Hilbert and Ackermann systematized predicate logic into a clean axiomatic textbook ([[hilbert-ackermann-1928]]), proving completeness for first-order logic and posing the [[entscheidungsproblem]]. Gödel's [[incompleteness]] theorems (1931; see [[godel-1931]]) showed that any consistent first-order system powerful enough to express arithmetic is necessarily incomplete — there are true statements it cannot prove (source: Principia Mathematica, vol. 1 (of 3).epub; 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

## Relationship to computability

The [[entscheidungsproblem]] — "is there a mechanical procedure to determine whether a given first-order logical statement is provable?" — was posed by [[hilbert-ackermann-1928]] and was the question that motivated Turing's 1936 paper (see [[turing-1936]]). Turing answered "no" by defining the [[turing-machine]] and proving the halting problem undecidable. Predicate logic is thus the direct context from which computability theory emerged (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Predicate logic vs. propositional logic

| Feature | Propositional logic | Predicate logic |
|---|---|---|
| Variables | Stand for propositions (true/false) | Stand for objects in a domain |
| Quantifiers | None | ∀ (for all), ∃ (there exists) |
| Internal structure | None — propositions are atomic | Predicates, functions, relations |
| Expressiveness | Can express "if A then B" | Can express "for all x, if P(x) then Q(x)" |
| Decidability | Decidable (truth tables) | Undecidable in general |

## Related pages

- [[frege-1879]]
- [[boolean-algebra]]
- [[formal-system]]
- [[russells-paradox]]
- [[whitehead-russell-1910]]
- [[hilbert-ackermann-1928]]
- [[entscheidungsproblem]]
- [[incompleteness]]
- [[godel-1931]]
- [[turing-1936]]
- [[computability]]
