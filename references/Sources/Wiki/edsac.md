# EDSAC

**Summary**: The Electronic Delay Storage Automatic Calculator, built at the University of Cambridge Mathematical Laboratory by Maurice Wilkes and his team, which ran its first program on 6 May 1949 -- the first computer to enter routine service as a stored-program scientific instrument.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## First run

On 6 May 1949 EDSAC executed a program written by Wilkes to compute and print a table of squares of the integers from 0 to 99. A second program shortly after computed a list of prime numbers. Both ran to completion and produced correct output. Where the [[manchester-baby|Manchester Baby]] (June 1948) had been a demonstration of principle on a 32-word memory, EDSAC was a full-scale machine designed from the start to be useful to scientists outside the computing group. (source: The Origins of Digital Computers - Unknown.pdf)

## Origin

Maurice Wilkes had attended the Moore School Lectures in the summer of 1946 -- a series of lectures by Eckert, Mauchly, von Neumann, Goldstine, Burks, and others that disseminated the [[edvac|First Draft]] ideas to the wider computing community. He returned to Cambridge convinced that a stored-program machine should be built immediately, and along the simplest workable lines rather than as a research vehicle for novel hardware. (source: The Origins of Digital Computers - Unknown.pdf)

This pragmatic stance made EDSAC the second stored-program computer to run -- and the first to do useful work.

## Architecture

EDSAC was a binary, serial, single-address machine (source: The Origins of Digital Computers - Unknown.pdf):

- **Word length**: 17 bits (later extended)
- **Memory**: 32 mercury delay-line tanks, each holding 32 words, for a total of 1,024 words. Mercury delay lines used ultrasonic pulses circulating through tubes of mercury; a pulse train re-entered the tube at one end as it emerged from the other, refreshed by transducers. Access was serial: the machine had to wait for the desired word to circulate past the reader.
- **Instruction set**: 18 instructions, including an "initial orders" routine -- the world's first bootstrap loader -- that could read further programs from paper tape.
- **Clock**: 500 kHz; about 650 instructions per second
- **Vacuum tubes**: about 3,000
- **Floor space**: 20 square metres

EDSAC's initial orders, designed by David Wheeler, included a one-letter mnemonic assembly notation -- the first assembler. Wheeler also invented the **subroutine** as a software construct on EDSAC, and the "Wheeler jump" that linked subroutine calls and returns. The subroutine library Wheeler, Wilkes, and Stanley Gill built up became the world's first piece of reusable software. Their 1951 book *The Preparation of Programs for an Electronic Digital Computer* was the first textbook of programming. (source: The Origins of Digital Computers - Unknown.pdf)

## The Wilkes & Renwick paper

Chapter 8.5 of Randell's anthology is M.V. Wilkes and W. Renwick, *The EDSAC*, a paper presented at the Manchester conference on the inauguration of EDSAC in June 1949, and Chapter 8.6 is B.H. Worsley's companion demonstration paper. Together they describe the machine, its instruction set, the initial orders, the first programs, and the operating procedure used at Cambridge. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance

EDSAC matters because it was *used*. From 1949 onwards Cambridge scientists from chemistry, biology, astronomy, and economics walked into the Mathematical Laboratory with computations they could not do by hand and walked out with results. Two pieces of work supported by EDSAC won Nobel Prizes -- John Kendrew's analysis of myoglobin structure (1962) and Andrew Huxley's modelling of nerve action potentials (1963).

The Cambridge group's pragmatism -- mercury delay lines because they were known to work, no fancy hardware, immediate focus on software tooling and a user community -- set the template for academic computing centres worldwide. The LEO (Lyons Electronic Office) computer, built by the J. Lyons & Co. tea-shop chain in 1951 based on EDSAC's design, was the first computer used for routine commercial business processing. (source: The Origins of Digital Computers - Unknown.pdf)

If the [[manchester-baby|Baby]] proved that stored-program computing was possible, EDSAC proved that it was *useful*.

## Related pages

- [[manchester-baby]]
- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[eniac]]
- [[turing-1936]]
- [[universal-machine]]
- [[randell-1973]]
- [[petzold-2023]]
