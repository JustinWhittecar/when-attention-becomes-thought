# AI Detection

**Summary**: Tools and methods for distinguishing AI-generated text from human writing, and the empirical finding that fine-tuning renders current detectors ineffective.

**Sources**: Chakrabarty et al. - 2026 - Readers Prefer Outputs of AI Trained on Copyrighted Books over Expert Human Writers.pdf

**Last updated**: 2026-05-11

---

## Detection accuracy before and after fine-tuning

The [[chakrabarty-et-al-2026]] study tested two state-of-the-art detectors -- Pangram and GPTZero -- on both in-context prompted and fine-tuned AI text.

Results at a detection threshold of 0.9:
- Human-written text: 0% false positive rate (never misclassified)
- In-context prompted AI text: 97% detected (Pangram), 91% detected (GPTZero)
- Fine-tuned AI text: 3% detected (Pangram), 0% detected (GPTZero)

[[fine-tuning]] on an author's complete works renders current detection tools essentially useless. (source: Chakrabarty et al. 2026)

## Why fine-tuning defeats detection

Mediation analysis revealed the mechanism. AI detectors largely rely on stylometric signatures -- patterns like cliche density, purple prose, and unnecessary exposition that characterize generic AI output. Fine-tuning eliminates these signatures by reshaping the model's output distribution to match a specific author's style.

Among MFA-trained readers, higher AI detection scores strongly predicted lower preference (each unit increase in detection score reduced selection odds by 6.3x for stylistic fidelity). After fine-tuning, this relationship was attenuated to near zero. The implication: the features that make text detectable as AI are the same features that make it read poorly. Remove the quality penalty, and you remove detectability. (source: Chakrabarty et al. 2026)

## Detection as quality signal

This creates a paradox for the [[copyright-and-ai]] debate: detection tools work precisely when AI text is inferior (and thus less threatening to markets), and fail precisely when AI text is competitive with human writing (and thus most threatening). The better AI gets at writing, the harder it becomes to identify. (source: Chakrabarty et al. 2026)

## Related pages

- [[chakrabarty-et-al-2026]]
- [[fine-tuning]]
- [[ai-creative-writing]]
- [[copyright-and-ai]]
