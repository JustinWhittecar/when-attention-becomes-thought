# Frege to Modern Notation: A Cheatsheet

Frege's notation is two-dimensional. Reading it on a page is a different experience from reading modern linear logic, and the conditional in particular is laid out in a way that surprises modern readers. This cheatsheet covers his core symbols from *Begriffsschrift* (1879) and the additions in *Grundgesetze der Arithmetik* (1893/1903).

## Core symbols (Begriffsschrift)

### Judgment stroke and content stroke

The two horizontal-and-vertical pieces at the left of every assertion.

| Frege | Modern | Meaning |
|---|---|---|
| `— A` (horizontal alone) | (the content of A) | "The content A," considered as a thought without asserting it. Just naming the proposition. |
| `⊢ — A` (vertical + horizontal) | `⊢ A` | "I assert that A is true." The short vertical is the *Urteilsstrich* (judgment stroke). |

The content stroke matters because Frege wants to separate the act of judging from the thing being judged. Modern logic mostly collapses this: when we write `A`, we're already implicitly asserting it.

### Negation

A small vertical stroke hanging below the content line, between the horizontal and the proposition.

```
              |
   ⊢ — ─┬─ A    ≡    ⊢ ¬A
        ↑
   negation tick
```

| Frege | Modern |
|---|---|
| Horizontal with downward tick before A | `¬A` |

### Conditional (the famous 2D form)

This is the one that trips everyone up. Frege draws the conditional as two horizontal lines joined at the left by a vertical bar:

```
   ┌── A         (top: consequent)
   │
   └── B         (bottom: antecedent)
```

This reads as: "if B then A," i.e. `B → A`. The consequent sits on top, the antecedent on the bottom. Modern notation puts the antecedent first, so the order feels reversed.

Asserted form (with judgment stroke at the very left):

```
       ┌── A
   ⊢ ──┤              ≡    ⊢ (B → A)
       └── B
```

Nested conditionals stack. `(C → (B → A))` becomes a 3-line stack with C at the bottom, B in the middle, A on top.

### Universal quantifier

A small concavity (cup) in the horizontal line, with a German Fraktur letter inside the cup. The same letter then appears in the proposition.

```
   ⊢ ── ⌣𝔞 ── Φ(𝔞)        ≡    ⊢ ∀a Φ(a)
```

The Fraktur letter signals "this is a bound variable." Free variables, by contrast, are written in italic Latin letters.

### Existential quantifier (derived)

Frege has no primitive existential. He builds it from negation and the universal:

| Frege construction | Modern |
|---|---|
| ¬ ∀a ¬ Φ(a) (in Frege's 2D form) | `∃a Φ(a)` |

In Frege's diagram, this looks like a content line with a negation tick, then a concavity for the universal, then another negation tick, then the proposition. Three pieces stacked left to right.

### Disjunction and conjunction (derived)

Frege also has no primitive `∨` or `∧`. They are derived:

| Frege construction | Modern |
|---|---|
| `(¬B → A)` | `A ∨ B` |
| `¬(A → ¬B)` | `A ∧ B` |

So when you see those combinations of negation tick and 2D conditional, recognize them as disguised disjunctions and conjunctions.

### Identity

In *Begriffsschrift* Frege used the symbol `≡` and called it "sameness of content" (*Inhaltsgleichheit*). By *Grundgesetze* he had switched to ordinary `=`, now read as identity of reference.

| Frege | Period | Modern |
|---|---|---|
| `A ≡ B` | Begriffsschrift | `A = B` (sameness of content) |
| `A = B` | Grundgesetze | `A = B` (identity) |

## Additions in *Grundgesetze* (1893)

### Truth-value names

Frege now treats truth-values as objects, with their own names.

| Frege | Modern | Meaning |
|---|---|---|
| The True | `⊤` | The truth-value true |
| The False | `⊥` | The truth-value false |

The horizontal stroke is now reinterpreted: `— A` denotes the True if A is the True, and the False otherwise. So the horizontal is itself a function from any object to a truth-value.

### Value-range operator (smooth breathing)

A Greek vowel with a smooth breathing mark (spiritus lenis) above it, written before a function expression, denotes the *value-range* (*Wertverlauf*) of that function.

```
   ἐ Φ(ε)            ≡    {x : Φ(x)}     (modern set-builder)
                     ≡    the graph / extension of Φ
```

The vowel ε under the breathing acts as a bound variable internal to the value-range operator. This is Frege's analogue of a function's extension or graph. It is also the locus of Russell's Paradox: Basic Law V says two functions have the same value-range iff they agree on every argument, and that law collapses under Russell's construction.

### Definite description (the backslash)

A symbol shaped like a backslash or a small reversed L, applied to a value-range, picks out the unique element of that range when one exists.

| Frege | Modern |
|---|---|
| `\ ἐ Φ(ε)` | `ιx Φ(x)`, i.e. "the unique x such that Φ(x)" |

If there is no unique such element, Frege's account assigns the value-range itself as the value (a stipulation that has no clean modern analogue).

### Definitions

Frege marks definitions with a doubled stroke or a specific definitional sign rather than the bare judgment stroke, signaling that the assertion holds by stipulation rather than by proof. Translations vary; a typical convention writes `⊢⊢` or `⫤` for definitional equivalence.

## How to read a Frege page

A few habits that make Frege easier to parse:

1. **Always start at the left.** Find the judgment stroke. Everything to the right is what is being asserted.
2. **Read the conditional bottom-up.** The bottom proposition is the antecedent ("if"), the top is the consequent ("then"). With nested conditionals, work from the bottom of the stack upward.
3. **Spot the negation ticks.** They are small vertical drops on the horizontal. Each one flips the truth of whatever it sits before.
4. **Spot the concavities.** A dip in the horizontal with a Fraktur letter in it is a universal quantifier binding that letter throughout the formula to its right.
5. **Translate to linear form before reasoning.** It is almost always faster to convert a complicated Frege formula into modern notation, do your reasoning, and then check the original than to manipulate the 2D form directly.

## Quick reference table

| Frege | Modern | Name |
|---|---|---|
| `⊢` | `⊢` | Judgment stroke |
| `—` | (no direct equivalent) | Content / horizontal stroke |
| Tick below horizontal | `¬` | Negation |
| 2D conditional (top consequent, bottom antecedent) | `B → A` | Conditional |
| Concavity with 𝔞 | `∀a` | Universal |
| `¬∀a ¬` | `∃a` | Existential (derived) |
| `(¬B → A)` | `A ∨ B` | Disjunction (derived) |
| `¬(A → ¬B)` | `A ∧ B` | Conjunction (derived) |
| `≡` (Begriffsschrift) | `=` | Identity (sameness of content) |
| `=` (Grundgesetze) | `=` | Identity |
| `ἐ Φ(ε)` | `{x : Φ(x)}` | Value-range |
| `\ ἐ Φ(ε)` | `ιx Φ(x)` | Definite description |
| The True | `⊤` | Truth-value |
| The False | `⊥` | Truth-value |

## Further reading

- Heijenoort, *From Frege to Gödel* (1967) reprints the *Begriffsschrift* in English with the 2D notation preserved. Useful for getting your eye in.
- Beaney, *The Frege Reader* (1997) gives modern translations alongside Frege's notation, with helpful translator's notes.
- Heck, *Reading Frege's Grundgesetze* (2012) walks through the value-range and definite-description machinery in modern terms.
