# Code: The Hidden Language of Computer Hardware and Software (Petzold, 2023)

**Summary**: Charles Petzold's popular-science book builds from flashlights and Morse code to a complete working CPU, demonstrating how simple physical principles — binary states, logic gates, memory — compose into a general-purpose computer.

**Sources**: Code the hidden language of computer hardware and software.pdf

**Last updated**: 2026-05-11

---

## Context

First published in 1999, *Code* was revised and expanded in 2023 (second edition). The second edition corrects the original's main weakness: the first edition stopped short of fully explaining CPU internals. The new edition adds roughly 70 pages and carries the reader through a complete central processing unit, including registers, buses, control signals, and the fetch-decode-execute cycle (source: Code the hidden language of computer hardware and software.pdf).

## Structure

The book's 28 chapters follow a strict progression from simple to complex:

1. **Codes and communication** (Ch. 1–3): Morse code, Braille, binary representation
2. **Electricity and switches** (Ch. 4–7): Flashlights, telegraphs, relays
3. **Logic gates** (Ch. 8): AND, OR, NOT, NAND, NOR from relay circuits — the hardware realization of [[boolean-algebra]] and [[shannon-1938]]
4. **Number systems** (Ch. 9–12): Decimal, binary, octal, hexadecimal, bytes
5. **Text encoding** (Ch. 13): ASCII to Unicode
6. **Arithmetic in hardware** (Ch. 14–16): Adders, subtractors, two's complement
7. **Memory** (Ch. 17–19): Flip-flops, latches, RAM
8. **The CPU** (Ch. 20–24): ALU, registers, buses, control signals, instruction decoding, loops, jumps, subroutines
9. **The ecosystem** (Ch. 25–28): Peripherals, operating systems, programming languages, the internet

(source: Code the hidden language of computer hardware and software.pdf)

## Key pedagogical moves

### Ancient technologies for universal principles

Petzold uses 19th-century technologies (telegraphs, relays) to explain principles that apply equally to modern transistors. The point is that the principles are universal: a relay and a transistor both implement a switch, and the logic built from either is the same [[boolean-algebra]] (source: Code the hidden language of computer hardware and software.pdf).

### Minimal metaphor

Unlike many popular computing books, *Code* avoids metaphors and analogies in favor of the actual language and symbols used by engineers. The reader builds real circuits (illustrated on the companion website CodeHiddenLanguage.com) and traces real signals through real logic (source: Code the hidden language of computer hardware and software.pdf).

### The CPU as composition

The book's climax is showing that a CPU is nothing more than a specific arrangement of the logic gates, memory elements, and arithmetic circuits introduced in earlier chapters. There is no new principle at the top — only composition. This makes the point that general-purpose computation emerges from simple, well-understood components (source: Code the hidden language of computer hardware and software.pdf).

## Significance for the book's arc

*Code* is the "how it's built" complement to the theoretical papers. Where [[boole-1854]] provides the algebra, [[shannon-1938]] the circuit mapping, and [[turing-1936]] the theory of computation, Petzold shows how all three come together in a physical machine. The CPU he constructs is a universal machine in Turing's sense — capable of executing any program, including the training and inference code for the [[transformer-architecture]].

## Related pages

- [[boolean-algebra]]
- [[shannon-1938]]
- [[turing-machine]]
- [[universal-machine]]
- [[computability]]
