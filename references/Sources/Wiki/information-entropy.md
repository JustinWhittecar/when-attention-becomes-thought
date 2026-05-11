# Information Entropy

**Summary**: Shannon's measure of the average information content (or uncertainty) per symbol produced by an information source, measured in bits.

**Sources**: A Mathematical Theory of Communication.pdf

**Last updated**: 2026-05-11

---

## Definition

For a discrete random variable X with possible values {x₁, x₂, ..., xₙ} and probability distribution p(xᵢ), the **entropy** is:

H(X) = −Σᵢ p(xᵢ) log₂ p(xᵢ)

Entropy is maximized when all outcomes are equally likely (maximum uncertainty) and minimized when one outcome has probability 1 (no uncertainty). The unit is **bits** when the logarithm base is 2 (source: A Mathematical Theory of Communication.pdf).

## Intuition

Shannon motivates the logarithmic measure on three grounds:

1. **Practical**: Engineering parameters (time, bandwidth, number of relays) vary linearly with the logarithm of the number of possibilities. Adding one relay doubles the number of states, adding 1 bit.
2. **Intuitive**: Two punched cards should have twice the information capacity of one.
3. **Mathematical**: Limiting operations are simpler in logarithmic form.

(source: A Mathematical Theory of Communication.pdf)

## Examples

| Source | Entropy |
|---|---|
| Fair coin | H = 1 bit |
| Biased coin (p=0.99) | H ≈ 0.08 bits |
| English text (~1.0–1.5 bits/char) | Much lower than log₂(27) ≈ 4.75 bits |
| Uniform over 26 letters + space | H = log₂(27) ≈ 4.75 bits |

The low entropy of English — relative to the maximum possible for a 27-symbol alphabet — reflects the redundancy of natural language: letter frequencies are unequal, digrams and trigrams are highly constrained, words follow grammatical patterns. This redundancy is what makes compression possible and what language models exploit (source: A Mathematical Theory of Communication.pdf).

## Connection to machine learning

The **cross-entropy** between a true distribution p and a model distribution q is:

H(p, q) = −Σᵢ p(xᵢ) log₂ q(xᵢ)

Cross-entropy is always ≥ H(p), with equality only when q = p. This is the standard loss function for training language models built on the [[transformer-architecture]]: the model's goal is to assign high probability to the actual next token, minimizing cross-entropy and thereby learning the statistical structure of the language. Shannon's entropy is the theoretical lower bound on how well any model can predict (source: A Mathematical Theory of Communication.pdf).

## Related pages

- [[information-theory]]
- [[channel-capacity]]
- [[shannon-1948]]
- [[transformer-architecture]]
