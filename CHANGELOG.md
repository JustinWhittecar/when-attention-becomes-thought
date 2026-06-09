# Changelog

All notable changes to this book are recorded here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

Mirrors `src/changelog.md`, which is what the built site shows.

## [Unreleased]

### Changed
- **Chapter 1 split into three chapters within Part I: Foundations.** The original Chapter 1, "The Logic Beneath the Machine," was divided along its existing section breaks into three: "The Logic Beneath the Machine" (the algebra of logic, Boole through truth tables), "The Limits of Computation" (Cantor, Goedel, Turing, and computability), and "Logic Becomes Information" (Shannon's circuits, one-bit memory, and information theory). All three join Part I: Foundations, now eight chapters. The remaining chapters were renumbered to ch04 through ch17; the book is now an Introduction and 17 chapters.
- **Structural pivot from 11 chapters to an Introduction and 15 chapters.** The book is now organized in three parts and opens with an unnumbered Introduction. Part I (Chapters 1-5) is a new foundations sequence that takes a reader with no background through the convergence of mathematical logic, neuroscience, and computer engineering, the hardware curve from vacuum tubes through TPUs, the perceptron-to-backprop story, and the recurrent era that the transformer was built to surpass. Part II (Chapters 6-11) is the modern stack, refocused around the foundation Part I now provides. Part III (Chapters 12-15) is the AGI question, the costs and critiques, what comes next, and the conclusion.
- **Pedagogical commitments formalized.** `FINISHING_PLAN.md` now codifies four standing rules: any hardware claim that depends on circuit-level behavior is shown in propositional logic before it is asserted in prose; any algorithm that carries the chapter's argument is shown in pseudocode before it is described; the CPU > GPU > TPU progression is the spine of the hardware story; and the book follows a "show, then tell" contract where a formal device introduced in chapter N is available as shorthand from chapter N+1 forward.
- **Repository restructured.** All in-progress material (reading notes, drafts, and scratch exports) now lives in a gitignored `working/` directory, so unfinished work never reaches the built site. The repository root was cleared of working files, stale exports, and editor artifacts.
- Existing chapter files renamed to their final positions. The opening chapter became the unnumbered Introduction, and "The Spark" is now Chapter 6.
- Chapter 1 closing roadmap rewritten to point the reader back to Boole rather than to 2017.
- `src/references.md` reorganized to match the new chapter ordering.
- `FINISHING_PLAN.md` rewritten with revised reading lists and per-chapter narrative jobs for every chapter.

### Added
- New scaffolding files for the foundations chapters, `ch01-logic-beneath-the-machine.md` through `ch05-sequences-and-memory.md`.
- New proposed-reading sections in `references.md` for the foundations chapters.
- New `src/end-matter/` section. The further-reading appendix moved here and is wired into `SUMMARY.md`, opening a place for reference tables and a glossary.
- `tools/` directory holding the mdBook citeproc preprocessor (`mdbook-citeproc.py`) and the IEEE citation style (`references/ieee.csl`).

### Removed
- Stale duplicate `.docx` exports, scattered `.DS_Store` files, and a stray empty directory cleared from the repository root.

## [0.2.0] - 2026-04-24

### Added
- **Chapter 1, "Why I Wrote This," is published.** First complete chapter. Covers the motivation for the book, the skeptic-to-persuaded arc, and a roadmap for the remaining chapters.
- Bibliography entries (`references/bibliography.bib`) for the sources cited in Chapter 1: Turing 1950, Vaswani 2017, Rein 2023 (GPQA), Porter & Machery 2024, Jones & Bergen 2025, Bubeck 2025, OpenAI 2025 IMO, DeepMind 2025 IMO, Chen 2026, Phan 2026 (HLE).

### Changed
- `src/references.md` Chapter 1 section now matches the chapter's actual citations, listed in the order they appear.

## [0.1.0] - 2026-04-22

### Added
- Repository scaffolding: mdBook structure, chapter files for all 10 chapters, references file, GitHub Actions workflow.
- Reading lists and narrative briefs for Chapters 2 through 10.
- Notes template in `notes/TEMPLATE.md`.

### Changed
- Merged preface into Chapter 1. Chapter 1 renamed from "Introduction" to "Why I Wrote This." `preface.md` and `ch01-introduction.md` removed; new file is `ch01-why-i-wrote-this.md`.
- Restructured `references.md` by chapter in reading order. Chapters 3-9 appear under a clearly-marked "Proposed reading (not yet incorporated)" section; entries graduate above that divider once the relevant chapter is drafted.

Initial import. Sections 1 and 2 moved from Google Doc.
