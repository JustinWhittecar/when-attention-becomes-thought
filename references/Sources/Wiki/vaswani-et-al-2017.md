# Attention Is All You Need (Vaswani et al., 2017)

**Summary**: This paper introduces the Transformer, a neural network architecture that replaces recurrence entirely with self-attention, achieving state-of-the-art results on machine translation while being far more parallelizable than previous approaches.

**Sources**: Attention Is All You Need.pdf

**Last updated**: 2026-05-11

---

## Context

By 2017, sequence-to-sequence models based on recurrent neural networks (RNNs) and LSTMs dominated machine translation and language modeling. These models processed tokens sequentially, creating a bottleneck: the hidden state at position t depends on position t−1, preventing parallelization across positions. Attention mechanisms existed as add-ons to RNNs, but no one had built an architecture using attention alone. Eight researchers at Google Brain and Google Research — Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser, and Polosukhin — proposed doing exactly that (source: Attention Is All You Need.pdf).

## Key contributions

### The Transformer architecture

The Transformer uses an encoder-decoder structure, but both encoder and decoder are built entirely from attention layers and feed-forward networks — no recurrence, no convolution.

- **Encoder**: A stack of N = 6 identical layers. Each layer has two sub-layers: (1) multi-head self-attention and (2) a position-wise feed-forward network. Residual connections and layer normalization surround each sub-layer.
- **Decoder**: Also N = 6 layers, with an additional third sub-layer performing multi-head attention over the encoder output. The decoder's self-attention is masked to prevent positions from attending to future tokens, preserving the auto-regressive property.

(source: Attention Is All You Need.pdf)

### Scaled dot-product attention

The core operation. Given queries Q, keys K, and values V:

Attention(Q, K, V) = softmax(QK^T / √d_k) V

The dot products of queries and keys are scaled by 1/√d_k to prevent the softmax from saturating into regions of extremely small gradients when d_k is large. The output is a weighted sum of the values, where the weights reflect the compatibility between each query and each key (source: Attention Is All You Need.pdf).

### Multi-head attention

Rather than computing a single attention function, the model projects Q, K, and V into h = 8 different subspaces (each of dimension d_k = d_v = 64), computes attention in parallel across all heads, concatenates the results, and projects back. This allows the model to attend to information from different representation subspaces at different positions simultaneously (source: Attention Is All You Need.pdf).

See [[self-attention]] and [[multi-head-attention]] for detailed concept pages.

### Positional encoding

Since the Transformer has no recurrence or convolution, it has no inherent sense of token order. The authors inject position information by adding sinusoidal functions to the input embeddings:

PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

The wavelengths form a geometric progression from 2π to 10000·2π. For any fixed offset k, PE(pos+k) can be represented as a linear function of PE(pos), which the authors hypothesized would help the model learn relative positions. See [[positional-encoding]] (source: Attention Is All You Need.pdf).

### Computational advantages

| Layer Type | Complexity per Layer | Sequential Ops | Max Path Length |
|---|---|---|---|
| Self-Attention | O(n²·d) | O(1) | O(1) |
| Recurrent | O(n·d²) | O(n) | O(n) |
| Convolutional | O(k·n·d²) | O(1) | O(log_k(n)) |

Self-attention connects all positions in O(1) sequential operations (vs. O(n) for RNNs) and has constant maximum path length between any two positions (vs. O(n) for RNNs). The tradeoff is O(n²·d) complexity per layer, which becomes expensive for very long sequences (source: Attention Is All You Need.pdf).

## Results

- **English-to-German** (WMT 2014): 28.4 BLEU, surpassing all previous models including ensembles by over 2 BLEU
- **English-to-French** (WMT 2014): 41.0 BLEU, new single-model SOTA
- Training cost: 3.5 days on 8 P100 GPUs for the big model — a fraction of competing approaches

(source: Attention Is All You Need.pdf)

## Significance for the book's arc

The Transformer is where the foundational arc — from [[formal-system]]s through [[computability]] through hardware — meets the modern AI arc. The architecture runs on the hardware that [[shannon-1938]] made designable and [[petzold-2023]] explains. It is trained by minimizing cross-entropy, the loss function derived from [[information-entropy]]. And its outputs are the basis for the [[turing-test]] results in [[jones-bergen-2025]] and the AGI claims in [[chen-et-al-2026]].

## Related pages

- [[transformer-architecture]]
- [[self-attention]]
- [[multi-head-attention]]
- [[positional-encoding]]
- [[information-entropy]]
- [[turing-test]]
