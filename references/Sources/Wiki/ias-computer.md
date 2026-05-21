# IAS computer

**Summary**: The Electronic Computer Project machine built at the Institute for Advanced Study in Princeton between 1946 and 1952 under John von Neumann's direction -- the first machine to fully implement the [[von-neumann-architecture|von Neumann architecture]] as a deliberate design (rather than as a retrofit), and the template that was copied at roughly a dozen institutions worldwide.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-13

---

## Origin

In the spring of 1946, while the [[eniac|ENIAC]] was being completed at the Moore School and the patent disputes between Eckert, Mauchly, and the University of Pennsylvania were intensifying, John von Neumann returned to the Institute for Advanced Study in Princeton with a plan to build a successor machine on the design principles he had laid out in the 1945 [[edvac|First Draft of a Report on the EDVAC]]. (source: The Origins of Digital Computers - Unknown.pdf)

The Electronic Computer Project at IAS was unusual in two ways:

- **It was the first computer project explicitly run by mathematicians for mathematicians.** Von Neumann's stated purpose was to provide a tool for numerical experiments on the partial differential equations of fluid dynamics, weather prediction, and the nascent field of hydrogen-bomb design.
- **It was deliberately designed to be copied.** Reports, schematics, and parts lists were published openly, in contrast to the patent-encumbered Eckert-Mauchly tradition. Von Neumann wanted the architecture to spread.

## The Burks, Goldstine, von Neumann reports

The IAS design was published in three reports, the most famous of which is *Preliminary Discussion of the Logical Design of an Electronic Computing Instrument* by Arthur Burks, Herman Goldstine, and John von Neumann (June 1946). This 42-page document is the polished, formally co-authored statement of the architecture sketched in von Neumann's solo 1945 [[edvac|First Draft]]. It is reprinted as Chapter 8.3 of [[randell-1973]]. (source: The Origins of Digital Computers - Unknown.pdf)

The *Preliminary Discussion* improves on the *First Draft* in several ways:

- The vocabulary is engineering rather than physiological -- "registers" and "memory" replace "organs" and "neurons."
- The instruction set is more carefully specified, including a clear treatment of conditional transfers.
- The memory technology has shifted from Eckert's mercury delay lines to Williams cathode-ray-tube storage, which gives true random access.
- The arithmetic is parallel (40 bits at a time) rather than serial.

Two follow-up reports in 1947 and 1948 -- *Planning and Coding of Problems for an Electronic Computing Instrument* by Herman Goldstine and von Neumann -- defined the first systematic notation for programming, including flowcharts.

## Architecture

The IAS machine as built had (source: The Origins of Digital Computers - Unknown.pdf):

- **40-bit words**, parallel arithmetic
- **1,024 words of Williams-tube memory** (40 tubes, one per bit position)
- **About 2,300 vacuum tubes**
- **Two instructions per word**, each with an opcode and an address
- **Roughly 10,000 additions per second** -- comparable to ENIAC but with stored programs and far less hardware

The machine was completed in June 1952, three and a half years after the Manchester Mark 1 had eclipsed the IAS schedule, and almost simultaneously with EDVAC's delivery to Aberdeen.

## The IAS family

The published reports led directly to a wave of computers built in the early 1950s, all based on the IAS design. They came to be called the "IAS-class" machines, "Princeton-class" machines, or simply "von Neumann machines." (source: The Origins of Digital Computers - Unknown.pdf)

The most notable copies included:

| Machine | Institution | First running |
|---|---|---|
| ILLIAC I | University of Illinois | 1952 |
| ORDVAC | Aberdeen Proving Ground (built at Illinois) | 1951 |
| JOHNNIAC | RAND Corporation | 1953 |
| MANIAC I | Los Alamos | 1952 |
| AVIDAC | Argonne National Laboratory | 1953 |
| ORACLE | Oak Ridge | 1953 |
| BESM-1 | Soviet Academy of Sciences (Moscow) | 1953 |
| WEIZAC | Weizmann Institute | 1955 |

By the mid-1950s the IAS-class machines were the workhorses of US national-laboratory computing. The first thermonuclear weapon calculations were run on MANIAC I; the Monte Carlo method was developed and refined on the IAS machine and ORDVAC; the first computer-generated random numbers and the first realistic weather simulations ran on this family.

## Why IAS, not EDVAC

The IAS report rather than the [[edvac|EDVAC First Draft]] became the template for postwar computer construction for a mix of intellectual and political reasons (source: The Origins of Digital Computers - Unknown.pdf):

- **It was the more polished document.** The *First Draft* was a Goldstine-circulated working paper with von Neumann's solo authorship; the *Preliminary Discussion* was a finished publication with three named authors and a clean technical argument.
- **It was unencumbered by patents.** The Moore School / Eckert-Mauchly patent disputes made it legally awkward to build a clone of EDVAC; the IAS reports were explicitly placed in the public domain.
- **It chose Williams tubes over mercury delay lines.** Random-access memory turned out to be the right architectural choice; the EDVAC's mercury delay lines became a dead end.
- **It published parts lists and schematics.** A team building a copy could literally order the parts from the IAS bills of materials.

## Significance

The IAS computer matters because it converted the [[stored-program-computer|stored-program]] idea from a one-off achievement (the [[manchester-baby|Manchester Baby]], June 1948) into a *reproducible engineering pattern*. Within five years of the *Preliminary Discussion*, a dozen institutions had working von Neumann machines, the architecture had stabilised, and the era of unique one-of-a-kind computers was over. The shift from "build a computer" to "build *this* computer" was the precondition for the commercial computer industry that emerged in the late 1950s and for the cumulative software ecosystem that followed. (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[eniac]]
- [[manchester-baby]]
- [[edsac]]
- [[harvard-mark-i]]
- [[randell-1973]]
- [[turing-1936]]
- [[universal-machine]]
