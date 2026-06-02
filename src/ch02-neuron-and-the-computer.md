# The Neuron and the Computer

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-21.*

## Narrative job

Show how, within two years of each other, two fields converged on the same primitive. McCulloch and Pitts argue in 1943 that because neurons fire all-or-none, a network of them computes propositional logic, which means thinking is, in principle, a formal operation. Two years later von Neumann picks up that vocabulary to specify the EDVAC, the stored-program architecture every modern computer inherits. End with the reader able to see why "the brain is a computer" is not a metaphor borrowed from mid-century engineering but a claim with a specific, traceable historical genealogy. This is also the chapter where we cash in on Chapter 1's propositional logic by showing both a McCulloch-Pitts neuron and an EDVAC instruction in those terms.

## Reading list

The first six entries are the spine. The remaining entries were added on 2026-05-21 to bring this chapter to the level of biographical detail, historiographical care, and primary-source grounding that Chapter 1 reached. Entries marked supplementary or optional are quick consults or counterweights, not full reading nights.

1. McCulloch, W. S. & Pitts, W. (1943). "A Logical Calculus of the Ideas Immanent in Nervous Activity." *Bulletin of Mathematical Biophysics*, 5(4), 115-133. The founding paper. Read it whole; it is fifteen pages.
2. Gefter, A. (2015). "The Man Who Tried to Redeem the World with Logic." *Nautilus*. Read with Smalheiser, N. R. (2000), "Walter Pitts," *Perspectives in Biology and Medicine*, 43(2), 217-226, and Abraham, T. H. (2016), *Rebel Genius: Warren S. McCulloch's Transdisciplinary Life in Science* (MIT Press). Supplementary, for biographical color. The human story behind the 1943 paper: Pitts the homeless teenage autodidact, the McCulloch household that took him in, and the later falling-out. Chapter 1 leaned on dedicated biographies for exactly this kind of texture.
3. Kleene, S. C. (1956). "Representation of Events in Nerve Nets and Finite Automata." In *Automata Studies*, Shannon, C. E. & McCarthy, J. (eds.), Princeton University Press, 3-41. Read after McCulloch-Pitts. Formalizes what McCulloch-Pitts nets actually compute, finite automata and regular events, and is the primary source for the Turing-equivalence claim the 1943 paper only asserts.
4. von Neumann, J. (1945). "First Draft of a Report on the EDVAC." Moore School of Electrical Engineering, University of Pennsylvania. Read Sections 1 through 8 carefully and Section 15 whole. The architectural blueprint that names McCulloch-Pitts neurons as its primitive and introduces stored-program computation.
5. von Neumann, J. (1958). *The Computer and the Brain.* Yale University Press (Silliman Lectures, published posthumously). Read whole; it is short. Von Neumann's own comparison of neural and digital computation, and a built-in counterweight: he argues the brain is not simply digital. Keeps the chapter's "brain is a computer" claim honest.
6. Aspray, W. (1990). *John von Neumann and the Origins of Modern Computing.* MIT Press. Read the EDVAC chapters. Historiography of von Neumann's computing work, including the First Draft authorship question and the Eckert-Mauchly credit dispute. The von Neumann counterpart to the biographies Chapter 1 relied on.
7. Godfrey, M. D. & Hendry, D. F. (1993). "The Computer as von Neumann Planned It." *IEEE Annals of the History of Computing*, 15(1), 11-21. Historiographical correction. Read alongside the First Draft to keep the popular "von Neumann bottleneck" caricature in proportion.
8. Backus, J. (1978). "Can Programming Be Liberated from the von Neumann Style? A Functional Style and Its Algebra of Programs." *Communications of the ACM*, 21(8), 613-641 (1977 Turing Award lecture). Read with Godfrey & Hendry. The source that coined the term "von Neumann bottleneck."
9. Turing, A. M. (1948). "Intelligent Machinery." National Physical Laboratory report (reprinted in *Machine Intelligence 5*, 1969). Supplementary. Turing's unpublished sketch of "unorganised machines," randomly wired networks of logical units that could be trained. A 1948 bridge between McCulloch-Pitts and Turing 1950, and a precedent for Chapter 4's perceptron.
10. Turing, A. M. (1950). "Computing Machinery and Intelligence." *Mind*, 59, 433-460. The chapter's closer. The question "can machines think?" becomes coherent only after Chapter 1's logic and this chapter's neuron-and-stored-program convergence are in place.
11. Wiener, N. (1948). *Cybernetics: or Control and Communication in the Animal and the Machine.* Read the introduction. Background. Cited where the chapter touches feedback and purpose.
12. Heims, S. J. (1991). *The Cybernetics Group.* MIT Press. Optional. The institutional history of the Macy Conferences, where McCulloch, Pitts, von Neumann, Wiener, and Shannon shared a room and "the brain is a computer" became a research program. Connective tissue, in Chapter 1's people-weaving style.
13. Hebb, D. O. (1949). *The Organization of Behavior.* Read Chapter 4 ("The First Stage of Perception"). The learning rule McCulloch-Pitts deliberately avoided, included here so that Chapter 4 has a precedent to invoke.
14. Lettvin, J. Y., Maturana, H. R., McCulloch, W. S. & Pitts, W. H. (1959). "What the Frog's Eye Tells the Frog's Brain." *Proceedings of the IRE*, 47(11), 1940-1951. Optional counterweight. The same authors, sixteen years later, finding the brain to be a messy feature-detector rather than a clean logic engine.

## Worked examples to build into the chapter

- A single McCulloch-Pitts neuron computing AND, OR, and NOT, expressed first as a propositional formula and then as a small circuit diagram. Reuses the propositional vocabulary from Chapter 1.
- The §7.3 EDVAC adder from von Neumann's First Draft, redrawn so the reader can see threshold-1, 2, and 3 elements computing carry and sum from the same three inputs. The same half-adder from Chapter 1, now built from neurons instead of gates.
- A pseudocode walkthrough of the EDVAC fetch-execute cycle: read instruction at address PC, decode, execute, increment PC. Three to five lines. The reader meets stored-program computation here.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

This chapter is historical. Update only if new scholarship reframes the McCulloch-Pitts to von Neumann lineage, or if Hebb's place in the connectionist genealogy is reassessed.
