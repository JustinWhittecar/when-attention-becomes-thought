# Changelog

All notable changes to this book are recorded here. Format loosely follows [Keep a Changelog](https://keepachangelog.com/).

Mirrors `src/changelog.md`, which is what the built site shows.

## [Unreleased]

### Changed
- **Structural pivot from 11 chapters to 16.** The book is now organized in three parts. Part I (Chapters 2-6) is a new foundations sequence that takes a reader with no background through the convergence of mathematical logic, neuroscience, and computer engineering, the hardware curve from vacuum tubes through TPUs, the perceptron-to-backprop story, and the recurrent era that the transformer was built to surpass. Part II (Chapters 7-12) is the modern stack, refocused around the foundation Part I now provides. Part III (Chapters 13-16) is the AGI question, the costs and critiques, what comes next, and the conclusion.
- **Pedagogical commitments formalized.** `FINISHING_PLAN.md` now codifies four standing rules: any hardware claim that depends on circuit-level behavior is shown in propositional logic before it is asserted in prose; any algorithm that carries the chapter's argument is shown in pseudocode before it is described; the CPU > GPU > TPU progression is the spine of the hardware story; and the book follows a "show, then tell" contract where a formal device introduced in chapter N is available as shorthand from chapter N+1 forward.
- Existing chapter files renamed to their new positions. Chapter 2 (The Spark) is now Chapter 7. Chapters 3-11 shift to Chapters 8-16.
- Chapter 1 closing roadmap rewritten to point the reader back to Boole rather than to 2017.
- `src/references.md` reorganized to match the new chapter ordering. Most former Chapter 2 entries redistributed across new Chapters 3, 4, 5, 6, and 7.
- `FINISHING_PLAN.md` rewritten with revised reading lists and per-chapter narrative jobs for all 16 chapters.

### Added
- New scaffolding files for `ch02-logic-beneath-the-machine.md`, `ch03-neuron-and-the-computer.md`, `ch04-tubes-to-tensors.md`, `ch05-learning-from-data.md`, and `ch06-sequences-and-memory.md`.
- New proposed-reading sections in `references.md` for Chapters 2, 4, 5, and 6.

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
