# Learning from Data

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-06.*

## Narrative job

Up to this point the machines have been told what to do. This is the chapter where they learn rules from examples. Rosenblatt's perceptron (1958) is the first concrete example: a McCulloch-Pitts neuron with adjustable weights and a learning rule. Minsky and Papert (1969) prove what it cannot do, and the field enters its first long winter. The PDP volumes (1986) and the backpropagation paper inside them are the answer: stack the units, learn the weights end-to-end, and the limitation dissolves. Distributed representations are the conceptual leap that makes the rest of the book possible: meaning lives in vectors, not symbols. End with the reader able to read pseudocode for perceptron training and gradient descent and recognize them as the same algorithm at different levels of generality.

## Pedagogical commitments for this chapter

- The chapter introduces three new formal objects: the weighted threshold neuron, the loss function, and the gradient. Each is shown in pseudocode in its smallest worked example before any prose claim depends on it.
- The leap from a single perceptron to a multi-layer network is shown explicitly. The reader sees that adding a layer is what allows XOR to be learned, and they see why Minsky and Papert's objection was technically right and historically misleading.

## Reading list

1. Rosenblatt, F. (1958). "The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain." *Psychological Review*, 65(6), 386-408. The founding paper of learning from examples. Read it whole.
2. Minsky, M. & Papert, S. (1969). *Perceptrons: An Introduction to Computational Geometry.* Read the introduction and the chapter on geometric predicates. The proof that drove the first AI winter.
3. Hinton, G. E. (1981). "Implementing Semantic Networks in Parallel Hardware." In Hinton & Anderson (Eds.), *Parallel Models of Associative Memory*, pp. 161-187. Where distributed representations enter the frame.
4. Rumelhart, D. E., McClelland, J. L. & the PDP Research Group (1986). *Parallel Distributed Processing: Explorations in the Microstructure of Cognition. Volume 1: Foundations.* MIT Press. Priority: Chapter 1 (the PDP framework) and Chapter 8 (Rumelhart, Hinton & Williams, "Learning Internal Representations by Error Propagation").
5. LeCun, Y. et al. (1989). "Backpropagation Applied to Handwritten Zip Code Recognition." *Neural Computation*, 1(4), 541-551. The first concrete demonstration that backprop scales to a real-world task. Short, clean, citable.
6. LeCun, Y., Bengio, Y. & Hinton, G. (2015). "Deep Learning." *Nature*, 521(7553), 436-444. The field-defining survey. Read for the framing the chapter ends on.
7. Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning.* Reference companion. Read the chapters on backpropagation and gradient-based optimization. Cite for the formal definitions when the chapter needs them.

## Worked examples to build into the chapter

- A perceptron computing AND, OR, and NAND, with weights given. Reuses the Chapter 3 vocabulary and shows the reader that a perceptron is a McCulloch-Pitts neuron with knobs.
- The XOR problem: show why a single perceptron cannot solve it (a propositional-logic argument), then show that a two-layer network can (a worked example with weights). This is the chapter's pedagogical pivot.
- Pseudocode for the perceptron learning rule: for each example, predict, compare to label, update weights in the direction of the error. Five lines.
- Pseudocode for stochastic gradient descent on a one-hidden-layer network. Eight to twelve lines. The reader sees the same shape as the perceptron rule, generalized.

## Exercises for the reader

To be drafted with the chapter.

## What to watch

Optimizer developments (Adam variants, second-order methods that actually scale), changes in standard training practice, and any reframing of the bias-variance and double-descent stories that changes how a beginner should think about generalization. Update when textbook practice shifts.
