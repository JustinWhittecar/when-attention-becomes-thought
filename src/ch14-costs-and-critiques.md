# The Costs and Critiques

> **This chapter is in progress.** What follows is the planned reading list and narrative outline. The finished prose will replace this scaffolding as the chapter is drafted. Track progress in the [changelog](changelog.md).

*Last updated: 2026-05-01.*

## Narrative job

Take the major critiques of contemporary AI seriously, in their strongest forms, so that the reader leaves the chapter able to tell a real concern from a moral panic. The chapter has just shown what current AI systems can plausibly do (Chapter 8). The honest next move is to ask what they cost, what they get wrong, and who carries the consequences. This chapter is not a debunking and not an indictment. It is the audit.

## Scope

Four categories with the strongest empirical grounding, treated as the chapter's main sections. The remaining categories (surveillance, misinformation and deepfakes, concentration of power, cognitive dependency) appear as shorter sub-sections or as further reading depending on space.

1. Environmental costs. Training compute, inference compute at deployment scale, electricity demand, water for cooling, and what numbers actually mean when stated as percentages of national grid load.
2. Copyright and training data. The legal status as of writing, the strongest fair-use arguments on both sides, and what the live cases (NYT v. OpenAI, Authors Guild) are actually contesting.
3. Bias and algorithmic discrimination. Where measured disparate impact is documented, where the harm chain runs from training data to deployed decisions, and where the hardest cases are no longer technical but distributive.
4. Labor and data work. The human pipeline behind RLHF and content moderation, working conditions for the people doing it, and the asymmetry between where value accrues and where harm lands.

## Reading list (starter)

*This is a starter set. The chapter's full reading program will be expanded as the chapter is drafted. The anchors and accessible-bridge entries open the list; section-specific entries follow.*

1. Crawford (2021), *Atlas of AI.* Cross-cutting STS anchor. Treats AI as an extractive industry across data, labor, environment, and power. The chapter's organizing argument runs through this book.
2. O'Neil (2016), *Weapons of Math Destruction.* The accessible bridge between academic critique and public discourse. The most likely book a layperson reader has already heard of; useful for orienting them before the technical literature.
3. Strubell, Ganesh & McCallum (2019), "Energy and Policy Considerations for Deep Learning in NLP." The paper that put training carbon cost on the field's agenda.
4. Patterson et al. (2021), "Carbon Emissions and Large Neural Network Training." Google's response, with a more careful accounting of what training a frontier model actually emits.
5. Henderson et al. (2023), "Foundation Models and Fair Use." The clearest current statement of where the legal debate sits and what doctrines are being tested.
6. Buolamwini & Gebru (2018), "Gender Shades." The audit that demonstrated commercial face-classification systems failed worst on the people they were most often used against.
7. Obermeyer et al. (2019), "Dissecting Racial Bias in an Algorithm Used to Manage the Health of Populations." The *Science* paper showing that proxies in training data can produce disparate impact even when race is not a feature.
8. Benjamin (2019), *Race After Technology.* Critical-race-tech framing of how "neutral" systems amplify hierarchy and carceral logics. Reads the empirical bias literature through a structural lens.
9. Eubanks (2018), *Automating Inequality.* Concrete state-power case studies (welfare, criminal justice) showing how automated decision systems reconfigure governance. The most accessible critical-tech book on this list.
10. Gray & Suri (2019), *Ghost Work.* The book on the human labor pipeline behind systems that read as automated.
11. Perrigo (2023), "Exclusive: OpenAI Used Kenyan Workers on Less Than $2 Per Hour to Make ChatGPT Less Toxic." *Time* investigation that named the conditions for current frontier-model RLHF labor.

## What to flag in the writing

Concrete numbers wherever possible, with their source and their year. Costs that have changed materially since 2022 should be flagged as moving targets, not stated as if static. Where a critique is contested in the literature, present both sides and the strongest evidence for each before stating a view.

## Out of scope for this chapter

Existential / catastrophic risk and long-run alignment concerns. Those are covered in Chapter 4 (Teaching Machines to Follow Intent) and Chapter 8 (The AGI Question). This chapter focuses on harms that have already landed or are landing now.
