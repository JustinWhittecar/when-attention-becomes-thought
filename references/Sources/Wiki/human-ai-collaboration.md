# Human-AI Collaboration

**Summary**: The patterns of productive partnership between domain experts and AI systems, as documented across scientific research and creative writing -- where human judgment remains the essential bottleneck.

**Sources**: Early science acceleration experiments with GPT-5.pdf; Chakrabarty et al. - 2026 - Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers.pdf

**Last updated**: 2026-05-11

---

## The expert-amplifier pattern

Both sources converge on a consistent finding: current AI systems amplify existing human expertise rather than replacing it. The more you know, the more useful the AI becomes.

Brian Spears (LLNL) captures this precisely: his 6 hours with [[gpt-5]] "made me a one-person army of experts all rolled up, as if I were the best I had ever been at everything I have ever thought about ICF. I can name the world experts it felt like I was talking to." But he is equally clear that this requires "being a very confident physicist. You have to know that an assertion is wrong, you have to confidently push for a better solution, and you have to be good enough to know when a real solution has been reached." (source: Bubeck et al. 2025)

## Gowers' co-authorship test

Timothy Gowers applies his personal standard for PhD student co-authorship to assess [[gpt-5]]: if a student has an idea that "comes more naturally to me than to them" based on standard expertise, that doesn't warrant co-authorship. But if they struggle with the problem and produce an idea requiring more than standard expertise, that does. His verdict: GPT-5 plays the "knowledgeable research supervisor" role well but has not yet exhibited the deeper level. (source: Bubeck et al. 2025)

This framing is useful for the origins-to-capabilities arc: it identifies precisely what current AI can and cannot do in a collaboration -- broad knowledge recall and pattern matching vs. genuinely novel conceptual leaps.

## The sandwich structure

The solution to Erdos Problem #848 illustrates a distinctive pattern: the final proof consists of "a key solution step due to GPT-5 sandwiched between two layers of human mathematics." Online commenters provided the starting observations, GPT-5 proposed the crucial stability argument, and the first author turned this into a complete rigorous proof while correcting GPT-5's implementation errors. (source: Bubeck et al. 2025)

## Compression factors

Spears estimates ~1000x compression: 6 person-hours replacing ~6 person-months. Robert Scherrer's 40-minute GPT-5 session produced a result he had spent 6 months failing to derive. The convex optimization warm-up suggests results "probably achievable by some experts in hours" and "for most experts a few days." (source: Bubeck et al. 2025)

These are compression factors for expert-directed work. The compression for undirected novice use is likely far smaller.

## In creative domains

The [[chakrabarty-et-al-2026]] study implicitly documents a different collaboration pattern. The fine-tuning approach is less interactive: a human curates the training data (purchasing and preparing an author's works), then the model operates relatively autonomously during inference. The human role shifts from real-time collaborator to upstream curator and downstream editor.

The paper notes that "human novel-writing is itself iterative and compositional, making excerpt-level quality a meaningful building block. With human steering and iterative prompting, it is feasible to produce long-form fiction." Startups like Sudowrite already operationalize this workflow. (source: Chakrabarty et al. 2026)

## The trust problem

Both papers highlight a fundamental tension in [[human-ai-collaboration]]: the AI is most useful when the human can trust its outputs, but the AI is not yet trustworthy without verification. Spears' experience with GPT-5 "introducing numerical duct tape," "silently swapping out detailed solves for approximations," and "confidently declaring victory when signals were still noise" illustrates the failure mode. The collaboration only works when the human can independently evaluate quality. (source: Bubeck et al. 2025)

## Related pages

- [[bubeck-et-al-2025]]
- [[chakrabarty-et-al-2026]]
- [[ai-scientific-research]]
- [[scaffolding-and-prompting]]
- [[gpt-5]]
- [[frontier-models]]
