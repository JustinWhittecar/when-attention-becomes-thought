# Jacquard loom

**Summary**: Joseph-Marie Jacquard's 1804 silk-weaving loom controlled by a chain of punched cards -- the first widely-deployed machine to take its sequence of operations from an external, removable, programmable medium, and the technological ancestor of every punched-card computer that followed.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-13

---

## Origin

The idea of using a perforated medium to control a weaving loom predates Jacquard. Randell's editorial introduction (Chapter I of [[randell-1973]]) traces the lineage (source: The Origins of Digital Computers - Unknown.pdf):

- **Basile Bouchon** (1725) used a perforated paper tape to control the warp threads of a draw loom, reducing the weaver's assistant's job to pressing the tape against a row of needles.
- **Jean-Baptiste Falcon** (~1728) extended Bouchon's scheme by introducing several rows of needles and replacing the continuous tape with a chain of strung-together perforated cards -- 400 or more cords could now be controlled.
- **Jacques de Vaucanson** (~1750) automated the loom further with a perforated cylinder, eliminating the operator -- but also reverted to a fixed medium, losing the unbounded program length that Falcon's card chain had provided.
- **Joseph-Marie Jacquard** (1804), assisted by Breton, returned to Falcon's card chain on top of Vaucanson's automation, producing the first commercially successful automatic loom.

By the 1830s thousands of Jacquard looms were in use across France and beyond. The combination of *unbounded program length* (a card chain can be extended indefinitely) and *full automation* (no operator needed once the chain is in place) is what made Jacquard's design the right model for general-purpose machine control.

## How it works

The Jacquard loom replaces the human "drawboy" -- the assistant who pulled cords to lift selected warp threads on each pass of the shuttle -- with a mechanism (source: The Origins of Digital Computers - Unknown.pdf):

1. A chain of stiff punched cards passes over a rectangular prism, one card per shuttle pass.
2. Each card presses against a grid of horizontal needles. Where the card has a hole, a needle passes through; where there is no hole, the needle is blocked.
3. Each needle controls a hook attached to one warp thread. Needles that pass through the card lift their hooks; needles that are blocked do not.
4. The shuttle then passes weft thread across the loom, going *over* the lifted warps and *under* the un-lifted ones, weaving the pattern encoded on the card.

A complex figured fabric -- like the silk portrait of Jacquard himself that Babbage owned and showed to visitors -- might be controlled by 24,000 cards or more.

## Why it matters for computing

The Jacquard loom is the direct ancestor of three different computing traditions (source: The Origins of Digital Computers - Unknown.pdf):

### 1. Babbage's Analytical Engine (1836-1871)

Babbage adopted Jacquard cards as the program-control mechanism for the [[analytical-engine|Analytical Engine]] in June 1836, abandoning his earlier "central barrel" scheme. He gave several reasons (preserved in his 1837 manuscript, see [[babbage-1837]]):

- Cards are easier to punch than to peg.
- Once a formula has been encoded on cards, the cards can be reused indefinitely.
- The card chain can be extended without limit, so program length is bounded only by the operator's patience.
- The cards become a permanent record of every formula run on the machine.

[[ada-lovelace|Ada Lovelace]] put it most famously in her Note A: "We may say most aptly that the Analytical Engine *weaves algebraical patterns* just as the Jacquard-loom weaves flowers and leaves." (source: A_Lovelace_offprints_IEEE_plus_postscript.pdf)

### 2. Hollerith's tabulator (1889)

Herman Hollerith adopted punched cards for his census-tabulation system ([[hollerith-1889]]), but with two crucial changes from Jacquard's design: he made cards *discrete units* (one card per person, rather than a continuous chain) and he sensed them *electrically* (a hole completes a circuit through a mercury cup) rather than mechanically. The Hollerith card became the founding technology of IBM and the dominant unit of 20th-century data processing.

### 3. The relay and electromechanical computers (1936-1944)

The programmable relay computers of the 1940s -- [[zuse-z3|Zuse's Z3]] (punched film), [[harvard-mark-i|Aiken's Mark I]] (punched paper tape), the Bell Labs relay computers -- all inherit Jacquard's basic pattern: program externally on a perforated medium, feed sequentially through the machine. The first machines to break with this pattern are the [[stored-program-computer|stored-program]] computers of 1948-1949, which finally bring the program inside the same electronic memory as the data.

## Significance

For 144 years, from Jacquard's 1804 loom to the [[manchester-baby|Manchester Baby's]] 1948 run, programs were physical: holes punched in cards, tape, or film. The whole vocabulary of "running a program," "loading a deck," "reading the next instruction" comes from this physical era. Even though modern computers store programs as electronic bit patterns in RAM, the conceptual model -- a sequence of discrete instructions read one after another -- is directly inherited from the Jacquard chain.

The cultural transmission is also direct: Babbage owned a woven silk portrait of Jacquard, Hollerith almost certainly knew of the Italian Bonelli/Bolmida/Vicenzia experiments with electrical Jacquard mechanisms in the 1850s, and the first IBM punched cards were sized to the dimensions Hollerith chose in 1889 -- which IBM then standardised as the 80-column card that defined computing into the 1970s. (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[analytical-engine]]
- [[babbage-1837]]
- [[ada-lovelace]]
- [[lovelace-1843]]
- [[hollerith-1889]]
- [[harvard-mark-i]]
- [[zuse-z3]]
- [[bell-labs-relay-computers]]
- [[stored-program-computer]]
- [[randell-1973]]
