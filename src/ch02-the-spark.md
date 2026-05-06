# The Spark: Self-Attention and the Transformer

> **This chapter is in progress.** The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-01.*

## Narrative job

Introduce the transformer architecture and the self-attention mechanism. Show why replacing recurrence with full parallelism changed the relationship between compute and capability, setting the stage for the scaling era.

## Reading list

1. McCulloch & Pitts (1943), "A Logical Calculus of the Ideas Immanent in Nervous Activity." The earliest mathematical model of the neuron. Establishes that networks of simple threshold units can compute any logical function, and gives von Neumann the "neuron" vocabulary he uses two years later in the First Draft. Read first to see that computing and neuroscience were entangled from the start, not separate disciplines that later collided.
2. von Neumann (1945), "First Draft of a Report on the EDVAC." The architectural substrate. The stored-program, fetch-one-instruction-at-a-time design that every later sequence model inherited as an unspoken prior. Read for the prior the rest of the chapter is working against.
3. Godfrey & Hendry (1993), "The Computer as von Neumann Planned It." Historiographical correction. The popular "von Neumann bottleneck" caricature is partly an artifact of what was actually built, not what was proposed. Read alongside the First Draft so any interpretive claim about "the von Neumann prior" is grounded.
4. Felker (1954), "Performance of TRADIC Transistor Digital Computer." The first US transistorized computer, built at Bell Labs nine years after the EDVAC report. The substrate that made everything downstream scalable. Read for concrete evidence of the chapter's compute-and-capability thesis: silicon, not vacuum tubes, is what let Moore's Law and eventually GPUs happen.
5. Hinton (1981), "Implementing Semantic Networks in Parallel Hardware." Distributed representations as the substrate. Where the idea of meaning-as-vector comes from.
6. Rumelhart, McClelland & the PDP Research Group (1986), *Parallel Distributed Processing, Vol. 1.* The founding text of modern connectionism. Priority chapters: Ch. 1 (the PDP framework) and Ch. 8 (Rumelhart, Hinton & Williams on backprop).
7. Werbos (1990), "Backpropagation Through Time: What It Does and How to Do It." Backprop generalized to recurrent computations. The training algorithm whose gradient pathologies the next paper addresses.
8. Hochreiter & Schmidhuber (1997), "Long Short-Term Memory." Gating as the fix for vanishing gradients in BPTT. The recurrent predecessor that made deep sequence models trainable.
9. Sutskever, Vinyals & Le (2014), "Sequence to Sequence Learning with Neural Networks." The encoder-decoder bottleneck that attention was invented to relieve.
10. Bahdanau, Cho & Bengio (2014), "Neural Machine Translation by Jointly Learning to Align and Translate." The attention mechanism as a patch on RNNs.
11. Luong, Pham & Manning (2015), "Effective Approaches to Attention-based Neural Machine Translation." Global vs. local attention and the dot-product variant that becomes scaled dot-product attention.
12. Vaswani et al. (2017), "Attention Is All You Need." The central paper. Recurrence dropped, parallelism gained.
13. Sutton (2019), "The Bitter Lesson." The philosophical closer: general methods plus compute beat clever structure.
