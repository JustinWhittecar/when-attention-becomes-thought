# Gödel Numbering

**Summary**: A method of encoding the symbols, formulas, and proofs of a formal system as natural numbers, enabling a system to make arithmetical statements about its own syntax -- the key technique behind Gödel's incompleteness theorems.

**Sources**: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf

**Last updated**: 2026-05-11

---

## How it works

Gödel's encoding has three layers:

### 1. Symbols to numbers

Each basic sign in the [[formal-system]] gets a unique natural number. Gödel assigns numbers to variables, logical connectives, quantifiers, parentheses, and the other symbols of his system P (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### 2. Formulas to numbers

A formula is a sequence of symbols. If the symbols have Gödel numbers n1, n2, ..., nk, then the formula's Gödel number is:

> 2^n1 * 3^n2 * 5^n3 * ... * pk^nk

where p1=2, p2=3, p3=5, ... are the first k prime numbers. By the fundamental theorem of arithmetic (unique prime factorization), this encoding is reversible: given the Gödel number, you can recover the original formula (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### 3. Proofs to numbers

A proof is a sequence of formulas. If the formulas have Gödel numbers m1, m2, ..., mj, then the proof's Gödel number is:

> 2^m1 * 3^m2 * ... * pj^mj

The same prime-factorization trick works at this level too (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## Why it matters

### Self-reference becomes arithmetic

Once syntax is encoded as numbers, metamathematical statements ("x is a proof of y," "y is provable") become arithmetical statements about natural numbers. The [[formal-system]] can now talk about itself using its own language. This is what allows Gödel to construct the sentence G that says, in effect, "this sentence is not provable" — the core of the first [[incompleteness]] theorem (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### Recursive relations

Gödel shows that the key metamathematical predicates — "x is a variable," "x is a formula," "x is a proof of y" — are all **primitive recursive** functions of the Gödel numbers. This means they can be computed by a step-by-step mechanical procedure, which is what makes the encoding useful rather than merely clever (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

### Data-instruction equivalence

Gödel numbering is conceptually analogous to the stored-program idea: in both cases, the "instructions" (formulas, programs) are represented as "data" (numbers, memory contents). Turing's [[universal-machine]] makes this analogy concrete — a single machine that reads an encoded description of another machine and simulates it. The progression runs: Gödel numbers (1931) -> Turing's description numbers (1936) -> von Neumann's stored-program architecture (1945).

## Gödel's 46 definitions

Gödel defines a sequence of 46 arithmetical concepts (definitions 1-46 in his paper) that correspond, via the encoding, to metamathematical concepts. Examples:

- **Definition 8**: The operation x * y yields the Gödel number of the concatenation of the strings whose Gödel numbers are x and y
- **Definition 45**: The relation x B y holds when x is the Gödel number of a proof of the formula whose Gödel number is y
- **Definition 46**: Bew(y) — "y is provable" — holds when there exists some x such that x B y

Definitions 1-45 are all primitive recursive. Definition 46 introduces an unbounded existential quantifier and is *not* recursive — a distinction critical to the proof (source: Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf).

## Related pages

- [[godel-1931]]
- [[incompleteness]]
- [[formal-system]]
- [[computability]]
- [[universal-machine]]
- [[turing-1936]]
- [[russells-paradox]]
