# Scaffolding and Prompting

**Summary**: Techniques for structuring interactions with AI systems to elicit better results, from simple prompt engineering to multi-step scaffolding strategies that prime the model's internal representations.

**Sources**: Early science acceleration experiments with GPT-5.pdf; Chakrabarty et al. - 2026 - Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers.pdf

**Last updated**: 2026-05-11

---

## Scaffolding as demonstrated in [[bubeck-et-al-2025]]

The most instructive example comes from Alex Lupsasca's black hole symmetry work. When asked directly to find the Lie point symmetries of the curved-space Kerr wave equation, [[gpt-5]] failed after 5 minutes and incorrectly reported no symmetries existed. But when first given the flat-space version of the same problem (which it solved correctly in 10 minutes), then asked the curved-space question again, it succeeded in 18 minutes with the correct SL(2,R) generators. (source: Bubeck et al. 2025)

The implication: the model needed to "warm up" via a simpler problem sharing the same symmetry structure. The authors suggest this reflects "retrieval or internal pattern activation" being primed by presenting a simpler member of the same class. This is a form of scaffolding that has no direct analogue in human tutoring -- it is closer to setting up the right activation patterns in a neural network. (source: Bubeck et al. 2025)

## Prompting strategies

### The "boomer prompt"
Brian Spears describes his approach to [[gpt-5]] as starting with what he calls (perhaps not affectionately) a "boomer prompt" -- a long, detailed initial specification of the entire problem, including physical regions, governing equations, boundary conditions, and desired outputs. This worked well for getting GPT-5 to set up a complete PDE model with appropriate physics. (source: Bubeck et al. 2025)

### In-context prompting for style
In [[chakrabarty-et-al-2026]], in-context prompting included 20 sample excerpts spanning an author's complete body of work, textual descriptions of the author's distinctive style, and detailed content specifications. Despite this extensive context, the resulting text was still strongly disfavored by MFA readers and easily detected as AI-generated. This establishes a ceiling for what prompting alone can achieve for style emulation -- [[fine-tuning]] was needed to cross the quality threshold. (source: Chakrabarty et al. 2026)

### Iterative correction
Multiple case studies in [[bubeck-et-al-2025]] show that the initial output is often wrong or incomplete, and the real value emerges through pushing back. Spears notes that when GPT-5 produces a pathological result and is re-prompted to examine it, the model "offered quite sophisticated solutions, including different implementations of FFTs to prevent aliasing, improved resolutions to track burn fronts, altered performance metrics to amplify signals." The key is expert confidence to reject false outputs and persist. (source: Bubeck et al. 2025)

## Scaffolding as a skill

Both papers implicitly argue that working effectively with AI is itself a learned skill -- one that requires domain expertise to practice well. The ability to design warm-ups, structure prompts, catch errors, and push back productively is not uniformly distributed. This has implications for who benefits from AI acceleration: experts with deep domain knowledge, not novices. (source: Bubeck et al. 2025)

## Related pages

- [[bubeck-et-al-2025]]
- [[chakrabarty-et-al-2026]]
- [[human-ai-collaboration]]
- [[ai-scientific-research]]
- [[gpt-5]]
