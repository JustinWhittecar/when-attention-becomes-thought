# A Symbolic Analysis of Relay and Switching Circuits (Shannon, 1938)

**Summary**: Claude Shannon's master's thesis demonstrates that Boolean algebra maps directly onto electrical relay circuits, enabling the systematic design and analysis of digital logic — the insight that made digital computing physically realizable.

**Sources**: A Symbolic Analysis of Relay and Switching Circuits.pdf

**Last updated**: 2026-05-12

---

## Context

By the late 1930s, telephone exchanges and industrial control systems used complex networks of electromagnetic relays, but their design was largely ad hoc. Engineers drew circuit diagrams and tested combinations by hand. Meanwhile, [[boolean-algebra]] — the system Boole had invented in 1854 (see [[boole-1854]]) — had remained a purely mathematical curiosity for 84 years. Shannon, then a 21-year-old master's student at MIT, recognized that the two-valued nature of relay contacts (open/closed) was identical to the two-valued nature of Boolean variables (0/1) (source: A Symbolic Analysis of Relay and Switching Circuits.pdf).

## Key contributions

### Boolean algebra ↔ switching circuits

Shannon establishes a precise isomorphism:

| Boolean algebra | Relay circuit |
|---|---|
| Variable = 1 | Relay closed (current flows) |
| Variable = 0 | Relay open (no current) |
| AND (xy) | Series connection |
| OR (x + y) | Parallel connection |
| NOT (x') | Normally-closed contact |

Any Boolean expression can be directly translated into a circuit, and any circuit can be described by a Boolean expression. This means all the theorems of Boolean algebra — De Morgan's laws, distributive laws, simplification rules — apply directly to circuit design (source: A Symbolic Analysis of Relay and Switching Circuits.pdf).

### Systematic circuit design

Rather than designing circuits by intuition, engineers could now:

1. Write a Boolean expression for the desired input-output behavior
2. Simplify the expression using algebraic rules
3. Translate the simplified expression into a circuit

This made it possible to prove that a circuit was correct and to find the simplest circuit for a given function — both impossible with ad hoc methods (source: A Symbolic Analysis of Relay and Switching Circuits.pdf).

### Practical applications

Shannon demonstrates the method on real engineering problems including:

- Designing relay circuits for a selective switching system
- Building an electric combination lock
- Implementing binary addition circuits

The binary adder example is particularly significant: it shows that arithmetic itself can be implemented in hardware, a step toward the general-purpose computer (source: A Symbolic Analysis of Relay and Switching Circuits.pdf).

## Significance for the book's arc

This paper is the bridge between abstract logic and physical hardware. Boole ([[boole-1854]]) showed that logic could be algebra. Turing ([[turing-1936]]) showed that computation could be formalized as a machine. Shannon showed that Boole's algebra could be directly implemented in electrical circuits — giving Turing's abstract machine a physical body. The same principles, scaled up from relays to vacuum tubes to transistors, underlie every digital computer, including those that train and run the [[transformer-architecture]] (see [[petzold-2023]] for the full hardware story).

Shannon's relay circuits are, in effect, the electrical miniaturization of the mechanical logic that Babbage built into the [[analytical-engine]] ([[babbage-1837]]). Where Babbage used gears, levers, and barrels to implement arithmetic and conditional branching, Shannon showed the same operations could be accomplished with switches and wires governed by [[boolean-algebra]].

## Legacy

Shannon's thesis has been called "possibly the most important, and also the most famous, master's thesis of the century" (Howard Gardner). The techniques it introduced remain the basis of digital logic design. Shannon went on to found [[information-theory]] a decade later with his 1948 paper (see [[shannon-1948]]).

## From relay logic to relay computers

Shannon's switching theory was almost immediately put to work in actual computing machines. George Stibitz at Bell Telephone Laboratories built the Model K (1937) and the Complex Number Computer (1940) using exactly the relay-and-Boolean-algebra principles Shannon had formalised; subsequent Bell Labs Models II-V (1943-1946) were full programmable relay computers, documented in Chapter 6 of [[randell-1973]]. [[harvard-mark-i|Howard Aiken's Harvard Mark I]] (1944) and [[zuse-z3|Konrad Zuse's Z3]] (1941) -- the latter built in Berlin without knowledge of Shannon's thesis but arriving at the same synthesis -- were the major programmable relay computers of the 1940s. The transition from relays to vacuum tubes ([[colossus]], [[eniac]]) and then to transistors did not change the underlying Boolean logic; Shannon's isomorphism survives every change of switching element.

## Related pages

- [[boolean-algebra]]
- [[boole-1854]]
- [[turing-1936]]
- [[petzold-2023]]
- [[shannon-1948]]
- [[information-theory]]
- [[analytical-engine]]
- [[babbage-1837]]
- [[harvard-mark-i]]
- [[zuse-z3]]
- [[colossus]]
- [[eniac]]
- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[randell-1973]]
