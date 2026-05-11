# Chakrabarty et al. (2026) -- Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers

**Summary**: A preregistered study comparing MFA-trained expert writers with three [[frontier-models]] (ChatGPT, Claude, Gemini) on style emulation of 50 award-winning authors. Fine-tuning on an author's complete works reverses expert reader preferences in favor of AI.

**Sources**: Chakrabarty et al. - 2026 - Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers.pdf

**Last updated**: 2026-05-11

---

## Study design

The experiment compared human MFA-trained writers against AI systems on a controlled task: write an excerpt of up to 450 words emulating the style and voice of a specific author. 50 internationally acclaimed authors were selected, including Nobel laureates (Han Kang, Annie Ernaux), Booker Prize winners (Salman Rushdie, Margaret Atwood, George Saunders), and Pulitzer Prize winners (Junot Diaz, Marilynne Robinson). (source: Chakrabarty et al. 2026)

Two AI conditions were tested:

1. **In-context prompting**: Models received the same writing prompt as human experts, including 20 sample excerpts from the target author, style descriptions, and content specifications.
2. **[[fine-tuning]]**: GPT-4o was additionally trained on each of 30 living authors' complete works, segmented into 250-650 word excerpts with content descriptions.

Evaluators included 28 MFA-trained readers from elite U.S. writing programs and 516 college-educated general readers recruited via Prolific. All evaluations were blind pairwise comparisons on two dimensions: stylistic fidelity and writing quality. (source: Chakrabarty et al. 2026)

## Key results

### In-context prompting

MFA-trained readers strongly preferred human writing:
- Stylistic fidelity: OR = 0.16 (six-fold preference for human)
- Writing quality: OR = 0.13 (eight-fold preference for human)

College-educated general readers diverged:
- Stylistic fidelity: OR = 1.06 (no significant preference)
- Writing quality: OR = 1.82 (significant preference *for* AI)

This split between expert and general readers is itself a significant finding. General readers -- who more closely represent the book-purchasing public -- already favored AI output even without [[fine-tuning]]. (source: Chakrabarty et al. 2026)

### Fine-tuning

Fine-tuning on an individual author's complete works reversed MFA reader preferences:
- Stylistic fidelity: OR = 8.16 (MFA readers now preferred AI)
- Writing quality: OR = 1.87 (MFA readers now preferred AI)

College-educated general readers showed even larger shifts:
- Stylistic fidelity: OR = 16.65
- Writing quality: OR = 5.42

Of 30 fine-tuned author models, 29 exceeded parity for stylistic fidelity (median win rate = 0.83) and 28 for writing quality (median = 0.67). Performance showed no systematic relationship with fine-tuning corpus size. (source: Chakrabarty et al. 2026)

## [[ai-detection]] collapse

State-of-the-art detectors (Pangram, GPTZero) correctly classified 97% of in-context prompted text as AI-generated but only 3% of fine-tuned text. Human-written text was never misclassified. (source: Chakrabarty et al. 2026)

Mediation analysis revealed the mechanism: [[fine-tuning]] eliminates detectable AI stylistic quirks -- particularly cliche density -- that both trigger detectors and penalize reader preferences. The relationship between detectability and preference is causal, not incidental: removing the "AI smell" removes the quality penalty. (source: Chakrabarty et al. 2026)

## Economics

Total AI generation costs (fine-tuning plus inference) ranged from $25 to $276 per author (median = $81). This represents approximately 0.3% of what MFA-trained writers would charge for a novel-length manuscript. The paper is careful to note this reflects raw generation costs only, not the human steering and editing required for publishable work. (source: Chakrabarty et al. 2026)

## [[copyright-and-ai]] implications

The paper argues these findings bear directly on the fourth fair use factor: "the effect of the use upon the potential market for or value of the copyrighted work."

Key legal arguments:
- The U.S. Copyright Office recognizes that "predicate copying" (copying books to train models) may cause market harm through competing works, even when outputs do not reproduce the copied works verbatim.
- Judge Chhabria in *Kadrey v. Meta* accepted the theory of "market dilution" -- AI-generated novels substituting for human-authored ones -- and provided a roadmap for what authors would need to show.
- The paper argues fine-tuning on individual authors' works should not qualify as fair use, since it targets particular authors and creates direct market substitutes.
- In-context prompting has a stronger fair use claim since general-purpose models serve many uses beyond author emulation.

The paper was independently corroborated by a New York Times blind quiz (86,000+ readers, 54% preferred AI text) and New Yorker reporting where accomplished novelists struggled to distinguish fine-tuned AI from human writing. (source: Chakrabarty et al. 2026)

## Significance for the origins-to-capabilities arc

This paper marks a concrete empirical threshold: the point at which AI systems, when given access to an author's body of work, produce writing that trained literary experts prefer to human expert writing in blind evaluation. It connects the trajectory from early language models to systems capable of economically threatening creative professions -- with the legal system still catching up.

## Related pages

- [[fine-tuning]]
- [[ai-creative-writing]]
- [[copyright-and-ai]]
- [[ai-detection]]
- [[frontier-models]]
