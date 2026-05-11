# The Logic Beneath the Machine

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-06.*

## Narrative job

Establish the deep idea behind every modern computer: that thinking can be done with arithmetic. Walk the reader from Boole's algebra of propositions, through Frege and Russell's formalization of logic, to Turing's 1936 definition of a computable function, to Shannon's 1937 discovery that switching circuits and Boolean logic are the same thing in different clothes. End with a worked half-adder, expressed in propositional logic and in pseudocode, so the reader leaves the chapter with a vocabulary they will use for the rest of the book. This is the chapter that the entire book stands on.

## Pedagogical commitments for this chapter

- Propositional logic is introduced here and used unembellished in every later hardware chapter. The reader learns AND, OR, NOT, NAND, XOR as truth-functional operators in this chapter, and we never re-explain them.
- Pseudocode is introduced here as a way to describe a procedure independently of any one programming language. The half-adder is the first worked pseudocode block.
- "Show, then tell." Every formal device that appears in prose later in the book is introduced here in its smallest worked example.

## Notation reference

The notation below is the modern conventions this book will use from this chapter forward. Boole's original notation (multiplication for AND, exclusive + for disjoint OR) gets shown in its historical context inside the chapter, then retired in favor of the table here. Once introduced, every later chapter assumes these without re-explanation.

| Symbol | Name | What it means |
| --- | --- | --- |
| ¬ | Not | The opposite. ¬P is true exactly when P is false. |
| ∧ | And | Both. P ∧ Q is true only when P and Q are both true. |
| ∨ | Or | Either, or both. P ∨ Q is true when at least one of P, Q is true. Inclusive, not exclusive. |
| ⊻ | Xor | Exactly one. P ⊻ Q is true when exactly one of P, Q is true, but not both. |
| ⊼ | Nand | Not both. The negation of ∧. False only when P and Q are both true. |
| ⊽ | Nor | Neither. The negation of ∨. True only when P and Q are both false. |
| ⇒ | Implies | If-then. P ⇒ Q reads "if P then Q." False only when P is true and Q is false. |
| ⇔ | If and only if | Same truth value. P ⇔ Q is true when P and Q are both true or both false. |
| ∀ | For all | For every. ∀x. P(x) reads "for every x, P holds of x." |
| ∃ | There exists | At least one. ∃x. P(x) reads "there is some x for which P holds." |
| 1 | True | The truth value true. A tautology evaluates to 1: A ∨ ¬A ≡ 1. The choice of 1 (rather than ⊤) is deliberate; the rest of the book builds on this toward binary, circuits, and machine code. |
| 0 | False | The truth value false. A contradiction evaluates to 0: A ∧ ¬A ≡ 0. |
| ≡ | Logically equivalent to | A claim that two formulas always agree. Sits outside the formula, where ⇔ sits inside it. |
| ∈ | Element of | Set or class membership. "x ∈ A" reads "x belongs to the class A." Honors Boole's class framing. |
| := | Is defined as | Names a new gadget in terms of old ones. "HA(A, B) := (A ⊻ B, A ∧ B)" defines the half-adder. |

Subscripts (A₀, A₁, …) are used for indexed bit positions in multi-bit work. They are typesetting, not new vocabulary.

## Reading list

1. Boole, G. (1854). *An Investigation of the Laws of Thought.* Read the introduction and Chapter II ("Of Signs in General"). The founding text. Read for the move from "logic is an art" to "logic is a calculus."
2. Frege, G. (1879). *Begriffsschrift.* Read the preface and the propositional fragment. The first complete formalization of inference. Skim the rest.
3. Whitehead, A. N. & Russell, B. (1910). *Principia Mathematica*, Vol. 1. Read the introduction. The reader does not need the full system; they need to see what a fully formalized derivation looks like.
4. Turing, A. M. (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem." *Proceedings of the London Mathematical Society*, 2nd ser., 42, 230-265. The central paper of the chapter. Read for the definition of a computable function and the construction of the universal machine.
5. Shannon, C. E. (1937). *A Symbolic Analysis of Relay and Switching Circuits.* MIT master's thesis. The bridge from logic to hardware. Short. Read it whole.
6. Shannon, C. E. (1948). "A Mathematical Theory of Communication." *Bell System Technical Journal*, 27, 379-423 and 623-656. Read Sections 1 through 6. The chapter on information theory will pull from here, but the reader meets entropy here for the first time as a formal quantity.
7. Petzold, C. (2022). *Code: The Hidden Language of Computer Hardware and Software*, 2nd ed. Reference companion. Cite for accessible exposition of relays-to-gates, not as a primary source.

## Worked examples to build into the chapter

- The truth tables for AND, OR, NOT, XOR, and NAND. Each accompanied by a one-line pseudocode definition.
- The half-adder, in three forms: truth table, propositional formula (sum = A XOR B; carry = A AND B), and pseudocode. This becomes the reader's first concrete experience of "logic implemented as a circuit."
- The full adder, built by chaining two half-adders and an OR. The reader sees their first composite circuit.
- One short pseudocode block for a multi-bit ripple-carry adder, to demonstrate that addition itself is just a chain of full adders.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

This chapter is foundational and will not need frequent updates as the field moves. Update only if a new historical scholarship shifts the standard reading of Boole, Turing, or Shannon.
