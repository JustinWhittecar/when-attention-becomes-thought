# Letter to Frege (Russell, 1902)

**Summary**: Bertrand Russell's 1902 letter to Gottlob Frege communicates the discovery of a contradiction — now known as Russell's paradox — in Frege's logical system, along with Frege's devastating reply acknowledging that the foundations of his life's work had been shaken.

**Sources**: Frege-Russell.pdf

**Last updated**: 2026-05-11

---

## Context

By 1902, Frege had published his *Begriffsschrift* (1879; see [[frege-1879]]) and the first volume of his *Grundgesetze der Arithmetik* (1893), which aimed to derive all of arithmetic from purely logical axioms. Russell, then finishing his own book on the principles of mathematics, had been studying Frege's work closely. He discovered that Frege's Basic Law V — which allows the unrestricted formation of sets from predicates — leads to a contradiction (source: Frege-Russell.pdf).

## The paradox

Russell's letter presents the paradox concisely: let w be the predicate "to be a predicate that cannot be predicated of itself." Can w be predicated of itself? If yes, then by definition it cannot. If no, then by definition it can. Either way, contradiction (source: Frege-Russell.pdf).

In set-theoretic terms: let R be the set of all sets that do not contain themselves. Is R a member of itself? If R is in R, then by definition R is not in R. If R is not in R, then by definition R is in R. This is [[russells-paradox]] (source: Frege-Russell.pdf).

Russell notes he had also communicated the paradox to Peano, "but he still owes me an answer" (source: Frege-Russell.pdf).

## Frege's reply

Frege's response (dated June 22, 1902) is remarkably honest. He acknowledges that Russell's discovery shakes "not only the foundations of my arithmetic, but also the sole possible foundations of arithmetic" — yet holds out hope that the essentials of his proofs remain intact. He admits the expression "a predicate is predicated of itself" is imprecise and reformulates the problem in terms of concepts and their extensions. He promises to address the paradox in an appendix to the forthcoming second volume of the *Grundgesetze* (source: Frege-Russell.pdf).

Frege closes by praising Russell's work: "The exact treatment of logic in fundamental questions, where symbols fail, has remained very much behind; in your works I find the best I know of our time" (source: Frege-Russell.pdf).

## The surrounding correspondence

The PDF also contains Russell's later "Letter to Russell" editorial context (dated November 22, 1902), along with Frege's letter to Russell of June 22, 1902. The exchange reveals the personal dimension of a foundational crisis: two of the greatest logicians alive grappling with the realization that naive set formation is inconsistent (source: Frege-Russell.pdf).

## Significance for the book's arc

This 5-page exchange is the hinge between two eras of logic:

- **Before**: Frege's [[frege-1879]] had created [[predicate-logic]]; his *Grundgesetze* aimed to reduce all of arithmetic to logic. The logicist dream appeared achievable.
- **After**: Russell and Whitehead spent a decade building [[whitehead-russell-1910]], which repairs the damage via the theory of types. Hilbert responded by launching his program to prove mathematics consistent ([[hilbert-ackermann-1928]]). Gödel ([[godel-1931]]) showed Hilbert's program was impossible. Turing ([[turing-1936]]) showed the decision problem was unsolvable.

The entire chain from Principia to Turing machines runs through this letter.

## Related pages

- [[russells-paradox]]
- [[frege-1879]]
- [[whitehead-russell-1910]]
- [[predicate-logic]]
- [[formal-system]]
- [[godel-1931]]
- [[hilbert-ackermann-1928]]
