# Sequences and Memory

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-06.*

## Narrative job

Real-world data unfolds in time. Speech is sequential. Language is sequential. The recurrent neural network is the first architectural answer to the question of how a network can have memory. Backpropagation through time (Werbos, 1990) is the training algorithm. Long Short-Term Memory (Hochreiter and Schmidhuber, 1997) is the gating mechanism that makes deep recurrent networks trainable in practice. The encoder-decoder architecture (Sutskever, Vinyals and Le, 2014) lets one network read a sequence and another write one, opening machine translation as the central testbed. Bahdanau, Cho and Bengio (2014), and then Luong, Pham and Manning (2015), introduce attention as a patch on the recurrent encoder-decoder: instead of squeezing the source through a single bottleneck vector, let the decoder look back at any encoder hidden state. End on the unsolved problem the recurrent backbone leaves on the table: even with attention, the encoder and decoder both serialize their own computation. That is the gap Chapter 7's transformer will close.

## Pedagogical commitments for this chapter

- The chapter introduces the idea of hidden state and the idea of an attention weight. Each is shown in pseudocode in its smallest worked example.
- The same translation example is carried through the chapter, first done by a vanilla RNN, then by an LSTM, then by an encoder-decoder with attention. The reader sees what each architectural change buys.

## Reading list

1. Elman, J. L. (1990). "Finding Structure in Time." *Cognitive Science*, 14(2), 179-211. The simple recurrent network. Read for the conceptual move from feedforward to recurrent.
2. Werbos, P. J. (1990). "Backpropagation Through Time: What It Does and How to Do It." *Proceedings of the IEEE*, 78(10), 1550-1560. The training algorithm.
3. Hochreiter, S. & Schmidhuber, J. (1997). "Long Short-Term Memory." *Neural Computation*, 9(8), 1735-1780. The gating mechanism.
4. Mikolov, T. et al. (2013). "Efficient Estimation of Word Representations in Vector Space" (word2vec). [arXiv:1301.3781](https://arxiv.org/abs/1301.3781). The breakthrough that made distributed word representations cheap and ubiquitous. Read for the embedding idea.
5. Sutskever, I., Vinyals, O. & Le, Q. V. (2014). "Sequence to Sequence Learning with Neural Networks." *NeurIPS 2014.* [arXiv:1409.3215](https://arxiv.org/abs/1409.3215). The encoder-decoder bottleneck attention was invented to relieve.
6. Bahdanau, D., Cho, K. & Bengio, Y. (2014). "Neural Machine Translation by Jointly Learning to Align and Translate." [arXiv:1409.0473](https://arxiv.org/abs/1409.0473). The attention mechanism as a patch on RNNs.
7. Luong, M.-T., Pham, H. & Manning, C. D. (2015). "Effective Approaches to Attention-based Neural Machine Translation." *EMNLP 2015.* [arXiv:1508.04025](https://arxiv.org/abs/1508.04025). Global vs. local attention and the dot-product variant that becomes scaled dot-product attention.
8. Cho, K. et al. (2014). "Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation." [arXiv:1406.1078](https://arxiv.org/abs/1406.1078). The GRU paper. Companion read to LSTM.

## Worked examples to build into the chapter

- A simple RNN unrolled over three time steps, drawn so the reader can see hidden state being passed forward. Pseudocode for one forward pass: five to seven lines.
- An LSTM cell, drawn with its three gates labeled. Pseudocode that shows the gates as multiplicative masks on the cell state: ten to fifteen lines. The reader leaves understanding gating as a soft form of "remember this, forget that."
- A worked translation example using encoder-decoder with attention. Show the alignment matrix for a four-word source and a four-word target so the reader sees attention as a learned alignment, not a black box.
- Pseudocode for scaled dot-product attention as Luong specifies it. Six to ten lines. This is the same operation Chapter 7 will lift out of the recurrent context and run in parallel.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

Modern post-transformer revivals of recurrence (Mamba, RWKV, the latest state-space models). Hybrid architectures. Anything that suggests recurrence is not simply the predecessor it currently looks like in this chapter. Update if the post-transformer landscape vindicates a recurrent comeback.
