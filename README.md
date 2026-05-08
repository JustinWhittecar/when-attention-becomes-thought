# When Attention Becomes Thought

By Justin Dielmann.

## What this is

A book-length synthesis tracing the intellectual arc from George Boole's 1854 algebra of logic to the 2026 *Nature* commentary arguing that AGI has been achieved. Written for a general reader who wants to understand how we got here, with primary citations throughout.

## Read it

The book is live at **[justinwhittecar.github.io/when-attention-becomes-thought](https://justinwhittecar.github.io/when-attention-becomes-thought/)**.

To build locally:

```bash
cargo install mdbook
mdbook serve --open
```

## Repository layout

```
/book.toml                 # mdBook config
/src/                      # chapter source (what the book is built from)
  SUMMARY.md               # table of contents
  ch01-why-i-wrote-this.md
  ch02-logic-beneath-the-machine.md
  ch03-neuron-and-the-computer.md
  ...
  ch16-conclusion.md
  references.md
  changelog.md
/papers/                   # local PDFs of primary sources (gitignored)
/references/bibliography.bib
/.github/workflows/        # GitHub Pages deployment
```

## Status

Chapter 1, *Why I Wrote This*, is published. Chapters 2 through 16 are in progress, organized in three parts: Foundations (Ch 2-6), The Modern Stack (Ch 7-12), and The Question (Ch 13-16). Chapters publish when they are ready; there is no committed schedule.

I write in public. Each Friday I post a build-in-public update on LinkedIn covering what I read that week, what I learned, and what is still unresolved. The [changelog](src/changelog.md) is the canonical record of what has shipped.

## A note on AI use

All first drafts, research, and personal experiences in this book are my own. AI tools were used throughout the process to help with outlining, editing, and critiquing the work.

## Contributing

If you find an error, or a primary source you think belongs here, open an issue. Pull requests welcome for citation fixes, typos, and broken links. For substantive additions, start with an issue so we can discuss the framing.

## License

Text: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
Code and configuration: [MIT](https://opensource.org/licenses/MIT).
See [`LICENSE`](LICENSE) for full terms.
