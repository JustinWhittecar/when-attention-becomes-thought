# Formal System

**Summary**: A set of symbols, formation rules, and transformation rules that together define a self-contained deductive apparatus — the framework within which logic, mathematics, and computation are defined.

**Sources**: Begriffsschrift.pdf, Principia Mathematica, vol. 1 (of 3).epub, On Computable Numbers, with an Application to the Entscheidungs Problem.pdf, 391249702-Hilbert-The-Principles-Of-Mathematical-Logic-pdf.pdf, Godel -- On Formally Undecidable Propositions of Principia Mathematica 1931.pdf

**Last updated**: 2026-05-11

---

## Definition

A formal system consists of:

1. **An alphabet** of symbols (e.g., variables, connectives, quantifiers, parentheses)
2. **Formation rules** (syntax) that define which strings of symbols are well-formed formulas (wffs)
3. **Axioms**: a set of wffs accepted without proof
4. **Inference rules**: mechanical procedures for deriving new wffs from existing ones (e.g., modus ponens: from "A" and "A → B," derive "B")

A **theorem** is any wff that can be derived from the axioms by repeated application of the inference rules. A **proof** is the sequence of steps leading to a theorem.

## Key examples in the wiki

| System | Source | Contribution |
|---|---|---|
| Begriffsschrift | [[frege-1879]] | First formal system for [[predicate-logic]] |
| Boolean algebra | [[boole-1854]] | Algebraic formal system for propositional logic |
| Principia Mathematica | [[whitehead-russell-1910]] | Formal system for all of mathematics (logicist program) |
| Hilbert-Ackermann | [[hilbert-ackermann-1928]] | Textbook axiomatization of propositional and predicate logic |
| Gödel's system P | [[godel-1931]] | The arithmetic fragment of PM used to prove [[incompleteness]] |
| Turing machines | [[turing-1936]] | Formal system for defining [[computability]] |

## The arc from formal systems to computers

The history traced by these sources is essentially the story of formal systems becoming physical:

1. **Frege (1879)**: Creates the first formal system powerful enough for mathematics ([[frege-1879]])
2. **Russell (1902)**: Discovers [[russells-paradox]], showing Frege's system is inconsistent ([[russell-1902]])
3. **Russell & Whitehead (1910)**: Build the most ambitious formal system ever attempted ([[whitehead-russell-1910]])
4. **Hilbert & Ackermann (1928)**: Systematize the logic, pose the [[entscheidungsproblem]] ([[hilbert-ackermann-1928]])
5. **Gödel (1931)**: Proves all sufficiently powerful formal systems are [[incompleteness|incomplete]] via [[godel-numbering]] ([[godel-1931]])
6. **Turing (1936)**: Responds by formalizing the notion of "mechanical procedure" itself — the [[turing-machine]] — and proves the Entscheidungsproblem undecidable ([[turing-1936]])
7. **Shannon (1938)**: Shows that formal logical operations can be implemented in physical circuits ([[shannon-1938]])
8. **Petzold (2023)**: Narrates how those circuits compose into a universal computer ([[petzold-2023]])

The formal system concept is thus the thread connecting abstract logic to physical computing.

## Properties of formal systems

- **Consistency**: No wff and its negation are both theorems
- **Completeness**: Every true wff is a theorem (Gödel showed this is impossible for systems expressing arithmetic — see [[incompleteness]])
- **Decidability**: There exists a mechanical procedure to determine whether any given wff is a theorem (Turing showed this is impossible for predicate logic — see [[entscheidungsproblem]])
- **Soundness**: Every theorem is true under the intended interpretation

## Related pages

- [[predicate-logic]]
- [[boolean-algebra]]
- [[computability]]
- [[turing-machine]]
- [[frege-1879]]
- [[russell-1902]]
- [[russells-paradox]]
- [[whitehead-russell-1910]]
- [[hilbert-ackermann-1928]]
- [[godel-1931]]
- [[incompleteness]]
- [[godel-numbering]]
- [[entscheidungsproblem]]
