# Wiki Index

**Summary**: Table of contents for the source wiki accompanying *When Attention Becomes Thought*.

**Last updated**: 2026-05-12

---

## Source summaries

### The mechanical origins of computing
- [[babbage-1837]] -- Babbage's *On the Mathematical Powers of the Calculating Engine*: the Mill-and-Store architecture of the Analytical Engine (1837)
- [[lovelace-1843]] -- Lovelace's translation of Menabrea with Notes A-G: the first computer program and the insight that machines can manipulate symbols, not just numbers (1843)
- [[hollerith-1889]] -- Hollerith's electric tabulating system for the 1890 US Census: the founding of what became IBM (1889)
- [[randell-1973]] -- Randell's anthology *The Origins of Digital Computers*: roughly thirty primary documents tracing the route from Babbage to EDSAC (1973)

### Foundational logic and mathematics
- [[cantor-1891]] -- Cantor's *Ueber eine elementare Frage der Mannigfaltigkeitslehre*: the diagonal argument and the uncountability of the reals (1891)
- [[frege-1879]] -- Frege's *Begriffsschrift*: the invention of modern predicate logic (1879)
- [[boole-1854]] -- Boole's *Laws of Thought*: Boolean algebra as the foundation of digital logic (1854)
- [[russell-1902]] -- Russell's letter to Frege communicating Russell's paradox (1902)
- [[whitehead-russell-1910]] -- Whitehead & Russell's *Principia Mathematica*: deriving mathematics from logic (1910)
- [[hilbert-ackermann-1928]] -- Hilbert & Ackermann's *Principles of Mathematical Logic*: systematizing logic, posing the Entscheidungsproblem (1928)
- [[godel-1931]] -- Gödel's *On Formally Undecidable Propositions*: the incompleteness theorems (1931)
- [[turing-1936]] -- Turing's *On Computable Numbers*: the Turing machine and the limits of computation (1936)

### The bridge to hardware
- [[shannon-1938]] -- Shannon's master's thesis: Boolean algebra maps onto switching circuits (1938)
- [[petzold-2023]] -- Petzold's *Code*: from flashlights to a complete CPU (2nd ed., 2023)

### From relays to stored programs
- [[zuse-z3]] -- Zuse's relay computer in wartime Berlin: first programmable, binary, floating-point machine (1941)
- [[harvard-mark-i]] -- Aiken and IBM's Automatic Sequence Controlled Calculator: Babbage's design built with electromechanical relays (1944)
- [[colossus]] -- Flowers's electronic codebreaking machines at Bletchley Park: first large-scale digital electronics, kept secret until 1972 (1944)
- [[eniac]] -- The Moore School's general-purpose electronic computer: 17,000 vacuum tubes, plug-board programmed (1946)
- [[edvac]] -- Von Neumann's *First Draft*: the design document that defined the stored-program architecture (1945)
- [[manchester-baby]] -- Williams and Kilburn's Small-Scale Experimental Machine: first to run a program from electronic memory (June 1948)
- [[edsac]] -- Wilkes's Cambridge machine: first stored-program computer in routine scientific service (May 1949)

### Information theory
- [[shannon-1948]] -- Shannon's *Mathematical Theory of Communication*: bits, entropy, and channel capacity (1948)

### The Transformer
- [[vaswani-et-al-2017]] -- Vaswani et al.'s *Attention Is All You Need*: the Transformer architecture (2017)

### AI and the Turing test
- [[jones-bergen-2025]] -- Jones & Bergen: LLMs pass the three-party Turing test (2025)
- [[chen-et-al-2026]] -- Chen, Belkin, Bergen & Danks: the case that AGI has been achieved (*Nature*, 2026)

### AI capabilities and society
- [[chakrabarty-et-al-2026]] -- Study showing fine-tuned AI writing is preferred over expert human writers
- [[bubeck-et-al-2025]] -- Case studies of GPT-5 accelerating scientific research across math, physics, biology, and CS

## Concepts

### Machines and architecture
- [[analytical-engine]] -- Babbage's design for a general-purpose mechanical computer with Mill (processor) and Store (memory)
- [[ada-lovelace]] -- The first computer programmer; recognized that computing machines operate on symbols, not just numbers
- [[stored-program-computer]] -- A computer that holds its program in the same memory as its data, allowing code to be loaded, modified, and computed on
- [[von-neumann-architecture]] -- The canonical organisation: shared memory, fetch-decode-execute control, binary arithmetic

### Logic and formal systems
- [[predicate-logic]] -- The branch of logic with quantifiers and predicates, invented by Frege
- [[boolean-algebra]] -- The two-valued algebraic system (AND, OR, NOT) underlying digital logic
- [[formal-system]] -- A set of symbols, rules, and axioms forming a self-contained deductive apparatus
- [[russells-paradox]] -- The set of all sets that don't contain themselves: the contradiction that broke Frege's system
- [[diagonal-argument]] -- Cantor's proof technique: construct an element that escapes any proposed listing
- [[uncountability]] -- The property of a set too large to be listed by the natural numbers
- [[incompleteness]] -- The property of a formal system that contains true statements it cannot prove
- [[godel-numbering]] -- Encoding symbols, formulas, and proofs as natural numbers for self-reference
- [[entscheidungsproblem]] -- Hilbert's decision problem, proved unsolvable by Turing in 1936

### Computation
- [[turing-machine]] -- Turing's abstract computing device: tape, head, states, and transition table
- [[universal-machine]] -- A Turing machine that can simulate any other Turing machine
- [[computability]] -- The study of which problems can be solved by mechanical procedures

### Information theory
- [[information-theory]] -- Shannon's mathematical framework for quantifying and transmitting information
- [[information-entropy]] -- The measure of average information content per symbol, in bits
- [[channel-capacity]] -- The maximum rate of reliable communication over a noisy channel

### Transformer internals
- [[transformer-architecture]] -- The attention-only neural network architecture underlying all modern LLMs
- [[self-attention]] -- The mechanism by which each position attends to all others in a sequence
- [[multi-head-attention]] -- Parallel attention in multiple learned subspaces
- [[positional-encoding]] -- Injecting sequence-order information into the Transformer

### AI evaluation
- [[turing-test]] -- Turing's test of machine intelligence, passed by GPT-4.5 in 2025

### AI capabilities and society
- [[fine-tuning]] -- Training a pre-trained model further on a narrow dataset to specialize its outputs
- [[ai-creative-writing]] -- The capacity of language models to produce literary fiction and creative nonfiction
- [[copyright-and-ai]] -- Legal questions around training on copyrighted works and market substitution
- [[ai-detection]] -- Tools and methods for distinguishing AI-generated text from human writing
- [[ai-scientific-research]] -- How frontier models contribute to active research across disciplines
- [[scaffolding-and-prompting]] -- Techniques for structuring AI interactions to elicit better results
- [[human-ai-collaboration]] -- Patterns of productive partnership between domain experts and AI systems
- [[gpt-5]] -- OpenAI's frontier model as of late 2025, central to the science acceleration paper
- [[frontier-models]] -- The most capable AI systems at any given time and what defines the frontier
