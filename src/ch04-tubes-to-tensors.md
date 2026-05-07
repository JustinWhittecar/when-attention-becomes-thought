# From Tubes to Tensors

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-06.*

## Narrative job

Tell the hardware story that every later chapter takes for granted. The vacuum tube gave us the first programmable machines. The transistor (Bell Labs, 1947) made them small and reliable. The integrated circuit made them dense. Moore's empirical observation that density would double every eighteen to twenty-four months held for half a century, and the compounding made things possible that nothing else could have. Then the chapter does the move that matters most for this book: it lays out CPU, GPU, and TPU as three answers to the question "what should silicon specialize in?" Each gets a worked propositional-logic circuit so the reader sees, not just hears, why parallel matrix multiplication is the operation modern AI runs on. The chapter closes on Sutton's Bitter Lesson: general methods plus compute beat clever structure, every time. By the end the reader understands hardware as a primary cause of the AI story, not its backdrop.

## Pedagogical commitments for this chapter

- The CPU > GPU > TPU progression is the spine. Each is introduced through a propositional-logic worked example so the reader can see the gates and the data flow, not just hear the marketing names.
- Pseudocode appears for one operation per architecture: a sequential loop on the CPU, a parallel-for on the GPU, and a systolic-array multiply on the TPU. The reader leaves understanding why the same arithmetic costs different amounts of time on different silicon.

## Reading list

1. Bardeen, J. & Brattain, W. H. (1948). "The Transistor, A Semi-Conductor Triode." *Physical Review*, 74, 230-231. The Bell Labs announcement. Short. Read for the historical hinge.
2. Felker, J. H. (1954). "Performance of TRADIC Transistor Digital Computer." *Proceedings of the December 8-10, 1954, Eastern Joint Computer Conference*, pp. 46-49. The first US transistorized computer, nine years after EDVAC.
3. Moore, G. E. (1965). "Cramming More Components onto Integrated Circuits." *Electronics*, 38(8), 114-117. The original Moore's Law paper. Three pages. Read it whole.
4. Mead, C. (1990). "Neuromorphic Electronic Systems." *Proceedings of the IEEE*, 78(10), 1629-1636. Sets up the question of what silicon ought to specialize in. Cite when introducing the GPU and TPU as answers.
5. Patterson, D. A. & Hennessy, J. L. (latest edition). *Computer Organization and Design.* Reference text. Read the chapters on instruction fetch, pipelining, and memory hierarchy. Cite for accessible exposition.
6. NVIDIA (2007). "NVIDIA CUDA Programming Guide" (early version). The release that turned graphics cards into general-purpose parallel computers. Read for the SIMT model.
7. Jouppi, N. P. et al. (2017). "In-Datacenter Performance Analysis of a Tensor Processing Unit." *ISCA 2017.* The TPU paper. Read for the systolic array and the matmul-as-primary-operation argument.
8. Sutton, R. S. (2019). "The Bitter Lesson." *Incomplete Ideas* blog. The closer.
9. Hennessy, J. L. & Patterson, D. A. (2019). "A New Golden Age for Computer Architecture." *Communications of the ACM*, 62(2), 48-60. The 2017 Turing Award lecture. Read for the framing of domain-specific architectures and what comes after Moore.

## Worked examples to build into the chapter

- A four-bit ripple-carry adder, in propositional logic, as the simplest concrete example of "the CPU's arithmetic logic unit." Builds directly on Chapter 2's half-adder and full-adder.
- The same arithmetic, replicated thirty-two times in parallel, as the GPU's signature move. Show the same gates with the same truth tables, but laid out so the reader sees throughput from replication.
- A 2x2 by 2x2 matrix multiply as a systolic array, the TPU's signature move. Show the data flow on a small grid so the reader can trace one element of the output back to the partial products that produced it.
- Pseudocode for the same matrix multiply written three ways: a triple nested loop (CPU), a parallel-for over rows (GPU), and a systolic schedule (TPU). The reader leaves understanding that the algorithm is the same; the silicon is what changes.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

Post-Moore architectures: chiplets, 3D-stacked memory, photonic interconnect, neuromorphic chips, the latest TPU and Trainium generations. Any serious benchmarking that changes the cost-per-FLOP comparison across architectures. Update this chapter when a new generation of accelerators ships with materially different economics.
