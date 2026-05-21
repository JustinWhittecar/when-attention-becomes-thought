# Bell Labs relay computers

**Summary**: The series of electromechanical relay computers designed by George Stibitz and collaborators at Bell Telephone Laboratories between 1937 and 1948 -- the first computers built directly on the foundation [[shannon-1938|Shannon's relay-and-Boolean-algebra]] thesis had established, and the only American electromechanical computing tradition to run in parallel with [[harvard-mark-i|Aiken at Harvard]].

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-13

---

## Model K and the Complex Number Computer

George Stibitz was a mathematician at Bell Telephone Laboratories who, in November 1937, built a small two-bit binary adder out of relays, batteries, flashlight bulbs, tin can lids, and metal strips at his kitchen table -- a prototype that became known as the "Model K" (for Kitchen). The device demonstrated that the relays Bell Labs already manufactured by the million for telephone exchanges could perform arithmetic. (source: The Origins of Digital Computers - Unknown.pdf)

Bell Labs took up the idea in 1938. By January 1940 Stibitz and Samuel Williams had built the **Complex Number Computer** (later called the Bell Labs Model I), a relay machine specialised for arithmetic on complex numbers -- the kind of calculation that filter and antenna design at Bell required. The Complex Number Computer used about 450 relays. (source: The Origins of Digital Computers - Unknown.pdf)

The machine made history in September 1940 when Stibitz demonstrated it remotely: he sent problems from a teletype at Dartmouth College in New Hampshire to the machine at Bell Labs in New York and received the answers back over a phone line. This was the first instance of remote computing -- the conceptual ancestor of every networked computation since.

## Models II through V

After the Complex Number Computer, Bell Labs built a sequence of progressively more general relay machines (source: The Origins of Digital Computers - Unknown.pdf):

| Model | Year | Purpose | Relays |
|---|---|---|---|
| Model II (Relay Interpolator) | 1943 | Anti-aircraft fire-control problems | ~440 |
| Model III (Ballistic Computer) | 1944 | Army Ordnance ballistic calculations | ~1,400 |
| Model IV | 1945 | Navy fire-control | ~1,400 |
| Model V | 1946-1947 | General purpose, two machines built | ~9,000 |
| Model VI | 1949 | Improved Model V | ~5,500 |

Models II-V are documented in Chapter 6 of [[randell-1973]] through four papers:

- Stibitz's 1940 internal memorandum *Computer* (Chapter 6.1) is the earliest description of his work.
- O. Cesareo's *The Relay Interpolator* (1946, Chapter 6.2) describes Model II.
- J. Juley's *The Ballistic Computer* (1947, Chapter 6.3) describes Model III.
- F.L. Alt's *A Bell Telephone Laboratories' Computing Machine* (1948, Chapter 6.4) describes Model V in detail, including its floating-point arithmetic and its programming by paper tape.

The Model V was Stibitz's most ambitious machine: a general-purpose, floating-point, multi-user, fault-tolerant relay computer with two processors and remote teletype consoles. Two were built; one went to NACA (later NASA) at Langley, the other to Aberdeen Proving Ground.

## Architecture choices

The Bell Labs machines made several design choices that contrast with their contemporaries (source: The Origins of Digital Computers - Unknown.pdf):

- **Bi-quinary decimal** (mostly), not binary. Stibitz used a coded decimal representation where each digit was encoded by exactly two relays out of seven -- a 2-of-7 scheme that allowed automatic error detection. If a relay failed, the count of "1" relays would no longer be 2 and the machine would halt. This made the Bell Labs machines famously reliable.
- **Self-checking arithmetic.** The Model V and Model VI ran every computation twice on parallel hardware and compared the results, halting if they disagreed.
- **Multiple problem positions.** The Model V had several teletype-console "problem positions" so multiple users could submit problems simultaneously -- an early form of time-sharing.
- **Floating-point in hardware** from Model III onward, with the same kind of normalised exponent-mantissa representation [[zuse-z3|Zuse]] had implemented independently in Berlin.

These choices reflected Bell Labs' core engineering culture: relays were cheap and well-understood at AT&T, error-detection was important because the machines ran unattended, and the goal was reliable production computing rather than electronic speed.

## Why they don't get the headlines

The Bell Labs relay machines were eclipsed in the historical record by [[eniac|ENIAC]] (1946) and the [[stored-program-computer|stored-program computers]] of 1948-1949 for one reason: they were electromechanical, not electronic, and ran a thousand times slower. By the time the Model V was operational in 1947, the writing was on the wall -- electronic vacuum-tube computing was the future, and even relay-machine adherents at Bell Labs eventually transitioned to building electronic computers.

But the Bell Labs machines mattered in three ways (source: The Origins of Digital Computers - Unknown.pdf):

1. **They were the first practical embodiment of [[shannon-1938|Shannon's]] switching theory.** Shannon's 1938 thesis was developed *at Bell Labs*; the Complex Number Computer was being built down the hall while Shannon was writing his thesis. The two pieces of work cross-pollinated directly.

2. **They proved fault-tolerant computing was possible.** The self-checking design philosophy -- run everything twice, compare, halt on mismatch -- influenced every subsequent generation of high-reliability computing, including the Apollo Guidance Computer and modern aerospace systems.

3. **They served as the production workhorses of US wartime science.** From 1943 to 1946, when [[eniac|ENIAC]] was still being built and [[colossus|Colossus]] was still secret, Models II-IV at Aberdeen and Langley computed ballistic tables, antenna patterns, and aircraft stability calculations that other machines could not handle.

## Related pages

- [[shannon-1938]]
- [[shannon-1948]]
- [[harvard-mark-i]]
- [[zuse-z3]]
- [[eniac]]
- [[colossus]]
- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[boolean-algebra]]
- [[randell-1973]]
