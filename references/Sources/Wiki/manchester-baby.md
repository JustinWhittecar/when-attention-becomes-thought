# Manchester Baby

**Summary**: The Small-Scale Experimental Machine built at the University of Manchester by Frederic Williams, Tom Kilburn, and Geoff Tootill -- the first computer to execute a program held in its own electronic memory, on 21 June 1948.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## What it did

On 21 June 1948 the Baby ran a 17-instruction program written by Tom Kilburn to find the highest proper factor of 2^18 = 262,144. After roughly 52 minutes of computation, executing some 3.5 million instructions, it returned the correct answer (131,072). This was the first occasion on which a [[stored-program-computer|stored program]] held in electronically writable memory was successfully executed by a computer. (source: The Origins of Digital Computers - Unknown.pdf)

## What was new

Earlier machines had been programmable, but their programs lived outside fast memory:

- [[eniac|ENIAC]] was programmed by plug-board wiring.
- [[harvard-mark-i|The Harvard Mark I]] read instructions from punched paper tape.
- [[zuse-z3|The Zuse Z3]] read instructions from punched film.
- [[colossus|Colossus]] was specialised for codebreaking and not Turing-complete.

The Baby was a deliberately minimal demonstration of the principle proposed in von Neumann's [[edvac|First Draft]] (1945): that instructions could be stored in the same electronic memory as data, fetched at electronic speed by a control unit. (source: The Origins of Digital Computers - Unknown.pdf)

## Williams-tube memory

The Baby's significance is inseparable from its memory technology. Williams and Kilburn had developed the **Williams tube**, which stored bits as electrostatic charges on the phosphor of a cathode-ray tube: a dot in one location meant 0, a dot in another meant 1. A second tube continuously refreshed the pattern by reading and rewriting it. The Baby had a single 32-by-32-bit tube -- 1,024 bits, or 32 words of 32 bits each -- which served as both program and data memory. (source: The Origins of Digital Computers - Unknown.pdf)

The Williams tube was the first practical random-access memory: any bit could be read or written in roughly 10 microseconds, in any order. Mercury delay lines (used by [[edsac|EDSAC]] and [[edvac|EDVAC]]) were faster per bit but serial-only, forcing the machine to wait for a word to circulate past the reader. Random access turned out to be the architecturally crucial property, and Williams tubes were copied by the IAS computer, ILLIAC, and others before being superseded by magnetic core memory in the early 1950s.

## Architecture

The Baby was a serial binary machine (source: The Origins of Digital Computers - Unknown.pdf):

- **Word length**: 32 bits
- **Memory**: 32 words on a single Williams tube
- **Instruction set**: 7 instructions (load negative, store, subtract, conditional skip, jump, halt, etc.)
- **Arithmetic**: subtraction only -- addition was done by subtracting the negative. This minimised the hardware needed to demonstrate the principle.
- **Clock**: about 100 microseconds per instruction
- **Vacuum tubes**: 550

Its purpose was not to be useful but to prove the Williams tube worked as memory. Once it had, the Manchester team scaled it up into the Manchester Mark 1 (1949) and then the commercial Ferranti Mark 1 (1951) -- the first computer that anyone could buy.

## The Williams & Kilburn paper

Chapter 8.4 of Randell's anthology is F.C. Williams and T. Kilburn, *Electronic Digital Computers* (Nature, 25 September 1948), a one-page note announcing the successful run. The paper is terse to the point of obscurity -- it gives the highest-factor result and the memory size, but no instruction set and no programming details. It was, however, the first public announcement that a stored-program computer existed and worked. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance

The Baby is the moment when [[turing-1936|Turing's universal machine]] first existed as physical hardware capable of running an arbitrary program from rewritable memory. Turing himself joined the Manchester team in 1948 and wrote the programming manual for the Mark 1 successor; this is one of the few cases where the inventor of a theoretical idea lived to write code for its physical realisation. (source: The Origins of Digital Computers - Unknown.pdf)

It is also where the chain to modern computing becomes unbroken: every laptop, phone, GPU cluster, and LLM-training rig descends, in an unbroken line of "successor machine inspired the next", from the Baby's 21 June 1948 run.

## Related pages

- [[edsac]]
- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[eniac]]
- [[colossus]]
- [[turing-1936]]
- [[universal-machine]]
- [[randell-1973]]
- [[petzold-2023]]
