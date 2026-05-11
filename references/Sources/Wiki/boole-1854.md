# An Investigation of the Laws of Thought (Boole, 1854)

**Summary**: George Boole's treatise establishes that the laws of human reasoning can be expressed as algebraic equations over the values 0 and 1, founding Boolean algebra and laying the mathematical groundwork for all digital computing.

**Sources**: An Investigation of the Laws of Thought.pdf

**Last updated**: 2026-05-11

---

## Context

Boole was Professor of Mathematics at Queen's College, Cork. His earlier pamphlet *The Mathematical Analysis of Logic* (1847) sketched the core idea; *The Laws of Thought* is the mature, extended treatment. The book's full title — *An Investigation of the Laws of Thought, on Which are Founded the Mathematical Theories of Logic and Probabilities* — signals its dual ambition: to algebraize both logic and probability theory (source: An Investigation of the Laws of Thought.pdf).

## Key contributions

### Boolean algebra

Boole introduces a symbolic system where classes of objects are represented by letters (x, y, z) and logical operations by algebraic operations:

- **AND** (intersection): xy means "things that are both x and y"
- **OR** (union): x + y means "things that are x or y"
- **NOT** (complement): 1 − x means "things that are not x"
- **Nothing**: 0 represents the empty class
- **Everything**: 1 represents the universe of discourse

The fundamental law that distinguishes Boolean algebra from ordinary algebra is the **idempotent law**: x² = x. A thing that is both "white" and "white" is simply "white." This single property, which does not hold for ordinary numbers (except 0 and 1), is what restricts the system to the values {0, 1} (source: An Investigation of the Laws of Thought.pdf).

### Logic as calculation

Boole demonstrates that syllogisms and other logical arguments can be solved by writing them as equations and applying algebraic manipulations — expansion, elimination of middle terms, reduction. This transforms logic from a philosophical art into a mechanical procedure, anticipating the idea of [[computability]] (source: An Investigation of the Laws of Thought.pdf).

### Probability as logic

The second half of the book extends the algebraic framework to probability, treating probability as a generalization of logic where truth values are replaced by degrees of belief. This is less well-remembered but historically significant for the Bayesian tradition (source: An Investigation of the Laws of Thought.pdf).

## The bridge to hardware

Boole's algebra remained a purely mathematical curiosity for 84 years — until Claude Shannon showed in his 1938 master's thesis (see [[shannon-1938]]) that Boolean algebra maps directly onto relay switching circuits. Every AND becomes a series circuit, every OR a parallel circuit, every NOT an inverter. This insight made digital computing physically possible.

## Limitations

Boole's system is propositional: it can express "all men are mortal" but cannot analyze the internal structure of predicates involving "all" and "some." That required Frege's invention of [[predicate-logic]] in the *Begriffsschrift* (see [[frege-1879]]). Boole also lacked a clear distinction between a logical system and its interpretation — a distinction that later became central to [[formal-system]] theory.

## Related pages

- [[boolean-algebra]]
- [[shannon-1938]]
- [[frege-1879]]
- [[formal-system]]
- [[computability]]
- [[predicate-logic]]
