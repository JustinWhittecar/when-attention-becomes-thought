# Changelog

This page mirrors the repo's `CHANGELOG.md`. Most readers will find the version-by-version notes below sufficient; the full file in the repo includes a few release-process details that don't render here.

## Unreleased

- **Structural pivot from 11 chapters to 16.** The book is now organized in three parts. Part I (Chapters 2-6) is a new foundations sequence that takes a reader with no background through the convergence of mathematical logic, neuroscience, and computer engineering, the hardware curve from vacuum tubes through TPUs, the perceptron-to-backprop story, and the recurrent era that the transformer was built to surpass. Part II (Chapters 7-12) is the modern stack. Part III (Chapters 13-16) is the AGI question, the costs and critiques, what comes next, and the conclusion.
- Pedagogical commitments formalized: propositional logic for hardware circuits, pseudocode for load-bearing algorithms, CPU > GPU > TPU as the spine of the hardware story, and a "show, then tell" contract where formal devices are introduced in their smallest worked example before any prose claim depends on them.
- Existing chapter files renamed to their new positions; Chapter 2 (The Spark) is now Chapter 7.
- Chapter 1 closing roadmap rewritten to point the reader back to Boole rather than to 2017.
- `references.md` reorganized to match the new chapter ordering.

## 0.2.0 — 2026-04-24

- **Chapter 1, "Why I Wrote This," is published.** First complete chapter. Covers the motivation for the book, the skeptic-to-persuaded arc, and a roadmap for the remaining chapters.
- Bibliography entries added for the sources cited in Chapter 1.
- `src/references.md` Chapter 1 section now matches the chapter's actual citations, listed in the order they appear.

## 0.1.0 — 2026-04-22

- Repository scaffolding: mdBook structure, chapter files for all chapters, references file, GitHub Actions workflow.
- Reading lists and narrative briefs for the remaining chapters.
- Notes template in `notes/TEMPLATE.md`.
- Merged preface into Chapter 1. Initial import; Sections 1 and 2 moved from Google Doc.
