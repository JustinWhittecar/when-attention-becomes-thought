# Boolean Algebra

**Summary**: A mathematical system for reasoning with two values (0 and 1) using the operations AND, OR, and NOT — the foundation of digital logic and circuit design.

**Sources**: An Investigation of the Laws of Thought.pdf, A Symbolic Analysis of Relay and Switching Circuits.pdf, Code the hidden language of computer hardware and software.pdf

**Last updated**: 2026-05-11

---

## Definition

Boolean algebra is an algebraic structure over the set {0, 1} with three operations:

- **AND** (conjunction, ·): returns 1 only if both operands are 1
- **OR** (disjunction, +): returns 1 if at least one operand is 1
- **NOT** (negation, ′): returns the opposite value

These operations satisfy a set of laws including commutativity, associativity, distributivity, identity, complement, and — crucially — the **idempotent law**: x · x = x. This law distinguishes Boolean algebra from ordinary algebra and restricts the system to the values {0, 1} (source: An Investigation of the Laws of Thought.pdf).

## Origins

George Boole introduced the algebra in *An Investigation of the Laws of Thought* (1854; see [[boole-1854]]). His original formulation used classes of objects rather than truth values: x represents a class, xy represents the intersection of classes x and y, and x + y their union. The fundamental law x² = x expresses the fact that the class of things that are both "white and white" is just the class of "white" things (source: An Investigation of the Laws of Thought.pdf).

## Key laws

| Law | AND form | OR form |
|---|---|---|
| Identity | x · 1 = x | x + 0 = x |
| Null | x · 0 = 0 | x + 1 = 1 |
| Idempotent | x · x = x | x + x = x |
| Complement | x · x′ = 0 | x + x′ = 1 |
| Commutative | xy = yx | x + y = y + x |
| Associative | (xy)z = x(yz) | (x+y)+z = x+(y+z) |
| Distributive | x(y+z) = xy + xz | x + yz = (x+y)(x+z) |
| De Morgan's | (xy)′ = x′ + y′ | (x+y)′ = x′y′ |

De Morgan's laws are particularly important for circuit design: they show that any circuit built from AND and NOT gates can be rebuilt using OR and NOT gates, and vice versa (source: An Investigation of the Laws of Thought.pdf).

## From algebra to circuits

For 84 years, Boolean algebra remained abstract mathematics. In 1938, Claude Shannon demonstrated that Boolean variables map directly onto relay contacts (see [[shannon-1938]]):

- Variable = 1 ↔ relay closed (current flows)
- Variable = 0 ↔ relay open (no current)
- AND ↔ series connection
- OR ↔ parallel connection
- NOT ↔ normally-closed contact

This isomorphism meant that every theorem of Boolean algebra was immediately a theorem about circuits, and every circuit could be analyzed algebraically. Modern logic gates (AND, OR, NOT, NAND, NOR, XOR) are direct hardware implementations of Boolean operations (source: A Symbolic Analysis of Relay and Switching Circuits.pdf).

## In modern computing

Boolean algebra underlies:

- **Logic gate design**: All digital circuits are compositions of Boolean operations ([[petzold-2023]])
- **CPU arithmetic**: Addition, subtraction, and comparison are built from Boolean gates
- **Programming languages**: Boolean expressions control if-statements, while-loops, and conditionals
- **Database queries**: SQL WHERE clauses are Boolean expressions
- **Search engines**: Query operators AND, OR, NOT

(source: Code the hidden language of computer hardware and software.pdf)

## Related pages

- [[boole-1854]]
- [[shannon-1938]]
- [[petzold-2023]]
- [[formal-system]]
- [[predicate-logic]]
- [[analytical-engine]]
- [[babbage-1837]]
