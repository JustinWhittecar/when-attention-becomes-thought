# Computability

**Summary**: The branch of mathematical logic and computer science concerned with which problems can be solved by mechanical procedures, formalized by Turing machines and equivalent models.

**Sources**: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf, Principia Mathematica, vol. 1 (of 3).epub, Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf, 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf

**Last updated**: 2026-05-11

---

## Definition

A function or problem is **computable** if there exists a [[turing-machine]] (or equivalent formalism) that computes it — that is, that halts with the correct answer for every valid input. A problem is **undecidable** if no such machine exists.

## Origins

Computability theory was born from the [[entscheidungsproblem]]: Hilbert's 1928 question (see [[hilbert-ackermann-1928]]) of whether there exists a mechanical procedure to determine the provability of any statement in [[predicate-logic]]. Three independent answers appeared in the 1930s:

| Formalism | Author | Year |
|---|---|---|
| Lambda calculus | Alonzo Church | 1936 |
| Turing machine | Alan Turing ([[turing-1936]]) | 1936 |
| Recursive functions | Kurt Gödel ([[godel-1931]]) / Stephen Kleene | 1931-36 |

All three formalisms define exactly the same class of computable functions. Turing proved in an appendix to his 1936 paper that his computability is equivalent to Church's effective calculability (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Key results

### The halting problem is undecidable

There is no general procedure to determine whether an arbitrary Turing machine halts on a given input. Turing proves this by a diagonal argument: assuming such a procedure exists leads to a contradiction (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### The Entscheidungsproblem is undecidable

Turing reduces the halting problem to the decision problem for predicate logic, showing that if the Entscheidungsproblem were decidable, the halting problem would be too — contradicting the result above (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### Gödel's incompleteness theorems

Any consistent [[formal-system]] powerful enough to express arithmetic contains true statements it cannot prove (first theorem) and cannot prove its own consistency (second theorem). Gödel proved this using [[godel-numbering]] to make the system refer to itself. His paper explicitly references [[whitehead-russell-1910]] in its title. See [[godel-1931]] and [[incompleteness]] (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## The Church-Turing thesis

The claim (not a theorem) that any function computable by an "effective procedure" — any method a human could carry out with pencil, paper, and unlimited time — is computable by a Turing machine. No counterexample has been found. This thesis underpins the confidence that digital computers can, in principle, compute anything that is computable at all.

## Computability and AI

Modern AI systems, including LLMs built on the [[transformer-architecture]], are computable functions: they take a finite input (a sequence of tokens) and produce a finite output via a deterministic (or pseudo-random) procedure running on a [[universal-machine]]. The question of whether such systems can exhibit intelligence is the subject of the [[turing-test]] and the debate in [[chen-et-al-2026]].

## Related pages

- [[turing-machine]]
- [[universal-machine]]
- [[turing-1936]]
- [[formal-system]]
- [[predicate-logic]]
- [[whitehead-russell-1910]]
- [[hilbert-ackermann-1928]]
- [[entscheidungsproblem]]
- [[godel-1931]]
- [[incompleteness]]
- [[godel-numbering]]
