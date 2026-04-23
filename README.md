# When Attention Becomes Thought

*A literature review tracing the path from transformers to artificial general intelligence, 2017 to 2026.*

By Justin Dielmann.

## What this is

A book-length synthesis of the research that connects the 2017 transformer paper to the 2026 *Nature* commentary arguing that AGI has been achieved. Written for a general reader who wants to understand how we got here, with primary citations throughout.

Inspired in structure by Robert Nystrom's *Crafting Interpreters* and Donald Knuth's *The Art of Computer Programming*: pedagogical voice, rigorous sourcing, exercises where useful.

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
  ch02-the-spark.md
  ch03-the-scaling-era.md
  ...
  references.md
  changelog.md
/papers/                   # local PDFs of primary sources (gitignored)
/references/bibliography.bib
/.github/workflows/        # GitHub Pages deployment
```

## Status

As of 2026-04-22, Chapters 1 and 2 are drafted. Chapters 3 through 10 are reading-phase scaffolds with source lists.

## Contributing

If you find an error, or a primary source you think belongs here, open an issue. Pull requests welcome for citation fixes, typos, and broken links. For substantive additions, start with an issue so we can discuss the framing.

## License

Text: [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).
Code and configuration: [MIT](https://opensource.org/licenses/MIT).
See [`LICENSE`](LICENSE) for full terms.
