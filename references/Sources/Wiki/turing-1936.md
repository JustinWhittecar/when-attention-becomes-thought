# On Computable Numbers, with an Application to the Entscheidungsproblem (Turing, 1936)

**Summary**: Alan Turing defines the Turing machine — a theoretical device that formalizes the concept of computation — and uses it to prove that the Entscheidungsproblem (decision problem) is undecidable, establishing the fundamental limits of what machines can compute.

**Sources**: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf

**Last updated**: 2026-05-11

---

## Context

David Hilbert had posed the [[entscheidungsproblem]] in [[hilbert-ackermann-1928]]: is there a mechanical procedure that can determine, for any mathematical statement expressed in formal logic, whether that statement is provable? Gödel's 1931 [[incompleteness]] theorems ([[godel-1931]], which explicitly referenced [[whitehead-russell-1910]]) had already shown that not all true statements are provable, but the question of whether provability itself is decidable remained open. Turing, then a 23-year-old student at Cambridge, answered it by first defining precisely what a "mechanical procedure" is (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Key contributions

### The Turing machine

Turing defines a computing machine as an abstract device consisting of:

- An infinite **tape** divided into squares, each capable of bearing a symbol
- A **head** that reads and writes one square at a time
- A finite set of **states** (m-configurations)
- A **transition table** that determines, given the current state and scanned symbol, what to write, which direction to move, and what state to enter next

The machine is **automatic** (an a-machine): its behavior is completely determined by the configuration. Turing also mentions **choice machines** (c-machines) that require external input at certain steps, but focuses exclusively on a-machines (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### Computable numbers

A real number is **computable** if there exists a circle-free Turing machine that, starting on a blank tape, prints the successive digits of its decimal expansion. Turing shows that computable numbers include all algebraic numbers, pi, e, and the zeros of Bessel functions — essentially every number that mathematicians work with. Yet the computable numbers are enumerable (countable), while the reals are not: "most" real numbers are not computable (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### The universal machine

Turing proves the existence of a **universal machine** U that can simulate any other Turing machine. Given an encoding (description number) of a machine M and its input, U reproduces M's behavior exactly. This is the theoretical foundation of the stored-program computer: a single machine that can execute any program (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### The halting problem

Using a diagonal argument (analogous to Cantor's proof that the reals are uncountable), Turing proves there is no general procedure to determine whether an arbitrary Turing machine will halt or run forever. This is the halting problem — the first concrete example of an undecidable problem (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### The Entscheidungsproblem is undecidable

Turing reduces the halting problem to the Entscheidungsproblem, showing that if there were a mechanical procedure to decide provability, it could be used to solve the halting problem — which he has just shown is impossible. Therefore the Entscheidungsproblem has no solution. Alonzo Church reached the same conclusion independently using lambda calculus; Turing proves in an appendix that the two notions of computability are equivalent (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Examples from the paper

Turing gives concrete examples of machines:

- **Machine I** computes the sequence 010101... using four states
- **Machine II** computes 0010110111011110... using five states and auxiliary "scratch" symbols on alternating squares

These examples illustrate the convention of using alternating F-squares (for output figures) and E-squares (for erasable working notes) — a technique analogous to separating output from working memory (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Significance for the book's arc

This paper is the pivot point of the entire narrative. It takes the formal-logic tradition of [[frege-1879]], [[boole-1854]], and [[whitehead-russell-1910]], and transforms it into a theory of physical machines. The [[turing-machine]] is the abstract blueprint that Shannon's switching circuits ([[shannon-1938]]) and Petzold's hardware narrative ([[petzold-2023]]) make concrete. And the idea that machines can be universal — capable of running any program — is what ultimately leads to LLMs and the [[turing-test]].

## Related pages

- [[turing-machine]]
- [[computability]]
- [[formal-system]]
- [[entscheidungsproblem]]
- [[incompleteness]]
- [[godel-1931]]
- [[hilbert-ackermann-1928]]
- [[whitehead-russell-1910]]
- [[shannon-1938]]
- [[universal-machine]]
- [[godel-numbering]]
