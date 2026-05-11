# Information Theory

**Summary**: The mathematical framework, founded by Claude Shannon in 1948, for quantifying information, analyzing communication channels, and understanding the fundamental limits of data compression and transmission.

**Sources**: A Mathematical Theory of Communication.pdf

**Last updated**: 2026-05-11

---

## Definition

Information theory provides mathematical tools for answering three fundamental questions:

1. **How much information does a source produce?** (answered by [[information-entropy]])
2. **How fast can information be transmitted over a channel?** (answered by [[channel-capacity]])
3. **How much can a message be compressed without loss?** (answered by the source coding theorem)

## Core concepts

### Information as surprise

Shannon's key insight is that information is a measure of surprise. A message that tells you something you already expected carries little information; a message that tells you something unlikely carries a lot. Formally, the information content of an event with probability p is −log₂(p) bits (source: A Mathematical Theory of Communication.pdf).

### Entropy

The average information per symbol produced by a source is its entropy H = −Σ p(i) log₂ p(i). See [[information-entropy]] for details (source: A Mathematical Theory of Communication.pdf).

### The communication model

Shannon models communication as: source → transmitter → channel (+ noise) → receiver → destination. This framework applies to any system that conveys information, from telegraph wires to neural networks. See [[shannon-1948]] (source: A Mathematical Theory of Communication.pdf).

### Channel capacity

Every noisy channel has a capacity C — the maximum rate at which information can be transmitted with arbitrarily low error probability. Shannon's noisy channel coding theorem proves that rates below C are achievable with proper encoding. See [[channel-capacity]] (source: A Mathematical Theory of Communication.pdf).

## Connection to machine learning

The cross-entropy loss function used to train modern LLMs is derived directly from Shannon's entropy. When a language model assigns probability p(w) to the next word w, the cross-entropy loss is −log₂ p(w) — exactly Shannon's measure of surprise. Minimizing cross-entropy is equivalent to maximizing the model's ability to predict the next token, which is equivalent to learning the statistical structure of language — the same structure Shannon explored with his n-gram approximations to English (source: A Mathematical Theory of Communication.pdf).

## Related pages

- [[information-entropy]]
- [[channel-capacity]]
- [[shannon-1948]]
- [[shannon-1938]]
- [[transformer-architecture]]
