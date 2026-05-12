# Harvard Mark I

**Summary**: The Automatic Sequence Controlled Calculator (ASCC), designed by Howard Aiken and built by IBM, installed at Harvard in 1944 -- a fifty-foot-long electromechanical relay computer that was the first large-scale automatic digital calculator in the United States, and the prototype of the "Harvard architecture" with separate program and data memories.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## Aiken's 1937 proposal

Chapter 5.1 of Randell's anthology reprints Aiken's 1937 internal memorandum, *Proposed Automatic Calculating Machine*, written while he was a graduate student at Harvard. Aiken needed to integrate the differential equations governing space-charge in vacuum tubes for his doctoral thesis and was frustrated by the time these calculations took. His memo argued that an automatic calculator capable of sequenced operations -- explicitly modelled on [[analytical-engine|Babbage's Analytical Engine]] -- could be built using existing IBM punched-card and tabulating technology. (source: The Origins of Digital Computers - Unknown.pdf)

Aiken's memo is one of the earliest documents to recognise that Babbage's hundred-year-old design was the right starting point for a modern computer. He writes that the four requirements for such a machine are: handling positive and negative numbers, transcendental functions, fully automatic operation, and the ability to compute the value of a function for a given argument. The memo became the basis for an IBM proposal in 1939; construction began at IBM's Endicott laboratory in 1939 and the machine was delivered to Harvard in February 1944. (source: The Origins of Digital Computers - Unknown.pdf)

## Physical design

The Mark I was electromechanical, not electronic. It used (source: The Origins of Digital Computers - Unknown.pdf):

- **765,000 components** including relays, rotary switches, and clutches
- About **3,500 multipole relays**
- A **50-foot-long shaft** running the length of the machine, driven by a 5-horsepower motor, providing synchronisation
- **72 mechanical accumulators**, each holding a signed 23-decimal-digit number
- **60 sets of rotary switches** for storing constants
- **Punched paper tape** for instructions, with three tapes that could be selected under operator control
- **Punched cards** for data input and printed tabulators for output

It performed three additions per second, one multiplication every six seconds, and one division every fifteen seconds. By comparison, [[eniac|ENIAC]] a few years later would do 5,000 additions per second -- the gap between electromechanical and electronic.

## The Harvard architecture

The Mark I is the prototype of what is now called the **Harvard architecture**: instructions and data live in physically separate memories with separate paths to the control unit. The Mark I had instructions on paper tape and data in mechanical registers; there was no way to write to the program tape from a computation, no way to compute on an instruction. (source: The Origins of Digital Computers - Unknown.pdf)

This separation has one big advantage -- the program is physically protected from being overwritten by buggy data -- and one big disadvantage: the machine cannot compile, interpret, or otherwise treat code as data. The opposing [[von-neumann-architecture|von Neumann architecture]] of [[edvac|EDVAC]] unifies the two memories.

Modern processors are mostly von Neumann from the programmer's perspective but use a Harvard arrangement internally between the instruction cache and the data cache for performance; embedded microcontrollers (PIC, AVR) often retain the Harvard split at the architectural level for safety reasons.

## The Aiken & Hopper paper

Chapter 5.2 of Randell's anthology reprints H.H. Aiken and Grace M. Hopper's 1946 paper *The Automatic Sequence Controlled Calculator* from *Electrical Engineering*. It is the first published technical description of the machine -- by then renamed the ASCC -- and the first widely-circulated paper authored in part by Grace Hopper, who had joined the Mark I team in 1944 as a Navy lieutenant and went on to invent the first compiler (A-0, 1952) and to lead the development of COBOL. Hopper's work on the Mark I included writing what was effectively the first programming manual. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance

The Mark I matters because it was the bridge between [[babbage-1837|Babbage's century-old design]] and the electronic computers that followed. It demonstrated:

1. **That Babbage's architectural ideas were sound.** A machine built on Mill-and-Store lines, programmed by punched tape, with conditional branching and iteration, actually worked and computed useful results -- though slowly.
2. **That a partnership between academia and industry could deliver a working programmable computer.** IBM's manufacturing capability plus Harvard's mathematical requirements produced the machine in five years.
3. **That sequence-controlled calculation had wartime value.** The Mark I spent most of 1944-1945 computing ballistic and naval tables for the US Navy, including computations supporting the Manhattan Project.

Aiken's IBM connection led to a sequence of successor machines (Mark II, III, IV) that explored increasingly electronic technology. But the architectural torch passed to ENIAC and EDVAC at Pennsylvania, and to the [[manchester-baby|Manchester]] and [[edsac|Cambridge]] groups in Britain. Aiken famously misjudged the electronic future, predicting in 1947 that "only six electronic digital computers would be required to satisfy the computing needs of the entire United States." (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[zuse-z3]]
- [[eniac]]
- [[edvac]]
- [[stored-program-computer]]
- [[von-neumann-architecture]]
- [[analytical-engine]]
- [[babbage-1837]]
- [[ada-lovelace]]
- [[randell-1973]]
- [[petzold-2023]]
