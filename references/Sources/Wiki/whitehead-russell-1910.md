# Principia Mathematica (Whitehead & Russell, 1910)

**Summary**: Alfred North Whitehead and Bertrand Russell's monumental three-volume work attempts to derive all of mathematics from purely logical axioms, introducing the theory of types and establishing the program of logicism.

**Sources**: Principia Mathematica, vol. 1 (of 3).epub

**Last updated**: 2026-05-11

---

## Context

After Russell discovered his paradox in Frege's system (1901) — see [[russells-paradox]] and [[russell-1902]] — he and Whitehead spent a decade constructing a logical system immune to such contradictions. *Principia Mathematica* (PM) is the result: three volumes published between 1910 and 1913, running to nearly 2,000 pages. It famously takes until page 362 of Volume 1 to prove that 1 + 1 = 2 (source: Principia Mathematica, vol. 1 (of 3).epub).

## Key contributions

### The theory of logical types

PM's central innovation is a hierarchy of types designed to block self-referential paradoxes. Individuals are type 0, sets of individuals are type 1, sets of sets are type 2, and so on. A set can only contain members of a lower type, so the "set of all sets that do not contain themselves" becomes an ill-formed expression — it violates the type constraints. This idea recurs throughout computer science in type systems for programming languages (source: Principia Mathematica, vol. 1 (of 3).epub).

### The vicious-circle principle

The foundation of the type theory is the vicious-circle principle: "Whatever involves all of a collection must not be one of the collection." If defining something requires referring to a totality, then that something cannot be a member of that totality. PM applies this principle systematically to propositions, propositional functions, and classes (source: Principia Mathematica, vol. 1 (of 3).epub).

### Logicism

PM embodies the philosophical program of logicism: the claim that all mathematical truths are logical truths, derivable from purely logical axioms using purely logical rules of inference. While Gödel's [[incompleteness]] theorems (1931; see [[godel-1931]]) showed this program cannot fully succeed — any consistent system powerful enough to express arithmetic contains true statements it cannot prove — PM remains the most thorough attempt at the program.

### Notation and formalism

PM introduced much of the logical notation still used today (with modifications), including the use of dots for conjunction, the horseshoe ⊃ for material implication, and systematic use of bound variables. The work demonstrated that an enormous body of mathematics could, in principle, be checked by purely mechanical means — a theme that directly influenced Turing's thinking about [[computability]] (source: Principia Mathematica, vol. 1 (of 3).epub).

## Significance for the book's arc

PM is the crucial middle link between Frege's formal logic ([[frege-1879]]) and Turing's theory of computation ([[turing-1936]]). Hilbert and Ackermann codified PM's logic into a clean textbook ([[hilbert-ackermann-1928]]) and posed the [[entscheidungsproblem]]. Gödel's 1931 paper ([[godel-1931]]) — whose title explicitly references *Principia Mathematica* — showed that PM's axioms are [[incompleteness|incomplete]]. Turing's 1936 paper responded to Gödel by defining computability precisely and proving the Entscheidungsproblem undecidable, inventing the [[turing-machine]] in the process.

## Limitations

- Gödel's [[incompleteness]] theorems (1931; see [[godel-1931]]) showed that PM's axioms are necessarily incomplete: there are true arithmetical statements that cannot be proved within the system.
- The axiom of reducibility, needed to make the ramified type theory workable, was controversial — many logicians saw it as ad hoc.
- The sheer scale and difficulty of the work meant few people ever read it cover to cover.

## Related pages

- [[formal-system]]
- [[predicate-logic]]
- [[frege-1879]]
- [[russell-1902]]
- [[russells-paradox]]
- [[hilbert-ackermann-1928]]
- [[godel-1931]]
- [[incompleteness]]
- [[turing-1936]]
- [[entscheidungsproblem]]
- [[computability]]
- [[boolean-algebra]]
