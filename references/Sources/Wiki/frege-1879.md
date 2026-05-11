# Begriffsschrift (Frege, 1879)

**Summary**: Gottlob Frege's *Begriffsschrift* ("concept-script") is the founding document of modern predicate logic, introducing quantifiers, propositional connectives, and a formal notation for expressing logical relationships that ordinary language obscures.

**Sources**: Begriffsschrift.pdf

**Last updated**: 2026-05-11

---

## Context

Before Frege, logic had barely advanced beyond the syllogistic framework Aristotle established two millennia earlier. Boole had made progress by algebraizing propositional logic (see [[boole-1854]]), but his system could not express statements involving "all" or "some" — the quantifiers that pervade mathematics and everyday reasoning. Frege set out to build a formal language rigorous enough to express the full content of mathematical proofs without any appeal to intuition.

## Key contributions

### Predicate logic with quantifiers

Frege introduced the universal quantifier ("for all x") and showed how the existential quantifier ("there exists an x") can be derived from it via negation. This gave logic the power to express statements like "every even number greater than 2 is the sum of two primes" — something [[boolean-algebra]] alone cannot do (source: Begriffsschrift.pdf).

### Function-argument structure

Rather than treating propositions as combinations of subject and predicate (the Aristotelian view), Frege analyzed them as functions applied to arguments. The proposition "Socrates is mortal" becomes the function "is mortal" applied to the argument "Socrates." This decomposition is the ancestor of the function-argument structure used in programming languages and lambda calculus (source: Begriffsschrift.pdf).

### A formal proof system

The *Begriffsschrift* contains axioms and inference rules sufficient to derive logical truths purely by symbol manipulation — no semantic interpretation required. This is among the first examples of what would later be called a [[formal-system]]: a set of symbols, formation rules, and transformation rules that together define a self-contained deductive apparatus (source: Begriffsschrift.pdf).

### Two-dimensional notation

Frege invented a distinctive tree-like notation that represents logical structure spatially on the page. While the notation never caught on (Russell and Peano's linear notations won out), the underlying ideas — distinguishing assertion from content, separating logical form from surface grammar — became permanent fixtures of logic (source: Begriffsschrift.pdf).

## Significance for the book's arc

The *Begriffsschrift* is the first step in the chain from [[predicate-logic]] to [[computability]] to modern computing. Frege showed that reasoning could be reduced to rule-governed symbol manipulation. Russell and Whitehead extended this vision in [[whitehead-russell-1910]]. Hilbert and Ackermann codified it in [[hilbert-ackermann-1928]]. Gödel showed its limits in [[godel-1931]]. And Turing, responding to Gödel, defined the [[turing-machine]] — the abstract device that became the blueprint for every computer.

## Limitations

Frege's system contained an unrestricted comprehension axiom that led to [[russells-paradox]] (1901): the set of all sets that do not contain themselves. Russell communicated the contradiction to Frege in a famous letter (see [[russell-1902]]); Frege acknowledged it shook the foundations of his work. This crisis forced a major revision of the logical foundations, carried out in [[whitehead-russell-1910]] via the theory of types.

## Related pages

- [[predicate-logic]]
- [[boolean-algebra]]
- [[formal-system]]
- [[boole-1854]]
- [[russell-1902]]
- [[russells-paradox]]
- [[whitehead-russell-1910]]
- [[hilbert-ackermann-1928]]
- [[godel-1931]]
- [[computability]]
