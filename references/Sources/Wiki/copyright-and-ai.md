# Copyright and AI

**Summary**: The legal questions surrounding the use of copyrighted works to train AI models, the market substitution created by AI outputs, and the emerging doctrine of "market dilution."

**Sources**: Chakrabarty et al. - 2026 - Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers.pdf

**Last updated**: 2026-05-11

---

## The core tension

Most technology companies building AI use massive datasets of books, typically without permission or licensing. In *Bartz v. Anthropic*, Judge Alsup noted that Anthropic acquired at least five million books from LibGen and two million from Pirate Library Mirror, and also cut millions of print books from their bindings, scanned them, and discarded the originals solely for training. Similar practices have triggered lawsuits against OpenAI, Meta, Microsoft, and Google. (source: Chakrabarty et al. 2026)

The legal question is whether this copying constitutes fair use when the resulting outputs do not reproduce the copied works verbatim.

## The fourth fair use factor

U.S. copyright law's fair use provision directs courts to consider four factors, but the most significant for AI training is the fourth: "the effect of the use upon the potential market for or value of the copyrighted work." Courts understand this as concerning market substitution. (source: Chakrabarty et al. 2026)

## Market dilution

The U.S. Copyright Office has recognized a theory of "market dilution": even when AI outputs are not copies of training data, the speed and scale of AI generation can flood the market and reduce sales of the source works. The Office stated: "If thousands of AI-generated romance novels are put on the market, fewer of the human-authored romance novels that the AI was trained on are likely to be sold." (source: Chakrabarty et al. 2026)

In *Kadrey v. Meta*, Judge Chhabria accepted this theory and outlined what authors must show: (1) the AI system is capable of generating substitutional books now or in the near future; (2) the AI-generated books compete in the same markets; (3) the competition displaces or diminishes demand; (4) the threat differs between a world where developers may copy the books and one where they may not. (source: Chakrabarty et al. 2026)

## Empirical evidence from [[chakrabarty-et-al-2026]]

The study provides direct empirical evidence for the first consideration: [[fine-tuning]] on individual authors' works produces outputs that readers prefer over expert human writing in blind evaluation. General readers -- the book-purchasing public -- preferred fine-tuned AI by a wide margin (writing quality OR = 5.42). The 99.7% cost reduction makes market entry trivial. (source: Chakrabarty et al. 2026)

Judge Chhabria speculated that established authors with dedicated readerships would face minimal substitution. The study's findings challenge this: fine-tuned AI emulations of distinctive voices were preferred even by MFA-trained readers, suggesting prominent authors may be just as vulnerable. (source: Chakrabarty et al. 2026)

## Fine-tuning vs. general training

A possible legal distinction: [[fine-tuning]] on individual authors' complete works should not be fair use because it specifically targets the author's market. In-context prompting from general-purpose models has a stronger fair use claim since the models serve many purposes beyond author emulation. However, even in-context models can generate author emulations, and general readers already prefer such outputs for quality. (source: Chakrabarty et al. 2026)

## Proposed remedies

- **Guardrails**: "Refusal protocols" blocking outputs when prompts request "in the style of" specific authors. Reinforcement learning to steer models away from stylistic imitation. Both remain imperfect and circumventable. (source: Chakrabarty et al. 2026)
- **Disclosure**: Conditioning fair use on prominent disclosure of AI origin. Whether disclosure diminishes AI's competitive advantage is an open question -- relative cost may sustain consumer substitution even with known provenance. (source: Chakrabarty et al. 2026)

## Related pages

- [[chakrabarty-et-al-2026]]
- [[fine-tuning]]
- [[ai-creative-writing]]
- [[ai-detection]]
