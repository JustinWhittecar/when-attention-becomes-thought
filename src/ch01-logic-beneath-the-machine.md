"The Analytical Engine has no pretensions whatever to *originate* anything. It can do whatever we know how to order it to perform. It can follow analysis; but it has no power of anticipating any analytical relations or truths." - Ada Lovelace [@lovelace1843notes, Note G, p. 722]

**I**

What do the writings of Lord Byron's daughter, the logical musings of a British code breaker, and the master's thesis of a middle-class kid from Michigan have in common? There is a strong argument that any one of the three is the origin of general-purpose computing. One hundred years before the first computer was built, Lord Byron's daughter Ada Lovelace theorized that Babbage's Analytical Engine was capable of processing not just numbers, but also symbols [@lovelace1843notes]. Alan Turing's refutation of Hilbert's decidability problem was the first conceptualization of what can be computed [@turing1936computable]. Finally, Claude Shannon's master's thesis demonstrated that circuits can be made to behave like Boolean logic [@shannon1937symbolic]. Each of these moments brings something important forward about mechanical thinking, so our understanding of what it means to be a "thinking machine" owes something to each.

Beginning in 1823, an unlikable British gentleman burned through government funding equal to roughly the cost of twenty-two steam locomotives (3.55 million dollars adjusted for inflation) before losing any chance of getting further funding [@swade2001difference]. Charles Babbage was famously abrasive, and his managerial and personality issues led to repeated problems and contributed not only to him losing funding for the project but also to losing key staff like Joseph Clement, his chief engineer. The goal of this machine, the Difference Engine, was calculating the logarithmic tables commonly used in navigation and which were often error-prone and tedious to verify. Babbage's project never recovered from losing its chief engineer, and he did not live to see the Difference Engine or any of his calculating machines completed.

Even though Babbage met constant manufacturing setbacks, even though he lost funding for his work, even though he had a bitterly disastrous falling out with his chief engineer, he continued work on his designs for calculating machines. This work culminated in the Analytical Engine, which he iterated on and attempted to find funding for until his death. He was confident that a machine capable of doing logical operations could be created and powered by steam. Phenomenally, the Analytical Engine he designed has since been shown to be Turing complete, and to have many features that would show up in modern computers over a century later. One of the most striking is that he was already separating compute (what he called the Mill) from memory (the Store). In addition, his machine contained modern features like microcode (using a system of barrels much like a music box), conditional logic, and even a modular input-output [@babbage1837powers]. While this machine still has not ever been built, his earlier machine, the Difference Engine, was built by London's Science Museum using only techniques available in the nineteenth century [@swade2001difference], showing that his specifications were completely accurate and that the advent of modern computing may have been delayed thanks to his unpleasant personality.

Ada Lovelace, one of Babbage's few close friends [@seymour2018byron], was completely enamored with his machines, and it is to her I want to give credit for theorizing just how robust the capabilities of the Analytical Engine were. In her words, "Supposing, for instance, that the fundamental relations of pitched sounds in the science of harmony and of musical composition were susceptible of such expression and adaptations, the engine might compose elaborate and scientific pieces of music of any degree of complexity or extent" [@lovelace1843notes, Note A, p. 694]. She was able to see that not only could Babbage's machine be used for complex math (which was Babbage's main goal), but it could also be used to operate on any kind of symbol whose basic operations were known. It is precisely this insight that is needed to really understand what computers are capable of and where their limits fall off, and as we move forward through this chapter towards Turing and ultimately Shannon, the path that we will follow is the one of how we can encode logic into symbols and the innovations in logic required to get us there.

While the story of logic reaches all the way back to the ancient Greeks, the foundations of what we use in modern computing were created in the early nineteenth century by a self-taught British school teacher named George Boole [@machale2014boole]. In his *An Investigation of the Laws of Thought*, he attempted to turn the rules of Aristotelian logic into a formal system. As the title of his work suggests, he thought of this project as something much larger: "in studying the laws of signs, we are in effect studying the manifested laws of reasoning" [@boole1854laws, p. 17]. In fact, George Boole's thinking on exactly what logic represented is well articulated by Kant in his preface to *The Critique of Pure Reason*. Kant not only believed that logic was the pure form of thought, the rules which make thinking possible, but also that Aristotelian logic was complete: "That logic has advanced in this sure course of a science since the earliest times, and yet has not been able to take a step forward since Aristotle, is owing to the fact that it is closed and completed." [@kant1787critique] This perspective that logic itself constitutes the rules by which we think is one of the strongest arguments put forth for modern computers being thinking machines, because the operations done on modern computers are fundamentally logic and as we will explore it was Boole who first gave us the logical tools used by those computers. In fact, the core of Boole's argument that linguistic universals point to "some deep foundation of agreement in the laws of the mind itself" [@boole1854laws, p. 17] will later be echoed in Chomsky's universal grammar and the computational theory of mind.

The most dramatic claim that Boole makes is "x² = x" is always true [@boole1854laws]. If you are at all familiar with ordinary math, it is trivial to find an example that falsifies this statement. In fact, simply checking the first two numbers on the number line will get you to a counterexample with 2² = 4. How can it be an absolute truth that "x² = x"? Boole's logic is a very special case of algebra, and in base 2 or binary, where only the numbers 0 and 1 exist, his premise holds. It is important to understand, however, why Boole needs "x² = x" to be true, and the explanation of that takes a little bit more time.

Boole is attempting to build a bridge between logic and arithmetic [@boole1854laws]. In the early nineteenth century, logic worked in the world of words and arguments, and had not yet been converted into the world of operations and variables. In order to convert words and arguments to operations and variables, Boole needs first to show that a real affinity exists between the two. Boole does this by building up the basic parts of logic into the symbols of math starting with variables. For Boole, the variable "x" is called a sign which could stand for anything from a noun (man) to an adjective (good) or even a verb (ran), and he is attempting to deduce the laws by which this sign might behave. If we were to take one of these signs and plug it into the equation and convert that to a sentence, it would read something like "The statements 'There is a man', 'There is a man' are equivalent to the statement 'There is a man'" which, while a little clumsy, is obviously true. This realization allows Boole to draw a direct equivalence between binary arithmetic and logic. In other words, Boole shows with the statement "x² = x" that for the special case of binary arithmetic, math happens to behave much like logic.

Boole's system, while incredibly elegant, had a major flaw. A phrase like "Ada loved Byron", which appears to be true[^1], is impossible to express in Boole's system. The trouble is that each of Boole's signs stands for a single idea, like "man" or "good", while "Ada loved Byron" is about two particular people and the way one of them is tied to the other, something his signs give us no way to build. It is this limitation which Frege would later set out to resolve, and in so doing he created predicate logic [@frege1879begriffsschrift], a system much closer to what we now use. Frege's work is incredibly dense and idiosyncratic and his notation is hard to follow and was almost entirely abandoned by later logicians [@wehmeier2022frege], so I will not spend too much time walking you through the steps he took.

What this book needs from Frege is a narrower part of his work, and we can state it plainly. Frege analyzed a logical statement as a kind of function [@frege1879begriffsschrift]: hand it the truth or falsity of the parts and it returns the truth or falsity of the whole. This truth-functional analysis is what ultimately leads Post and Wittgenstein to later create truth tables [@anellis2011truthtables], which make seeing the relationship between binary arithmetic and logic much simpler. The easiest truth function to understand is negation (¬).

**Negation**

| P     | ¬ P   |
|-------|-------|
| 0 (F) | 1 (T) |
| 1 (T) | 0 (F) |

Above is the truth table for P and ¬ P using both the binary values and logical values. This table shows what happens to ¬ P when P is either false or true. If P is false then ¬ P is true, and if P is true then ¬ P is false. Let's look at another table to see how this applies to arithmetic symbols.

**Conjunction (And)**

| P | Q | P ∧ Q | P · Q |
|---|---|-------|-------|
| 0 | 0 | 0     | 0     |
| 0 | 1 | 0     | 0     |
| 1 | 0 | 0     | 0     |
| 1 | 1 | 1     | 1     |

Here we have conjunction. On the first three rows we can see that if either variable P or Q is ever false then the statement P and Q is also false. It is a bit easier to understand by looking at the last row though where we see that the statement P and Q is true if and only if both P and Q are true. What is interesting here is that the P · Q column matches the P ∧ Q column exactly. Conjunction is binary multiplication. This is precisely the affinity that Boole noticed, and it is the foundation on which we will ultimately build circuits. Frege's truth-functional analysis remains the standard way of analyzing logic to this day.

To help solidify the point, let's look at the truth table for the expression x² = x.

**Binary Expression of x² = x**

| x | x · x | x² | x² = x |
|---|-------|----|--------|
| 0 | 0     | 0  | ✓      |
| 1 | 1     | 1  | ✓      |

It is from this basis that the whole world of mathematical logic is born. I want this to really sink in as it is the groundwork for much of the discussions to come. There is an affinity between the truth values for logical statements and binary arithmetic. If you, like Kant, take logic as the fundamental tools of thought, then binary arithmetic and mathematical logic being the same tool set means any system that can do math is in a sense thinking. This is the line of reasoning underlying the computational theory, and it is in this sense that the question "can machines think?" has been answered.

**II**

"I believe: Everything that can be object of scientific thinking in general, as soon as it is ripe for formation of a theory, runs into the axiomatic method and thereby indirectly to mathematics" - David Hilbert, *Axiomatic Thinking* [@hilbert1917axiomatic]

All of this sets the groundwork for the crisis in math that Cantor ignites just before the start of the twentieth century, which runs straight through from him to Turing. Turing is the person the popular imagination often conjures as the start of modern computing, and his work now inspires those well outside of mathematics and logic. During his time, the story we are about to tell interested only those working on the hardest problems in math and logic. The Turing machine he would imagine was, however, an artifice for responding to a deeply technical question about mathematical logic. In order to understand how it came to be let's backtrack a couple of steps to talk first about Cantor, Hilbert, Gödel, Russell, and the debate which the Turing machine resolved.

David Hilbert is perhaps the best place for us to begin, as he set down a challenge for logicians and mathematicians to answer a set of very real and important questions, one of which the Turing machine answers. He wanted to prove that mathematics was three things: complete, decidable, and consistent [@hilbert1917axiomatic]. If this was the case it would mean that all mathematical statements could be proven using logic, that there existed a logical procedure to determine the truth of any statement in finite steps, and that the system was free of contradictions. In Hilbert's mind, if these things held true, math would be on the surest possible footing. Even before Hilbert laid out this program, the seeds of its demise had already been sown.

Cantor is an incredibly interesting figure, and if you ever want to explore the life of a troubled genius I cannot think of a more appropriate one. He is in many ways the archetype of a man haunted by his own thoughts, and spent much of his life in and out of mental hospitals, ultimately dying in a sanatorium [@dauben1990cantor]. While his life and death are tragic tales, his work in mathematics is awe-inspiring not just because it would start a whole new branch of mathematics, set theory, but also because the exact same technique he used to make his most startling claim would be used for two of the most important proofs at the foundation of all modern computing[^2].

Cantor's proof shows that given any infinite list of binary sequences you can mechanically construct a binary sequence not on the list by flipping the diagonal [@cantor1891diagonal]. There is an important thing embedded in this statement. I want you to pay attention to the word *construct*, as his proof is not so much the creation of a contradiction, but instead it is a proof by construction. What is required here is that you are able to use his method to construct a sequence not on the original list. You do this by flipping numbers along the diagonal. This is much easier to see if we give an example:

Suppose we have the following list of binary sequences. The diagonal positions are bolded:

|     | 1     | 2     | 3     | 4     | 5     | 6     | 7     |
|-----|-------|-------|-------|-------|-------|-------|-------|
| s₁  | **1** | 0     | 1     | 1     | 0     | 0     | 1     |
| s₂  | 0     | **1** | 1     | 0     | 1     | 0     | 0     |
| s₃  | 1     | 1     | **0** | 0     | 1     | 1     | 0     |
| s₄  | 0     | 0     | 1     | **1** | 0     | 1     | 1     |
| s₅  | 1     | 0     | 0     | 1     | **1** | 1     | 0     |
| s₆  | 0     | 1     | 1     | 0     | 0     | **1** | 1     |
| s₇  | 1     | 1     | 0     | 1     | 0     | 0     | **1** |

Reading down the diagonal we get the sequence:

**1 1 0 1 1 1 1**

Now we flip each bit to construct a new sequence:

**0 0 1 0 0 0 0**

This new sequence cannot appear anywhere on the original list. It differs from s₁ at position 1, from s₂ at position 2, from s₃ at position 3, and so on. For every sequence sₙ on the list, our new sequence differs from sₙ at position n by construction. So we have built, mechanically, a binary sequence that is provably not on the list. Since the table above is finite we could of course always extend the table to include this new item, but imagine instead that each row and column continued infinitely. We would still be able to follow the diagonal on that table flipping 1s and 0s to create a binary sequence not on the list, because it would differ from every binary sequence by a digit along the diagonal we created. This is what it means to be an uncountable infinity.

This idea of an uncountable infinity set off a firestorm in mathematics, and even led to one mathematician referring to Cantor as a corrupter of the youth [@dauben1990cantor]. The idea that one infinity like the integers (1, 2, 3, 4, etc.) could be by definition countable, but another infinity could be uncountable like infinite binary sequences, was even considered a theological problem, with some thinkers saying that he was challenging the existence of God (a claim Cantor himself disputed, as he believed that his work was spoken directly to him by God). To say that Cantor's diagonalization argument was controversial would be more than just a dramatic understatement.

The largest problem this led to is stated cleanly by Bertrand Russell, who asks: does the set of all sets that do not contain themselves contain itself? [@russell1902letter] This question leads to a paradox. If the set does not contain itself, it must contain itself, but if it does contain itself, it can't contain itself. A common restatement of the paradox is called the barber paradox, which asks whether the barber who is responsible for shaving all men who do not shave themselves is required to shave himself. This problem is the problem of self-reference, and both examples are constructed much like the diagonal argument. The trick in Russell's paradox is the same self-reference move: just as Cantor's diagonal sequence is defined by its relationship to every sequence on the list, Russell's paradoxical set is defined by its relationship to every set (specifically, whether each set contains itself).

Bertrand Russell, in the writing of *Principia Mathematica* with Alfred Whitehead [@whitehead1910principia], continued the work of Boole and Frege in attempting to encode all of mathematics in logic. Their work was, at the time, the most complete example, taking 379 pages to build up from simple axioms to the proof that 1+1=2. Their project is in many ways still ongoing in similar projects like the Lean Mathlib library, currently formalizing huge tracts of modern mathematics. For Russell and Whitehead to make their logical system work, they had to rely on type theory to resolve the problem of self-reference seen in the paradoxes above[^3]. Russell's fix here will likely feel familiar to modern programmers: it is the same kind of move that TypeScript makes on top of JavaScript, where a layer of type discipline rules out certain constructions before they can cause problems at runtime.

What Russell does is lay out a hierarchy of types where type 0 individuals are concrete objects, type 1 is sets of individuals, type 2 is sets of sets of individuals, and so on [@whitehead1910principia]. As a rule, a set can only contain members of a strictly lower type, meaning that no set can ever contain itself, because to do so would require it to contain a member of its own type. The paradoxical set, "all sets that do not contain themselves," depends on the possibility of self-membership to even be meaningful, so Russell's hierarchy dissolves the paradox by making it unspeakable. Decades later, mathematicians would discover that Russell's types and the propositions of logic were in fact the same thing, and that every program in a typed language is, in a precise sense, a mathematical proof.

It is from these foundations that the largest blow to Hilbert's program would come. Ironically, the day before Hilbert would give one of his most famous speeches, where the epitaph that would later mark his grave was stated ("We must know! We will know!") [@reid1996hilbert], a young Kurt Gödel presented a paper [@godel1931incompleteness] which showed definitively that any formal system robust enough to express arithmetic was incomplete, hammering the first of three nails in the coffin of Hilbert's formal program. The next nail would come a few years later with Gödel's second paper, showing that any formal system strong enough to express arithmetic and which is consistent cannot prove its own consistency.

It is worth taking a second here to understand how exactly Gödel did this, as his method lends important concepts to computing. These days we take it for granted that concepts, ideas, and even colors can be stored as nothing more than digits, but this was by no means intuitive in the early twentieth century, and Gödel took this idea to an extreme no one was really thinking about at the time. He actually encoded mathematical formulas as numbers [@godel1931incompleteness]. He did this by assigning each symbol a number using prime factorization. This had an incredibly important payoff. It meant that not only could the equation be converted into its Gödel number, but a Gödel number could be converted back into its equation.

There is a real beauty in the simplicity of this process. Mathematical statements are themselves numbers. Statements about mathematical statements (like "this formula is provable") also become statements about numbers with their own Gödel numbers. This insight that mathematical statements can be converted into numbers is something to hold onto as it will eventually become the core trick for creating general-purpose computers. In addition, this means mathematics can now talk about itself mechanically using arithmetic. Because of this, Gödel is able to use Cantor's diagonalization to construct something incredibly shocking.

Imagine a grid where rows are formulas (each one a statement schema with a single blank to fill in, like "_ is prime" or "_ is divisible by 3"), columns are numbers we could plug into the blank, and each cell asks whether the resulting filled-in statement is provable in our formal system. So the cell at row i, column j asks: "is the statement F_i(j) provable?"

|         | (1)   | (2)   | (3)   | (4)   | (5)   | (6)   | (7)   |
|---------|-------|-------|-------|-------|-------|-------|-------|
| F₁      | **✓** | ✓     | ✗     | ✓     | ✗     | ✓     | ✓     |
| F₂      | ✓     | **✗** | ✓     | ✗     | ✓     | ✓     | ✗     |
| F₃      | ✗     | ✓     | **✓** | ✓     | ✗     | ✗     | ✓     |
| F₄      | ✓     | ✓     | ✗     | **✗** | ✓     | ✓     | ✓     |
| F₅      | ✗     | ✗     | ✓     | ✓     | **✓** | ✗     | ✓     |
| F₆      | ✓     | ✓     | ✗     | ✗     | ✓     | **✓** | ✗     |
| F₇      | ✓     | ✗     | ✓     | ✓     | ✗     | ✓     | **✗** |

Read down the diagonal and you get the sequence of statements F₁(1), F₂(2), F₃(3), and so on. Each one is a formula applied to its own Gödel number. This is Gödel's diagonal, and it is the direct analog of Cantor's diagonal we showed earlier in bits.

Now Gödel constructs a new formula. He defines G as the statement: "the formula F_x(x) is not provable," where x is the blank to fill in. Like every other formula in the system, G has a Gödel number. Call it g. When we plug g into G's blank, we get the closed statement G(g), which says: "F_g(g) is not provable." But G itself is F_g, so G(g) is saying "G(g) is not provable." The statement asserts its own unprovability[^4]. This is Gödel's version of Cantor flipping each digit along the diagonal. Gödel's construction negates the property "is provable" along the diagonal to create a formula that disagrees with what the system would have to say about it.

Now look at what this forces:

- If G(g) is provable, then it is true, so G(g) is not provable. Contradiction. The system is inconsistent.
- If G(g) is not provable, then it is true (it correctly states its own unprovability), but the system cannot prove it. The system is incomplete.

Either the system contradicts itself or it cannot capture its own truths. There is no third option. Hilbert wanted mathematics to be both complete and consistent. Gödel proved it cannot be both. The construction is the same diagonal trick Cantor used decades earlier. Where Cantor used it to show that some infinities cannot be enumerated, Gödel used it to show that some truths cannot be proven. The idea that mathematical operations could be encoded as numbers, and that those numbers could in turn be operated upon, would not stay confined to logic for long. Within fifteen years, John von Neumann would recognize that this is exactly how a computer should be built.

But Cantor's diagonalization argument has not had its fill. Hilbert also asked for a system that was decidable, and it is precisely that problem which Turing sets out to solve. Unfortunately, once again we will learn that we won't know, we can't know. In fact, in Turing's own introduction to his paper he states "In particular, it is shown (§11) that the Hilbertian Entscheidungsproblem can have no solution" [@turing1936computable, p. 231]. In other words, there is not a mechanical procedure that, given a mathematical formula, decides in finite steps whether that formula is provable. In order to do this, Turing must first define what a mechanical procedure actually means without counting on intuition.

Turing introduces a machine that consists of a tape divided into squares that are either empty, contain a 1, or contain a 0, and which a read/write head can scan one at a time [@turing1936computable]. This machine has a finite set of states it can be in, and a table of rules it follows based on which state it is in. These rules are things like when in state "x" move back three squares and print 1, or when in state "y" erase the symbol on the current square. That's it, that is the whole machine. The finite table of rules can drive an infinite output[^5]. Turing describes the kind of machine that repeats forever as **circle-free**, and, somewhat counterintuitively, calls a machine **circular** if it eventually stops printing fresh digits or gets stuck in a loop. Importantly, he defines a computable sequence as one that some circle-free machine prints and a computable number is the real number whose binary expansion is that sequence.

As Gödel did with formulas, Turing turns his machines into numbers. Every Turing machine is a finite table of rules, finite set of symbols, and finite set of states. Interestingly, this means that the whole of the machine can be written out as a string of symbols, and that string can be encoded into a single number using Gödel's same method. Turing calls this number the D.N (description number) of the machine. This means you could feed the description number of a Turing machine into another Turing machine and operate on it. In other words, a single machine can in principle simulate any other. This is the exact mechanism of self-reference that causes issues for Russell in his *Principia*, but this method of one machine being able to simulate another by reading its description number will inspire John von Neumann to put programs and data in the same place in our next chapter.

Let's dig into what Turing actually does. Imagine a table where rows are circle-free Turing machines indexed by their description number (M₁, M₂, M₃, and so on), columns are output positions on the tape, and each cell is the bit that machine Mᵢ prints in position j.

|     | (1)   | (2)   | (3)   | (4)   | (5)   | (6)   | (7)   |
|-----|-------|-------|-------|-------|-------|-------|-------|
| M₁  | **0** | 1     | 0     | 1     | 0     | 1     | 0     |
| M₂  | 1     | **1** | 0     | 0     | 1     | 1     | 0     |
| M₃  | 0     |   1   | **1** | 0     | 0     | 1     | 1     |
| M₄  | 1     |   0   |   0   | **0** | 1     | 0     | 1     |
| M₅  | 0     |   0   |   1   | 1     | **0** | 1     | 1     |
| M₆  | 1     |   1   |   0   | 1     | 0     | **0** | 0     |
| M₇  | 0     |   1   |   1   | 0     | 1     | 1     | **1** |

Read down the diagonal and you get the sequence:

0 1 1 0 0 0 1

That is the first bit M₁ prints, the second bit M₂ prints, the third bit M₃ prints, and so on. Each entry is a machine's output read at its own description-number position. This is Turing's diagonal, the direct analog of Cantor's diagonal and Gödel's diagonal.

Just like we did in the last two examples, flip every bit to construct a new sequence:

1 0 0 1 1 1 0

Call this sequence β′. By construction, β′ differs from M₁'s output at position 1, from M₂'s output at position 2, from Mᵢ's output at position i, for every machine on the list. So β′ is a binary sequence that no machine on this list prints. Remember now that our rows are all circle-free machines, so β′ is by construction not a computable sequence. Cantor flipped bits to escape an enumeration of the real numbers. Gödel flipped "provable" to "not provable" along the diagonal to escape an enumeration of formulas. Turing flips bits, again, to escape an enumeration of machines.

How does all of this apply to Hilbert and decidability? Turing takes his proof a step further. In order to actually create the table above, you need a method for enumerating machines that are circle-free. This requires being able to look at an arbitrary description number and decide whether the machine it describes is circle-free. Turing supposes such a machine does exist and calls it "D". But if D exists, something strange follows. With D in hand we could walk through every description number in turn, ask D which ones name circle-free machines, and keep only those. That gives us the complete list. And once we have the list, computing β′ is itself a mechanical procedure: to get its i-th digit, find the i-th circle-free machine, run it out to position i, and flip the bit it prints. Every step in that procedure is something a machine can do, so β′ would be the output of some circle-free machine.

This immediately leads us to a paradox. We built β′ precisely so that it differs from every circle-free machine on the list by at least one digit, so β′ is the output of no circle-free machine at all. It cannot both be printed by a circle-free machine and printed by none of them. The only thing we assumed along the way was that D exists. Therefore, we can only suppose that machine D cannot exist. This cleanly puts the final nail in the coffin of Hilbert's program by showing that it is not possible for a machine to exist which can answer decidability.

In addition to a solution to Hilbert's decidability problem, we also get a rigorous definition of computability. That is to say, we have a formal definition without reference to our intuition of what it means to compute some number. Note that this definition also means that there are only countably many Turing machines, but there are uncountably many real numbers, so *most* numbers are not computable. Importantly, Turing does go on to show that all of the numbers mathematicians actually use are computable, meaning that we have real boundaries around what is computable and what is not computable, and we know that we can compute a great many incredibly important things.

**III**

"This calculus is shown to be exactly analogous to the calculus of propositions used in the symbolic study of logic." - Claude Shannon, *A Symbolic Analysis of Relay and Switching Circuits* [@shannon1937symbolic]

The stage has now been set for twenty-two-year-old Claude Shannon to write his master's thesis after a summer working on Vannevar Bush's differential analyzer where he sees relay banks doing combinatorial work for which there is no theory [@soni2017mindatplay]. It is 1937, before World War II and barely a year after Turing's work *On Computable Numbers* was published. This is the moment we have been building towards. What Shannon notices in his paper is the secret that makes all of modern computing function. He realizes that circuits behave remarkably like binary arithmetic [@shannon1937symbolic]. All of the work done in logic and math, even Turing's conceptual project imagining this binary machine, was done without an engineering solution like modern binary circuits.

Shannon, however, discovers a bridge from the conceptual world to the physical world. Shannon realizes that a switch behaves a lot like a logical variable. Let's build this up from first principles. Imagine a light switch: when flipped up, the current flows and your light turns on (this is the closed state where the circuit is connected), but flip it down and the current stops and your light turns off (this is the open state where the circuit is not connected). Going back to our truth tables, we can think of closed as True or 1, and open as False or 0. We can then arrange switches so the result is the opposite of what goes in. The circuits themselves convert on to off, and off to on. This set of circuits would have the same truth table as the one we created for ¬ (NOT).

But how do we do this? A relay's coil can drive two kinds of contact. Some close when the coil is energized. Others open. Wire one of each on the same relay and you have two outputs that move in opposite directions: when one is closed, the other is open. Call the first contact P. The second is ¬P.

**Negation (Not)**

| P | ¬P |
|---|----|
| 0 (open)   | 1 (closed) |
| 1 (closed) | 0 (open)   |

As promised we have the negation truth table I showed a few pages back, only now we are describing a piece of hardware. The ¬ in the negation table is a thing you can build out of brass[^6]. In general, when designing circuits we would use the following notation for a ¬ gate:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 50" width="70" height="36" stroke="currentColor" fill="none" stroke-width="1.5"><line x1="0" y1="25" x2="15" y2="25"/><polygon points="15,10 15,40 50,25" stroke-linejoin="round"/><circle cx="53" cy="25" r="3"/><line x1="56" y1="25" x2="70" y2="25"/></svg>

A simple ¬ circuit is not particularly useful though. What we need are enough logical operations (logic gates) to actually start to express the whole formal system, and Shannon delivers. If you put two switches in a row (in series) then both of them have to be closed (true) for current to flow which gives us the same truth table as we had for ∧ (AND).

**Conjunction (And)**

| P | Q | P ∧ Q |
|---|---|-------|
| 0 (open)   | 0 (open)   | 0 |
| 0 (open)   | 1 (closed) | 0 |
| 1 (closed) | 0 (open)   | 0 |
| 1 (closed) | 1 (closed) | 1 |

 <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 50" width="70" height="36" stroke="currentColor" fill="none" stroke-width="1.5"><line x1="0" y1="17" x2="15" y2="17"/><line x1="0" y1="33" x2="15" y2="33"/><path d="M 15,10 L 35,10 A 15,15 0 0 1 35,40 L 15,40 Z" stroke-linejoin="round"/><line x1="50" y1="25" x2="70" y2="25"/></svg>

If instead you connect the circuits side by side, electricity can pass through either one. The truth table for this behaves exactly like ∨ (inclusive OR).

**Disjunction (Or)**

| P | Q | P ∨ Q |
|---|---|-------|
| 0 (open)   | 0 (open)   | 0 |
| 0 (open)   | 1 (closed) | 1 |
| 1 (closed) | 0 (open)   | 1 |
| 1 (closed) | 1 (closed) | 1 |

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 50" width="70" height="36" stroke="currentColor" fill="none" stroke-width="1.5"><line x1="0" y1="17" x2="16" y2="17"/><line x1="0" y1="33" x2="16" y2="33"/><path d="M 10,10 Q 25,25 10,40 Q 35,40 55,25 Q 35,10 10,10 Z" stroke-linejoin="round"/><line x1="55" y1="25" x2="70" y2="25"/></svg>

From these three operations, the rest of math can be deduced as is done in Russell and Whitehead's *Principia*. This means we now have the designs to implement `(A ∧ B) ∨ ¬C` in circuits. In fact, every row of every truth table can now correspond to an arrangement of switches, meaning that if we can express it using logic, then we can express it in circuits.

To move forward from here we need to talk about ⊕ (XOR). Up to this point we have been working with the inclusive OR where if either or both of the variables are true then the whole statement is true. For ⊕, we are saying that if either variable but not both is true, then the statement is true. Expressed as a logical statement it looks like this `A ⊕ B ≡ (A ∨ B) ∧ ¬(A ∧ B)` with the following truth table.

**Exclusive Disjunction (XOr)**

| P | Q | P ⊕ Q |
|---|---|-------|
| 0 (open)   | 0 (open)   | 0 |
| 0 (open)   | 1 (closed) | 1 |
| 1 (closed) | 0 (open)   | 1 |
| 1 (closed) | 1 (closed) | 0 |

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 70 50" width="70" height="36" stroke="currentColor" fill="none" stroke-width="1.5"><line x1="0" y1="17" x2="16" y2="17"/><line x1="0" y1="33" x2="16" y2="33"/><path d="M 4,10 Q 19,25 4,40" stroke-linejoin="round"/><path d="M 11,10 Q 26,25 11,40 Q 35,40 55,25 Q 35,10 11,10 Z" stroke-linejoin="round"/><line x1="55" y1="25" x2="70" y2="25"/></svg>

XOR is important because it allows us to do something powerful as we build circuits that do arithmetic. We already know that ∧ (AND) is multiplication, but addition is a bit trickier. It generally behaves like regular disjunction, but with a special case when both values are true. In this instance the disjunction table would give us 1, but we have a problem: the 1 we get in disjunction should be carried. In fact, what we would have if we used disjunction for addition is "1+1=1", which is the case for Boolean logic.

To do binary arithmetic we want 1+1=10, and to design a circuit for that we need ⊕ (XOR). The logical description of that circuit is `HA(P, Q) := (P ⊕ Q, P ∧ Q)` which has the following truth table.

<div align="center" style="margin: 1em 0;">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 460 130" width="460" stroke="currentColor" fill="none" stroke-width="1.5" style="font-family: ui-sans-serif, system-ui; font-size: 13px; max-width: 100%; height: auto;"><text x="5" y="34" stroke="none" fill="currentColor">P</text><text x="5" y="104" stroke="none" fill="currentColor">Q</text><line x1="15" y1="30" x2="170" y2="30"/><line x1="50" y1="30" x2="50" y2="80"/><path d="M 50,80 L 74,80 A 6,6 0 0 1 86,80 L 155,80" stroke-linejoin="round"/><circle cx="50" cy="30" r="2.5" fill="currentColor" stroke="none"/><line x1="15" y1="100" x2="155" y2="100"/><line x1="80" y1="50" x2="80" y2="100"/><line x1="80" y1="50" x2="170" y2="50"/><circle cx="80" cy="100" r="2.5" fill="currentColor" stroke="none"/><path d="M 159,20 Q 174,40 159,60" stroke-linejoin="round"/><path d="M 166,20 Q 181,40 166,60 Q 195,60 215,40 Q 195,20 166,20 Z" stroke-linejoin="round"/><line x1="215" y1="40" x2="295" y2="40"/><text x="300" y="44" stroke="none" fill="currentColor">Sum (P ⊕ Q)</text><path d="M 155,70 L 175,70 A 20,20 0 0 1 175,110 L 155,110 Z" stroke-linejoin="round"/><line x1="195" y1="90" x2="295" y2="90"/><text x="300" y="94" stroke="none" fill="currentColor">Carry (P ∧ Q)</text></svg>

</div>

| P | Q | sum (P ⊕ Q) | carry (P ∧ Q) |
|---|---|-------------|---------------|
| 0 | 0 | 0           | 0             |
| 0 | 1 | 1           | 0             |
| 1 | 0 | 1           | 0             |
| 1 | 1 | 0           | 1             |

In this table our normal sum column is ⊕ and the information about carrying a digit is the ∧ column. These two operations together give us only half of the picture, hence the name. The other half of the full adder is the ability to bring in a carry digit to the addition. For the full adder we have to take three inputs, our original P, Q for the values we are adding, and another input Z for the presence of a carry digit. This will give us two outputs: our sum and the presence of a carry digit. Here is the logic of that circuit `FA(P, Q, Z) := (P ⊕ Q ⊕ Z, (P ∧ Q) ∨ (Z ∧ (P ⊕ Q)))`. This is two half-adders feeding an ∨ for the carry digit[^7].

<div align="center" style="margin: 1em 0;">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 210" width="560" stroke="currentColor" fill="none" stroke-width="1.5" style="font-family: ui-sans-serif, system-ui; font-size: 13px; max-width: 100%; height: auto;"><text x="5" y="54" stroke="none" fill="currentColor">P</text><text x="5" y="84" stroke="none" fill="currentColor">Q</text><text x="5" y="164" stroke="none" fill="currentColor">Z</text><line x1="15" y1="50" x2="140" y2="50"/><line x1="15" y1="80" x2="140" y2="80"/><rect x="140" y="30" width="80" height="70" fill="none"/><text x="180" y="71" stroke="none" fill="currentColor" text-anchor="middle" font-size="15" font-weight="600">HA</text><line x1="220" y1="50" x2="280" y2="50"/><line x1="220" y1="80" x2="220" y2="120"/><path d="M 220,120 L 269,120 A 6,6 0 0 1 281,120 L 420,120" stroke-linejoin="round"/><line x1="15" y1="160" x2="275" y2="160"/><line x1="275" y1="80" x2="275" y2="160"/><line x1="275" y1="80" x2="280" y2="80"/><rect x="280" y="30" width="80" height="70" fill="none"/><text x="320" y="71" stroke="none" fill="currentColor" text-anchor="middle" font-size="15" font-weight="600">HA</text><line x1="360" y1="50" x2="510" y2="50"/><text x="515" y="54" stroke="none" fill="currentColor">Sum</text><line x1="360" y1="80" x2="360" y2="160"/><line x1="360" y1="160" x2="420" y2="160"/><path d="M 405,110 Q 425,140 405,170 Q 450,170 480,140 Q 450,110 405,110 Z" stroke-linejoin="round"/><line x1="480" y1="140" x2="510" y2="140"/><text x="515" y="144" stroke="none" fill="currentColor">Carry</text></svg>

</div>

| P | Q | Z | P ⊕ Q | P ∧ Q | Z ∧ (P ⊕ Q) | sum | carry |
|---|---|---|-------|-------|-------------|-----|-------|
| 0 | 0 | 0 | 0     | 0     | 0           | 0   | 0     |
| 0 | 0 | 1 | 0     | 0     | 0           | 1   | 0     |
| 0 | 1 | 0 | 1     | 0     | 0           | 1   | 0     |
| 0 | 1 | 1 | 1     | 0     | 1           | 0   | 1     |
| 1 | 0 | 0 | 1     | 0     | 0           | 1   | 0     |
| 1 | 0 | 1 | 1     | 0     | 1           | 0   | 1     |
| 1 | 1 | 0 | 0     | 1     | 0           | 0   | 1     |
| 1 | 1 | 1 | 0     | 1     | 0           | 1   | 1     |

I want you to stop for a second and appreciate what has happened here. Shannon has in the most basic of ways carried the bridge built between math and logic to physical systems. He has shown that circuits obey the laws of math, logic, and some would argue thought itself. He has converted logic to matter.

Shannon's master's thesis does not stop there. In what feels almost like a throwaway statement, he describes a circuit we can write as `X = (S ∨ X) ∧ ¬R`[^8]. This circuit does something remarkable. It wires a relay's own contact back into its own coil through a start switch S and a release switch R, giving a circuit that latches: pressing start drives S to 1, which forces the OR to 1, and (so long as R is 0) the AND drives X to 1. Once X is 1, the OR stays at 1 through the X term alone, even after the start switch springs back open, and the relay holds itself energized until the release switch is pressed, which sends ¬R to 0, collapses the AND, and clears the latch.

<div align="center" style="margin: 1em 0;">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 180" width="430" stroke="currentColor" fill="none" stroke-width="1.5" style="font-family: ui-sans-serif, system-ui; font-size: 13px; max-width: 100%; height: auto;"><text x="5" y="44" stroke="none" fill="currentColor">S</text><text x="5" y="134" stroke="none" fill="currentColor">R</text><line x1="15" y1="40" x2="160" y2="40"/><line x1="15" y1="130" x2="110" y2="130"/><path d="M 140,30 Q 160,50 140,70 Q 180,70 200,50 Q 180,30 140,30 Z" stroke-linejoin="round"/><line x1="200" y1="50" x2="225" y2="50"/><line x1="225" y1="40" x2="225" y2="50"/><line x1="225" y1="40" x2="250" y2="40"/><polygon points="110,120 110,140 140,130" stroke-linejoin="round"/><circle cx="144" cy="130" r="3"/><line x1="147" y1="130" x2="236" y2="130"/><line x1="236" y1="60" x2="236" y2="130"/><line x1="236" y1="60" x2="250" y2="60"/><path d="M 250,30 L 270,30 A 20,20 0 0 1 270,70 L 250,70 Z" stroke-linejoin="round"/><line x1="290" y1="50" x2="380" y2="50"/><text x="385" y="54" stroke="none" fill="currentColor">X</text><line x1="310" y1="50" x2="310" y2="10"/><line x1="110" y1="10" x2="310" y2="10"/><line x1="110" y1="10" x2="110" y2="60"/><line x1="110" y1="60" x2="160" y2="60"/><circle cx="310" cy="50" r="2.5" fill="currentColor" stroke="none"/></svg>

</div>

This creates a circuit that depends on its own present output to compute its next output. It is a circuit that remembers. It is the first published one-bit memory. Specifically, it is an SR latch, the simplest member of the flip-flop family. Every register and KV cache descends from this circuit. Information theory, the study of what we are storing in memory, will ultimately be the legacy for which Shannon is celebrated. Here, in his earliest work, we are already seeing the seeds of what is to come.

After graduating, Shannon went to work at Bell Labs, and worked on a wide variety of problems, but he continued to have a particular interest in information theory. In fact, when Alan Turing visited the US during the war, he met with Shannon for tea every day [@soni2017mindatplay]. It is during this period that Shannon would lay the groundwork for the entire field of information theory, but much of that work stayed classified for many years due to the war. After the war, he wrote out his thoughts in the unclassified paper *A Mathematical Theory of Communication* [@shannon1948communication], where he asks and answers the question: what is flowing through switches or along telephone lines? If you are thinking that the answer is obviously electricity, I will forgive you, because Shannon's position on this is one I still struggle to wrap my head around.

"The fundamental problem of communication is that of reproducing at one point either exactly or approximately a message selected at another point. Frequently the messages have meaning; that is they refer to or are correlated according to some system with certain physical or conceptual entities. These semantic aspects of communication are irrelevant to the engineering problem." [@shannon1948communication, p. 379]. Shannon is saying that the meaning of a message is irrelevant to the engineering of communicating that message. He is doing something important here. We saw a similar trick with Boole setting aside the question of metaphysics to explore the relationship between signs. Shannon sets aside the question of meaning from the selection of messages. This trick allows the engineer to care only about what message is selected from how many options.

<div align="center" style="margin: 1em 0;">

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 360" width="600" stroke="currentColor" fill="none" stroke-width="1.5" style="font-family: ui-sans-serif, system-ui; font-size: 13px; max-width: 100%; height: auto;"><text x="70" y="60" text-anchor="middle" stroke="none" fill="currentColor">INFORMATION</text><text x="70" y="76" text-anchor="middle" stroke="none" fill="currentColor">SOURCE</text><text x="200" y="76" text-anchor="middle" stroke="none" fill="currentColor">TRANSMITTER</text><text x="500" y="76" text-anchor="middle" stroke="none" fill="currentColor">RECEIVER</text><text x="630" y="76" text-anchor="middle" stroke="none" fill="currentColor">DESTINATION</text><rect x="30" y="90" width="80" height="60"/><rect x="160" y="90" width="80" height="60"/><rect x="460" y="90" width="80" height="60"/><rect x="590" y="90" width="80" height="60"/><line x1="110" y1="120" x2="160" y2="120"/><line x1="240" y1="120" x2="335" y2="120"/><line x1="365" y1="120" x2="460" y2="120"/><line x1="540" y1="120" x2="590" y2="120"/><rect x="335" y="105" width="30" height="30"/><text x="287" y="140" text-anchor="middle" stroke="none" fill="currentColor">SIGNAL</text><text x="418" y="140" text-anchor="middle" stroke="none" fill="currentColor">RECEIVED</text><text x="418" y="156" text-anchor="middle" stroke="none" fill="currentColor">SIGNAL</text><text x="70" y="172" text-anchor="middle" stroke="none" fill="currentColor">MESSAGE</text><text x="630" y="172" text-anchor="middle" stroke="none" fill="currentColor">MESSAGE</text><line x1="350" y1="240" x2="350" y2="135"/><rect x="310" y="240" width="80" height="60"/><text x="350" y="324" text-anchor="middle" stroke="none" fill="currentColor">NOISE</text><text x="350" y="340" text-anchor="middle" stroke="none" fill="currentColor">SOURCE</text></svg>

</div>

It is here, in this paper, that we first see the word "bit" used[^9]. Bit is a creative shortening of binary digit, and is, to this day, how we talk about digital information. Shannon shows that any device with two stable positions, like the SR latch defined in his earlier paper, stores 1 bit of information. In addition, "N" such devices store "N" bits, because the number of possible states for those devices is 2^N and log₂ 2^N is N. This one did not click for me at first, so let's build up to what Shannon is saying bit by bit.

Picture one switch. It is either on or off. In other words, one switch has exactly two states.

| Switch 1 |
|:---:|
| 0 |
| 1 |

What happens if we have two switches? We have the two states from the first switch multiplied by the two states from the second switch, because we can have any combination of states between the two switches.

| Switch 1 | Switch 2 |
|:---:|:---:|
| 0 | 0 |
| 0 | 1 |
| 1 | 0 |
| 1 | 1 |

In other words, we double the number of possibilities. Now we have four possibilities: off-off, off-on, on-off, on-on. If we add a third switch we would double the number of possibilities again, giving us eight states:

| Switch 1 | Switch 2 | Switch 3 |
|:---:|:---:|:---:|
| 0 | 0 | 0 |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |
| 1 | 1 | 1 |

Four switches would give us sixteen possible states. "N" switches give 2 multiplied by itself "N" times, or 2^N states.

| Number of switches | Possible states |
|:---:|:---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 10 | 1,024 |
| 20 | 1,048,576 |
| N | 2^N |

Shannon is measuring information by the number of switches it takes to store that information. One switch is one bit of information. Two switches is two bits. "N" switches is "N" bits. The compact way to write the relationship between the number of switches and the number of states they produce is log₂ 2^N = N. That notation looks intimidating, but it is just the mathematical way of saying that if you start with "N" switches and double the arrangements "N" times, then asking how many doublings it took gives you back "N". The exponent 2^N runs the doubling forward and log₂ runs it backward.

Let's take a second to appreciate what Shannon is doing. His thesis showed that switches can be used to represent logic and that switches are two-state devices. The bit is the unit that measures what one such device can hold. The same physical object that in his earlier work expressed logic is now storing information. Entropy, capacity, and redundancy, the three other concepts the chapter takes from this paper, will all be measured in bits.

Why is it that Shannon cares so much about bits? This is after all a lot of trouble to go through and a lot of math to do about binary digits. Shannon worked for Bell Labs, a phone company, and the practical question he is driving at is: how many phone calls can you pack into a copper wire? All of this work is in the interest of efficiently transmitting messages along wires. In other words, Shannon wants to know what is the capacity of a telephone wire. He actually generalizes this question to talk about the capacity of any given channel. That generalization is useful for us, because messages travel along everything from teletype lines to fiber optic cables. Shannon's math can be used to work out, for any channel, how much information it can move per unit of time. The simplest version of this follows the bit count we already have.

A teletype machine, which is the 1940s version of a printer connected over a wire, sends one of 32 different characters with each press of its key. We just saw that distinguishing among 2^N possibilities takes N bits, so distinguishing among 32 possibilities (which is 2^5) takes 5 bits. Every character the teletype sends carries 5 bits of information across the wire. If the machine sends one character per second, its capacity is 5 bits per second. If it sends ten characters per second, 50 bits per second.

Shannon writes this in a single formula: C = lim log N(T) / T [@shannon1948communication]. N(T) is the number of distinct messages the channel (C) can produce in time T. The log is base 2, which means the answer comes out in bits. A logarithm answers the question: what power do I raise the base to in order to reach this number? Log base 2 of 4 is 2, because 2 × 2 = 4. Log base 2 of 8 is 3, because 2 × 2 × 2 = 8. Log base 2 of 32 is 5, because 2 × 2 × 2 × 2 × 2 = 32. Dividing by T turns a total bit count into a per-second rate. The "lim" just means "as T gets large." For the teletype we can ignore it, since the answer is the same at every scale.

Now let's apply the formula to the teletype. The machine sends one character every second. Each character carries 5 bits, which is another way of saying each character is one of 32 possible symbols (because 2 × 2 × 2 × 2 × 2 = 32). How many distinct T-second messages can the machine produce? Thirty-two possibilities in the first second, another thirty-two in the second, and so on, giving: N(T) = 32^T, which is the same as 2^(5T). The log base 2 of 2^(5T) is 5T. Divide by T and you get 5. So the channel capacity is 5 bits per second.

The case of the teletype is relatively simple. Real channels usually carry constraints (which symbols can follow which, symbols of different durations) that make N(T) much harder to count. Shannon develops the machinery for these cases later in *A Mathematical Theory of Communication*. The techniques themselves are not important here. What matters is that they exist: every channel has a capacity, and the teletype just happens to be the one where you can read it off in a line.

The formula itself, C = log N, is the mathematical expression of the number of bits it takes to determine one of N equally-likely outcomes. It is exactly the same calculation we did for switches: "N" possible states means log N bits to pick one out. Shannon, however, is not just concerned with evenly distributed sets. In fact most of the information we care about does not have equally likely outcomes. For example, "e" is used more commonly than "q" when writing. Intuitively, this difference in probability should change the bit count of the information.

Shannon did find a more general way to measure information, one that works when outcomes are uneven. He calls this quantity entropy[^10]. The capacity formula we just worked through is the special case of it where every outcome is equally likely. Entropy is the general version, and we just went through how to compute it when every outcome has the same probability.

Looking more closely at Shannon's own work helps a lot here [@shannon1948communication]. Let's take the string of letters:

XFOML RXKHRJFFJUJ

This sequence was generated by selecting letters from a list containing the alphabet and a blank space with equal probability. It reads like nonsense. In fact, you could not properly speak it out loud as the distribution of letters does not lend itself to language. Now look at this sequence:

OCRO HLI RGWR NMIELWIS

It was generated using the same list, but with letters having the same frequency we see in everyday English. It still reads like nonsense, but you could almost say these words.

ON IE ANTSOUTINYS ARE T INCTORE

This example was constructed with the same list, but now the frequency of characters cares not just about everyday English, but also the immediately preceding character. At this point, I could now almost believe this is some ancient form of English which I have not learned. We are already seeing the first recognizable words appear with "on" and "are".

Stop for a moment and appreciate this point. By attending not just to the likelihood a given letter occurs, but also to the letters around it, we get something that looks very close to language.

We can keep going. Look at this sequence:

IN NO IST LAT WHEY CRATICT FROURE

This was built the same way, but now each character cares about the two letters before it rather than just one. The fragments are longer and more word-shaped. "WHEY" is a real word. "CRATICT" and "FROURE" are not, but they are the kind of thing that could be a word. If you told me this was simply a language I do not know that is closely related to English, I would have a hard time arguing with you.

Shannon then makes a jump. Instead of working letter by letter, he switches to whole words. Look at what comes out:

REPRESENTING AND SPEEDILY IS AN GOOD

Every word here is a real, properly spelled English word, picked by how often it shows up in English. And yet it is still nonsense. "IS AN GOOD" is something no English speaker would ever say. Picking real words is not enough on its own. The order they come in has to matter too.

Shannon gives another example worth exploring in more detail. He opens a book and picks a word, then flips to another page and reads until he finds that word again. He then records the next word, and starts the process over. This technique, which is very similar to modern corpus sampling, produces this:

THE HEAD AND IN FRONTAL ATTACK ON AN ENGLISH WRITER

Now the frequency of a word cares about the word right before it, and whole clauses appear. "FRONTAL ATTACK ON AN ENGLISH WRITER" is a phrase you could drop into a sentence without anyone noticing.

Stop again and look at what we just did. Nothing in any of this knows what a single word means. There is no dictionary involved, no sense of what the words point at in the world. The only thing being modeled is how often one token follows another. And yet, rung by rung, we went from noise, to pronounceable noise, to real words, to fragments, to grammar, to whole clauses. Something that looks like real command of language fell out of nothing but the frequency of token sequences.

Shannon then makes the claim that "a sufficiently complex stochastic process will give a satisfactory representation of a discrete source" [@shannon1948communication, p. 385]. This is the main thesis of statistical language modeling, written in 1948.

Every time we let the model take in more of the surrounding context, the output got more organized. Letter frequencies gave us letter clusters. Letter pairs gave us word fragments. Word pairs gave us clauses. Keep going down that line. A model that looks back not one word but hundreds of them, and learns the frequencies from a large corpus of data instead of from flipping through a single book, should give us something that reads a lot like real text.

That is what we are doing with modern LLMs. We are taking Shannon's n-gram idea and pushing the "n" out to the length of a context window, thousands of tokens, and learning the distribution from huge corpuses of data. As processors and data have gotten more and more complex, we have pushed this idea to its extreme. Encoded in the distributions of words and the relationship between how often those words show up and irrespective of the meaning of those words is information.

We have been using the word *information* loosely. The ladder of approximations showed that the distribution of tokens carries it, and a few pages before that I promised a way to measure it, a quantity Shannon calls entropy. Now we build the ruler.

Start with what we already understand. Picking one character out of 32 takes 5 bits. We got that from switches: 32 is 2 multiplied by itself five times, and the log base 2 of 32 is 5. Here is the same fact told a different way. Before the character arrives there are 32 possibilities. After it arrives there is one. The character cleared away 32-possibilities-worth of uncertainty, and the size of what it cleared away, measured in bits, is 5.

Now narrow the focus from a whole stream down to a single outcome. When one specific thing happens, how surprised should you be? If it was certain to happen, not at all. The sun rising tomorrow tells you nothing you did not already know. The rarer the event, the more surprising it is when it arrives. Shannon makes this precise. An outcome that happens with probability p carries a surprise of log base 2 of 1/p.

Check that against the bits we already have. An event with a 1-in-32 chance has p = 1/32, so 1/p = 32, and the log base 2 of 32 is 5. A 1-in-32 event carries 5 bits of surprise. That is the same 5 bits it took to pick one character out of 32, and it should be, because learning that a 1-in-32 event happened is the same act as singling out one option from 32. Surprise, measured in bits, is just the number of bits it takes to pick the outcome out of the lineup. And a certain event, with p = 1, has 1/p = 1, and the log base 2 of 1 is 0. A sure thing carries zero bits of surprise. The formula agrees with common sense at both ends.

A source does not produce one outcome, it produces a stream of them. Some symbols are common and barely surprising. Others are rare and carry a jolt. Shannon's question is: on average, how much surprise does this source produce per symbol? To take the average we weight each outcome's surprise by how often that outcome actually shows up. Symbol i appears a pᵢ fraction of the time and carries log base 2 of 1/pᵢ bits of surprise when it does. Sum that product over every symbol the source can produce:

H = Σ pᵢ log₂(1/pᵢ)

That is entropy. It is the average surprise per symbol. You will usually see it written in a slightly different form. Pulling the fraction out of the logarithm flips its sign, because the log of 1/p is just the negative of the log of p, which gives:

H = -Σ pᵢ log₂ pᵢ

The two are the same formula. The first one says what entropy means, average surprise. The second one is the way it is conventionally written. Do not let the minus sign in front trouble you, it is bookkeeping for the flipped fraction, nothing more.

Now collect what this buys us. If all N outcomes are equally likely, every one of them has probability 1/N, every one carries log base 2 of N bits of surprise, and the average of a pile of identical numbers is just that number. Entropy becomes log N, which is exactly the capacity formula from earlier. The equally-likely case was never a separate idea. It was entropy all along, in the one situation simple enough that we could reach it by counting switches.

The interesting case is the uneven one. Recall that *e* is far more common than *q* in English. An *e*, being common, has a high probability and therefore carries little surprise. A *q*, being rare, carries a lot. Entropy averages the two, and the averaging is weighted: the small surprise of *e* is multiplied by the large fraction of the time *e* appears, and the large surprise of *q* is multiplied by the tiny fraction of the time *q* appears. Work it through for all twenty-six letters and a space, and the entropy of English comes out below log base 2 of 27, which is the value you would get if every letter were equally likely. The unevenness pulls the number down. This is worth stating plainly: structure lowers entropy. A source with lopsided, predictable statistics produces less surprise per symbol than a source where anything goes. That is the same fact the ladder of approximations was showing us from the other direction. Each rung captured more structure, a more structured source is more predictable, and a more predictable source has lower entropy.

I have been handing you the entropy formula as though it were obvious. Shannon does better than that. He asks what we should want from any honest measure of uncertainty, writes down three requirements, and proves that exactly one formula satisfies all three. The requirements are reasonable. First, continuity: a tiny change in the probabilities should produce only a tiny change in the measure, no sudden jumps. Second, monotonicity: if the outcomes are all equally likely, then having more of them should mean more uncertainty, because choosing one option out of ten is a more uncertain business than choosing one out of two. Third, decomposition: if you make a choice in two steps instead of one, the total uncertainty should add up the same either way. Shannon proves that the only formula meeting all three is H = -K Σ pᵢ log pᵢ. The K is just a units knob, the choice between measuring in inches or centimeters. Set it for base-2 logarithms and the unit is the bit.

Then Shannon does something that, the first time I read the paper, I had to read twice. Having just proved that his formula is the unique one satisfying three reasonable requirements, he turns around and tells you the proof does not matter. His words: the three requirements are "in no way necessary for the present theory" [@shannon1948communication]. The real justification of the definition, he says, will lie in its implications.

Shannon is not claiming entropy fell out of the sky as the only measure the universe would permit. He is saying something more modest and more honest. Here is a definition. It is reasonable. It will earn its place by what it lets us do, not by being forced on us.

A definition in a research paper is a bet, not a discovery, and Shannon placed his bet and told you plainly that it was one. The decades of information theory, digital communication, and machine learning since have settled the bet in his favor. The move to notice, the move worth carrying into your own thinking, is that he justified the definition by its productivity rather than its inevitability.

The whole idea fits in one picture. Take the smallest source that is still interesting, one with two outcomes, a coin. It comes up heads with probability p and tails with probability 1 minus p. Its entropy is the average surprise of a flip, and we can plot that entropy against p.

<div align="center" style="margin: 1em 0;">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 470 290" width="470" stroke="currentColor" fill="none" stroke-width="1.5" style="font-family: ui-sans-serif, system-ui; font-size: 13px; max-width: 100%; height: auto;"><line x1="60" y1="36" x2="60" y2="240"/><line x1="60" y1="240" x2="430" y2="240"/><line x1="56" y1="40" x2="60" y2="40"/><text x="50" y="44" text-anchor="end" stroke="none" fill="currentColor">1</text><text x="50" y="244" text-anchor="end" stroke="none" fill="currentColor">0</text><line x1="60" y1="240" x2="60" y2="244"/><line x1="240" y1="240" x2="240" y2="244"/><line x1="420" y1="240" x2="420" y2="244"/><text x="60" y="258" text-anchor="middle" stroke="none" fill="currentColor">0</text><text x="240" y="258" text-anchor="middle" stroke="none" fill="currentColor">0.5</text><text x="420" y="258" text-anchor="middle" stroke="none" fill="currentColor">1</text><text x="245" y="280" text-anchor="middle" stroke="none" fill="currentColor">p  (probability of heads)</text><text x="22" y="138" text-anchor="middle" stroke="none" fill="currentColor" transform="rotate(-90 22 138)">H  (bits per flip)</text><path d="M 240,40 L 240,240" stroke-dasharray="3 3" stroke-width="1"/><path d="M 60,240 L 78,183 L 96,146 L 114,118 L 132,96 L 150,78 L 168,64 L 186,53 L 204,46 L 222,41 L 240,40 L 258,41 L 276,46 L 294,53 L 312,64 L 330,78 L 348,96 L 366,118 L 384,146 L 402,183 L 420,240"/><circle cx="240" cy="40" r="2.5" fill="currentColor" stroke="none"/></svg>
</div>

Read the curve from the edges in. At the far left, p is 0: the coin never comes up heads, every flip is tails, you are never surprised, and the entropy is 0. At the far right, p is 1: the coin is all heads, equally boring, entropy 0 again. In the middle, at p equal to one half, the coin is fair, every flip is a genuine question with no way to guess the answer, and the entropy reaches its highest value, exactly 1 bit. Between the middle and the edges the curve slopes down. A coin weighted to land heads 80 percent of the time sits partway down the slope, carrying less than a full bit per flip, because you can guess it correctly most of the time and a flip you can half-guess is only half a surprise.

That curve is the entire concept. Entropy is highest when you know least and lowest when you know most, and any structure at all, any departure from everything-equally-likely, pulls the number down off the peak. It is the same reason English, with its lopsided letter frequencies, carries less than log base 2 of 27 bits per letter.

Shannon closes the section by working out the formal properties of H, the rules of thumb the rest of information theory runs on. I have collected them in a footnote[^11]. One of them belongs here in the main text. If you know one thing, your uncertainty about a second thing related to it can only fall, never rise. Knowing the first letter of a word can make the next letter easier to guess, and it can never make it harder. The size of that help is itself a measurable quantity. Shannon does not name it in this paper, but later workers will, and they will call it mutual information. It becomes the central tool for asking what a trained model has actually learned from its data, and we will return to it when the book reaches that question.

That is everything the paper needs to hand us. Step back and remember the hedge from a few pages ago: Shannon told us his definition of entropy would be justified not by being inevitable but by being productive. The returns are in. Entropy became the foundation of digital communication, the basis of the statistical language models that have run quietly inside phones and search engines for decades, the training signal behind every modern neural network, and the measuring stick interpretability researchers now use to study those same networks. Few definitions in the history of engineering have paid off on the scale of this one.

The sentence of the paper that has aged best, we passed earlier: a sufficiently complex stochastic process will give a satisfactory representation of a discrete source. The rest of this book follows how the phrase *sufficiently complex* got unpacked. We will follow this thread through the coding theory of the 1950s, through Chomsky's argument that grammar could never be reduced to statistics, through the revival of statistical language modeling in the 1990s, and into the 2010s, when *sufficiently complex* came to mean a model with billions of adjustable parameters trained on a large fraction of everything ever written. What such a model encodes, when it encodes text, is a learned approximation of the joint distribution Shannon described in 1948. The question this book is building toward is what structure that approximation has. Shannon set meaning aside as irrelevant to the engineering. We are going to ask whether, once the distribution is rich enough, meaning quietly finds its way back in.

Any of the individuals mentioned in this chapter could be argued to be the origin of the story we are telling, and countless others contributed to the work of creating the incredible machines we now take for granted. What I have laid out in this chapter are the earliest threads I think are important to the story. Ada Lovelace, Alan Turing, and Claude Shannon each mark important moments in the origins of artificial intelligence, and each one's work still inspires and influences the industry today. After reading this work, I would not fault you for arguing that Babbage, Russell, or even Cantor is the real origin. The truth is, computing has from the beginning been part of a larger project. Its origins lie in the innate desire to understand what it is to think.


[^1]: She chose to be buried by him in their family cemetery, in spite of her mother's deep loathing of the man, leading to her mother refusing to attend the funeral [@seymour2018byron].

[^2]: The whole of Cantor's diagonalization argument is only about three pages, and requires no real background in math or logic to follow. It is entirely worth taking a moment to pull up his paper [@cantor1891diagonal] to read through. Of all the works that I have referenced so far, it is by far the easiest to read in the original.

[^3]: Russell sent his paradox to Frege in a letter in 1902 [@russell1902letter], just as Frege was finishing the second volume of his Grundgesetze, and Frege added an appendix to the volume that was already at the printer [@frege1903grundgesetze], acknowledging with extraordinary grace that Russell's discovery had undermined his life's work.

[^4]: The actual construction is more technical. Gödel had to show that the operation 'substitute the Gödel number of a formula into itself' could be expressed as arithmetic within the system. I have chosen to simplify it here to make the work a bit more accessible.

[^5]: In his paper Turing describes a machine that prints 010101 repeating forever [@turing1936computable, p. 233]

[^6]: Shannon's 1937 thesis [@shannon1937symbolic] ran the algebra in the opposite polarity. He used a quantity called hindrance, where 0 means closed and 1 means open. Series in his algebra is `+` and parallel is `·`, and any theorem in his system carries over to the modern one by swapping zeros and ones throughout. The flip to "high voltage on the wire is 1" congeals in the late 1940s as vacuum tubes and then transistors replace relays.

[^7]: Chaining together "n" full-adders gives an "n"-bit ripple-carry adder, which is how every modern ALU does integer addition at its lowest level. What we use to create these circuits has changed from relays to vacuum tubes, to the transistor over the last century, but the fundamental algebra is the same.

[^8]: Shannon's 1937 thesis [@shannon1937symbolic] wrote this same circuit as `X = RX + S` in hindrance algebra, where 0 means closed (current flowing) and 1 means open. In that polarity `+` is series and `·` is parallel, the reverse of what those symbols mean in the modern Boolean convention used throughout this book.

[^9]: Shannon credits a coworker, John Tukey, with creation of the term "bit" [@shannon1948communication].

[^10]: Shannon did not coin the word entropy, he borrowed it. The expression −Σ pᵢ log pᵢ already appears in nineteenth-century statistical mechanics, in Ludwig Boltzmann's work on heat [@sharp2015boltzmann], where the pᵢ are the probabilities of the microscopic states a gas might be in. The borrowing is more than a pun. In 1957 the physicist E. T. Jaynes argued that thermodynamic entropy simply is information entropy [@jaynes1957information], a measure of an observer's uncertainty about which microscopic state a system occupies. The strong form of that claim is still debated by philosophers of physics, but the formal identity of the two quantities is not. It is the first of several moments in this book where two fields discover, to mutual surprise, that they have been studying the same object under different names.

[^11]: Shannon derives several properties of H directly from the formula [@shannon1948communication]. The ones worth knowing: H is zero exactly when one outcome is certain, since a foregone conclusion carries no surprise; H is largest when every outcome is equally likely, reaching log n for "n" outcomes, which is why English text, with its lopsided letter frequencies, carries fewer bits per letter than a random string of the same alphabet would; and the uncertainty of two things taken together is never greater than the sum of their separate uncertainties, with equality only when they are independent. That last point has a one-sided cousin, the conditioning inequality H(y) ≥ Hₓ(y), which says formally that knowing x never increases uncertainty about y. The gap between the two sides, H(y) − Hₓ(y), is the mutual information mentioned above.
