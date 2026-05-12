# ENIAC

**Summary**: The Electronic Numerical Integrator and Computer, built at the Moore School of Electrical Engineering at the University of Pennsylvania between 1943 and 1946 -- the first general-purpose, fully electronic, digital computer, and the machine whose construction prompted the design of the [[von-neumann-architecture|von Neumann architecture]].

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## Origin

ENIAC was commissioned in June 1943 by the US Army Ballistic Research Laboratory at Aberdeen Proving Ground, which urgently needed ballistic firing tables for new artillery pieces. The existing differential analyser at the Moore School and the human "computers" (mostly women, including Kay McNulty, Betty Jennings, Betty Snyder, Marlyn Wescoff, Fran Bilas, and Ruth Lichterman, who would later program the machine) could not keep up with wartime demand. John Mauchly had circulated a 1942 memo, "The Use of High-Speed Vacuum Tube Devices for Calculating" (reprinted as Chapter 7.4 in Randell), proposing an electronic alternative. J. Presper Eckert led the engineering. (source: The Origins of Digital Computers - Unknown.pdf)

The machine was completed in late 1945 and publicly unveiled on 15 February 1946. It came too late to compute wartime firing tables but was almost immediately put to work on a thermonuclear weapon feasibility study for Los Alamos. (source: The Origins of Digital Computers - Unknown.pdf)

## Physical scale

ENIAC was the largest electronic device built up to that point (source: The Origins of Digital Computers - Unknown.pdf):

- **17,468 vacuum tubes** (mostly twin-triodes), plus 7,200 crystal diodes
- **70,000 resistors**, **10,000 capacitors**, **1,500 relays**, **6,000 manual switches**
- **27 tons** of weight, **1,800 square feet** of floor space
- **150 kilowatts** of power consumption (the standing joke that the lights of Philadelphia dimmed when ENIAC was switched on was repeated often enough to enter folklore)
- **5,000 additions per second** -- roughly a thousand times faster than the contemporary [[harvard-mark-i|Harvard Mark I]]

The machine used decimal arithmetic, with ten-position ring counters built from flip-flops representing each digit. There were twenty accumulators, each capable of holding a ten-digit signed number and performing addition or subtraction. (source: The Origins of Digital Computers - Unknown.pdf)

## Not a stored-program computer

ENIAC's most important *limitation* shaped the design of every machine that followed. It was programmed by physically connecting its functional units with patch cables on plug-boards and setting thousands of rotary switches. Setting up a new problem could take days of physical labour. The six women hired as ENIAC's original programmers worked from logical diagrams of the machine, translating high-level algorithms into sequences of plug-board wirings. (source: The Origins of Digital Computers - Unknown.pdf)

This labour-intensive process was the practical problem that von Neumann's *First Draft of a Report on the EDVAC* (1945) was written to solve. The solution -- holding the program in fast electronic memory rather than on plug-boards -- became the [[stored-program-computer|stored-program]] idea. (source: The Origins of Digital Computers - Unknown.pdf)

In 1948 ENIAC itself was retrofitted to run in a quasi-stored-program mode, with a small set of instructions stored in function-table switches, extending its useful life until 1955.

## The Goldstine & Goldstine paper

Chapter 7.5 of Randell's anthology reprints H.H. Goldstine and A. Goldstine's 1946 paper, "The Electronic Numerical Integrator and Computer (ENIAC)," published in *Mathematical Tables and Other Aids to Computation*. It is the first comprehensive published description of the machine, and it lays out the accumulator-and-multiplier organisation, the master programmer, and the cycle-by-cycle operation of the machine. The paper does not describe the plug-board programming in detail because it was still considered sensitive. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance

ENIAC matters in three ways (source: The Origins of Digital Computers - Unknown.pdf):

1. **It proved electronic computing was feasible at scale.** Skeptics had argued that a machine with 17,000 vacuum tubes would fail within minutes -- the mean time between failures of a single tube was thousands of hours, but with 17,000 of them the expected time between *some* failure was minutes. Eckert's engineering practices (running tubes well below their rated voltages, never powering the machine down) achieved actual mean times between failures of about half a day, enough to be useful.

2. **It was a thousand times faster than the best electromechanical machines.** This made calculations that had been impractical -- ballistic trajectories, weather prediction, Monte Carlo simulations of neutron diffusion -- routine. The speed gap convinced the postwar scientific community that electronic computers, not relay machines, were the future.

3. **Its programming problem motivated the von Neumann architecture.** Without ENIAC's plug-board agony, there would have been no urgency to invent the stored-program design. The two machines are the two halves of the same story: ENIAC is what electronic computing looks like before [[edvac|EDVAC]], and EDVAC is what it looks like after.

## Related pages

- [[edvac]]
- [[von-neumann-architecture]]
- [[stored-program-computer]]
- [[manchester-baby]]
- [[edsac]]
- [[harvard-mark-i]]
- [[colossus]]
- [[zuse-z3]]
- [[turing-1936]]
- [[shannon-1938]]
- [[randell-1973]]
- [[petzold-2023]]
