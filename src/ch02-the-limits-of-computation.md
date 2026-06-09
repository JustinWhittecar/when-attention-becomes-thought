"I believe: Everything that can be object of scientific thinking in general, as soon as it is ripe for formation of a theory, runs into the axiomatic method and thereby indirectly to mathematics" - David Hilbert, *Axiomatic Thinking* [@hilbert1917axiomatic]

The bridge from logic to arithmetic sets the groundwork for the crisis in math that Cantor ignites just before the start of the twentieth century, which runs straight through from him to Turing. Turing is the person the popular imagination often conjures as the start of modern computing, and his work now inspires those well outside of mathematics and logic. During his time, the story we are about to tell interested only those working on the hardest problems in math and logic. The Turing machine he would imagine was, however, an artifice for responding to a deeply technical question about mathematical logic. In order to understand how it came to be let's backtrack a couple of steps to talk first about Cantor, Hilbert, Gödel, Russell, and the debate which the Turing machine resolved.

David Hilbert is perhaps the best place for us to begin, as he set down a challenge for logicians and mathematicians to answer a set of very real and important questions, one of which the Turing machine answers. He wanted to prove that mathematics was three things: complete, decidable, and consistent [@hilbert1917axiomatic]. If this was the case it would mean that all mathematical statements could be proven using logic, that there existed a logical procedure to determine the truth of any statement in finite steps, and that the system was free of contradictions. In Hilbert's mind, if these things held true, math would be on the surest possible footing. Even before Hilbert laid out this program, the seeds of its demise had already been sown.

Cantor is an incredibly interesting figure, and if you ever want to explore the life of a troubled genius I cannot think of a more appropriate one. He is in many ways the archetype of a man haunted by his own thoughts, and spent much of his life in and out of mental hospitals, ultimately dying in a sanatorium [@dauben1990cantor]. While his life and death are tragic tales, his work in mathematics is awe-inspiring not just because it would start a whole new branch of mathematics, set theory, but also because the exact same technique he used to make his most startling claim would be used for two of the most important proofs at the foundation of all modern computing[^1].

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

Bertrand Russell, in the writing of *Principia Mathematica* with Alfred Whitehead [@whitehead1910principia], continued the work of Boole and Frege in attempting to encode all of mathematics in logic. Their work was, at the time, the most complete example, taking 379 pages to build up from simple axioms to the proof that 1+1=2. Their project is in many ways still ongoing in similar projects like the Lean Mathlib library, currently formalizing huge tracts of modern mathematics. For Russell and Whitehead to make their logical system work, they had to rely on type theory to resolve the problem of self-reference seen in the paradoxes above[^2]. Russell's fix here will likely feel familiar to modern programmers: it is the same kind of move that TypeScript makes on top of JavaScript, where a layer of type discipline rules out certain constructions before they can cause problems at runtime.

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

Now Gödel constructs a new formula. He defines G as the statement: "the formula F_x(x) is not provable," where x is the blank to fill in. Like every other formula in the system, G has a Gödel number. Call it g. When we plug g into G's blank, we get the closed statement G(g), which says: "F_g(g) is not provable." But G itself is F_g, so G(g) is saying "G(g) is not provable." The statement asserts its own unprovability[^3]. This is Gödel's version of Cantor flipping each digit along the diagonal. Gödel's construction negates the property "is provable" along the diagonal to create a formula that disagrees with what the system would have to say about it.

Now look at what this forces:

- If G(g) is provable, then it is true, so G(g) is not provable. Contradiction. The system is inconsistent.
- If G(g) is not provable, then it is true (it correctly states its own unprovability), but the system cannot prove it. The system is incomplete.

Either the system contradicts itself or it cannot capture its own truths. There is no third option. Hilbert wanted mathematics to be both complete and consistent. Gödel proved it cannot be both. The construction is the same diagonal trick Cantor used decades earlier. Where Cantor used it to show that some infinities cannot be enumerated, Gödel used it to show that some truths cannot be proven. The idea that mathematical operations could be encoded as numbers, and that those numbers could in turn be operated upon, would not stay confined to logic for long. Within fifteen years, John von Neumann would recognize that this is exactly how a computer should be built.

But Cantor's diagonalization argument has not had its fill. Hilbert also asked for a system that was decidable, and it is precisely that problem which Turing sets out to solve. Unfortunately, once again we will learn that we won't know, we can't know. In fact, in Turing's own introduction to his paper he states "In particular, it is shown (§11) that the Hilbertian Entscheidungsproblem can have no solution" [@turing1936computable, p. 231]. In other words, there is not a mechanical procedure that, given a mathematical formula, decides in finite steps whether that formula is provable. In order to do this, Turing must first define what a mechanical procedure actually means without counting on intuition.

Turing introduces a machine that consists of a tape divided into squares that are either empty, contain a 1, or contain a 0, and which a read/write head can scan one at a time [@turing1936computable]. This machine has a finite set of states it can be in, and a table of rules it follows based on which state it is in. These rules are things like when in state "x" move back three squares and print 1, or when in state "y" erase the symbol on the current square. That's it, that is the whole machine. The finite table of rules can drive an infinite output[^4]. Turing describes the kind of machine that repeats forever as **circle-free**, and, somewhat counterintuitively, calls a machine **circular** if it eventually stops printing fresh digits or gets stuck in a loop. Importantly, he defines a computable sequence as one that some circle-free machine prints and a computable number is the real number whose binary expansion is that sequence.

As Gödel did with formulas, Turing turns his machines into numbers. Every Turing machine is a finite table of rules, finite set of symbols, and finite set of states. Interestingly, this means that the whole of the machine can be written out as a string of symbols, and that string can be encoded into a single number using Gödel's same method. Turing calls this number the D.N (description number) of the machine. This means you could feed the description number of a Turing machine into another Turing machine and operate on it. In other words, a single machine can in principle simulate any other. This is the exact mechanism of self-reference that causes issues for Russell in his *Principia*, but this method of one machine being able to simulate another by reading its description number will inspire John von Neumann to put programs and data in the same place, an idea a later chapter develops.

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


[^1]: The whole of Cantor's diagonalization argument is only about three pages, and requires no real background in math or logic to follow. It is entirely worth taking a moment to pull up his paper [@cantor1891diagonal] to read through. Of all the works that I have referenced so far, it is by far the easiest to read in the original.

[^2]: Russell sent his paradox to Frege in a letter in 1902 [@russell1902letter], just as Frege was finishing the second volume of his Grundgesetze, and Frege added an appendix to the volume that was already at the printer [@frege1903grundgesetze], acknowledging with extraordinary grace that Russell's discovery had undermined his life's work.

[^3]: The actual construction is more technical. Gödel had to show that the operation 'substitute the Gödel number of a formula into itself' could be expressed as arithmetic within the system. I have chosen to simplify it here to make the work a bit more accessible.

[^4]: In his paper Turing describes a machine that prints 010101 repeating forever [@turing1936computable, p. 233]

