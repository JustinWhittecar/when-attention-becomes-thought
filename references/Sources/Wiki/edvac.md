# EDVAC and the First Draft

**Summary**: The Electronic Discrete Variable Automatic Computer -- proposed in John von Neumann's 1945 *First Draft of a Report on the EDVAC* as the successor to ENIAC -- and the design document that defined the [[stored-program-computer|stored-program]] [[von-neumann-architecture|architecture]].

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## The document

The *First Draft of a Report on the EDVAC* is a 101-page typescript dated 30 June 1945 and circulated by Herman Goldstine of the Moore School (University of Pennsylvania) under John von Neumann's name only. It is reprinted as Chapter 8.1 of Randell's anthology. (source: The Origins of Digital Computers - Unknown.pdf)

The *First Draft* was never formally completed; it was meant as an internal working paper synthesising months of discussions between von Neumann, J. Presper Eckert, John Mauchly, Goldstine, and Arthur Burks during the construction of [[eniac|ENIAC]]. Goldstine sent mimeographed copies to several dozen people in 1945. This circulation -- and the fact that von Neumann's name alone appeared on it -- made the document the public anchor for the design ideas it contained, with consequences for credit and patent law that took decades to resolve. (source: The Origins of Digital Computers - Unknown.pdf)

## Key ideas

The *First Draft* introduces, in roughly this order (source: The Origins of Digital Computers - Unknown.pdf):

1. **Functional decomposition** of the computer into five organs: central arithmetic (CA), central control (CC), memory (M), input (I), and output (O). See [[von-neumann-architecture]].

2. **Binary representation** of numbers, justified by the two-state nature of the available switching elements (vacuum tubes, then later relays and transistors) and by the simpler arithmetic circuits that result. This is the architectural application of [[shannon-1938|Shannon's]] result that [[boolean-algebra]] maps onto switching circuits.

3. **A single addressable memory holding both orders and numbers.** This is the decisive break from [[eniac|ENIAC]] and from the [[harvard-mark-i|Harvard]]-style separation of program and data tapes. Von Neumann argues that the same physical store should hold instructions and data because the machine should be able to compute on its own instructions.

4. **The fetch-decode-execute cycle** as the basic operating rhythm of the control organ.

5. **Conditional transfers** -- instructions that change the program counter only if some condition (typically the sign of an accumulator) holds. This is what gives a stored-program machine its [[universal-machine|universality]].

6. **A first attempt at an instruction set** -- thirty-odd opcodes covering arithmetic, memory transfers, conditional transfers, and I/O.

7. **Mercury delay lines as memory.** Eckert had proposed using ultrasonic waves circulating in tubes of mercury as a serial-access memory. The *First Draft* adopted this scheme, though Williams cathode-ray-tube storage would soon supersede it.

The document uses a quasi-physiological vocabulary -- "organs", "neurons", "associative memory" -- influenced by the [[https://en.wikipedia.org/wiki/Warren_Sturgis_McCulloch|McCulloch]]-Pitts 1943 paper on neural logic. This vocabulary did not survive into the engineering literature, but the substantive design did.

## The physical EDVAC

The machine itself was built much more slowly than the document was circulated. After patent disputes between the Moore School, Eckert, Mauchly, and the University of Pennsylvania, Eckert and Mauchly left in 1946 to form their own company. The remaining team completed EDVAC in 1949 and delivered it to the Ballistic Research Laboratory at Aberdeen in 1951. By that time the [[manchester-baby|Manchester Baby]] (1948) and [[edsac|EDSAC]] (1949) had already demonstrated the stored-program design in working hardware. (source: The Origins of Digital Computers - Unknown.pdf)

EDVAC as eventually built had:
- About 6,000 vacuum tubes (a third of ENIAC's count)
- 1,024 words of mercury delay-line memory, each 44 bits wide
- Roughly 1,100 additions per second
- Serial (one-bit-at-a-time) arithmetic, in contrast to ENIAC's parallel decimal

EDVAC remained in service until 1961.

## The IAS report

Closely related to the *First Draft* is the second document in Randell's Chapter 8: Arthur Burks, Herman Goldstine, and John von Neumann's 1946 report *Preliminary Discussion of the Logical Design of an Electronic Computing Instrument*, written at the Institute for Advanced Study at Princeton. The IAS report is the more polished, public, and formally co-authored statement of the same architecture, and it served as the blueprint for the IAS computer (1952), the ILLIAC, the JOHNNIAC, the AVIDAC, the ORDVAC, and a dozen other "von Neumann machines" built in universities around the world in the early 1950s. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance for the wiki's arc

The *First Draft* is the single document that turned [[turing-1936|Turing's universal machine]] from a theoretical construction into an engineering blueprint. Turing's 1936 paper had shown that a single machine could simulate any other if it could read the other machine's description from a tape; the *First Draft* identified that "description on a tape" with a region of fast electronic memory, and from there the entire modern computing era follows.

Every chip that trains a [[transformer-architecture|Transformer]], every CPU that runs PyTorch, every GPU that performs the matrix multiplications inside [[self-attention]], is a descendant of this 101-page typescript. (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[eniac]]
- [[manchester-baby]]
- [[edsac]]
- [[harvard-mark-i]]
- [[turing-1936]]
- [[universal-machine]]
- [[shannon-1938]]
- [[boolean-algebra]]
- [[randell-1973]]
- [[petzold-2023]]
