# Changelog

This page mirrors the repo's `CHANGELOG.md`. Most readers will find the version-by-version notes below sufficient; the full file in the repo includes a few release-process details that don't render here.

## Unreleased

- **Chapter 1 split into three chapters within Part I: Foundations.** The original Chapter 1, "The Logic Beneath the Machine," was divided along its existing section breaks into three: "The Logic Beneath the Machine" (the algebra of logic, Boole through truth tables), "The Limits of Computation" (Cantor, Goedel, Turing, and computability), and "Logic Becomes Information" (Shannon's circuits, one-bit memory, and information theory). All three join Part I: Foundations, now eight chapters. The remaining chapters were renumbered to ch04 through ch17; the book is now an Introduction and 17 chapters.
- **Structural pivot from 11 chapters to an Introduction and 15 chapters.** The book is now organized in three parts and opens with an unnumbered Introduction. Part I (Chapters 1-5) is a new foundations sequence that takes a reader with no background through the convergence of mathematical logic, neuroscience, and computer engineering, the hardware curve from vacuum tubes through TPUs, the perceptron-to-backprop story, and the recurrent era that the transformer was built to surpass. Part II (Chapters 6-11) is the modern stack. Part III (Chapters 12-15) is the AGI question, the costs and critiques, what comes next, and the conclusion.
- Pedagogical commitments formalized: propositional logic for hardware circuits, pseudocode for load-bearing algorithms, CPU > GPU > TPU as the spine of the hardware story, and a "show, then tell" contract where formal devices are introduced in their smallest worked example before any prose claim depends on them.
- Existing chapter files renamed to their final positions; the opening chapter is now an unnumbered Introduction, and "The Spark" is Chapter 6.
- Chapter 1 closing roadmap rewritten to point the reader back to Boole rather than to 2017.
- `references.md` reorganized to match the new chapter ordering.
- A Further Reading appendix has been added, opening a new End Matter section of the book.

## 0.2.0 - 2026-04-24

- **Chapter 1, "Why I Wrote This," is published.** First complete chapter. Covers the motivation for the book, the skeptic-to-persuaded arc, and a roadmap for the remaining chapters.
- Bibliography entries added for the sources cited in Chapter 1.
- `src/references.md` Chapter 1 section now matches the chapter's actual citations, listed in the order they appear.

## 0.1.0 - 2026-04-22

- Repository scaffolding: mdBook structure, chapter files for all chapters, references file, GitHub Actions workflow.
- Reading lists and narrative briefs for the remaining chapters.
- Notes template in `notes/TEMPLATE.md`.
- Merged preface into Chapter 1. Initial import; Sections 1 and 2 moved from Google Doc.
