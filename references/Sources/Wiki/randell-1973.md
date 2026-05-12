# Randell (ed.) -- The Origins of Digital Computers: Selected Papers (1973)

**Summary**: Brian Randell's anthology of roughly thirty primary documents tracing the hardware lineage of the modern computer from Babbage's 1837 manuscript on the Analytical Engine to the EDSAC demonstration of 1949 -- the route from mechanical calculation to the stored-program electronic computer.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-12

---

## Context

Edited by Brian Randell (Professor of Computing Science, University of Newcastle upon Tyne) and published by Springer-Verlag in 1973, this 458-page anthology collects "first-hand contemporary accounts" of the inventions that produced the digital computer. Many of the papers had never been previously published or were only available in obscure proceedings; several were translated into English for this volume from German, French, and Spanish originals. (source: The Origins of Digital Computers - Unknown.pdf)

Randell's stated aim was to cover "each significant milestone on the route from BABBAGE to EDSAC." The wiki's existing [[babbage-1837]] entry is the opening paper of this anthology (Chapter 2.1); reading the full collection reveals the rest of the route -- the hundred-year arc that the wiki had previously skipped over between [[shannon-1938]]'s relay logic and the [[vaswani-et-al-2017|Transformer]]. (source: The Origins of Digital Computers - Unknown.pdf)

## Structure

The book is organised in eight chapters, each prefaced by an editorial introduction:

1. **Introduction** -- mechanical digital calculation (Schickard, Pascal, Leibniz, Thomas), sequence control (Bouchon, Falcon, Vaucanson, Jacquard) (source: The Origins of Digital Computers - Unknown.pdf)
2. **Analytical Engines** -- Babbage (1837), Merrifield (1879), H.P. Babbage (1910), Ludgate (1909), Torres y Quevedo (1914, 1920), Couffignal (1938) (source: The Origins of Digital Computers - Unknown.pdf)
3. **Tabulating Machines** -- Hollerith (1889), Couffignal (1933), Dreyer & Walther (1946) (source: The Origins of Digital Computers - Unknown.pdf)
4. **Zuse and Schreyer** -- Zuse's 1936 German patent application on automatic execution of calculations, Schreyer (1939), Zuse's retrospective (1962) (source: The Origins of Digital Computers - Unknown.pdf)
5. **Aiken and IBM** -- Aiken's 1937 proposal, the Automatic Sequence Controlled Calculator paper by Aiken & Hopper (1946), Eckert (1948), Sheldon & Tatum on the IBM Card-Programmed Electronic Calculator (1951) (source: The Origins of Digital Computers - Unknown.pdf)
6. **Bell Telephone Laboratories** -- Stibitz (1940), the Relay Interpolator (Cesareo, 1946), the Ballistic Computer (Juley, 1947), Alt's Bell Labs machine (1948) (source: The Origins of Digital Computers - Unknown.pdf)
7. **The Advent of Electronic Computers** -- Phillips on binary calculation (1936), Atanasoff (1940), Michie on the Bletchley machines (1972), Mauchly (1942), Goldstine & Goldstine on ENIAC (1946) (source: The Origins of Digital Computers - Unknown.pdf)
8. **Stored Program Electronic Computers** -- von Neumann's *First Draft of a Report on the EDVAC* (1945), Mauchly (1947), Burks, Goldstine & von Neumann on the IAS computer (1946), Williams & Kilburn on the Manchester Baby (1948), Wilkes & Renwick on EDSAC (1949), Worsley on the EDSAC demonstration (1949) (source: The Origins of Digital Computers - Unknown.pdf)

The volume ends with an extensive bibliography (pages 403-444) and subject index.

## Key threads

### From calculation to computation

Randell's editorial introduction emphasises that the idea of mechanised arithmetic (Schickard 1623, Pascal 1642, Leibniz 1671) was older and more widespread than the idea of a *program-controlled* machine. The decisive step was the marriage of arithmetic mechanism with sequence control (source: The Origins of Digital Computers - Unknown.pdf). Sequence control had its own deep history -- pegged cylinders in church clocks, the Jacquard loom (1804) -- but it became *computational* only when Babbage combined it with arithmetic in the [[analytical-engine]].

### The hundred-year gap

After Babbage's death in 1871 the Analytical Engine was largely forgotten. Practical computing developed instead along three more limited tracks (source: The Origins of Digital Computers - Unknown.pdf):

- **Difference engines** built by Scheutz, Wiberg, Grant, Hamann, and others
- **Commercial calculating machines** descended from the Thomas Arithmometer
- **Punched-card tabulators** invented by [[hollerith-1889|Hollerith]] for the 1890 US Census, becoming the foundation of IBM

None of these were general-purpose computers. Randell's chapters 3-6 document how piecemeal extensions of these limited machines -- adding sequence control, conditional branching, and floating-point arithmetic -- eventually produced the relay-based programmable calculators of [[harvard-mark-i|Aiken at Harvard]], Stibitz at Bell Labs, and [[zuse-z3|Zuse]] in Berlin.

### The electronic transition

The papers in chapter 7 mark the move from electromechanical relays to vacuum tubes. Atanasoff's 1940 machine at Iowa State was the first electronic digital calculating device, though it was special-purpose. The [[colossus|Colossus machines]] at Bletchley Park (1943-44) were the first large-scale electronic digital computers, but their existence remained secret until 1972 -- which is why Michie's chapter in Randell is one of the earliest published accounts. The [[eniac]] (1946) was the first general-purpose electronic computer to enter widespread public knowledge. (source: The Origins of Digital Computers - Unknown.pdf)

### The stored-program revolution

Chapter 8 contains the single most influential document in the history of computer architecture: John von Neumann's *First Draft of a Report on the EDVAC* (1945), which defines what is now called the [[von-neumann-architecture|von Neumann architecture]]. The chapter then traces how this design was realised in working machines: the [[manchester-baby|Manchester Baby]] (June 1948), [[edsac|EDSAC]] (May 1949), and the IAS computer at Princeton. By the end of 1949, the stored-program computer existed. Everything from that point forward -- including the GPUs that train and run [[transformer-architecture|Transformers]] -- is a refinement of the architecture set out in chapter 8 of this book. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance for the wiki

This single anthology supplies the connective tissue between the wiki's existing pages on logic and theory ([[turing-1936]], [[shannon-1938]]) and the modern era of electronic computing implied by [[petzold-2023]] and [[vaswani-et-al-2017]]. It is the source for the following new concept pages:

- [[stored-program-computer]]
- [[von-neumann-architecture]]
- [[eniac]]
- [[edvac]]
- [[manchester-baby]]
- [[edsac]]
- [[harvard-mark-i]]
- [[zuse-z3]]
- [[colossus]]
- [[hollerith-1889]]

## Notes

- The PDF is a 458-page Google Books scan of the 1973 softcover reprint of the hardcover first edition. It is image-only (jbig2 / jpeg) with no extractable text layer; content was read as images.
- The Babbage 1837 paper already in the wiki (entered as `babbage-1837.md`) is Chapter 2.1 of this book, reprinted from the original Buxton MS7 manuscript at the Museum of the History of Science, Oxford. The wiki had previously treated it as a standalone source; it can now also be cross-referenced as part of this collection.
- Many of the included papers are themselves translations (Torres y Quevedo from Spanish, Couffignal from French, Zuse from German, Dreyer & Walther from German) prepared specifically for this volume.

## Related pages

- [[babbage-1837]]
- [[analytical-engine]]
- [[ada-lovelace]]
- [[shannon-1938]]
- [[turing-1936]]
- [[petzold-2023]]
- [[stored-program-computer]]
- [[von-neumann-architecture]]
- [[eniac]]
- [[edvac]]
- [[manchester-baby]]
- [[edsac]]
- [[harvard-mark-i]]
- [[zuse-z3]]
- [[colossus]]
- [[hollerith-1889]]
