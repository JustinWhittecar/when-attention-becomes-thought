# Entscheidungsproblem (Decision Problem)

**Summary**: The question, posed by Hilbert, of whether there exists a mechanical procedure to determine the provability of any statement in first-order logic -- answered "no" independently by Church and Turing in 1936, with Turing's proof giving rise to the Turing machine.

**Sources**: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf, On Computable Numbers, with an Application to the Entscheidungs Problem.pdf

**Last updated**: 2026-05-11

---

## The question

The *Entscheidungsproblem* (German: "decision problem") asks:

> Is there an algorithm that takes as input any formula of first-order [[predicate-logic]] and determines, in a finite number of steps, whether that formula is universally valid (true in every interpretation)?

Hilbert and Ackermann posed the problem formally in Section III, §12 of their [[hilbert-ackermann-1928]]. Hilbert believed the answer was "yes" — that mathematics was, in principle, mechanically decidable (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

## Why the answer is "no"

### Turing's proof (1936)

Turing answered the Entscheidungsproblem by first defining precisely what a "mechanical procedure" is: the [[turing-machine]]. He then proved that the **halting problem** — whether a given Turing machine halts on a given input — is undecidable. Finally, he reduced the Entscheidungsproblem to the halting problem: if there were a mechanical procedure to decide universal validity, it could be used to solve the halting problem, which is impossible. See [[turing-1936]] (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### Church's proof (1936)

Alonzo Church independently proved the same result using lambda calculus. Turing showed in an appendix to his paper that his notion of computability is equivalent to Church's, establishing the **Church-Turing thesis** (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## The chain of events

1. **1879**: Frege invents [[predicate-logic]] ([[frege-1879]])
2. **1901**: Russell discovers [[russells-paradox]] in Frege's system
3. **1910**: Russell and Whitehead build [[whitehead-russell-1910]] to repair the damage
4. **1928**: Hilbert and Ackermann pose the Entscheidungsproblem ([[hilbert-ackermann-1928]])
5. **1931**: Gödel proves that formal systems of arithmetic are incomplete ([[godel-1931]]) — but the decidability question remains open
6. **1936**: Turing proves the Entscheidungsproblem undecidable, inventing the [[turing-machine]] in the process ([[turing-1936]])

## Relationship to Gödel's results

Gödel's [[incompleteness]] theorems (1931) showed that not all true arithmetic statements are provable, but this did not directly settle the Entscheidungsproblem. Incompleteness says "some truths have no proof"; undecidability says "there is no algorithm to find proofs even when they exist." Turing's result is strictly stronger: it shows there is no mechanical procedure even to determine provability (let alone truth).

## Partial decidability

While the full Entscheidungsproblem is undecidable, restricted fragments of predicate logic are decidable:

- **Propositional logic** ([[boolean-algebra]]): decidable via truth tables
- **Monadic predicate calculus** (predicates of one variable): decidable, as shown in [[hilbert-ackermann-1928]]
- **Presburger arithmetic** (addition without multiplication): decidable, as proven by Presburger in 1930

It is only the full first-order predicate calculus — with both addition and multiplication, or with polyadic predicates — that is undecidable (source: 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf).

## Related pages

- [[hilbert-ackermann-1928]]
- [[turing-1936]]
- [[turing-machine]]
- [[computability]]
- [[predicate-logic]]
- [[incompleteness]]
- [[godel-1931]]
- [[boolean-algebra]]
