# A Mathematical Theory of Communication (Shannon, 1948)

**Summary**: Claude Shannon's foundational paper introduces information theory — the mathematical framework for quantifying, transmitting, and compressing information — defining the bit, information entropy, and channel capacity.

**Sources**: A Mathematical Theory of Communication.pdf

**Last updated**: 2026-05-11

---

## Context

Published in the *Bell System Technical Journal*, this paper emerged from Shannon's work at Bell Labs on communication systems. Building on earlier work by Nyquist and Hartley, Shannon set out to create a general theory that accounted for noise in the channel and the statistical structure of messages. The result was a complete mathematical framework that unified telegraphy, telephony, and radio under a single theory (source: A Mathematical Theory of Communication.pdf).

## Key contributions

### The bit

Shannon defines the fundamental unit of information: the binary digit, or **bit** (a term suggested by J. W. Tukey). A device with two stable positions — a relay, a flip-flop — stores one bit. N such devices store N bits, since the total number of possible states is 2^N. The choice of a logarithmic base determines the unit: base 2 gives bits, base 10 gives decimal digits, base e gives natural units (source: A Mathematical Theory of Communication.pdf).

### The communication model

Shannon defines a general communication system with five components:

1. **Information source** — produces the message
2. **Transmitter** — encodes the message into a signal
3. **Channel** — the medium (wire, radio, etc.) that carries the signal, subject to noise
4. **Receiver** — decodes the signal back into a message
5. **Destination** — the intended recipient

This model applies to telegraphy, telephony, television, and — by extension — to any system that transmits information, including the forward pass of a neural network (source: A Mathematical Theory of Communication.pdf).

### Information entropy

Shannon defines the entropy H of a discrete information source as:

H = −Σ p(i) log p(i)

This measures the average information content per symbol — or equivalently, the average uncertainty about what symbol will come next. High entropy means high unpredictability (and more information per symbol); low entropy means redundancy. Shannon shows that English text has considerable redundancy, which is why compression is possible (source: A Mathematical Theory of Communication.pdf).

### Channel capacity

The **capacity** C of a discrete channel is the maximum rate at which information can be transmitted reliably. For a noiseless channel with N possible signals of duration T:

C = lim (log N(T)) / T as T → ∞

Shannon proves that for a noisy channel, reliable communication is possible at any rate below capacity, provided one uses sufficiently clever encoding. This is the **noisy channel coding theorem** — one of the most surprising results in the theory, because it says noise does not fundamentally limit communication, only the rate (source: A Mathematical Theory of Communication.pdf).

### Stochastic processes as language models

Shannon models information sources as stochastic processes — sequences of symbols chosen according to probability distributions that may depend on preceding symbols. He constructs a series of increasingly accurate approximations to English:

- **Zero-order**: symbols chosen uniformly at random
- **First-order**: symbols chosen with English letter frequencies, but independently
- **Second-order**: digram (two-letter) statistics
- **Third-order**: trigram statistics
- **Word-level**: words chosen independently with English word frequencies

These approximations demonstrate how statistical structure constrains language — a principle that underlies modern [[transformer-architecture]] language models, which learn far deeper statistical patterns from data (source: A Mathematical Theory of Communication.pdf).

## Significance for the book's arc

Shannon's 1948 paper completes his contribution to the foundations of computing. His 1938 thesis ([[shannon-1938]]) showed how to build digital logic from Boolean algebra. This paper provides the theory for what flows through those circuits: information, measured in bits. The concept of [[information-entropy]] connects directly to the cross-entropy loss function used to train LLMs, and Shannon's language-modeling experiments are the direct ancestor of the statistical approach that produced GPT and the [[transformer-architecture]].

## Related pages

- [[information-entropy]]
- [[channel-capacity]]
- [[shannon-1938]]
- [[boolean-algebra]]
- [[transformer-architecture]]
- [[information-theory]]
