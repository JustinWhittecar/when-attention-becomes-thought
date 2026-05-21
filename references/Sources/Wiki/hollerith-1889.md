# Hollerith -- An Electric Tabulating System (1889)

**Summary**: Herman Hollerith's 1889 paper describing the electric tabulating machine he had developed for the 1890 United States Census -- the first practical punched-card data-processing system and the technological foundation of the firm that became IBM.

**Sources**: The Origins of Digital Computers - Unknown.pdf

**Last updated**: 2026-05-13

---

## The problem

The 1880 US Census had taken seven years to tabulate by hand. With population growth and an increasing number of questions per person, the Census Bureau projected that the 1890 returns would still be in the process of being counted when the 1900 census began. The Bureau ran a competition in 1888 to find a faster method; Hollerith's electric tabulating machine won, and was used for the entire 1890 census, completing the basic tabulation in six weeks. (source: The Origins of Digital Computers - Unknown.pdf)

## The technology

Hollerith's system had three elements (source: The Origins of Digital Computers - Unknown.pdf):

1. **The card.** Each person's responses were encoded as a pattern of holes punched in a stiff paper card the size of an 1887 US dollar bill (later standardised as the 80-column IBM card). Different positions on the card represented age brackets, sex, race, occupation, marital status, and so on.

2. **The pantograph punch.** A clerk read the census schedule and pressed a stylus into one of dozens of holes in a guide plate; the pantograph mechanism transferred the position to a punch that perforated the card.

3. **The tabulating machine.** The card was placed under a matrix of spring-loaded pins. Where there was a hole, a pin descended through and dipped into a mercury cup, completing an electrical circuit. The circuit advanced an electromechanical counter -- one for each question of interest. A sorting machine routed cards into compartments according to which holes were punched.

The key innovation was the use of *electrical* sensing of punched holes. Earlier punched-tape and punched-card devices ([[jacquard-loom|Jacquard looms]], music-box drums) used mechanical sensing, where pins felt the surface for holes. Electrical sensing was faster, more reliable, and allowed many holes to be sensed simultaneously by a circuit matrix. (source: The Origins of Digital Computers - Unknown.pdf)

## From census to IBM

Hollerith founded the Tabulating Machine Company in 1896 to commercialise his system. The 1900 and 1910 US censuses used Hollerith equipment; so did the censuses of Russia, Austria, Norway, Canada, and several others. In 1911 the Tabulating Machine Company merged with two other firms to form the Computing-Tabulating-Recording Company; in 1924 the merged firm was renamed International Business Machines. (source: The Origins of Digital Computers - Unknown.pdf)

By the 1930s IBM was the world's dominant supplier of office computing equipment, with a global installed base of card-sorters, tabulators, accounting machines, and key-punches. This installed base is what [[harvard-mark-i|Howard Aiken]] proposed to repurpose in 1937 -- his Mark I was, in essence, an automatic sequence controller bolted onto existing IBM tabulating technology. The chain from Hollerith to Aiken to the Mark I to the postwar electronic computers is direct and largely uninterrupted. (source: The Origins of Digital Computers - Unknown.pdf)

## Significance

Hollerith's system matters for three reasons (source: The Origins of Digital Computers - Unknown.pdf):

1. **It established punched-card data processing as the dominant pre-electronic information technology.** For sixty years from 1890 to 1950, almost all large-scale data processing -- payroll, insurance, accounting, inventory, scientific tabulation -- ran on Hollerith-style equipment. The infrastructure, conventions, and clerical workforce that this created were the substrate on which the first electronic computers landed.

2. **It introduced the *card* as the fundamental unit of data.** The 80-column punched card defined the form factor of computer input and output well into the 1970s. FORTRAN was written on punched cards; the original C reference manual specifies 80-column lines because of cards.

3. **It is the institutional bridge from the 19th to the 20th century.** Hollerith's 1889 paper, [[babbage-1837|Babbage's 1837 manuscript]], and von Neumann's 1945 *First Draft* are three of the four primary documents that define the prehistory of the modern computer. (The fourth is [[turing-1936|Turing's 1936 paper]].) Without Hollerith's commercial success, IBM would not have existed; without IBM, the Mark I would not have been built; without the Mark I, the cultural conviction that an automatic calculating machine was a serious engineering project would have been much weaker.

It is also worth noting the darker side of this history: Hollerith equipment was used by the German government in the 1930s and 1940s for census and identification purposes, including population tracking that fed into the Holocaust. The use of computing technology for state surveillance and categorisation begins not in the digital era but with the 1890 census. (source: The Origins of Digital Computers - Unknown.pdf)

## Related pages

- [[harvard-mark-i]]
- [[analytical-engine]]
- [[babbage-1837]]
- [[jacquard-loom]]
- [[eniac]]
- [[randell-1973]]
