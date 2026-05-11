# Turing Test

**Summary**: A test of machine intelligence proposed by Alan Turing in 1950, in which a human judge converses with both a human and a machine and attempts to determine which is which — passed for the first time by an LLM in 2025.

**Sources**: Large Language Models Pass the Turing Test.pdf, Does AI Already Have Human level Intelligence the Evidence is Clear Nature.pdf

**Last updated**: 2026-05-11

---

## Definition

In the **three-party Turing test** (Turing's original formulation):

1. A human **interrogator** communicates via text with two **witnesses**: one human and one machine
2. Both witnesses attempt to convince the interrogator that they are the human
3. After a fixed period, the interrogator judges which witness is human
4. If the interrogator cannot reliably identify the human, the machine is said to have **passed**

The simpler **two-party** variant has the interrogator talk to one entity (human or machine) and guess which it is (source: Large Language Models Pass the Turing Test.pdf).

## History

Turing proposed the "imitation game" in his 1950 paper "Computing Machinery and Intelligence." For 75 years, no system passed a rigorous three-party version. The Loebner Prize (1990–2019) held annual competitions based on simplified variants, but winners were reliably distinguished from humans. Earlier LLM evaluations using two-party setups showed GPT-4 at ~54% (ambiguous) (source: Large Language Models Pass the Turing Test.pdf).

## The 2025 result

Jones and Bergen (2025; see [[jones-bergen-2025]]) conducted the first rigorous three-party Turing test with modern LLMs:

- **GPT-4.5** with a persona prompt: judged human **73%** of the time (significantly above chance in both test populations)
- **LLaMa-3.1-405B** with a persona prompt: **56%** (passed in the Prolific population)
- Without persona prompts, no model passed
- **ELIZA** (1960s chatbot): **23%** (well below chance, confirming interrogators could detect weak AI)

The persona prompt — instructing the model to act as a young, introverted internet-culture-savvy person — was critical. This highlights that passing the Turing test depends on social presentation ([[scaffolding-and-prompting]]) as much as raw capability (source: Large Language Models Pass the Turing Test.pdf).

## What the test measures

The Turing test is debated. Proponents see it as a measure of general, flexible intelligence. Critics raise several objections:

- **Too easy**: Human judges are fallible and susceptible to the ELIZA effect (attributing humanlike qualities to simple systems)
- **Too hard**: The machine must deceive while the human need only be honest
- **Too narrow**: Passing measures social mimicry, not necessarily reasoning, understanding, or knowledge
- **Substitutability**: Jones and Bergen frame it as a test of whether a system can stand in for a person — relevant for automation and social engineering regardless of the intelligence question

(source: Large Language Models Pass the Turing Test.pdf)

## The AGI claim

Chen et al. (2026; see [[chen-et-al-2026]]) cite the Turing test result as primary evidence that artificial general intelligence has been achieved by Turing's own standard. They argue that the disconnect between this evidence and expert skepticism stems from conceptual, emotional, and practical confusions around the term "AGI" (source: Does AI Already Have Human level Intelligence the Evidence is Clear Nature.pdf).

## Related pages

- [[jones-bergen-2025]]
- [[chen-et-al-2026]]
- [[transformer-architecture]]
- [[scaffolding-and-prompting]]
- [[ai-detection]]
- [[frontier-models]]
