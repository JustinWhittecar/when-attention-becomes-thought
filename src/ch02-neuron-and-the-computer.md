# The Neuron and the Computer

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-06.*

## Narrative job

Show how, within two years of each other, two fields converged on the same primitive. McCulloch and Pitts argue in 1943 that because neurons fire all-or-none, a network of them computes propositional logic, which means thinking is, in principle, a formal operation. Two years later von Neumann picks up that vocabulary to specify the EDVAC, the stored-program architecture every modern computer inherits. End with the reader able to see why "the brain is a computer" is not a metaphor borrowed from mid-century engineering but a claim with a specific, traceable historical genealogy. This is also the chapter where we cash in on Chapter 2's propositional logic by showing both a McCulloch-Pitts neuron and an EDVAC instruction in those terms.

## Reading list

1. McCulloch, W. S. & Pitts, W. (1943). "A Logical Calculus of the Ideas Immanent in Nervous Activity." *Bulletin of Mathematical Biophysics*, 5(4), 115-133. The founding paper. Read it whole; it is fifteen pages.
2. von Neumann, J. (1945). "First Draft of a Report on the EDVAC." Moore School of Electrical Engineering, University of Pennsylvania. Read Sections 1 through 8 carefully and Section 15 whole. The architectural blueprint that names McCulloch-Pitts neurons as its primitive and introduces stored-program computation.
3. Godfrey, M. D. & Hendry, D. F. (1993). "The Computer as von Neumann Planned It." *IEEE Annals of the History of Computing*, 15(1), 11-21. Historiographical correction. Read alongside the First Draft to keep the popular "von Neumann bottleneck" caricature in proportion.
4. Turing, A. M. (1950). "Computing Machinery and Intelligence." *Mind*, 59, 433-460. The chapter's closer. The question "can machines think?" becomes coherent only after Chapter 2's logic and this chapter's neuron-and-stored-program convergence are in place.
5. Wiener, N. (1948). *Cybernetics: or Control and Communication in the Animal and the Machine.* Read the introduction. Background. Cited where the chapter touches feedback and purpose.
6. Hebb, D. O. (1949). *The Organization of Behavior.* Read Chapter 4 ("The First Stage of Perception"). The learning rule McCulloch-Pitts deliberately avoided, included here so that Chapter 5 has a precedent to invoke.

## Worked examples to build into the chapter

- A single McCulloch-Pitts neuron computing AND, OR, and NOT, expressed first as a propositional formula and then as a small circuit diagram. Reuses the propositional vocabulary from Chapter 2.
- The §7.3 EDVAC adder from von Neumann's First Draft, redrawn so the reader can see threshold-1, 2, and 3 elements computing carry and sum from the same three inputs. The same half-adder from Chapter 2, now built from neurons instead of gates.
- A pseudocode walkthrough of the EDVAC fetch-execute cycle: read instruction at address PC, decode, execute, increment PC. Three to five lines. The reader meets stored-program computation here.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

This chapter is historical. Update only if new scholarship reframes the McCulloch-Pitts to von Neumann lineage, or if Hebb's place in the connectionist genealogy is reassessed.
