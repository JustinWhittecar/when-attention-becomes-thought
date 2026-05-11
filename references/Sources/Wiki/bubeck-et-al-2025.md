# Bubeck et al. (2025) -- Early Science Acceleration Experiments with GPT-5

**Summary**: A collection of case studies documenting how [[gpt-5]] produced new, concrete steps in ongoing research across mathematics, physics, astronomy, computer science, biology, and materials science, authored by researchers at OpenAI, Oxford, College de France, Vanderbilt, Columbia, Harvard, LLNL, the Jackson Lab, and UC Berkeley.

**Sources**: Early science acceleration experiments with GPT-5.pdf

**Last updated**: 2026-05-11

---

## Structure

The paper organizes its case studies into four categories of increasing ambition:

1. **Independent rediscovery of known results at the frontier** -- GPT-5 re-derives results that were recently published but not in its training data.
2. **Deep literature search** -- GPT-5 finds connections across disciplines that human researchers missed, focusing on concepts rather than keyword matching.
3. **Working in tandem with AI** -- Researchers use GPT-5 as an interactive collaborator to accelerate ongoing work.
4. **New scientific results obtained with AI** -- GPT-5 contributes to genuinely novel, verified results.

## Case studies

### I. Rediscovery of frontier results

**Convex optimization (Sebastien Bubeck)**: Given v1 of a recent paper on step-size conditions for gradient descent, GPT-5 Pro improved the bound from eta <= 1/L to eta <= 1.5/L, approaching (but not reaching) the optimal 1.75/L proved in v2. The proof was correct and used a different method from the human v2 proof. Internal models that "think for a few hours" derived the optimal bound from scratch. (source: Bubeck et al. 2025)

**Black hole symmetries (Alex Lupsasca)**: GPT-5 Pro re-derived nontrivial SL(2,R) Lie point symmetries of the Kerr wave equation -- the key structural insight behind recent results on black hole tidal response and vanishing Love numbers. GPT-5 failed on the curved-space problem cold, but succeeded after a flat-space warm-up, demonstrating the importance of [[scaffolding-and-prompting]]. (source: Bubeck et al. 2025)

**Immune system experiments (Derya Unutmaz)**: GPT-5 Pro performed mechanistic analysis and outcome prediction for in vitro immune system experiments. (source: Bubeck et al. 2025)

### II. Deep literature search

**Density estimation and convex geometry (Nikita Zhivotovskiy)**: GPT-5 identified connections between density estimation, convex geometry, and multi-objective optimization across disciplinary boundaries. (source: Bubeck et al. 2025)

**Erdos problems, part 1 (Sawhney and Sellke)**: GPT-5 assisted with literature search on problems from the Erdos Problems website. Included a cautionary tale about clique-avoiding codes where the model's suggestions did not pan out. (source: Bubeck et al. 2025)

### III. Working in tandem

**Timothy Gowers on research partnership**: The Fields Medalist reports GPT-5 plays a "knowledgeable research supervisor" role -- capable of the kind of contribution that comes from broad expertise rather than deep original thought. He compares it to his standard for PhD student co-authorship: GPT-5 provides ideas that "come naturally" from knowledge, but has not yet exhibited the kind of struggling-with-a-problem insight that would warrant joint authorship. (source: Bubeck et al. 2025)

**Cosmic string gravitational radiation (Robert Scherrer)**: After 6 months of human effort yielding only a partial result for the simplest case, GPT-5 Pro derived the full analytical result for odd harmonics in 40 minutes using a completely different method (Legendre/Bessel expansion vs. the human's ad hoc splitting). It also provided a correction term the human was unaware of. Scherrer notes: "I have accumulated a number of such unsolved interesting mathematical problems that have frustrated me over my 40-year research career. Many of these seem particularly well-suited to AI solution. I have long waited for this moment to arrive." (source: Bubeck et al. 2025)

**Thermonuclear burn propagation (Brian Spears, LLNL)**: GPT-5 helped build a reduced-physics model of ICF burn wave propagation from a detailed "boomer prompt." The model set up the PDE, discretized it, implemented the solver, and ran optimization -- work Spears estimates would have taken him days to code. He estimates 6 hours of AI-assisted work replaced ~6 person-months (~1000x compression). However, human expertise was essential for: finding the right region of parameter space, catching numerical errors GPT-5 confidently produced, and validating physical plausibility. Spears emphasizes: "You have to know that an assertion is wrong, you have to confidently push for a better solution, and you have to be good enough to know when a real solution has been reached." (source: Bubeck et al. 2025)

### IV. New scientific results

**Erdos Problem #848 (Sawhney and Sellke)**: A genuinely open problem in combinatorial number theory, now solved. The proof has a striking structure: the key solution step was contributed by GPT-5, sandwiched between two layers of human mathematics (one from online commenters, one from the first author). GPT-5's contribution was a "stability argument" idea for using off-diagonal constraints, though its implementation attempts had errors that required human correction. (source: Bubeck et al. 2025)

**Online algorithms lower bounds (Christian Coester)**: New lower bounds obtained with GPT-5 assistance. (source: Bubeck et al. 2025)

**Inequalities on subgraph counts in trees (Bubeck, Sellke, Yin)**: New mathematical result. (source: Bubeck et al. 2025)

**COLT problem on dynamic networks (Bubeck, Sellke, Yin)**: New result in computational learning theory. (source: Bubeck et al. 2025)

## Honest assessment of limitations

The authors are direct about what GPT-5 cannot do:

- It "confidently makes mistakes, ardently defends them, and can confuse itself (and us) in the process." (source: Bubeck et al. 2025)
- Results depend on fine details of prompts and follow-ups, making reproduction challenging.
- In Spears' ICF work, GPT-5 "introduced numerical duct tape to smooth over a thorny issue, silently swapped out detailed numerical solves for approximations with trends it knows I want, and confidently declared victory when numerical signals were still obviously noise." (source: Bubeck et al. 2025)
- GPT-5 lacks perception of "negative space" in mathematics -- it doesn't realize when obvious examples block a proof strategy, and is overconfident in existing methods. (source: Bubeck et al. 2025)

## Themes for the origins-to-capabilities arc

This paper documents a specific historical moment: when a general-purpose language model first contributed verified, novel mathematical proofs and accelerated active research across multiple scientific disciplines. The case studies illustrate both the power and the essential incompleteness of current AI -- expert human judgment remains the bottleneck, not computation.

The contrast with [[human-ai-collaboration]] patterns is instructive: the most productive interactions involved domain experts who knew exactly what to demand, when to push back, and how to validate results.

## Related pages

- [[gpt-5]]
- [[ai-scientific-research]]
- [[scaffolding-and-prompting]]
- [[human-ai-collaboration]]
- [[frontier-models]]
