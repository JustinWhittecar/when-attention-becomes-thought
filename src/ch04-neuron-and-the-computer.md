# The Neuron and the Computer

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-08-15.*

## Narrative job

Show that computing's founding formal object was a model of a neuron, proposed in 1943 by two men trying to explain a brain, and then borrowed in 1945 by von Neumann for a different reason entirely: substrate-independence, not imitation. The imitation therefore sits in the material rather than in each builder's motive, which is why it survived builders who were not imitating anything. Turing 1948 then makes it deliberate and extends it from the unit to the upbringing. End with the reader able to see "the brain is a computer" as a design programme with a date, an object, a lineage, and a stated exam, and to see why the imitation game is that programme's terminal test rather than a philosopher's dodge. This is also the chapter where we cash in on Chapter 1's propositional logic by showing both a McCulloch-Pitts neuron and an EDVAC instruction in those terms.

## Reading list

The first six entries plus Turing 1948 and 1950 are the spine, and their reading notes are complete. The remaining entries are targeted consults, pulled in during drafting rather than read as full nights. Godfrey & Hendry 1993 and Backus 1978 moved to Chapter 5 on 2026-08-15: the von Neumann bottleneck is a hardware argument and belongs with the hardware chapter.

1. McCulloch, W. S. & Pitts, W. (1943). "A Logical Calculus of the Ideas Immanent in Nervous Activity." *Bulletin of Mathematical Biophysics*, 5(4), 115-133. The founding paper. Read it whole; it is fifteen pages.
2. Gefter, A. (2015). "The Man Who Tried to Redeem the World with Logic." *Nautilus*. Read with Smalheiser, N. R. (2000), "Walter Pitts," *Perspectives in Biology and Medicine*, 43(2), 217-226, and Abraham, T. H. (2016), *Rebel Genius: Warren S. McCulloch's Transdisciplinary Life in Science* (MIT Press). Supplementary, for biographical color. The human story behind the 1943 paper: Pitts the homeless teenage autodidact, the McCulloch household that took him in, and the later falling-out. Chapters 1 to 3 leaned on dedicated biographies for exactly this kind of texture.
3. Kleene, S. C. (1956). "Representation of Events in Nerve Nets and Finite Automata." In *Automata Studies*, Shannon, C. E. & McCarthy, J. (eds.), Princeton University Press, 3-41. Read after McCulloch-Pitts. Formalizes what McCulloch-Pitts nets actually compute, finite automata and regular events, and is the primary source for the Turing-equivalence claim the 1943 paper only asserts.
4. von Neumann, J. (1945). "First Draft of a Report on the EDVAC." Moore School of Electrical Engineering, University of Pennsylvania. Read Sections 1 through 8 carefully and Section 15 whole. The architectural blueprint that names McCulloch-Pitts neurons as its primitive and introduces stored-program computation.
5. von Neumann, J. (1958). *The Computer and the Brain.* Yale University Press (Silliman Lectures, published posthumously). Read whole; it is short. Von Neumann's own comparison of neural and digital computation, and a built-in counterweight: he argues the brain is not simply digital. Keeps the chapter's "brain is a computer" claim honest.
6. Aspray, W. (1990). *John von Neumann and the Origins of Modern Computing.* MIT Press. Read the EDVAC chapters. Historiography of von Neumann's computing work, including the First Draft authorship question and the Eckert-Mauchly credit dispute. The von Neumann counterpart to the biographies Chapters 1 to 3 relied on.
7. Turing, A. M. (1948). "Intelligent Machinery." National Physical Laboratory report (reprinted in *Machine Intelligence 5*, 1969). Supplementary. Turing's unpublished sketch of "unorganised machines," randomly wired networks of logical units that could be trained. A 1948 bridge between McCulloch-Pitts and Turing 1950, and a precedent for Chapter 6's perceptron.
8. Turing, A. M. (1950). "Computing Machinery and Intelligence." *Mind*, 59, 433-460. The chapter's closer. The question "can machines think?" becomes coherent only after Chapter 1's logic and this chapter's neuron-and-stored-program convergence are in place.
9. Wiener, N. (1948). *Cybernetics: or Control and Communication in the Animal and the Machine.* Read the introduction. Background. Cited where the chapter touches feedback and purpose.
10. Heims, S. J. (1991). *The Cybernetics Group.* MIT Press. Optional. The institutional history of the Macy Conferences, where McCulloch, Pitts, von Neumann, Wiener, and Shannon shared a room and "the brain is a computer" became a research program. Connective tissue, in the people-weaving style of Chapters 1 to 3.
11. Hebb, D. O. (1949). *The Organization of Behavior.* Read Chapter 4 ("The First Stage of Perception"). The learning rule McCulloch-Pitts deliberately avoided, included here so that Chapter 6 has a precedent to invoke.
12. Lettvin, J. Y., Maturana, H. R., McCulloch, W. S. & Pitts, W. H. (1959). "What the Frog's Eye Tells the Frog's Brain." *Proceedings of the IRE*, 47(11), 1940-1951. Optional counterweight. The same authors, sixteen years later, finding the brain to be a messy feature-detector rather than a clean logic engine.

## Worked examples to build into the chapter

- A single McCulloch-Pitts neuron computing AND, OR, and NOT, expressed first as a propositional formula and then as a small circuit diagram. Reuses the propositional vocabulary from Chapter 1.
- The §7.3 EDVAC adder from von Neumann's First Draft, redrawn so the reader can see threshold-1, 2, and 3 elements computing carry and sum from the same three inputs. The same half-adder from Chapter 3, now built from neurons instead of gates.
- A pseudocode walkthrough of the EDVAC fetch-execute cycle: read instruction at address PC, decode, execute, increment PC. Three to five lines. The reader meets stored-program computation here.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

This chapter is historical. Update only if new scholarship reframes the McCulloch-Pitts to von Neumann lineage, or if Hebb's place in the connectionist genealogy is reassessed.
