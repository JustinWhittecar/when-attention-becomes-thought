# The Spark: Self-Attention and the Transformer

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-06.*

## Narrative job

Drop recurrence. Keep attention. Show that the transformer architecture, by replacing the sequential bottleneck of the recurrent encoder-decoder with a fully parallel attention mechanism, unlocked a new relationship between compute and capability. By this point the reader has already met scaled dot-product attention as a patch on RNNs (Chapter 5) and the GPU as the silicon that rewards parallel matrix multiplication (Chapter 3). This chapter does the synthesis: when attention becomes the only mechanism a sequence model needs, the operation that dominates is matmul, the silicon that runs matmul fastest is the GPU, and the relationship between training compute and model capability becomes the story of the next decade. End by setting up the scaling era.

## Pedagogical commitments for this chapter

- The full transformer block is built up from pieces the reader has already met: scaled dot-product attention (Chapter 5), feedforward layers (Chapter 4), residual connections and layer normalization (introduced here, in pseudocode, before any prose claim depends on them).
- Pseudocode for self-attention, multi-head attention, and a single transformer block. Each is small enough to read in one sitting.
- A worked example showing why self-attention is parallel where recurrence is sequential, expressed in terms of which operations can run on which step of which timestep. The reader leaves understanding the architectural argument, not just the marketing line.

## Reading list

1. Vaswani, A. et al. (2017). "Attention Is All You Need." *NeurIPS 2017.* [arXiv:1706.03762](https://arxiv.org/abs/1706.03762). The central paper. Read it whole.
2. Ba, J. L., Kiros, J. R. & Hinton, G. E. (2016). "Layer Normalization." [arXiv:1607.06450](https://arxiv.org/abs/1607.06450). Background for the normalization step inside a transformer block.
3. He, K. et al. (2016). "Deep Residual Learning for Image Recognition." *CVPR 2016.* Background for the residual connections inside a transformer block. Vision context, but the mechanism is the same.
4. Dai, Z. et al. (2019). "Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context." [arXiv:1901.02860](https://arxiv.org/abs/1901.02860). The first significant patch on the original transformer. Cite where the chapter touches "what was missing in the 2017 paper."
5. Su, J. et al. (2021). "RoFormer: Enhanced Transformer with Rotary Position Embedding." [arXiv:2104.09864](https://arxiv.org/abs/2104.09864). The position-encoding refinement that became standard. Cite when introducing positional encoding so the reader knows the 2017 sinusoidal version is a footnote.
6. Tay, Y. et al. (2022). "Efficient Transformers: A Survey." *ACM Computing Surveys.* Optional. Cite for the post-2017 efficiency landscape.

## Worked examples to build into the chapter

- Scaled dot-product attention written out as pseudocode: matmul, scale, softmax, matmul. Six lines. The reader has seen this before in Chapter 5, recurrent context. Now it stands alone.
- Multi-head attention as the same operation run in parallel with different learned projections. Pseudocode: ten to twelve lines. The reader sees that "multi-head" is just "do the same thing several times with different views and concatenate."
- A single transformer block: attention, residual, layer norm, feedforward, residual, layer norm. Pseudocode: fifteen lines. This is the unit that everything later in the book is built from.
- A diagram showing two encoder layers running in parallel across a four-token sequence. The same diagram drawn for an LSTM would be a diagonal staircase. The contrast is the chapter's central image.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

The post-transformer architecture conversation: Mamba, state-space models, the latest hybrid designs. Whether attention remains the dominant primitive past the late 2020s. Update if a successor architecture displaces the transformer at frontier scale.
