# Why I Wrote This

*Last updated: 2026-04-22.*

I am from a generation that grew up discovering the internet. I still remember the first time I was able to use MapQuest to print out directions somewhere, and I recall the magic of first navigating via smartphone. As a young man, I was obsessed with sci-fi and devoured books like *Snow Crash* and *Neuromancer*, and my homelab is named after an Isaac Asimov character.

Alan Turing to my people is a celebrity on the scale of any president or pop star that has ever lived, and while I got my degree in English, my obsession with AI systems and machine learning has defined my career. It has informed the companies I have worked at and the roles I have chosen to accept. In fact, it is arguably why I wound up as a product manager. In my world, it has not been uncommon for the public to imagine we are much further along than we are. From tech CEOs promising capabilities that are decades away will happen next year, to sci-fi and TV setting entirely unrealistic expectations, AI has been plagued by way too much noise and way too little signal.

At least, that is what I thought before this last year.

When I stumbled upon "Does AI already have human-level intelligence? The evidence is clear" in *Nature*, I found myself nodding along. The authors argue, convincingly, that AI has by any reasonable standard already surpassed the vision laid out by Alan Turing way back in 1950. In March 2025, GPT-4.5 was judged by humans in a Turing test to be human 73% of the time, more often than actual humans were judged to be human (Jones & Bergen, 2025). Let that sink in for a second. LLMs are now more likely to be judged human than you are.

By February 2026, a team of researchers spanning philosophy, machine learning, linguistics, and cognitive science concluded that "by reasonable standards, including Turing's own, we have artificial systems that are generally intelligent" and that "the long-standing problem of creating AGI has been solved" (Chen et al., 2026). How they got to that conclusion is a story worth telling properly, and that is what this review sets out to do.

My goal here is to trace the research that brought us to this point in a way that only a fan could. While I have had the extreme privilege of building systems on top of these models, I have been at best an awe-inspired onlooker, and I hope I can share some of that awe with you. I am not setting out to convince you of the truth of the AGI argument. I am setting out to show you the chain of breakthroughs that made the argument possible, and to let you decide for yourself.

Our story begins in 2017 with a single architectural innovation: the transformer (Vaswani et al., 2017). The mechanism of self-attention, which allows every element in a sequence to attend to every other element in parallel, replaced the sequential bottleneck of recurrent neural networks and unlocked a new relationship between computation, data, and capability. What followed was not a single breakthrough but a chain of them, each building on the last in ways that were sometimes predicted by scaling laws and sometimes genuinely surprising. Models trained on this architecture went on to achieve gold-medal performance at the International Mathematical Olympiad, collaborate with leading mathematicians to prove theorems, generate scientific hypotheses validated in experiments, solve PhD-level examination problems, and compose poetry that readers preferred over human-written work (Bubeck et al., 2025; Rizvi et al., 2025; Chakrabarty et al., 2025). None of that was obvious in 2017. All of it is documented.

We will follow that chain across six stages:

1. **The transformer architecture** and the self-attention mechanism that made everything else possible (Chapter 2).
2. **The scaling era**, in which larger models trained on more data revealed emergent abilities that no amount of engineering on smaller models could produce (Chapter 3).
3. **The alignment revolution**, in which reinforcement learning from human feedback transformed raw language models into systems that could follow instructions and engage in directed problem-solving (Chapter 4).
4. **The reasoning revolution**, in which reinforcement learning with verifiable rewards, chain-of-thought prompting, and test-time scaling gave language models something resembling deliberate, multi-step thought (Chapter 5).
5. **Mechanistic interpretability**, in which researchers traced the internal computations of frontier models and found structured reasoning circuits, planning behavior, and multi-hop inference rather than shallow pattern matching (Chapter 6).
6. **The agentic era**, in which reasoning models were embedded in autonomous systems that use tools, coordinate with other agents, and execute complex multi-step tasks in the real world (Chapter 7).

We conclude by examining the AGI question directly: what the accumulated evidence means, what the strongest objections are, and what remains unsolved (Chapter 8).

This review is for fellow fans of the field and science fiction nerds alike. It is for anyone who wants to know what we know about how this technology works and came to be. My contribution is not new empirical results but a synthesis: a single document that traces, with primary citations, the path from "Attention Is All You Need" to "Does AI Already Have Human-Level Intelligence? The Evidence Is Clear," and helps in the process share just how magical it is that we are now turning sand into thinking beings.

## A note on the form

This is a living document. It is organized as chapters on GitHub and built as a book with [mdBook](https://rust-lang.github.io/mdBook/). Each chapter names the date it was last updated. New sources are added via pull request. A changelog in the repository records what changed between versions.

If you find an error, or a source I should have read, please open an issue.

---

## Expansion outline (working notes)

*Target: ~2000 words. Remove this section before publishing.*

| Section | Target words | What it does |
|---|---|---|
| Personal opening (sci-fi / Turing / internet) | 250 | Warm in. Voice established. |
| Who I am professionally | 300 | Credibility. Specifics about career, systems you've built, who you've translated between. |
| The pivot: what changed in 2024-2026 | 350 | Why this book exists now. Walk through the cascade of moments. |
| Why I'm writing this, and why now | 300 | The gap this book fills. Between-the-researchers-and-the-laypeople audience. |
| Who this is for | 150 | Not researchers, not total newcomers. The informed curious. |
| What I promise you | 200 | Primary sources, steelmanned counterarguments, an honest landing. |
| The roadmap | 350 | The existing six-stage list, with one payoff line per stage. |
| A note on the form | 100 | Existing text. |
