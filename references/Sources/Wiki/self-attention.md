# Self-Attention

**Summary**: A mechanism that computes a representation of each position in a sequence by attending to all other positions in the same sequence, enabling the model to capture dependencies regardless of distance.

**Sources**: Attention Is All You Need.pdf

**Last updated**: 2026-05-11

---

## Definition

Self-attention (also called intra-attention) relates different positions of a single sequence to compute a new representation of that sequence. Each position produces a **query**, a **key**, and a **value** vector. The output for each position is a weighted sum of all value vectors, where the weights are determined by the compatibility (dot product) between that position's query and every position's key.

## Scaled dot-product attention

Given matrices Q (queries), K (keys), and V (values):

Attention(Q, K, V) = softmax(QK^T / √d_k) V

- **QK^T**: computes compatibility scores between every pair of positions
- **/ √d_k**: scaling factor that prevents dot products from growing large and pushing the softmax into saturation (where gradients are extremely small)
- **softmax**: normalizes scores into a probability distribution (attention weights)
- **× V**: produces a weighted combination of values

(source: Attention Is All You Need.pdf)

## Why scaling matters

If the components of q and k are independent random variables with mean 0 and variance 1, their dot product has mean 0 and variance d_k. For large d_k, the dot products can be very large in magnitude, causing the softmax to produce near-one-hot distributions where gradients vanish. Dividing by √d_k keeps the variance at 1 regardless of dimension (source: Attention Is All You Need.pdf).

## Three uses in the Transformer

The [[transformer-architecture]] uses self-attention in three distinct ways:

1. **Encoder self-attention**: every position in the encoder attends to every position in the encoder (bidirectional)
2. **Decoder self-attention (masked)**: every position in the decoder attends only to earlier positions (causal / auto-regressive), enforced by masking future positions with −∞ before the softmax
3. **Encoder-decoder attention**: decoder queries attend to encoder keys and values (cross-attention, technically not self-attention)

(source: Attention Is All You Need.pdf)

## Computational properties

- **Path length**: O(1) — any position can attend directly to any other position, unlike RNNs where information must propagate through O(n) steps
- **Parallelization**: O(1) sequential operations — all positions are computed simultaneously, unlike the O(n) sequential dependency of recurrence
- **Cost**: O(n²·d) per layer — quadratic in sequence length, which becomes the bottleneck for very long sequences

(source: Attention Is All You Need.pdf)

## Interpretability

Self-attention provides a degree of interpretability: the attention weights show which positions influence which. Vaswani et al. observe that individual attention heads learn to perform distinct tasks, and many exhibit behavior related to syntactic and semantic structure (source: Attention Is All You Need.pdf).

## Related pages

- [[multi-head-attention]]
- [[transformer-architecture]]
- [[vaswani-et-al-2017]]
- [[positional-encoding]]
