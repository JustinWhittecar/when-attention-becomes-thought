# Transformer Architecture

**Summary**: A neural network architecture based entirely on attention mechanisms, introduced in 2017, that replaced recurrence and convolution as the dominant approach to sequence modeling — the foundation of all modern large language models.

**Sources**: Attention Is All You Need.pdf

**Last updated**: 2026-05-11

---

## Overview

The Transformer, introduced by Vaswani et al. (see [[vaswani-et-al-2017]]), is an encoder-decoder architecture that processes sequences using only attention and feed-forward layers — no recurrence, no convolution. This design enables massive parallelization during training and achieves constant-length paths between any two positions in a sequence (source: Attention Is All You Need.pdf).

## Architecture

### Encoder

A stack of N = 6 identical layers. Each layer contains:

1. **[[multi-head-attention]]** (self-attention): every position attends to every other position
2. **Position-wise feed-forward network**: two linear transformations with ReLU activation, applied independently to each position

Each sub-layer has a residual connection and layer normalization: output = LayerNorm(x + Sublayer(x)). All sub-layers produce outputs of dimension d_model = 512.

### Decoder

Also N = 6 layers, with an additional third sub-layer:

1. **Masked [[self-attention]]**: positions can only attend to earlier positions (preserving auto-regressive property)
2. **Encoder-decoder attention**: queries from the decoder, keys and values from the encoder output
3. **Position-wise feed-forward network**

### Input processing

- Token embeddings convert discrete tokens to d_model-dimensional vectors
- [[positional-encoding]] (sinusoidal functions) is added to provide sequence-order information
- The same weight matrix is shared between the two embedding layers and the pre-softmax linear transformation, multiplied by √d_model in the embedding layers

(source: Attention Is All You Need.pdf)

## Core mechanisms

### [[self-attention]]

Attention(Q, K, V) = softmax(QK^T / √d_k) V

The dot product of queries and keys, scaled by 1/√d_k, determines attention weights. The output is a weighted sum of values. This connects all positions in O(1) sequential operations, compared to O(n) for RNNs.

### [[multi-head-attention]]

Instead of a single attention function, Q, K, and V are projected into h = 8 parallel subspaces (each d_k = d_v = 64). Attention is computed independently in each head, results are concatenated and projected back. This allows the model to attend to different types of information at different positions simultaneously.

(source: Attention Is All You Need.pdf)

## Computational properties

| Property | Self-Attention | Recurrent | Convolutional |
|---|---|---|---|
| Complexity/layer | O(n²·d) | O(n·d²) | O(k·n·d²) |
| Sequential ops | O(1) | O(n) | O(1) |
| Max path length | O(1) | O(n) | O(log_k(n)) |

Self-attention is faster than recurrence when n < d (the common case for typical sequence lengths). The O(n²) scaling becomes a limitation for very long sequences (source: Attention Is All You Need.pdf).

## Impact

The Transformer architecture is the basis for:

- **GPT** series (OpenAI): decoder-only Transformers for language generation
- **BERT** (Google): encoder-only Transformers for language understanding
- **GPT-4.5**: the model that passed the [[turing-test]] in [[jones-bergen-2025]]
- **LLaMa** (Meta): open-weight decoder-only Transformers
- Vision Transformers (ViT), audio models, protein folding models, and more

The architecture's training loss is cross-entropy — directly derived from Shannon's [[information-entropy]] — making it the modern successor to Shannon's n-gram language modeling experiments in [[shannon-1948]].

## Related pages

- [[vaswani-et-al-2017]]
- [[self-attention]]
- [[multi-head-attention]]
- [[positional-encoding]]
- [[information-entropy]]
- [[turing-test]]
