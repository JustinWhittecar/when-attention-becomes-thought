# Turing Machine

**Summary**: An abstract computing device consisting of an infinite tape, a read/write head, and a finite state machine — Turing's formalization of what it means to compute, and the theoretical blueprint for every digital computer.

**Sources**: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf

**Last updated**: 2026-05-11

---

## Definition

A Turing machine, as defined in Turing's 1936 paper (see [[turing-1936]]), consists of:

- An **infinite tape** divided into squares, each bearing a symbol (or blank)
- A **head** that can read the current square, write a symbol, and move one square left or right
- A finite set of **states** (m-configurations): q₁, q₂, ..., qₙ
- A **transition table** mapping (current state, scanned symbol) → (symbol to write, direction to move, next state)

The machine is **automatic** (an a-machine): given the current configuration, its next action is completely determined. Turing also defines **choice machines** (c-machines) that sometimes require external input, but focuses on a-machines (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Key properties

### Determinism

At each step, the transition table specifies exactly one action. There is no ambiguity or choice.

### Halting

A machine **halts** when it reaches a configuration for which no transition is defined. A **circle-free** machine is one that never stops producing output symbols. A **circular** machine eventually stops producing output (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

### The F-square / E-square convention

Turing uses alternating squares: F-squares hold the output (the computed number), while E-squares hold scratch work that can be erased. This is analogous to the distinction between output and working memory in modern computers (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## The universal Turing machine

Turing proves the existence of a **universal machine** U that can simulate any Turing machine M. Given an encoding of M (its "description number") written on the tape, U reads M's transition table and executes it step by step. This is the theoretical foundation of the stored-program computer: a single machine that can run any program. See [[universal-machine]] (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## From theory to hardware

The Turing machine is an abstraction — it has an infinite tape, which no physical machine can have. But its principles map onto real computers:

| Turing machine | Physical computer |
|---|---|
| Tape | Memory (RAM, disk) |
| Head | CPU (reads/writes memory) |
| State | Program counter + registers |
| Transition table | Instruction set |

The earliest design for such a machine was Babbage's [[analytical-engine]] ([[babbage-1837]]), which separated processing (the Mill) from memory (the Store) and used Operation Cards for instructions -- the same division shown in this table, realized in mechanical gears rather than electronic circuits.

Shannon's 1938 thesis ([[shannon-1938]]) showed how to build the logical components from circuits. Petzold's *Code* ([[petzold-2023]]) shows how those components compose into a complete CPU that is, in effect, a universal Turing machine with finite memory.

## The Church-Turing thesis

Turing showed in an appendix to his 1936 paper that his notion of computability is equivalent to Alonzo Church's lambda calculus. The **Church-Turing thesis** — not a theorem but a widely accepted claim — states that any function computable by an "effective procedure" is computable by a Turing machine. No counterexample has ever been found (source: On Computable Numbers, with an Application to the Entscheidungs Problem.pdf).

## Related pages

- [[turing-1936]]
- [[universal-machine]]
- [[computability]]
- [[formal-system]]
- [[entscheidungsproblem]]
- [[godel-1931]]
- [[hilbert-ackermann-1928]]
- [[shannon-1938]]
- [[petzold-2023]]
- [[analytical-engine]]
- [[babbage-1837]]
- [[cantor-1891]]
- [[diagonal-argument]]
