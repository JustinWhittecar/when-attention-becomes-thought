# The Neuron and the Computer

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-09-29.*

## Narrative job

Show that computing's founding formal object was a model of a neuron, proposed in 1943 by two men trying to explain a brain, and then borrowed in 1945 by von Neumann for a different reason entirely: substrate-independence, not imitation. The imitation therefore sits in the material rather than in each builder's motive, which is why it survived builders who were not imitating anything. Close on the credit question, settled the way Chapters 1 to 3 settled Boole and Lovelace, and on the patent ruling that put the design in the public domain. This is also the chapter where we cash in on Chapter 1's propositional logic by showing both a McCulloch-Pitts neuron and an EDVAC instruction in those terms. What happened to the object next (Turing's attempt to teach it, the audits of what it lacked, and the imitation game) is Chapter 5.

## Reading list

The first four entries are the spine, and their reading notes are complete. The biography entry is a targeted consult, pulled in during drafting. Godfrey & Hendry 1993 and Backus 1978 moved to Chapter 6 on 2026-08-15, since the von Neumann bottleneck is a hardware argument. Turing 1948 and 1950, Kleene 1956, von Neumann 1958, Hebb, Wiener, Heims, and Lettvin et al. moved to Chapter 5 when this chapter was split on 2026-09-29.

1. McCulloch, W. S. & Pitts, W. (1943). "A Logical Calculus of the Ideas Immanent in Nervous Activity." *Bulletin of Mathematical Biophysics*, 5(4), 115-133. The founding paper. Read it whole; it is fifteen pages.
2. Gefter, A. (2015). "The Man Who Tried to Redeem the World with Logic." *Nautilus*. Read with Smalheiser, N. R. (2000), "Walter Pitts," *Perspectives in Biology and Medicine*, 43(2), 217-226, and Abraham, T. H. (2016), *Rebel Genius: Warren S. McCulloch's Transdisciplinary Life in Science* (MIT Press). Supplementary, for biographical color. The human story behind the 1943 paper: Pitts the homeless teenage autodidact, the McCulloch household that took him in, and the later falling-out.
3. von Neumann, J. (1945). "First Draft of a Report on the EDVAC." Moore School of Electrical Engineering, University of Pennsylvania. Read Sections 1 through 8 carefully and Sections 14 and 15 whole. The architectural blueprint that names McCulloch-Pitts neurons as its primitive and introduces stored-program computation.
4. Aspray, W. (1990). *John von Neumann and the Origins of Modern Computing.* MIT Press. Read the EDVAC chapters. Historiography of von Neumann's computing work, including the First Draft authorship question and the Eckert-Mauchly credit dispute.

## Worked examples to build into the chapter

- A single McCulloch-Pitts neuron computing AND, OR, and NOT, expressed first as a propositional formula and then as a small circuit diagram. Reuses the propositional vocabulary from Chapter 1.
- The circle: a neuron that feeds its own output back to itself and so holds one bit, the same latch Shannon built from a relay in Chapter 3.
- The §7.3 EDVAC adder from von Neumann's First Draft, redrawn so the reader can see threshold-1, 2, and 3 elements computing carry and sum from the same three inputs. The adder from Chapter 3, now built from neurons instead of gates.
- The EDVAC fetch-execute cycle as pseudocode, the book's first: the control takes words as they arrive at its connection with memory, and a transfer order moves that connection. The reader meets stored-program computation here.

## Exercises for the reader

To be drafted at the editing pass.

## What to watch

This chapter is historical. Update only if new scholarship reframes the McCulloch-Pitts to von Neumann lineage, or if the Eckert-Mauchly credit question is reopened.
