# Incompleteness

**Summary**: The property of a formal system that contains true statements it cannot prove -- established as unavoidable for any consistent system expressing arithmetic by Gödel's incompleteness theorems (1931).

**Sources**: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf, Principia Mathematica, vol. 1 (of 3).epub

**Last updated**: 2026-05-11

---

## Definition

A [[formal-system]] is **complete** if, for every well-formed formula F in the system, either F or its negation is provable. A system that is not complete is **incomplete**: it contains statements that are neither provable nor disprovable within the system.

Gödel's first incompleteness theorem (1931) proves that incompleteness is inescapable for any formal system that is:
1. **Consistent** (does not prove contradictions)
2. **Effectively axiomatized** (there is a mechanical procedure to check whether something is an axiom)
3. **Powerful enough to express basic arithmetic** (addition and multiplication of natural numbers)

(source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf)

## The two theorems

### First incompleteness theorem

Any consistent, effectively axiomatized formal system F that can express arithmetic contains a sentence G such that:
- G is true (in the standard model of arithmetic)
- Neither G nor its negation is provable in F

G is constructed via [[godel-numbering]] to be a sentence that, in effect, says "I am not provable in F." If F is consistent, G must be true and unprovable (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### Second incompleteness theorem

No consistent, effectively axiomatized formal system F that can express arithmetic can prove its own consistency. Specifically, the sentence "F is consistent" — which can be formulated as an arithmetic statement via Gödel numbering — is not provable in F (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## What incompleteness does NOT mean

- It does **not** mean mathematics is unreliable or that we cannot know truth. It means no single formal system captures all mathematical truths.
- It does **not** apply to all formal systems — only to those powerful enough to express arithmetic. Propositional logic ([[boolean-algebra]]) and the monadic predicate calculus are both complete.
- It does **not** mean the unprovable sentences are unknowable. We can recognize that Gödel's G is true by reasoning *about* the system from outside it.

## Impact on Hilbert's program

Hilbert had hoped to prove, by finitary means, that all of mathematics is consistent and complete. The first theorem destroys completeness; the second destroys the hope of a finitary consistency proof. Together they ended Hilbert's program as originally conceived. See [[hilbert-ackermann-1928]] for the context of Hilbert's questions, and [[godel-1931]] for the proof (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## Relationship to undecidability

Incompleteness and undecidability are related but distinct:

| | Incompleteness | Undecidability |
|---|---|---|
| Says | Some truths have no proof | No algorithm can find all proofs |
| Proved by | Gödel (1931) | Turing (1936) |
| Method | [[godel-numbering]] and self-reference | [[turing-machine]] and diagonalization |
| Applies to | Formal systems expressing arithmetic | First-order [[predicate-logic]] in general |

Turing's resolution of the [[entscheidungsproblem]] is the computational counterpart of Gödel's result. See [[turing-1936]].

## The incompleteness of Principia Mathematica

Gödel's paper title explicitly names [[whitehead-russell-1910]]. His formal system P is essentially the arithmetic fragment of *Principia Mathematica*. The theorems show that PM, despite its 2,000 pages of derivations, necessarily leaves some arithmetic truths unproved (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## Related pages

- [[godel-1931]]
- [[godel-numbering]]
- [[formal-system]]
- [[entscheidungsproblem]]
- [[hilbert-ackermann-1928]]
- [[whitehead-russell-1910]]
- [[computability]]
- [[turing-1936]]
