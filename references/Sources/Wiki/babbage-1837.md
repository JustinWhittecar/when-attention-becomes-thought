# Babbage -- On the Mathematical Powers of the Calculating Engine (1837)

**Summary**: Charles Babbage's 1837 paper describing the architecture and mathematical capabilities of his Analytical Engine, introducing the Mill-and-Store separation that prefigures the processor-memory distinction in all modern computers.

**Sources**: On the Mathematical Powers of the Calculating Engine.pdf

**Last updated**: 2026-05-12

---

## Context

Written on 26 December 1837, this is one of the earliest detailed technical accounts of the [[analytical-engine]]. Babbage's purpose is "to show the degree of assistance which mathematical science is capable of receiving from mechanism." The paper survives only as the Buxton MS7 manuscript at the Museum of the History of Science, Oxford, and was published for the first time as Chapter 2.1 of [[randell-1973|Brian Randell's *The Origins of Digital Computers*]] (Springer-Verlag, 1973). (source: On the Mathematical Powers of the Calculating Engine.pdf)

This document predates every other source in the wiki and describes the machine that [[ada-lovelace]] would later write the first program for in 1843.

## The Mill and the Store

Babbage divides the calculating part of the engine into two portions (source: On the Mathematical Powers of the Calculating Engine.pdf):

1. **The Mill** -- where all operations are performed
2. **The Store** -- where numbers are originally placed and to which computed results are returned

A plan of the engine shows circles placed around a great central wheel constituting the Mill, with a longitudinal section adjoining it representing the Store. Two axes -- the *Ingress Axis* and the *Egress Axis* -- connect the Mill with the Store. (source: On the Mathematical Powers of the Calculating Engine.pdf)

This separation of processing from storage is the architectural ancestor of the modern CPU-memory distinction described in [[petzold-2023]] and formalized abstractly in the [[turing-machine]].

## Components of the Mill

The Mill consists of ten named subsystems (source: On the Mathematical Powers of the Calculating Engine.pdf):

1. **Figure Axes** -- Transfer numbers between axes. Support *Stepping down* (shifting digits lower, equivalent to dividing by 10) and *Stepping up* (shifting higher, equivalent to multiplying by 10). Register axes R and R1 convey the two highest figures of the dividend to the Selecting apparatus.
2. **Carriage Axes** -- Execute the carry operation when numbers are added or subtracted. Three carriages (F, 'F, "F) can be connected to figure axes or other parts of the Mill.
3. **Table Figure Axes** -- Ten axes, nine containing the multiplication table of one factor (or the divisor in division), the tenth containing the complement of the divisor. Wheels can be *stepped up* or *stepped down*.
4. **Digit Counting Apparatus** -- Tracks digit positions during operations.
5. **Selecting Apparatus** -- Directs the flow of computation, a primitive form of conditional branching.
6. **Barrels** -- Encode sequences of operations, analogous to microcode.
7. **Reducing Apparatus for Barrels** -- Simplifies barrel configurations.
8. **Operation Cards** -- Punch cards that specify which operations to perform, directly ancestral to the concept of a stored program.
9. **Repeating Apparatus** -- Enables loops by re-executing sequences of operations.
10. **Combinatorial Counting Apparatus** -- Manages complex counting operations.

## The "Running Up" mechanism

When a subtraction produces a result greater than the number subtracted from, the mechanism produces a carry in the "forty first cage." A lever connected to this part issues a *Running up* warning, which then governs many parts of the engine according to circumstances. This is an early form of overflow detection and conditional control flow. (source: On the Mathematical Powers of the Calculating Engine.pdf)

## Significance

This paper is the earliest systematic description of a general-purpose programmable computer in the wiki's collection. Key architectural ideas that persist:

- **Separation of processing and memory** (Mill/Store) -- the same division appears in [[shannon-1938]]'s relay circuits and in every modern CPU
- **Operation cards** -- external instructions controlling the machine, a precursor to programs
- **Repeating apparatus** -- the concept of looping, which [[ada-lovelace]] would formalize in her Note G on Bernoulli numbers
- **Carry propagation and overflow detection** -- fundamental to the arithmetic logic described in [[petzold-2023]] and [[boolean-algebra]]

## Forward to working machines

Babbage's Mill-and-Store separation, with operation cards driving the sequence and a repeating apparatus enabling loops, was reconstituted a century later in the [[harvard-mark-i|Harvard Mark I]] (paper-tape program, mechanical accumulators) and the [[zuse-z3|Zuse Z3]] (punched-film program, relay arithmetic). The architectural lineage runs through these electromechanical machines to [[eniac|ENIAC]] (plug-board electronic) and finally to [[edvac|EDVAC]] and the [[von-neumann-architecture|von Neumann architecture]], where the operation cards finally enter the same memory as the data and the [[stored-program-computer|stored-program computer]] begins.

## Related pages

- [[analytical-engine]]
- [[ada-lovelace]]
- [[lovelace-1843]]
- [[shannon-1938]]
- [[petzold-2023]]
- [[turing-machine]]
- [[boolean-algebra]]
- [[computability]]
- [[randell-1973]]
- [[harvard-mark-i]]
- [[zuse-z3]]
- [[eniac]]
- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[hollerith-1889]]
