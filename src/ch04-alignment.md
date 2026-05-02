# Teaching Machines to Follow Intent

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-01.*

## Narrative job

Explain how raw language models became useful assistants. Show the alignment problem in its concrete form (a model that completes your question rather than answering it) and the techniques that closed the gap. End on the hinge: alignment directs capability, it does not create capability.

## Reading list

1. Russell (2019), *Human Compatible.* Alignment from a control-theory perspective by an AIMA author. Read first as the conceptual frame: the chapter's technical machinery has to do something, and Russell names what.
2. Christian (2020), *The Alignment Problem.* Layperson-accessible grounding of the alignment thesis in real ML failures (fairness, interpretability, RL). The case file that motivates the technical papers below.
3. Christiano et al. (2017), "Deep Reinforcement Learning from Human Preferences." The conceptual seed.
4. Stiennon et al. (2020), "Learning to Summarize with Human Feedback." The scale-up to language.
5. Ouyang et al. (2022), InstructGPT. The central paper.
6. Bai et al. (2022), Constitutional AI. Anthropic's alternative.
7. Askell et al. (2021), "A General Language Assistant as a Laboratory for Alignment." The HHH framing.
8. Rafailov et al. (2023), Direct Preference Optimization. The simplification that replaced PPO in practice.
9. Casper et al. (2023), "Open Problems and Fundamental Limitations of RLHF." The skeptical synthesis.

## What to watch

Developments in preference learning beyond DPO (IPO, SimPO, KTO). Work on reward model robustness. Any large study of sycophancy and reward hacking in deployed models.
