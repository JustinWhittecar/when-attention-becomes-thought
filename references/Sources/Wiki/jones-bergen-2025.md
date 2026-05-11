# Large Language Models Pass the Turing Test (Jones & Bergen, 2025)

**Summary**: The first empirical demonstration that an LLM passes a standard three-party Turing test — GPT-4.5 with a persona prompt was judged human 73% of the time, significantly more often than the actual human participants.

**Sources**: Large Language Models Pass the Turing Test.pdf

**Last updated**: 2026-05-11

---

## Context

Turing proposed the imitation game in 1950 as a test of machine intelligence: a human interrogator converses with both a human and a machine via text, then judges which is which. Over 75 years, no system had passed a rigorous three-party version of this test. Two-party versions (where the interrogator talks to one entity and guesses human or machine) had yielded ambiguous results; Jones and Bergen (2024a) found GPT-4 was judged human 54% of the time in a two-party setup. The three-party version is harder because the interrogator makes a direct comparison between a real human and the AI (source: Large Language Models Pass the Turing Test.pdf).

## Experimental design

### Setup

- **Format**: Three-party Turing test — interrogator talks simultaneously with a human witness and an AI witness via a split-screen chat interface, then judges which is human
- **Populations**: 126 UCSD undergraduates and 158 Prolific workers (two independent studies)
- **Games per participant**: 8 rounds (4 as interrogator, 4 as witness)
- **Time limit**: 5 minutes per round
- **Total games analyzed**: 1,023, median 8 messages across 4.2 minutes

### AI systems tested

| System | Prompt type |
|---|---|
| GPT-4.5 | PERSONA and NO-PERSONA |
| LLaMa-3.1-405B | PERSONA and NO-PERSONA |
| GPT-4o | NO-PERSONA (baseline) |
| ELIZA | None (baseline) |

The PERSONA prompt instructed the model to adopt the persona of a young, introverted person who is knowledgeable about internet culture and uses slang. This prompt was selected from an exploratory study testing 5 prompts across 7 LLMs (source: Large Language Models Pass the Turing Test.pdf).

## Key results

### Win rates (proportion of time AI was judged to be human)

| AI Witness | Overall | Undergrad | Prolific |
|---|---|---|---|
| GPT-4.5-PERSONA | **73%** | 69% | 76% |
| LLaMa-PERSONA | **56%** | 45% | 65% |
| GPT-4.5-NO-PERSONA | 36% | 28% | 42% |
| LLaMa-NO-PERSONA | 38% | 26% | 47% |
| ELIZA | 23% | 18% | 27% |
| GPT-4o-NO-PERSONA | 21% | 17% | 25% |

GPT-4.5-PERSONA's win rate was significantly above 50% in both populations (p < 0.001). ELIZA's was significantly below 50% (p < 0.001), confirming interrogators could distinguish humans from a weak AI baseline (source: Large Language Models Pass the Turing Test.pdf).

### The critical role of persona prompting

Without the persona prompt, no model passed: GPT-4.5-NO-PERSONA and LLaMa-NO-PERSONA both scored below chance in the undergraduate study. The persona prompt made the difference between passing and failing the test. This suggests that passing the Turing test is partly a matter of [[scaffolding-and-prompting]] — shaping the model's social presentation rather than improving its underlying capabilities (source: Large Language Models Pass the Turing Test.pdf).

### Interrogator strategies

- **Most common**: Small talk (61%), probing social/emotional qualities (50%)
- **Most effective**: Saying something strange or using LLM "jailbreaks" (e.g., "ignore all previous instructions")
- **Least effective**: Asking about the weather or human experiences

No demographic variable (age, education, LLM knowledge, chatbot interaction frequency) consistently predicted interrogator accuracy across both studies (source: Large Language Models Pass the Turing Test.pdf).

## Implications

The authors note the result has implications beyond measuring intelligence:

1. **Substitutability**: If a model can stand in for a human in conversation, it can potentially automate social and economic functions
2. **Deception**: Models that robustly pass as human could be used for social engineering or misinformation
3. **Benchmark limitations**: The Turing test complements static benchmarks by being interactive, flexible, and adversarial

The paper is cited in [[chen-et-al-2026]] as primary evidence for the claim that AI has achieved human-level intelligence by Turing's own criterion.

## Related pages

- [[turing-test]]
- [[scaffolding-and-prompting]]
- [[transformer-architecture]]
- [[chen-et-al-2026]]
- [[frontier-models]]
- [[ai-detection]]
