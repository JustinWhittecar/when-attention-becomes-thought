# Multi-Head Attention

**Summary**: A mechanism that runs multiple self-attention operations in parallel across different learned subspaces, allowing the model to attend to different types of information at different positions simultaneously.

**Sources**: Attention Is All You Need.pdf

**Last updated**: 2026-05-11

---

## Definition

Instead of computing a single attention function with d_model-dimensional keys, values, and queries, multi-head attention:

1. **Projects** Q, K, V into h separate subspaces using learned linear projections
2. **Computes** [[self-attention]] independently in each subspace (head)
3. **Concatenates** the h outputs
4. **Projects** the concatenation back to d_model dimensions

Formally:

MultiHead(Q, K, V) = Concat(head₁, ..., headₕ) W^O

where headᵢ = Attention(Q Wᵢ^Q, K Wᵢ^K, V Wᵢ^V)

(source: Attention Is All You Need.pdf)

## Parameters in the original Transformer

| Parameter | Value |
|---|---|
| h (number of heads) | 8 |
| d_model (model dimension) | 512 |
| d_k = d_v (per-head dimension) | 64 (= d_model / h) |

Because each head operates in a reduced dimension (64 instead of 512), the total computational cost is similar to single-head attention with full dimensionality (source: Attention Is All You Need.pdf).

## Why multiple heads?

With a single attention head, the weighted average over values tends to be dominated by a few high-scoring positions, inhibiting the model's ability to attend to information from different representation subspaces. Multiple heads solve this by allowing the model to simultaneously:

- Track syntactic relationships in one head
- Track semantic relationships in another
- Track positional patterns in a third
- And so on

Vaswani et al. observe that different heads in their trained models do indeed learn distinct, interpretable attention patterns (source: Attention Is All You Need.pdf).

## Related pages

- [[self-attention]]
- [[transformer-architecture]]
- [[vaswani-et-al-2017]]
- [[positional-encoding]]
