# Reading notes: Chapter 3 (The Neuron and the Computer)

*One entry per paper, in reading-list order. Fill the seven fields during reading nights. The synthesis block at the bottom is for synthesis night, after all entries are complete.*

*Matches the chapter file at `src/ch03-neuron-and-the-computer.md` and the reading list in `FINISHING_PLAN.md`.*

---

## McCulloch & Pitts (1943): A Logical Calculus of the Ideas Immanent in Nervous Activity
**Link.** [doi:10.1007/BF02478259](https://doi.org/10.1007/BF02478259). *Bulletin of Mathematical Biophysics*, 5(4), 115-133.
*Read as the chapter opener. Computing and neuroscience were entangled from the start: McCulloch (a neuropsychiatrist) and Pitts (a logician) showed that networks of simple threshold units can compute any logical function. Two years later von Neumann uses their vocabulary in the First Draft. Use this entry to anchor the chapter's claim that neural-network thinking predates computers, not the other way around.*

**One-sentence thesis.** Because neurons fire all-or-none, the activity of any nervous net can be written as a proposition in two-valued logic, which means brains are formal logical machines and (when paired with structured environment) are Turing-complete.

**What it argues.** The all-or-none firing law lets every neuron be represented as a proposition asserting its adequate stimulus, so feedforward nets correspond exactly to Boolean formulas and looped nets correspond to finite state machines whose behavior must be expressed via existential quantification over state-histories. The bridge runs both ways: any net's behavior reduces to a logical expression, and any logical expression meeting causality and a recursive realizability condition can be built as a net. The reductive payoff is that mental life, in any of its branches, can be deduced from neurophysiology with no remainder.

**The evidence.** The paper is theorem-driven, not data-driven. The empirical inputs are the neurophysiological constants used as boundary conditions: latent addition window ~0.25 ms, synaptic delay >0.5 ms, sub-1 ms inhibition (which had recently ruled out the older internuncial-only account), and absolute refractoriness during firing. The mathematical evidence is Theorems 1 through 10, especially Theorem 7's reduction of alterable synapses to circles, Theorem 8's existence of solutions for looped nets, Theorem 9's complete (but 2^{2^n}-sized) characterization of realizable behavior, and Theorem 10's practical recursive recipe. The Turing-equivalence claim at the end of Section 3 is asserted rather than proved here. Clinical phenomena (tinnitus, paraesthesias, hallucinations, eyewitness contradiction, memory inaccuracy) are offered as informal confirmation of the irreciprocity of causality.

**Pull quotes.**
- "Because of the 'all-or-none' character of nervous activity, neural events and the relations among them can be treated by means of propositional logic." (p. 99)
- "With determination of the net, the unkowable object of knowledge, the 'thing in itself,' ceases to be unknowable." (p. 113)

**Connections.**
*Depends on:* Russell and Whitehead's *Principia Mathematica* for the propositional formalism and dot conventions; Carnap's *Logical Syntax of Language* (Language II) for the metalogical notation; Turing's 1936 paper for the standard of computability; the neurophysiological tradition that established all-or-none firing (Adrian and others).
*Makes possible:* Von Neumann's *First Draft of a Report on the EDVAC* (1945), which adopts the McCulloch-Pitts neuron as the abstract logical element; Wiener's *Cybernetics* (1948), which extends the feedback-and-purpose paragraphs of Section 4; Hebb's *Organization of Behavior* (1949), which fills in the learning rule that Theorem 7 deliberately avoids; Kleene's 1951 work on regular events and finite automata, which formalizes what looped nets actually compute; Rosenblatt's perceptron (1958); and the entire computational theory of mind.

**What confused me / what I want to verify.**
- The Turing-equivalence claim is dropped in casually at the end of Section 3. Where is it actually proved? Kleene 1951 seems like the likely formalization but I want to check.
- Theorem 9's decidability is technically true but useless at 2^{2^n} class enumerations. Is there modern work that gives a better characterization, or does the practical answer just become "use Theorem 10 plus regular language theory"?
- The reduction "psychon = single neuron firing" looks shakier given what we now know about glia, neuromodulation, ephaptic coupling, and population coding. What does the equivalent claim look like in 2026 terms?
- Theorem 7 says learning can be replaced by circles. Hebb's rule says learning is synaptic plasticity. Are these compatible views or rival ones? How did the field reconcile them?
- The Carnap Language II notation is genuinely hard to read. Worth a sidebar on what was lost when this notation fell out of use.

**Teaching angle.** In 1943 a neuropsychiatrist and a homeless teenage logician working at Chicago figured out that because neurons fire in binary, the brain does the same kind of math you find in a logic textbook. Two years later von Neumann picked up their notation to describe the first stored-program computer. So when people say computers were inspired by brains, they're being more literally accurate than they probably realize. The same paper also quietly dissolves Kant's noumenon problem, foreshadows cybernetics, and tells Freud his patient histories aren't strictly necessary for prognosis. Not bad for fifteen pages.

---

## von Neumann (1945): First Draft of a Report on the EDVAC
**Link.** [PDF (MIT mirror)](https://web.mit.edu/sts.035/www/PDFs/edvac.pdf). Moore School of Electrical Engineering, University of Pennsylvania.

*Read as architectural background. This is not a paper in the technical lineage of attention. It is the founding statement of stored-program, sequential-fetch computation, the prior the rest of the chapter is working against.*

**One-sentence thesis.** Von Neumann argues that a high-speed computing machine should be specified at the level of propositional logic over idealized neurons rather than at the level of physical components, and that its operation should consist of a control unit attending sequentially to instructions stored in a single unified memory alongside the numerical data those instructions act upon.

**What it argues.** Two stacked abstractions. First, the elements of the machine are to be McCulloch-Pitts threshold neurons (E-elements) firing on a synchronous clock, so the design becomes a propositional-logic problem independent of whether vacuum tubes, relays, or any other substrate ultimately realizes it. Second, the program itself lives in memory as binary words distinguished from numerical data by a single leading bit. Programs and data live in the same place, are made of the same stuff (binary words), and are accessed by the same mechanism. The control unit reads a word, and a single leading bit tells it whether it is being told what to do or being given something to compute on. Together these two abstractions yield a machine whose entire next state is determined by which address its control unit is currently attending to.

**The evidence.** This is a design paper, not an experimental one. Its "evidence" is engineering analysis applied at every step. Quantities to keep handy: vacuum-tube synaptic delay τ on the order of one microsecond (10⁻⁶ s); 30-bit standard numbers; ~1,000 to 1,500 elementary steps per multiplication; total memory target of 2¹⁸ ≈ 262,144 bits, organized as 8,192 minor cycles of 32 bits each across ~256 delay-line organs of 1,024-bit capacity; ~1,000 vacuum tubes for CA and CC combined versus ~2,500 for memory (so the machine is mostly memory). Every architectural decision is derived from these numbers: binary because tubes are two-state, serial because element-count economy, clock synchrony because real neural delays would jitter the logic past usability.

**Pull quotes.**
- "the neurons of the higher animals are definitely elements in the above sense" (§4.2, p. 5).
- McCulloch-Pitts citation immediately following the above. (§4.2, p. 5.) [Copy when transcribing.]
- The "main bottleneck ... at the memory" sentence in §12.4 (p. 28). [Copy.]
- The orders-vs-numbers definition in §15.1 (p. 39): the stored-program concept in one sentence, where i₀ = 0 marks a number and i₀ = 1 marks an order. [Copy.]
- The "exclusion of a dispersion" passage on the dispersionless synaptic delay τ in §6.3 (p. 9). [Copy. This is the line that makes the propositional-logic abstraction tractable.]

**Connections.** Depends on McCulloch & Pitts (1943, "A logical calculus of the ideas immanent in nervous activity") for the neural primitive; depends on Boolean logic and binary arithmetic; tacitly depends on Turing 1936 for the conceptual horizon of universality, though Turing is never cited. Makes possible: every subsequent von Neumann architecture machine; the conceptual frame in which Turing 1950 ("Computing Machinery and Intelligence") becomes a coherent question; the symbol-processing view of mind in mid-twentieth-century cognitive science; and, one step further out, the transformer's attention mechanism as a soft, parallel, learned generalization of EDVAC's address register pointing into M.

**Sidebar candidates.**
- *The §7.3 adder as worked example of the abstraction in action.* Three E-elements with thresholds 1, 2, 3 receive the same three inputs (the two addend bits plus a carry-in held in a τ-delay loop). The threshold-2 element directly **is** the carry-out (fires iff at least two of three inputs are 1). The sum bit is the propositional formula sum = (P ∧ ¬Q) ∨ R, where P, Q, R are the threshold-1, 2, 3 elements firing on the same inputs. This is binary addition rewritten as a sentence in propositional logic over neurons, with one bit of state held in a feedback loop, evaluated once per τ. The hardware question has been completely deferred. Use this in the chapter to show the abstraction concretely rather than asserting it.
- *Is this the first concrete explanation of programming?* Pre-EDVAC machines were "programmed" by physical rewiring (ENIAC plugboards) or by feeding a card-by-card sequence of fixed operations (Babbage, IBM tabulators). What §15 introduces is something stronger: a symbolic instruction format in which orders are linguistic objects (binary words with a defined syntax), stored alongside data, fetched by attention, and executable in arbitrary sequence. That is much closer to "programming" in the modern sense than anything that came before. Worth tracing the historiographical claim: where do scholars (Aspray, Mahoney, Priestley) place the origin of "programming as a concept"? Verify whether §15 is in fact treated as the founding moment, or whether earlier texts (Turing 1936, Zuse, Aiken) are credited.
- *Where universality enters.* Turing is never named. Is universality implicit in the §15 code structure, or does it need to be imported from Turing 1936 to be claimed?

**What confused me / what I want to verify.**
- The E-element diagram syntax. Resolved: small open circle at the line junction = inhibitory synapse; plain line = excitatory; threshold is the number of tick-marks inside the circle (1, 2, or 3); an arrowhead on a line = a τ delay; double arrowhead = 2τ; inhibition is absolute (one inhibitory pulse vetoes firing regardless of excitatory count); junctions are bidirectional except at the three connection points of the E-element itself.
- Conflated τ with memory-loop time. τ is the elementary tick (one E-element's synaptic delay). A memory loop is some integer multiple of τ. The clock's deep job is to make time discrete, which is what makes propositional logic over neurons computable as a discrete dynamical system.
- The relation between the §4 abstraction and the §15 stored-program move. They are layered, not parallel: §4 makes the components formal, §15 makes the behavior formal, and §15 is only possible because §4 has already turned the substrate into a logic-evaluating medium capable of interpreting a stored program at all.
- Open research question: if EDVAC is the architectural prior the chapter is working against, what specifically is being challenged? The single-address sequential-attention model? The programmer-stipulated semantics of stored content (versus trained, statistical content in LLMs)? The symbol-grounding asymmetry between stipulated and learned representations? Each targets a different layer of von Neumann's stack and would generate a different argument.

**Teaching angle.** "Before EDVAC, programming a computer meant physically rewiring it. Von Neumann's idea was to put the program inside the same memory as the data, distinguished by a single leading bit, so the machine's behavior becomes a symbolic formula it reads out of itself. For that to work he first had to redescribe the machine's components as idealized neurons doing propositional logic, so the substrate would be flexible enough to interpret a stored program at all. The result is a machine whose 'attention' is a register pointing at a word in memory, and whose 'thinking' is whatever logical operation that word names. That architecture is the ancestor of every computer since, and it's the moment in the historical record when 'does this machine think?' becomes a coherent question instead of a category mistake."
---

## Godfrey & Hendry (1993): The Computer as von Neumann Planned It

**Link.** [PDF (Stanford mirror)](http://cva.stanford.edu/classes/cs99s/papers/godfrey-computer-as-von-neumann-planned-it.pdf). *IEEE Annals of the History of Computing*, 15(1), 11-21. [doi:10.1109/85.194088](https://doi.org/10.1109/85.194088).

*Read as historiographical correction to the First Draft. The standard "von Neumann bottleneck" story is partly an artifact of what was actually built (IAS, EDVAC-as-constructed). Use this entry to record where the popular caricature diverges from von Neumann's actual proposal, so the chapter's interpretive claims about "the von Neumann prior" are defensible.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{{quote}}" (p. {{n}})
- "{{quote}}" (p. {{n}})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---


---

## Synthesis

*Fill on synthesis night, after all entries above are complete. The questions below are prompts, not a fixed schema.*

**The arc.** What story do these papers tell when read in order? One paragraph.

**Worked examples to commit to.** What propositional-logic circuits or pseudocode blocks does this chapter need? List them so writing nights have something to draft against.

**Connections backward.** What from earlier chapters does this chapter assume the reader has already met? Name the specific concept and the chapter where it was introduced.

**Connections forward.** What does this chapter set up that a later chapter will pay off? Name the chapter and the move.

**Sidebar candidates.** Confusions and verifications from individual entries that deserve a callout box rather than the main text.

**Open threads.** Claims I want to make in prose that the reading does not yet support. What further reading or verification is needed?
