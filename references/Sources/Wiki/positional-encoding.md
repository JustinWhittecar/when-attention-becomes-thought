# Positional Encoding

**Summary**: A technique for injecting sequence-order information into the Transformer architecture, which otherwise has no inherent notion of position because it lacks recurrence and convolution.

**Sources**: Attention Is All You Need.pdf

**Last updated**: 2026-05-11

---

## The problem

The [[transformer-architecture]] processes all positions in parallel via [[self-attention]]. Unlike RNNs, which process tokens sequentially and thereby encode order implicitly, the Transformer treats its input as a set — the same output would result regardless of token order. To make the model sensitive to position, information about each token's location must be explicitly injected (source: Attention Is All You Need.pdf).

## Sinusoidal encoding (original Transformer)

Vaswani et al. add a positional encoding vector to each input embedding before feeding it into the encoder and decoder stacks. The encoding uses sine and cosine functions at different frequencies:

PE(pos, 2i) = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))

where `pos` is the position and `i` is the dimension index. Key properties:

- Each dimension corresponds to a sinusoid with a unique wavelength, forming a geometric progression from 2π to 10000·2π
- For any fixed offset k, PE(pos+k) can be represented as a linear function of PE(pos), which the authors hypothesized would help the model learn to attend by relative position
- The encoding has the same dimension d_model as the embeddings, so the two can be summed directly

(source: Attention Is All You Need.pdf)

## Learned vs. fixed

Vaswani et al. also experimented with learned positional embeddings and found "nearly identical results" to the sinusoidal version. They chose the sinusoidal version because it might allow the model to extrapolate to sequence lengths longer than those encountered during training — a potential advantage that learned embeddings lack (source: Attention Is All You Need.pdf).

## Later developments

Since the original Transformer, many alternative positional encoding schemes have been developed:

- **Rotary Position Embeddings (RoPE)**: encode relative position by rotating query and key vectors, used in LLaMa and many modern LLMs
- **ALiBi**: add a linear bias to attention scores based on distance, without explicit positional vectors
- **Relative position encodings**: directly bias attention scores based on the distance between positions

These are not covered in the original paper but represent the ongoing evolution of the idea.

## Related pages

- [[self-attention]]
- [[multi-head-attention]]
- [[transformer-architecture]]
- [[vaswani-et-al-2017]]
