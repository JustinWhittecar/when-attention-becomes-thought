# Zuse Z3

**Summary**: Konrad Zuse's electromechanical relay computer, completed in Berlin in May 1941 -- the first working programmable, fully automatic, binary, floating-point computer in history.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## Origin

Konrad Zuse was a young civil engineer in Berlin who, like Howard Aiken at Harvard, was frustrated by the labour of repetitive numerical calculations -- in his case, structural analysis of aircraft wings at the Henschel aircraft factory. Starting in 1935 in his parents' apartment, working largely alone and with no knowledge of [[babbage-1837|Babbage's]] or [[analytical-engine|Lovelace's]] work, Zuse designed and built a sequence of mechanical and then electromechanical calculators (source: The Origins of Digital Computers - Unknown.pdf):

- **Z1** (1938) -- entirely mechanical, with sliding metal plates for memory. The arithmetic worked; the memory was unreliable.
- **Z2** (1940) -- mechanical memory replaced by relay arithmetic. A working prototype.
- **Z3** (May 1941) -- fully relay-based, 22-bit floating-point, programmable from punched film. The first complete working automatic computer.
- **Z4** (1945) -- a more reliable Z3-class machine, evacuated from Berlin in 1945, eventually installed at the ETH Zurich in 1950 where it ran productively for years.

Zuse's 1936 German patent application *Verfahren zur selbsttätigen Durchführung von Rechnungen mit Hilfe von Rechenmaschinen* (Method for the automatic execution of calculations with the aid of calculating machines) is reprinted in extract as Chapter 4.1 of Randell's anthology. His 1962 retrospective *Entwicklungslinien einer Rechengeräte-Entwicklung von der Mechanik zur Elektronik* is Chapter 4.3. (source: The Origins of Digital Computers - Unknown.pdf)

## Architecture

The Z3 was notable for combining several design choices that no other machine of the period combined (source: The Origins of Digital Computers - Unknown.pdf):

- **Binary**, not decimal. Zuse chose binary on the same grounds [[shannon-1938|Shannon]] had identified independently in 1938: two-state mechanical and electrical elements map naturally onto binary digits.
- **Floating-point arithmetic** with a 22-bit word (1 sign bit, 7-bit signed exponent, 14-bit mantissa). This was decades ahead of contemporaneous American machines, which used fixed-point arithmetic into the 1950s.
- **Programmable from punched film** -- 35mm movie film with holes punched in eight tracks. The film was a loop, allowing repetition, but there was no conditional branching in the Z3 (it could be simulated by manual intervention).
- **2,600 relays** -- 1,400 for memory (64 words of 22 bits) and 1,200 for arithmetic and control.
- **5-10 Hz clock**, doing about 3-4 additions per second or one multiplication in 3 seconds.

Zuse's design was electromechanical because vacuum-tube technology was unavailable to him under wartime conditions -- his colleague Helmut Schreyer (whose 1939 vacuum-tube proposal is Chapter 4.2 of Randell) had argued for an electronic design but could not get the components. (source: The Origins of Digital Computers - Unknown.pdf)

## Fate

The original Z3 was destroyed in an Allied bombing raid on Berlin in 1944, before any public demonstration. Zuse and Schreyer's work was unknown outside Germany during the war and remained obscure for decades afterwards. A replica of the Z3 was built in 1961 and is preserved at the Deutsches Museum in Munich. (source: The Origins of Digital Computers - Unknown.pdf)

In 1998, Raul Rojas formally proved that the Z3, although lacking conditional branching, is Turing-complete: branching could be simulated by running a long film loop and using arithmetic to zero out unwanted operations. This is a theoretical curiosity rather than a practical claim -- Zuse himself did not think of his machine as universal in [[turing-1936|Turing's]] sense.

## Significance

The Z3 matters for three reasons:

1. **Independent convergence on the same design.** Zuse, working alone in wartime Berlin with no knowledge of Babbage, Aiken, or the British and American projects, arrived at a binary, floating-point, automatic, programmable computer at the same moment Aiken and the [[harvard-mark-i|Harvard team]] were building their decimal version. The convergence is evidence that the design space of practical computers, given the available technology, was narrow.

2. **Floating-point in 1941.** The Z3's floating-point unit -- with normalised mantissa, signed exponent, and handling of exceptional values like infinity and undefined -- was a design that the rest of computing took two decades to catch up to. The IEEE 754 floating-point standard (1985) generalises ideas Zuse implemented in relays in 1941.

3. **Demonstration that the European computing tradition was real.** Until Randell's anthology made Zuse's work accessible in English in 1973, the history of computing as taught in the United States and Britain often skipped from Babbage to ENIAC. Zuse's chapters in Randell were one of the first widely-circulated English-language records of an independent German tradition that ran in parallel with the Anglo-American story. (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[harvard-mark-i]]
- [[eniac]]
- [[edvac]]
- [[stored-program-computer]]
- [[von-neumann-architecture]]
- [[shannon-1938]]
- [[boolean-algebra]]
- [[turing-1936]]
- [[analytical-engine]]
- [[randell-1973]]
