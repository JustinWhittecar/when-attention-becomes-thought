# Colossus

**Summary**: The series of large-scale electronic codebreaking machines designed by Tommy Flowers and operated at Bletchley Park from 1944, used to break the German Lorenz teleprinter cipher -- the first programmable electronic digital computers, kept secret until 1972.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## What they were for

By 1942 Bletchley Park was reading German Enigma traffic at industrial scale, but a higher-security cipher -- the Lorenz SZ40/42 teleprinter cipher, codenamed "Tunny" -- was being used for the most sensitive communications between Hitler and his field marshals. Tunny was attacked by manual and electromechanical methods (the Heath Robinson machines) but the analysis required massive amounts of statistical correlation between two paper tapes running in synchrony, and the tapes shredded constantly. Tommy Flowers, an engineer at the Post Office Research Station at Dollis Hill, proposed replacing one of the paper tapes with a fully electronic implementation using vacuum tubes -- generating the key-stream internally rather than reading it from tape. (source: The Origins of Digital Computers - Unknown.pdf)

Colossus Mark 1 entered service in February 1944. Colossus Mark 2, with 2,400 vacuum tubes (1,600 in Mark 1), arrived just before D-Day in June 1944 and was producing strategic intelligence by then. Ten Colossi were operating by the end of the war. (source: The Origins of Digital Computers - Unknown.pdf)

## Architecture

Colossus was not a general-purpose computer. It was programmable in the sense that it could be reconfigured by switches and plug-boards to perform different statistical operations on the input cipher tape, but it could not store programs in memory and was not [[turing-1936|Turing-complete]]. (source: The Origins of Digital Computers - Unknown.pdf)

Its design features included:

- **1,600-2,400 vacuum tubes** -- more than any earlier machine, vastly more reliable than skeptics had predicted
- **Photoelectric paper-tape reader** running at 5,000 characters per second (later 25,000 with the Mark 2's parallel reading)
- **Shift registers and ring counters** implemented in vacuum tubes for high-speed Boolean operations
- **Programmable Boolean function** computed from up to five characters of the cipher tape and the simulated key-stream
- **Conditional output and counters** that tallied matches according to operator-defined statistical tests

The machine implemented exactly the kind of high-speed Boolean computation that [[shannon-1938|Shannon]] had analysed in abstract terms; in operational terms it was the first demonstration that vacuum-tube digital logic could be made reliable at scale. (source: The Origins of Digital Computers - Unknown.pdf)

## Turing's role at Bletchley

Alan Turing was at Bletchley Park from 1939 to 1945. His contribution was principally to the Enigma attack -- the Bombe machine, an electromechanical device that searched for Enigma rotor settings, was designed by Turing and Gordon Welchman. Turing also did statistical and theoretical work that fed into the Tunny attack and the Newmanry section that ran Colossus, but the Colossus design itself was Flowers's engineering. Turing's 1936 paper had defined the universal machine; Bletchley showed that very specialised electronic machines could be built and made to work. The two threads -- universal computation in theory, electronic digital logic in practice -- would converge after the war in the [[manchester-baby|Manchester]] and [[edvac|Princeton]] projects. (source: The Origins of Digital Computers - Unknown.pdf)

## Secrecy and its consequences

The British government classified Colossus as a state secret in 1945. The ten wartime machines were dismantled (eight immediately, two retained at GCHQ until the 1960s); their plans were burnt; the personnel were sworn to secrecy. As a result, the standard published histories of computing written through the 1960s identified [[eniac|ENIAC]] (February 1946) as the first large-scale electronic digital computer. The truth that Colossus had been doing electronic digital logic on a comparable scale two years earlier became publicly known only in 1972, with the publication of Brian Randell's research and Donald Michie's chapter in this anthology. (source: The Origins of Digital Computers - Unknown.pdf)

## The Michie chapter

Chapter 7.3 of Randell's anthology is Donald Michie's 1972 paper *The Bletchley Machines* -- one of the very first published accounts of Colossus, written by a former Bletchley cryptanalyst who had been part of the Newmanry section. The chapter is short by anthology standards (Randell was operating under the constraint that much detail was still classified) but it was decisive in shifting the historical consensus. Subsequent declassifications in 1996 and 2000 made the full Colossus design public; a functional rebuild has operated at the National Museum of Computing since 2007. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance

Colossus matters for three reasons:

1. **It proved electronic digital logic could be built reliably at scale**, a year and a half before ENIAC demonstrated the same thing publicly. Flowers's design practices (running tubes well below rated voltage, never powering the machine down) directly informed the design philosophy that Eckert applied to ENIAC.

2. **It is the missing link** between Turing's 1936 abstract universal machine and the postwar British computing efforts. Many of the Manchester Baby's designers and users had Bletchley backgrounds. The cultural transmission from secret wartime electronic computing to the first stored-program computer was direct.

3. **Its secrecy distorts the historical record** in a way that took decades to repair. Without Randell's 1973 anthology -- the first major scholarly work to acknowledge Colossus existed -- the standard story of computing might still skip from Babbage to ENIAC, leaving out the wartime electronic digital tradition entirely.

## Related pages

- [[eniac]]
- [[turing-1936]]
- [[universal-machine]]
- [[shannon-1938]]
- [[boolean-algebra]]
- [[edvac]]
- [[manchester-baby]]
- [[turing-test]]
- [[randell-1973]]
