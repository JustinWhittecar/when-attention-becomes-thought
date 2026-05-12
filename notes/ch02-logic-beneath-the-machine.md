# Reading notes: Chapter 2 (The Logic Beneath the Machine)

*One entry per paper, in reading-list order. Fill the seven fields during reading nights. The synthesis block at the bottom is for synthesis night, after all entries are complete.*

*Matches the chapter file at `src/ch02-logic-beneath-the-machine.md` and the reading list in `FINISHING_PLAN.md`.*

---

## Babbage (1837): On the Mathematical Powers of the Calculating Engine

**Link.** In Brian Randell (ed.), *The Origins of Digital Computers: Selected Papers*, 3rd ed., Springer 1982, pp. 19-54. [doi:10.1007/978-3-642-61812-3_2](https://doi.org/10.1007/978-3-642-61812-3_2). Manuscript dated 26 December 1837; first published by Allan Bromley in 1973.

*Mechanical computation's first full articulation, including the conditional branch and the loop. Read for the mill-and-store proto-architecture that von Neumann revisits a century later, and to see how far mechanism can go without a formal theory of computation behind it.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Lovelace (1843): Sketch of the Analytical Engine, with Notes by the Translator

**Link.** L. F. Menabrea, *Sketch of the Analytical Engine Invented by Charles Babbage*, translated and annotated by Ada Augusta, Countess of Lovelace. Originally in *Scientific Memoirs*, vol. 3 (1843), pp. 666-731. Reprinted with postscript in *IEEE Annals of the History of Computing* offprints, [TCD mirror](https://publications.scss.tcd.ie/kronos/A_Lovelace_offprints_IEEE_plus_postscript.pdf).

*Read the Notes, especially Note A (on the distinction between the engine and what it computes) and Note G (Bernoulli numbers, and the famous denial that the engine can originate anything). The first treatment of programming as a symbolic activity distinct from the underlying mechanism, and the limit Turing later answers from the other side.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Boole (1854): An Investigation of the Laws of Thought

**Link.** [Project Gutenberg](https://www.gutenberg.org/ebooks/15114).

*Read the introduction and Chapter II ('Of Signs in General'). The founding text. Read for the move from 'logic is an art' to 'logic is a calculus.'*

**One-sentence thesis.** Reasoning obeys laws as formal as those of arithmetic, and once propositions and classes are encoded as algebraic symbols obeying a single new rule (idempotence, x² = x), the entire apparatus of ordinary algebra becomes a calculus of thought operating on a two-valued structure.

**What it argues.** Boole argues that logic is not an art of correct reasoning but a science of laws, and that those laws are best expressed in the symbolic language of algebra. Operations on classes (intersection, disjoint union, complement) are represented by the algebraic operations of multiplication, addition, and subtraction, with one departure from ordinary algebra: the idempotent law x² = x. Because that equation has only the roots 0 and 1 in ordinary arithmetic, the algebra of thought is forced into a two-valued structure. The metaphysical question of whether the signs represent things in the world or conceptions in the mind is deliberately bracketed; what matters is the laws the signs obey, not what they ultimately denote.

**The evidence.** Not empirical. The case is made by demonstration: Boole derives the algebraic laws (commutativity xy = yx, distributivity x(y + z) = xy + xz, idempotence x² = x) from the operation of class selection, shows that natural-language connectives ("and", "or") can be reduced to + and ×, reduces all verbs to the substantive verb "is" plus a class symbol, and exhibits worked examples in which classical syllogisms fall out as algebraic manipulations. The persuasive force is the internal consistency and reach of the system, not data.

**Pull quotes.**

- "A sign is an arbitrary mark, having a fixed interpretation, and susceptible of combination with other signs in subjection to fixed laws dependent upon their mutual interpretation." (p. 18)
- "the equation x² = x, considered as algebraic, has no other roots than 0 and 1." (p. 26)
- "Language is an instrument of human reason, and not merely a medium for the expression of thought, is a truth generally admitted." (p. 17)
- "whether we regard signs as the representatives of things and of their relations, or as the representatives of the conceptions and operations of the human intellect, in studying the laws of signs, we are in effect studying the manifested laws of reasoning." (p. 17)

**Connections.** Depends on Aristotelian term logic (refined through Whately and Thomson, whom Boole cites as expected background) and on the eighteenth and nineteenth century algebraic tradition that had already abstracted operations away from numerical content. Makes possible Frege's predicate logic in 1879 (which fills the gap Boole's term logic cannot: relations and quantifiers), Shannon's switching algebra in 1937 (which recognizes that electrical circuits are another instantiation of the same two-valued algebra), and the entire project of mechanizing inference that culminates in Turing's universal machine and modern computing. The substrate-independent character of Boole's laws is also the implicit groundwork for twentieth century functionalism in philosophy of mind.

**What confused me / what I want to verify.**

- Boole's + is exclusive disjunction with the awkward constraint that the addends must be disjoint classes; inclusive "or" has to be derived as x + y(1 - x). When and how does this get cleaned up into the modern Boolean algebra where + is inclusive OR by default? (Likely Jevons and Schröder, late nineteenth century. Verify.)
- The reduction of all verbs to "is" plus a class symbol cannot cleanly express two-place relations like "John loves Mary." This is the limitation that motivates Frege's *Begriffsschrift* and predicate logic. Strong sidebar candidate, since it is the through-line from this entry to the next.
- Boole's claim that linguistic universals point to "some deep foundation of agreement in the laws of the mind itself" prefigures Chomsky's universal grammar and the computational theory of mind. Verify the citation chain in Chomsky's *Cartesian Linguistics*.
- The metaphysical neutrality (signs as things vs. signs as conceptions) is a strategic move that buys substrate independence: the same formal structure can be instantiated in marks on paper, neurons, electrical switches, transistors. Worth examining in the final chapters whether modern LLMs put this neutrality under pressure: when a transformer manipulates token embeddings, what are those tokens *of*?
- Note correction to my reading notes: xy = yx is the *commutative* law, not "the law of equivalence." The law of equivalence is x = x.

**Teaching angle.** The whole chapter turns on one observation. Boole notices that if you treat classes as algebraic symbols, selecting "things that are x and x" gives back just "things that are x." In symbols: x times x equals x. In ordinary arithmetic that equation has only two solutions, 0 and 1. So the algebra of thought is forced to be a two-valued algebra. From there everything else follows: classes become 0s and 1s, propositions become 0s and 1s, switches become 0s and 1s, transistors become 0s and 1s. Boole did not intend to invent the computer, but he wrote down its formal substrate eighty years before anyone built one. When Shannon shows in 1937 that wiring switches in series behaves like multiplication and wiring them in parallel behaves like addition, he is not translating Boole into hardware; he is noticing that the hardware was already obeying Boole's laws.

---

## Frege (1879): Begriffsschrift

**Link.** English translation in van Heijenoort (Ed.), *From Frege to Gödel*, Harvard University Press, 1967.

*Read the preface and the propositional fragment. The first complete formalization of inference. Skim the rest.*

**One-sentence thesis.** Inference itself can be reduced to the manipulation of formal symbols according to explicit rules, and once you build a notation precise enough to make every step of a proof mechanically checkable, logic becomes a calculus you could in principle hand to a machine.

**What it argues.** Frege argues that ordinary language is too ambiguous and context-dependent to support rigorous proof, and that mathematics in particular requires a notation in which every inferential gap is visible. He builds such a notation, a two-dimensional "concept-script," from two primitive signs (the conditional and negation) plus two structural strokes: a content stroke that marks a content as judgeable, and a judgment stroke that asserts it. On this base he gives a small set of axioms and a single rule of inference (modus ponens), then derives a substantial body of logic from it. The deeper philosophical claim, defended later in the *Grundlagen* (1884), is that arithmetic is analytic in a reformed Kantian sense: derivable from logic alone, without appeal to intuition. *Begriffsschrift* is the notational machinery that makes that claim even checkable.

**The evidence.** Not empirical. The case is made by demonstration. Frege exhibits a complete formal system, namely primitive signs, axioms, one inference rule, and a worked development that proves a long list of theorems entirely within the calculus, culminating in substantive results about the ancestral of a relation that prepare the ground for arithmetic. The persuasive force is that the proofs actually go through using only the rules he has stated. No appeal to meaning, intuition, or natural-language paraphrase is required.

**Pull quotes.** (Page numbers from van Heijenoort 1967, Bauer-Mengelberg translation.)

- "To prevent anything intuitive [Anschauliches] from penetrating here unnoticed, I had to bend every effort to keep the chain of inferences free of gaps. In attempting to comply with this requirement in the strictest possible way I found the inadequacy of language to be an obstacle." (Preface, p. 5)
- "[The ideography's] first purpose, therefore, is to provide us with the most reliable test of the validity of a chain of inferences and to point out every presupposition that tries to sneak in unnoticed, so that its origin can be investigated." (Preface, p. 6)
- "I believe that I can best make the relation of my ideography to ordinary language [Sprache des Lebens] clear if I compare it to that which the microscope has to the eye." (Preface, p. 6)
- "Let us call the horizontal stroke the *content stroke* and the vertical stroke the *judgment stroke*. The content stroke will in general serve to relate any sign to the totality of the signs that follow the stroke. Whatever follows the content stroke must have a content that can become a judgment." (§2, p. 12)
- "A distinction between subject and predicate does not occur in my way of representing a judgment." (§3, p. 12)

**Connections.** Depends on Boole's algebraic move (the very idea of treating inference as symbol manipulation), on the older Leibnizian dream of a *characteristica universalis*, and on Kant's analytic/synthetic distinction, which Frege accepts in order to redraw. Makes possible Whitehead and Russell's *Principia* (1910), Hilbert's program of formalization in the 1920s, Gödel's incompleteness theorems (which require a Frege-style formal system to even state), Turing's analysis of computability (which formalizes what "mechanical proof checking" means), and via the Curry-Howard correspondence the entire tradition of typed programming languages and proof assistants. The act/content distinction (judgment stroke vs. content stroke) reappears in modern type theory as the distinction between a *judgment* and a *proposition*, a thread still alive in Lean and Agda.

**What confused me / what I want to verify.**

- Frege's `≡` in §8 is *identity of content*, not the modern biconditional. It is roughly coreference under different signs (the morning-star / evening-star case). Verify how cleanly this maps onto the later Sinn/Bedeutung distinction in the 1892 paper, and decide whether the chapter handles it as a sidebar or absorbs it silently.
- The two-dimensional notation. Almost nobody reads Frege in the original. Verify that the linear notation we use today crystallizes with Peano (1889) and is then propagated by Russell, rather than emerging earlier or later.
- Frege's axioms include double negation elimination (`¬¬a → a`), which is classical, not intuitionistic. The constructive turn (Brouwer, Heyting, BHK semantics) is a later move. Probably out of scope here; flag forward to ch15.
- Sheffer (1913) showed NAND alone suffices as a primitive. Frege's choice of conditional plus negation is therefore a design decision, not a forced one. Strong sidebar candidate on "minimal sets of connectives," since the same compression idea recurs in Shannon (a switch is one bit, and any circuit is composed switches).
- The judgment stroke is doing more work than first appears. In modern type theory the judgment vs. proposition distinction is still load-bearing. Worth verifying the citation chain Frege to Brouwer to Heyting to Kolmogorov to Martin-Löf, since this might be the cleanest single thread from *Begriffsschrift* to a contemporary proof assistant.
- Russell's paradox (1902) blows up Frege's *Grundgesetze*. Verify it does *not* undermine *Begriffsschrift*: my current understanding is that the propositional and quantificational core is intact, and what Russell kills is Frege's later attempt to define classes via Basic Law V. Get this precise so the chapter does not overstate the damage.
- The reduction of two-place relations like "John loves Mary" is exactly what Boole's term logic could not do. This is the hinge to the Boole entry above (already flagged there as a sidebar candidate). Confirm the through-line so the two entries reinforce each other.
- Modus ponens as inference rule vs. `(B ⇒ A) ∧ B` as truth-functional combination: easy to conflate (I did, in my Zotero notes). Frege is the one who first cleanly separates them. Possible callout box on "rules vs. connectives."

**Teaching angle.** Boole gave us an algebra of logic. Frege gives us a *calculus*. The difference matters. In Boole's system you compute with classes the way you compute with numbers, but the laws of inference are still being read off intuitively from the algebra. Frege does something more radical: he writes inference itself down as a finite list of axioms and one rule (modus ponens), so that "does this proof go through?" becomes a yes-or-no question you can answer by inspection. He pulls apart three things earlier logic had run together: the *content* of a proposition, the *assertion* of it, and the *rules* for moving from one assertion to another. Once those are separated, you have, for the first time in history, an object you could in principle hand to a machine and ask whether the proof is valid. Everything from *Principia* through Gödel through Turing through modern proof assistants is working in the space Frege opened. The catch is notational. Frege drew his formulas in two dimensions, with the conditional as a vertical hook running down the page, and almost nobody since has read him in the original. The linear notation we use today is a later cleanup, largely from Peano and Russell. So *Begriffsschrift*'s importance is conceptual, not typographic. You read it for the move, not the marks.

---

## Cantor (1891): Ueber eine elementare Frage der Mannigfaltigkeitslehre

**Link.** *Jahresbericht der Deutschen Mathematiker-Vereinigung*, vol. 1 (1891), pp. 75-78. English translation in William Ewald (ed.), *From Kant to Hilbert: A Source Book in the Foundations of Mathematics*, vol. 2, Oxford University Press 1996, pp. 920-922.

*The diagonal argument in its original form. Short. The technical move Russell flags, Goedel reuses to construct his unprovable sentence, and Turing reuses to show no machine can decide whether arbitrary machines are circle-free. Read once, slowly, so the later reuses land.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Whitehead & Russell (1910): Principia Mathematica, Vol. 1

**Link.** Cambridge University Press.

*Read the introduction. The reader does not need the full system; they need to see what a fully formalized derivation looks like.*

**One-sentence thesis.** Pure mathematics can be derived in full from a small base of logical axioms expressed in a Peano-style notation, and the credibility of those axioms rests not on their self-evidence but on the body of ordinary mathematics they reproduce, with the doctrine of types adopted as the price of avoiding the contradictions that wrecked Frege's parallel attempt.

**What it argues.** The introduction is a defense of method, not a derivation. Three moves matter for the chapter. First, the direction of justification is reversed: axioms are believed because they reproduce the mathematics we already trust, not because they are intuitively obvious. Second, the system is claimed to be sufficient but explicitly not necessary, which is the disposition of an engineer choosing tools rather than a metaphysician seeking truth. Third, paradox is blocked structurally by the doctrine of types, which forbids a predicate from applying to itself across the same hierarchical level. Whitehead and Russell decline to commit to a single formulation of types, noting that "hardly anything in our book would be changed by the adoption of a different form." Around these three commitments the introduction also describes a working practice that matters later: proofs begin fully explicit and are gradually compressed as patterns become recognized, with the standing constraint that any compression can be re-expanded by reference back to a fully spelled-out predecessor.

**The evidence.** Not empirical. The persuasive force is twofold. First, demonstration that the system in fact reproduces the body of ordinary mathematics, with the theory of series in Vol. III explicitly built on Cantor. Second, contrast with Frege: Frege's apparently more parsimonious system collapsed under Russell's 1902 paradox, which Whitehead and Russell describe by saying that Frege "in common with all other logicians ancient and modern, had allowed some error to creep into his premisses." The doctrine of types is the visible scar from that wound and, in their telling, evidence that the inductive method has done real work, because the contradictions could not have been detected from inside the prior axioms alone.

**Pull quotes.** (Page numbers from the 1910 Cambridge first edition front matter, as Justin's Zotero annotations record.)

- "what were formerly taken, tacitly or explicitly, as axioms, are either unnecessary or demonstrable" (p. v).
- "the chief reason in favour of any theory on the principles of mathematics must always be inductive, i.e. it must lie in the fact that the theory in question enables us to deduce ordinary mathematics" (p. v).
- "In mathematics, the greatest degree of self-evidence is usually not to be found quite at the beginning, but at some later point; hence the early deductions, until they reach this point, give reasons rather for believing the premisses because true consequences follow from them, than for believing the consequences because they follow from the premisses." (p. v)
- "All that is affirmed is that the ideas and axioms with which we start are sufficient, not that they are necessary." (p. vi)
- "We have sought always the most general reasonably simple hypothesis from which any given conclusion could be reached." (p. vi)
- "It must be remembered that we are not affirming merely that such and such propositions are true, but also that the axioms stated by us are sufficient to prove them." (p. vii)
- "The proofs of the earliest propositions are given without the omission of any step, but as the work proceeds the proofs are gradually compressed, retaining however sufficient detail to enable the reader by the help of the references to reconstruct proofs in which no step is omitted." (p. vii)
- "some form of the doctrine of types must be adopted if the contradictions were to be avoided" (p. vii).
- "hardly anything in our book would be changed by the adoption of a different form of the doctrine of types." (p. vii)
- "In the matter of notation, we have as far as possible followed Peano, supplementing his notation, when necessary, by that of Frege or by that of Schröder." (p. viii)
- "Where we differ from him, it is largely because the contradictions showed that he, in common with all other logicians ancient and modern, had allowed some error to creep into his premisses; but apart from the contradictions, it would have been almost impossible to detect this error." (p. ix)
- "theory of series, our whole work is based on that of Georg Cantor" (p. ix).

**Connections.** Depends on Frege's *Begriffsschrift* for the conditional-and-negation propositional calculus and the program of explicit formalization; on Peano for the linear, one-dimensional notation that makes the proofs writable on a page; on Schröder for parts of the algebraic-logic apparatus; on Cantor's theory of order types for the substantive content of the series theory in Vol. III; and on Russell's own 1902 letter to Frege for the paradox that motivates the doctrine of types. Makes possible: Hilbert's formalism program of the 1920s; Gödel's incompleteness theorems (1931), which require a system formal enough to be its own subject matter and which take *Principia* by name as their target; Church's typed lambda calculus (1940) and through it the entire family of typed programming languages (ML, OCaml, Haskell, TypeScript, Rust) and modern proof assistants (Lean, Agda, Coq); and, more broadly, the very idea that "is this proof valid?" can be made a yes-or-no question answerable by mechanical inspection. The fully formalized derivation the introduction promises is what makes Turing's 1936 question about mechanical decidability coherent at all.

**What confused me / what I want to verify.**

- The introduction names "the theory of series" by Cantor as the foundation of Vol. III's substantive mathematics. Add Cantor to the reading list. The relevant texts are *Beiträge zur Begründung der transfiniten Mengenlehre* (1895, 1897) and the *Grundlagen einer allgemeinen Mannigfaltigkeitslehre* (1883). Decide whether the chapter handles Cantor as a sidebar or as its own entry. If transfinite arithmetic and order types are doing real work in the chapter's argument about formalization, the entry is justified.
- The exact form of the doctrine of types used in *Principia* is the *ramified* theory, not the *simple* theory of types that becomes standard later. Russell himself moves toward the simple theory in the 1925 second-edition introduction. Worth knowing the difference well enough to be precise in the chapter, since the simple theory is what programming languages inherit, not the ramified one.
- The axiom of reducibility, added to make the ramified hierarchy do useful mathematical work and criticized almost immediately as a relapse into the kind of unjustified posit Whitehead and Russell had set out to avoid. Verify whether to address in main text (it is the most candid place in the system where the inductive defense visibly leans on a tool the authors themselves are not comfortable with) or in a sidebar.
- The Russell paradox arc as a sequence: 1902 letter to Frege, the appendix to Frege's *Grundgesetze* Vol. II, the recasting that becomes *Principia* in 1910. Get the timing right so the chapter does not telescope an eight-year reckoning into a single moment.
- The "sufficient, not necessary" disclaimer. Is this the first time a foundational text in mathematics explicitly disowns the claim that its axioms are uniquely correct? Euclid did not. Frege did not. Hilbert's formalism is later and is the natural successor here. Worth checking the historiography (Mancosu, Ferreirós) to confirm the priority claim before making it in the chapter.
- The compression-of-proofs passage on p. vii has a clean structural analogy with compilation in programming and with the move from explicit features to learned representations in neural networks. The introduction makes reconstructibility the constraint on compression: any compressed step must be re-expandable by reference back to an explicit form. That constraint dissolves in a neural network, where the learned weights cannot be decompressed into legible steps. Strong sidebar candidate, and probably one of the chapter's load-bearing connections to the later chapters on interpretability.
- One thing to be careful about in the writing. The doctrine of types tames paradox at the symbolic level (Russell's paradox, the liar family). It does not resolve undecidability. Turing proves in 1936 that halting is undecidable even in systems whose terms are perfectly well typed. So when the chapter explains what types buy us, it should say "no paradox" and not "no undecidability." These are different limits and the book later relies on Turing's limit being real.

**Teaching angle.** By 1910 Frege has shown that inference itself can be written as a calculus. Whitehead and Russell take the next step. Over almost two thousand dense pages they actually derive a substantial chunk of mathematics from a tiny base, with every step explicit. Three things in their introduction matter more than the system itself. First, they reverse the direction of justification. The axioms are not believed because they are obvious. They are believed because what comes out of them is the mathematics we already trust. That is the empirical attitude turned on logic, and it is the same epistemology we now apply to a trained model: we judge by what the system produces, not by whether the premises read as self-evident. Second, they claim only sufficiency, not necessity. Their axioms work; another set might work equally well; they are tools, not revealed truths. Euclid believed in his postulates. Frege believed in his. *Principia* explicitly disowns that ambition, which is the disposition of an engineer at the foundations of mathematics rather than a metaphysician. Third, they adopt the doctrine of types against their preferences, because Russell's paradox forced their hand. A predicate cannot apply to itself across the same hierarchical level. Forbid that one move and the paradoxes go away. The same discipline migrates into every typed programming language we use today, from ML to TypeScript to Lean. It does not make computation decidable; that limit waits for Turing. What types do is tame paradox at the symbolic level, which is enough to make systematic formal work possible. The quietest move in the introduction is the most useful for the book's arc. Proofs are spelled out fully at first and then compressed as patterns become recognized, with the standing constraint that any compression can be re-expanded back to the explicit form. That is what understanding looks like once it has been compiled. A neural network's learned weights are compiled understanding in the same sense, with one important difference: the reconstructibility constraint is gone. You cannot decompress a weight matrix back into steps. That tension, mechanism that works versus mechanism legible to humans, is the through-line of everything that follows.

---

## Hilbert & Ackermann (1928): Principles of Mathematical Logic

**Link.** *Grundzuege der theoretischen Logik*, Springer 1928. English translation of the 1938 second edition: *Principles of Mathematical Logic*, ed. Robert E. Luce, Chelsea 1950.

*The textbook where the Entscheidungsproblem is named and formally posed: is there a mechanical procedure that decides, for any first-order formula, whether it is provable? Read the introduction and Chapter III. This is the question Turing answers in 1936; the chapter cannot make Turing land without it.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Goedel (1931): On Formally Undecidable Propositions of Principia Mathematica and Related Systems I

**Link.** "Ueber formal unentscheidbare Saetze der Principia Mathematica und verwandter Systeme I," *Monatshefte fuer Mathematik und Physik*, vol. 38 (1931), pp. 173-198. English translation in Jean van Heijenoort (ed.), *From Frege to Goedel: A Source Book in Mathematical Logic, 1879-1931*, Harvard University Press 1967, pp. 596-616 (trans. Bauer-Mengelberg). Standalone English edition: Meltzer & Braithwaite, Basic Books 1962.

*Incompleteness. The first proof that formalism has limits internal to itself, and the direct precedent for Turing's encoding-and-diagonalize move. Read the introduction and the proof of Theorem VI; skim the arithmetization apparatus the first time through, return for it on a second reading.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Turing (1936): On Computable Numbers, with an Application to the Entscheidungsproblem

**Link.** [doi:10.1112/plms/s2-42.1.230](https://doi.org/10.1112/plms/s2-42.1.230). *Proceedings of the London Mathematical Society*, 2nd ser., 42, 230-265.

*The central paper of the chapter. Read for the definition of a computable function and the construction of the universal machine. Take it slow.*

**One-sentence thesis.** Computation itself can be formalized as the operation of a finite-state machine on a one-dimensional tape, and once formalized, the same machinery yields two results in the same breath: a single universal machine can simulate any other (so general-purpose computing is possible at all) and certain precisely stated questions about machine behavior have no mechanical answer (so Hilbert's Entscheidungsproblem cannot be solved).

**What it argues.** Turing builds, in eleven sections, both an abstract model of computation and the proof of its limits. §1 defines the bare-bones machine: a finite-state head reading and writing on an unbounded tape of squares. §§2-7 develop this into a working formalism through examples, abbreviated tables (m-functions, which behave as macros for reusable subroutines), and an encoding scheme that turns any machine into a single integer (its description number). The encoding lets §6 build the universal machine, which takes any other machine's description number on its tape and simulates it. This is the first instance in history of program-as-data. §8 then uses the same encoding for a diagonal argument: if there existed a machine that could decide whether arbitrary machines are "circle-free" (keep producing output forever), you could construct a self-referential machine that contradicts whatever the decider says about it, so no such decider exists. §§9-10 argue that the resulting class of computable numbers captures the intuitive concept of computability (the seed of the Church-Turing thesis) and that this class includes π, e, the algebraic numbers, the zeros of the Bessel functions, and essentially everything mathematicians ordinarily care about. §11 reduces the Entscheidungsproblem to the undecidability of §8: for any Turing machine ℳ, construct a first-order formula Un(ℳ) such that Un(ℳ) is provable if and only if ℳ ever prints 0; since the right side is undecidable, so is the left. Hilbert's question has no positive answer.

**The evidence.** Not empirical. The case is made by construction and by diagonalization. Turing exhibits a complete formal model and shows that you can build inside it: example machines, m-functions as composed subroutines, an encoding of arbitrary machines as integers, and finally the universal machine itself. The impossibility results are then proved against this scaffolding using the same diagonal trick Cantor used to show the reals are uncountable and Gödel used to construct his unprovable sentence. The persuasive force is twofold. The model is precise enough to support proof, and the proof falls out of self-reference that the model itself makes possible. Universality and undecidability are theorems of the same formalism, born together.

**Pull quotes.**

- "It is possible to invent a single machine which can be used to compute any computable sequence." (§6, p. 241)
- "We may compare a man in the process of computing a real number to a machine which is only capable of a finite number of conditions q₁, q₂, ..., q_R, which will be called 'm-configurations'." (§1, p. 231)
- "No real attempt will be made to justify the definitions given until we reach §9. For the present I shall only say that the justification lies in the fact that the human memory is necessarily limited." (§1, p. 231)
- "In §8 it is shown that there can be no general process for determining whether a given number is satisfactory or not." (§5, p. 241)
- "It may be thought that arguments which prove that the real numbers are not enumerable would also prove that the computable numbers and sequences cannot be enumerable. ... The fallacy in this argument lies in the assumption that β is computable." (§8, p. 246)
- "Computing is normally done by writing certain symbols on paper. We may suppose this paper is divided into squares like a child's arithmetic book." (§9, p. 249)
- "In particular, it is shown (§11) that the Hilbertian Entscheidungsproblem can have no solution." (preamble, p. 231)

**Connections.** Depends on Frege's formalization of inference (which makes "is this proof valid?" a yes-or-no question), on Hilbert and Ackermann's 1928 *Grundzüge der theoretischen Logik* (where the Entscheidungsproblem is named and formally posed), on Cantor's 1891 diagonal argument (the technical core of §8), on Gödel's 1931 incompleteness theorem (the precedent for the encoding-and-diagonalize move), and on Church's 1936 paper using lambda calculus (which independently arrived at the same Entscheidungsproblem result, with equivalence to Turing's framework proved in the appendix). Makes possible von Neumann's stored-program architecture (EDVAC, 1945) and through it every working computer since; the entire family of interpreters, virtual machines, and emulators that descend from the universal machine; the Church-Turing thesis as a load-bearing claim across CS and philosophy of mind; complexity theory and the reduction technique (Cook 1971 on NP-completeness uses the same reduction style); and the precise framing of "computability" as a mathematical class rather than an intuitive notion, which is what every later limit theorem in computer science is proved against.

**What confused me / what I want to verify.**

- The m-function notation in §4 is genuinely brutal and OCR makes it worse. The functions f, e, r, l, c, pe, re, ce, cr, cp, cpe are subroutines built from primitive operations. Capital Fraktur letters (𝔄, 𝔅, ℭ) are continuation parameters (where to jump next); lowercase Greek (α, β, γ) are tape-symbol parameters. m-functions are macros that expand into the underlying state-transition table at substitution time, not function calls at runtime; each "call" generates fresh expanded states, which is why machines built from many m-function invocations have an explosion of m-configurations even though the source looks compact. Maintain a side glossary for the chapter and decide whether to walk readers through `find` (the simplest m-function) as a worked example.
- The corrected diagonal argument in §8 turns on H having description number K and encountering itself at section K. The mechanism: D's job is to classify *all* machines, so it must classify H itself, and H is engineered so that whatever D says about H is wrong. The self-reference is not incidental; it is what supplies the diagonal entry. Same structural move as Gödel's "this sentence is not provable" and Russell's paradoxical set. Verify the genealogy of "self-reference + diagonalization → impossibility" through Cantor, Gödel, Turing, and possibly Tarski (undefinability of truth, same year 1936).
- The polarity inversion between Turing's "circle-free" framing and the modern halting problem: Turing wants infinite output (because real numbers have infinite expansions), so circle-free is success. Modern computing wants termination, so halting is success. They are duals of the same impossibility. Worth a clean paragraph in the chapter that handles both framings without conflating them.
- Gödel's incompleteness vs Turing's undecidability is the distinction most readers will conflate. Completeness is about whether truths can be reached in principle (Gödel kills this for arithmetic-strong systems). Decidability is about whether you can mechanically find proofs in finite time (Turing kills this for first-order logic). They attack different legs of Hilbert's program. First-order logic is in fact *complete* in the semantic sense (Gödel 1929) but undecidable (Turing 1936). PA is incomplete and undecidable. Get this precise; the chapter cannot afford to fold them together.
- The Church-Turing thesis is a thesis, not a theorem. The intuitive side of "computable" has no formal definition for the equivalence to be proved against. Type (a) in §9 is Turing's analysis of human computation under finiteness constraints; it is the strongest possible argument short of a proof. Worth handling explicitly in the chapter so the reader does not assume the equivalence is mathematical.
- Direction of the §11 reduction. To transfer undecidability from machine-behavior (known undecidable, §8) to provability, build Un(ℳ) such that Un(ℳ) is provable iff ℳ prints 0. The construction goes machine → formula; the reduction goes machine-question → logic-question. Reductions only transfer undecidability in one direction, and getting the direction wrong is the most common mistake. Worth a teaching sidebar.
- Church 1936 was published a few months before Turing and reached the same conclusion via lambda calculus. Newman convinced the editors that Turing's machine formulation was distinct enough to warrant separate publication. The appendix proves equivalence between machine-computability and lambda-definability, which is the seed of the formal Church-Turing thesis (any two reasonable models of computation are equivalent). Post 1936 also published independently with a model very similar to Turing's. Verify the timeline (April Church, May Turing receipt, October Post) and decide whether to handle Church and Post in a single sidebar.
- §10's importance is structural even though most of it can be compressed. Without it the reader could conclude that "computable" is a narrow technical class. The corollaries (π, e, algebraic numbers, Bessel zeros) are reassurance that the impossibility results in §8 do not damage everyday mathematics; they constrain meta-questions about machines, not the numbers themselves.
- The two-stage construction of 𝒰 in §6 (first 𝒰' that records traces, then the modification that prints output) is doing real work. Stage 1 establishes universal simulation; stage 2 extracts output. The pattern "simulate the whole behavior, then project out what you want" is now everywhere in software (logging, monitoring, observability), and worth flagging as part of Turing's quiet inheritance.

**Teaching angle.** Boole made logic algebraic. Frege made inference formal. Russell built mathematics on logic. Hilbert then asked the natural next question: is the resulting system decidable? Given any logical formula, can we mechanically decide whether it is provable? In 1936 Turing answers no, and in the process he invents the mathematical object we now call a computer. He starts from scratch. He imagines a machine with the bare minimum: a tape of squares, a head that reads and writes one square at a time, a finite set of internal states, and a handful of primitive operations. He shows that even this stripped-down setup can compute anything any other reasonable model of computation can compute. He calls this his "contention"; we now call it the Church-Turing thesis. Then he shows two things that look opposite but are not. First, there is one such machine, the universal machine, that can simulate any other if you feed it the other machine's description as input. This is the conceptual leap from special-purpose machines to general-purpose computing, and every computer ever built is its descendant. Second, the same machinery that makes universality possible (program-as-data, self-reference) also makes some questions about machines undecidable. There is no machine that can decide, in general, whether another machine will keep producing output forever. By a careful translation, this means there is also no machine that can decide whether an arbitrary first-order formula is provable. Hilbert's decision problem has no solution. The dream of fully mechanizing mathematics ends in this paper. Three pages after the proof, the paper just stops.

---

## Shannon (1937): A Symbolic Analysis of Relay and Switching Circuits

**Link.** [DSpace MIT](https://dspace.mit.edu/handle/1721.1/11173).

*MIT master's thesis. The bridge from logic to hardware. Short. Read it whole.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Shannon (1948): A Mathematical Theory of Communication

**Link.** *Bell System Technical Journal*, 27, 379-423 and 623-656.

*Read Sections 1-6. The reader meets entropy as a formal quantity here for the first time.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Petzold (2022): Code: The Hidden Language of Computer Hardware and Software (2nd ed.)

**Link.** Microsoft Press.

*Reference companion. Cite for accessible relays-to-gates exposition, not as a primary source.*

**One-sentence thesis.** In your own words. If you cannot write this, you did not understand the paper.

**What it argues.** Two or three sentences. The argument, not the abstract.

**The evidence.** What experiments, what data, what numbers. Specific.

**Pull quotes.**

- "{quote}" (p. {n})

**Connections.** What this paper depends on. What it makes possible. One sentence each.

**What confused me / what I want to verify.** Open questions. These often become sidebars.

**Teaching angle.** If I were explaining this to someone at dinner, what would I say?

---

## Synthesis

*Fill on synthesis night, after all entries above are complete. The questions below are prompts, not a fixed schema.*

**The arc.** What story do these papers tell when read in order? One paragraph.

**Worked examples to commit to.** What propositional-logic circuits or pseudocode blocks does this chapter need? List them so writing nights have something to draft against.

**Connections backward.** What from earlier chapters does this chapter assume the reader has already met? Name the specific concept and the chapter where it was introduced.

**Connections forward.** What does this chapter set up that a later chapter will pay off? Name the chapter and the move.

**Sidebar candidates.** Confusions and verifications from individual entries that deserve a callout box rather than the main text.

**Open threads.** Claims I want to make in prose that the reading does not yet support. What further reading or verification is needed?
