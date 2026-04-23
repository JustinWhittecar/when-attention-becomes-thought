# "When Attention Becomes Thought": A Reading-First Finishing Plan

*Written 2026-04-22. Replaces the previous plan.*

## The shape of the work

You have Sections 1 and 2 in your own voice. Everything from Section 3 on is research scaffolding you are going to replace. That reframes the project. You are not editing a draft. You are writing a book, one chapter at a time, in the tradition of Nystrom's *Crafting Interpreters* and Knuth's *Art of Computer Programming*: read the primary sources, internalize them, then teach them.

This plan is built around that. It is a reading program first, a writing program second, and a publishing program third.

Six things shape every decision below:

1. You are writing for a general reader. Not a researcher. Not a layperson either. Assume someone curious, smart, willing to be taught, not willing to be condescended to.
2. Your influences are pedagogical. *Crafting Interpreters* earns its voice because Nystrom built everything he describes. *TAOCP* earns its authority by citing every source it stands on. You want both.
3. You are writing to last. This is a living document. Structure it so a 2027 update is a pull request, not a rewrite.
4. You work in 1-2 hour sessions. The plan honors that. No session should require keeping state across nights.
5. You want credibility. That means primary sources, not summaries. When you cite Vaswani et al., you have read Vaswani et al.
6. You hate em dashes. I will not use them.

## The workflow, in one paragraph

For each section, you will do three kinds of nights: **reading nights** (one paper per hour, with notes), **synthesis nights** (connect the papers you read, write an outline for the section), and **writing nights** (draft the section in one sitting, no research). Typically: four reading nights, one synthesis night, two writing nights, one revision night per section. Eight sessions per section, roughly. Eight sections left. Call it 64 sessions, or about three to four months at five sessions a week. That is the honest timeline.

## The note-taking method

Open a single markdown file per section, in a `notes/` folder next to the manuscript. Call it `section-03-scaling.md`, `section-04-alignment.md`, and so on. For each paper you read, add an entry with this structure:

```
## Vaswani et al. (2017) — Attention Is All You Need

**One-sentence thesis.** [In your own words. If you cannot write this, you did not understand the paper.]

**What it argues.** [2-3 sentences. The argument, not the abstract.]

**The evidence.** [What experiments, what data, what numbers. Specific.]

**Pull quotes.** [2-5 verbatim lines you might use in the book. Always with page number.]

**Connections.** [What this paper depends on; what it makes possible. One sentence each.]

**What confused me / what I want to verify.** [Open questions. These become sidebars.]

**Teaching angle.** [If I were explaining this to someone at dinner, what would I say?]
```

That last field is the secret. It is where your voice lives. A general reader does not need the paper's abstract. They need the dinner-table version.

A good synthesis night is when you read all seven or eight entries for a section, look for the throughline, and write the outline. If the throughline does not appear, you need to read one more paper or re-read the one you were laziest on.

---

## Section-by-section reading plan

For each section: what to read, in what order, what to watch for, and what the section's narrative job is.

### Section 3: The Scaling Era

**Narrative job.** Show that after 2017, the dominant lesson was not a new architecture but a new relationship between scale and capability. End on the "emergence" claim and the controversy around it so Section 5 has somewhere to go.

**Read in this order:**

1. **Radford et al. (2018), "Improving Language Understanding by Generative Pre-Training"** (GPT-1 paper). Short. Establishes the pretraining paradigm.
2. **Devlin et al. (2019), "BERT"**. The other fork in the road. Contrast BERT's bidirectional masking with GPT's autoregressive objective.
3. **Radford et al. (2019), "Language Models are Unsupervised Multitask Learners"** (GPT-2). Specifically read the first three sections. This is where "zero-shot" as a concept enters the frame.
4. **Raffel et al. (2020), "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"** (T5). You can skim the experiments. The contribution you care about is the framing: every task as text to text.
5. **Brown et al. (2020), "Language Models are Few-Shot Learners"** (GPT-3). The central paper of this section. Read it carefully. Pay attention to Section 3 (few-shot learning) and the discussion of what changes at scale.
6. **Kaplan et al. (2020), "Scaling Laws for Neural Language Models"**. Focus on the log-linear claim and what quantities it relates.
7. **Hoffmann et al. (2022), "Training Compute-Optimal Large Language Models"** (Chinchilla). Read the correction to Kaplan.
8. **Wei et al. (2022), "Emergent Abilities of Large Language Models"**. The qualitative claim.
9. **Schaeffer, Miranda & Koyejo (2023), "Are Emergent Abilities of Large Language Models a Mirage?"** NeurIPS 2023 best paper. The skeptical counter. Read this. It sharpens your treatment of "emergence" enormously.

**What to watch for across these.** The shift from task-specific fine-tuning to general pretraining. Why decoder-only won for generation even though encoder-decoder was arguably more elegant. What "scaling law" precisely means (and what it does not mean). What the word "emergent" is doing and who disagrees. The first evidence of in-context learning, which will matter for every later section.

**Narrative arc of the section.** Architecture gave us a substrate; scale gave us a surprise. Emergence is real, contested, and sets up every later chapter. Do not resolve the emergence debate. Plant it.

### Section 4: Alignment and Post-Training

**Narrative job.** Explain how raw language models became useful assistants. Show the alignment problem in its concrete form (a model that completes your question rather than answering it) and the series of techniques that closed the gap. End by noting: alignment directs capability, it does not create capability. That is the hinge into reasoning.

**Read in this order:**

1. **Christiano et al. (2017), "Deep Reinforcement Learning from Human Preferences"**. The conceptual seed. Pre-language-model. Read it because the framework is cleaner than the later language-model version.
2. **Stiennon et al. (2020), "Learning to Summarize with Human Feedback"**. The scale-up to language. Short.
3. **Ouyang et al. (2022), "Training Language Models to Follow Instructions with Human Feedback"** (InstructGPT). The central paper.
4. **Bai et al. (2022), "Constitutional AI: Harmlessness from AI Feedback"**. Anthropic's alternative. Read it in full, it is load-bearing.
5. **Askell et al. (2021), "A General Language Assistant as a Laboratory for Alignment"**. The HHH (helpful, harmless, honest) framing. Short, influential.
6. **Rafailov et al. (2023), "Direct Preference Optimization"**. The simplification that quietly replaced PPO at many labs. Important because it tells you the field is still iterating.
7. **Casper et al. (2023), "Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback"**. The skeptical synthesis. Read this to avoid writing a triumphalist chapter.

**What to watch for.** The three-stage pipeline (SFT, reward model, PPO) and why each step exists. The alignment tax: does post-training make models dumber? What "helpful, harmless, honest" actually operationalizes. Why CAI mattered (human labor, scalability, transparency of principles). Why DPO displaced PPO in practice. The open problems Casper names: reward hacking, sycophancy, limits of human raters.

**Narrative arc.** The pretrained model is a savant with no social skills. Alignment is the finishing school. But the finishing school cannot teach what the savant does not know, and that is where Section 5 has to go.

### Section 5: The Reasoning Revolution

**Narrative job.** Make the case that something qualitatively new happened between late 2024 and 2025 with reasoning-trained models, while fairly representing the live debate about whether that something is new capability or more efficient sampling from existing capability.

**Read in this order:**

1. **Wei et al. (2022), "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"**. The seed.
2. **Kojima et al. (2022), "Large Language Models are Zero-Shot Reasoners"**. The "Let's think step by step" paper.
3. **Wang et al. (2022), "Self-Consistency Improves Chain of Thought Reasoning"**.
4. **Yao et al. (2023), "Tree of Thoughts"**.
5. **OpenAI (2024), o1 system card and "Learning to Reason with LLMs" blog post**. Both together. The product reveal.
6. **OpenAI (2025), o3/o4-mini system card**. For the scaling evidence and tool integration.
7. **Shao et al. (2024), "DeepSeekMath: Pushing the Limits of Mathematical Reasoning"**. The GRPO paper. Read the algorithm section carefully.
8. **DeepSeek-AI (2025), "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"**. The central paper of this section. Spend extra time on the R1-Zero section and the "aha moment" discussion.
9. **Guo et al. (2025), DeepSeek-R1 in Nature**. Read for the peer-reviewed articulation.
10. **Wen et al. (2025), "Reinforcement Learning for Reasoning in Large Language Models with One Training Example"** or whichever CoT-Pass@K paper is current. The paper that answers "does RL expand the reasoning frontier?"
11. **Kumar et al. (2024), "Training Language Models to Self-Correct via Reinforcement Learning"**. A good complementary read for the self-correction angle.

**What to watch for.** The distinction between inference-time techniques (CoT, self-consistency, ToT) and training-time techniques (RLVR). What RLVR optimizes that RLHF does not. The compute-at-inference shift: more thinking time yields better answers. The R1-Zero result and why it is philosophically load-bearing (self-verification emerging from pure RL). The CoT-Pass@K metric and why it matters to skeptics.

**Narrative arc.** Prompting techniques showed the latent ability was there. RL training pulled it out reliably. The field's best attempt at a skeptical counter (RL just compresses sampling) has been answered, at least partially, by CoT-Pass@K. Thinking longer makes models better, and that is not a trivial observation.

### Section 6: Mechanistic Interpretability

**Narrative job.** Turn the empirical case into a structural one. If we want to know whether the reasoning in Section 5 is "real," we look inside. Show what the tools can see, what they find, and what they cannot yet see.

**Read in this order:**

1. **Olah et al. (2020), "Zoom In: An Introduction to Circuits"**. The foundational framework. Read this even though it is about vision models. It sets the conceptual vocabulary (features, circuits).
2. **Elhage et al. (2021), "A Mathematical Framework for Transformer Circuits"**. Dense. Work through Sections 1-3 carefully. Skip the one-layer-model details if you are pressed for time; the big ideas are attention heads as computational units and induction heads.
3. **Elhage et al. (2022), "Toy Models of Superposition"**. Read this. The superposition hypothesis is the reason interpretability is hard.
4. **Bricken et al. (2023), "Towards Monosemanticity"**. The sparse autoencoder breakthrough. Read the feature case studies (Arabic, DNA, base64) for the voice as much as the result.
5. **Templeton et al. (2024), "Scaling Monosemanticity"**. The Claude 3 Sonnet features, including the famous Golden Gate Bridge feature.
6. **Ameisen, Lindsey et al. (2025), "Circuit Tracing: Revealing Computational Graphs in Language Models"**. The methodology paper.
7. **Lindsey et al. (2025), "On the Biology of a Large Language Model"**. The findings paper. Spend time on the specific case studies: multi-hop reasoning, poetry planning, medical diagnosis. These are the passages that carry the argumentative weight.
8. **Nanda et al. (2023), "Progress Measures for Grokking via Mechanistic Interpretability"**. A complementary read. Interpretability applied to training dynamics rather than inference.

**What to watch for.** The progression: neurons are the wrong unit, features are the right unit, circuits are how features interact. What superposition actually claims. How SAEs work conceptually. The specific findings in "Biology of an LLM": what exactly was observed when the model generated "Austin" for "what is the capital of the state containing Dallas," what exactly was observed in the poetry case. These are the passages where your general reader will lean in.

**Narrative arc.** We used to treat LLMs as black boxes because we did not have tools. We have tools now. What they see inside is structured computation, not shallow pattern matching. The tools are still partial (Anthropic estimates ~25% coverage) and that is honest. But the direction of the evidence is unambiguous.

### Section 7: From Reasoning to Agency

**Narrative job.** Show the transition from a system that generates text to a system that takes action. Give a general reader enough to understand why this is a regime change, not a UX change. End on where the frontier actually is (long-horizon tasks under economic pressure).

**Read in this order:**

1. **Yao et al. (2022), "ReAct: Synergizing Reasoning and Acting in Language Models"**. The pattern that made everything else possible.
2. **Shinn et al. (2023), "Reflexion: Language Agents with Verbal Reinforcement Learning"**. Self-improvement via reflection.
3. **Anthropic (2024), "Introducing the Model Context Protocol"** blog post, plus the MCP specification. Read the spec. Short and clarifying.
4. **Google (2025), Agent-to-Agent Protocol (A2A) announcement and spec**.
5. **Zechner, M. (2025), "Build Your Own Minimal Coding Agent"** blog post. This is load-bearing for your narrative because the four-tools-and-a-short-prompt claim matters to the argument.
6. **The OpenClaw README or the blog post that went with its release**. For the behavioral evidence.
7. **METR (2025), task horizon report**. The doubling-every-seven-months claim. Read the methodology appendix.
8. **HKUDS, ClawWork paper (2026)**. For the economic-pressure evaluation methodology.
9. **The agentic AI survey, arXiv:2510.25445**. For a taxonomy and the model-native paradigm.
10. **Jimenez et al. (2024), "SWE-bench"**. Because software engineering is the clearest domain where agents have moved from demos to production utility.

**What to watch for.** The two moves in an agent: tool use and planning. Why protocols (MCP, A2A) matter for this field specifically (combinatorial integration problem). Why Pi's minimalism is a thesis about what frontier models already know. What the METR time-horizon metric actually measures and what its projection assumes.

**Narrative arc.** Reasoning was the unlock. Tools were the amplifier. Protocols were the standardization. The evidence is not yet as mature as Section 6 but the trajectory is clear.

### Section 8: The AGI Question

**Narrative job.** This is the section readers came for. Treat the Chen et al. commentary as one input among several rather than the load-bearing argument. Give the skeptics their best day. Then state where you come down, honestly.

**Read in this order:**

1. **Turing (1950), "Computing Machinery and Intelligence"**. Read it. It is shorter than you remember and smarter than most summaries of it.
2. **Chen, Belkin, Bergen & Danks (2026), "Does AI already have human-level intelligence?"** *Nature*, 650, 36-40. Read it twice. Note exactly where their argument rests on definitions (what AGI is not) and where it rests on evidence.
3. **Bubeck et al. (2023), "Sparks of Artificial General Intelligence"** (GPT-4 paper). The Microsoft claim that started the serious modern debate.
4. **Bender, Gebru, McMillan-Major & Shmitchell (2021), "On the Dangers of Stochastic Parrots"**. The anchor skeptical paper. Read the "what is language" section with particular care.
5. **Chollet (2019), "On the Measure of Intelligence"**. Long but foundational. The skill-acquisition-efficiency definition is what you want.
6. **Chollet (2024/2025), ARC Prize report, latest edition**. For the empirical skeptical case.
7. **LeCun (2022), "A Path Towards Autonomous Machine Intelligence"**. His JEPA-oriented alternative. You do not have to agree. You have to represent it fairly.
8. **Marcus (2020/2024), "The Next Decade in AI"** plus his most recent substack synthesis. For a consistently critical voice with specific predictions.
9. **Kambhampati et al. (2024), "Position: LLMs Can't Plan, But Can Help Planning in LRM-Modulo Frameworks"** (ICML 2024). Specific, falsifiable, worth engaging.
10. **Aschenbrenner (2024), "Situational Awareness"**. A non-academic meta-view you do not have to agree with to learn from.
11. **Stanford AI Index Report, latest edition**. For the empirical backdrop.
12. **Jones & Bergen (2025)** arXiv:2503.23674. The Turing test paper. Verify the 73% claim from the primary source.

**What to watch for.** Where each author's position stands or falls. Chen et al. is strongest on the definitional move (what AGI is not). Chollet is strongest on the operational definition (skill-acquisition efficiency). LeCun is strongest on what is missing (world models, planning in the architectural sense). Marcus is strongest on reliability. Bender et al. is strongest on the meaning-versus-form distinction.

**Narrative arc.** This is the chapter where your voice carries the most weight. A general reader wants to know what you think. Tell them, but earn it first. Represent the strongest version of each skeptical position, then say where you land and why.

### Section 9: Open Problems and What Comes Next

**Narrative job.** Keep it honest. The fastest way to lose credibility with a technical reader is to write a chapter that reads like a press release. Name what is unsolved.

**Read in this order:**

1. **The latest Stanford AI Index Report**. For the field-wide picture.
2. **Hendrycks et al., "Humanity's Last Exam"** (most recent iteration). For where evaluations are going.
3. **One recent post or paper from Anthropic on Responsible Scaling Policies**.
4. **One recent paper on non-transformer architectures**: Mamba (Gu & Dao, 2023), the Large Concept Model paper (Meta), or whichever diffusion-language-model result is current.
5. **Any 2026 paper on automated interpretability**. The hand-crafted circuit-tracing approach does not scale; the field is working on it.

**What to watch for.** What the field itself calls out as unsolved. Reliability (hallucination, brittle generalization). Interpretability at scale. Safety and governance. Post-transformer architectures. The societal questions your current draft ends on.

### Section 10: Conclusion

**Narrative job.** Do not summarize. Argue. The conclusion of a book like this is where the author is allowed to say "here is what I believe and why." Your current conclusion does this well already. Polish, do not rewrite.

---

## The writing program

### Per-section rhythm

For each section, plan for roughly eight sessions:

- Sessions 1-4: Read one paper per session. Take notes as described above. No writing prose yet.
- Session 5: Synthesis. Re-read your own notes. Write a one-page outline for the section in your voice. If anything in the outline does not have a primary source behind it, either find one or cut it.
- Sessions 6-7: Draft. First half one night, second half the next. Do not look at papers; look only at your notes.
- Session 8: Revise. Read aloud. Cut 10%.

### Voice rules (your own style guide)

Write these down and pin them above your desk. Two rules from each influence and two of your own.

From *Crafting Interpreters*:

- Every technical term is introduced before it is used. No exceptions.
- Sidebars carry the curiosity. The main text carries the argument. Learn to separate the two.

From *TAOCP*:

- Every claim cites a primary source. Not a secondary summary.
- Exercises matter. At the end of each section, include two or three "Exercises for the Reader" that invite the reader to verify, extend, or challenge what they just read. This is not filler; it is how you teach them to think.

Your own:

- No em dashes.
- The personal voice from Section 1 is the ceiling, not the floor. Every later section has permission to be that warm.

### Dealing with "the industry keeps moving"

You are writing a living document. Build the seams in now.

1. Put a "Current as of: <date>" line at the top of every section.
2. Every section ends with a "What to watch" subsection. Three or four items. A year from now these are the paragraphs you will revise first.
3. Every citation goes into a single bibliography file. Use BibTeX or CSL-JSON so you can re-render the book with a single command when you add sources.

---

## The GitHub book track

Run this in parallel. Start it now so you are not scrambling at the end.

**Tooling.** Use **mdBook** (Rust-based, simple, Markdown in, HTML out, produces the kind of clean technical book that *Crafting Interpreters* aimed at). If you want richer figures or code execution, **Quarto** is the alternative. Avoid Docusaurus for this unless you already know it; it is built for doc sites, not books.

**Repo layout.**

```
/when-attention-becomes-thought
  /book
    book.toml
    /src
      SUMMARY.md
      introduction.md
      ch01-spark.md
      ch02-scaling.md
      ...
  /notes          # your reading notes, public or private at your choice
    section-03-scaling.md
    ...
  /references
    bibliography.bib
  /figures
    ...
  README.md
  CHANGELOG.md
```

**Minimum setup, in order:**

1. Create the repo. Make it public from day one. A half-finished public book is more credible than a finished private one.
2. Install mdBook. Commit the config and an empty SUMMARY.md.
3. Copy your existing Sections 1 and 2 into `ch01-spark.md` (and an introduction file). Make a first commit. The book exists.
4. Set up GitHub Actions to build the book on push and deploy to GitHub Pages. Fifteen minutes. Makes the book live.
5. Add a CHANGELOG.md entry every time you update a section. This is your LinkedIn post material.

**LinkedIn strategy.**

Each section is a LinkedIn post when it ships. Not the whole section. A 300-400 word summary with the key insight, one quote, and a link to the book. That is eight to ten high-value posts over the next three months, each pointing back to a permanent URL you control. The posts compound. The book compounds. LinkedIn is the amplifier, not the deliverable.

---

## Start here, tonight

If you have an hour or two right now, the highest-leverage moves are:

1. Create the repo. Install mdBook. Move your existing Section 1 and Section 2 in. Commit. Push. (~45 min.)
2. Create `notes/section-03-scaling.md`. Paste the template from earlier in this document. Save the file. That is the start of Section 3. (~10 min.)
3. Download Vaswani et al. (2017), Radford et al. (2018), and Brown et al. (2020) as PDFs into a `papers/` folder. Even if you do not read tonight, the papers are one click away tomorrow. (~10 min.)

That gets you to a running start with visible progress in under an hour. Next session you begin reading.

---

## What I can do next, on request

- Pull and preview any of the primary sources above (I can fetch arXiv abstracts and excerpts).
- Draft a voice sample for a single subsection so you can see how Section 3 might open, then discard it and write your own.
- Build the initial mdBook scaffold in the repo for you, so step 1 above is a clone rather than a setup.
- Create the note-taking template as a reusable markdown file you can copy per paper.
- Review individual section drafts as you finish them, against the voice rules above.
