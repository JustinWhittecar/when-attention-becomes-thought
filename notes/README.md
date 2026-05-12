# Reading notes

One file per chapter, named to match the corresponding chapter file in `src/`. One entry per paper inside each file, using the structure in `TEMPLATE.md`.

These notes are the raw material for the book. They are not polished. They are public so readers can see the work and other researchers can catch errors.

## Files

The notes folder mirrors the chapter ordering in `src/SUMMARY.md`. After the structural pivot of 2026-05-06, the file names align to the 16-chapter arc:

```
notes/
  ch02-logic-beneath-the-machine.md
  ch03-neuron-and-the-computer.md
  ch04-tubes-to-tensors.md
  ch05-learning-from-data.md
  ch06-sequences-and-memory.md
  ch07-the-spark.md
  ch08-the-scaling-era.md
  ch09-alignment.md
  ch10-reasoning.md
  ch11-interpretability.md
  ch12-agency.md
  ch13-agi-question.md
  ch14-costs-and-critiques.md
  ch15-open-problems.md
  TEMPLATE.md
  personal-shelf.md
  drafts/
```

There is no `ch01-...md` notes file; Chapter 1 is personal voice, not a research synthesis.

The reading lists inside each file match `FINISHING_PLAN.md`. When that document changes, the corresponding notes file should be updated to match.

## Workflow

1. **Reading night.** Pick the next paper in the chapter's reading list. Open the relevant notes file. Fill in all seven fields of the template. Do not skip "Teaching angle."
2. **Synthesis night.** Re-read the chapter's notes file top to bottom. Fill in the Synthesis block at the bottom. Sketch the worked examples (propositional-logic circuits, pseudocode blocks) the chapter's prose will reference.
3. **Writing night.** Open the chapter file in `src/`. Write from the notes, not the papers.

Every paper that ends up cited in `src/` should have a matching entry in the chapter's notes file and a matching citation in `src/references.md` by the time the chapter is drafted.

## Other files

`personal-shelf.md` is a private working shelf for books and resources consulted but not on the public reading lists. Gitignored.

`drafts/` contains older working drafts and one-off pieces (chapter scaffolds from the previous 11-chapter structure, an early LinkedIn post). Some of these were made obsolete by the 2026-05-06 restructure and are kept here for reference only; clean up at leisure.
