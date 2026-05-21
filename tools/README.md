# Build tooling

## mdbook-citeproc.py

An mdBook preprocessor that resolves `[@bibkey]` citations into IEEE-numbered
references and generates the References page.

- Citations are written in the chapter source as `[@key]` or `[@key, p. 17]`.
- At build time the preprocessor numbers them in order of first appearance,
  rewrites each span to `[N]` / `[N, p. 17]`, and fills `references.md` with the
  IEEE-formatted reference list.
- Source of truth: `references/bibliography.bib`. Style: `references/ieee.csl`.
- Only `[@...]` spans and the references page are rewritten; SVG, tables, and
  footnotes are passed through untouched.

Setup: `pip install -r tools/requirements.txt`
