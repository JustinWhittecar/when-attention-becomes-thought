#!/usr/bin/env python3
"""mdBook preprocessor: resolve [@bibkey] citations into IEEE-numbered
references and generate the References page with citeproc-py + ieee.csl.

It only rewrites [@...] citation spans and the references page. All other
content (inline SVG, tables, footnotes) is passed through untouched.
"""
import sys, json, re, warnings
warnings.filterwarnings('ignore')

BIB_PATH = 'references/bibliography.bib'
CSL_PATH = 'references/ieee.csl'

def log(*a):
    print('[citeproc]', *a, file=sys.stderr)

# mdBook asks "supports <renderer>" first; answer yes for everything.
if len(sys.argv) > 1 and sys.argv[1] == 'supports':
    sys.exit(0)

import bibtexparser
from bibtexparser.bparser import BibTexParser

def _clean(s):
    return (s.replace('``', '“').replace("''", '”')
             .replace('--', '–').replace('\\&', '&').replace('~', ' ').strip())

def _names(field):
    out = []
    for n in field.split(' and '):
        n = n.strip()
        if ',' in n:
            fam, giv = n.split(',', 1)
            out.append({'family': fam.strip(), 'given': giv.strip()})
        elif n:
            out.append({'literal': n})
    return out

_TYPE = {'book': 'book', 'article': 'article-journal', 'incollection': 'chapter',
         'inbook': 'chapter', 'mastersthesis': 'thesis', 'phdthesis': 'thesis',
         'inproceedings': 'paper-conference', 'misc': 'document', 'techreport': 'report'}

def _to_csl(e):
    c = {'id': e['ID'], 'type': _TYPE.get(e['ENTRYTYPE'], 'document')}
    if 'author' in e: c['author'] = _names(e['author'])
    if 'editor' in e: c['editor'] = _names(e['editor'])
    for bk, ck in [('title', 'title'), ('publisher', 'publisher'), ('school', 'publisher'),
                    ('address', 'publisher-place'), ('volume', 'volume'), ('number', 'issue'),
                    ('doi', 'DOI'), ('url', 'URL'), ('series', 'collection-title'),
                    ('note', 'note'), ('type', 'genre'), ('journal', 'container-title'),
                    ('booktitle', 'container-title')]:
        if bk in e: c[ck] = _clean(e[bk])
    if 'pages' in e: c['page'] = _clean(e['pages'])
    if 'year' in e:
        d = ''.join(ch for ch in e['year'] if ch.isdigit())
        if d: c['issued'] = {'date-parts': [[int(d)]]}
    return c

def load_bib(path):
    p = BibTexParser(common_strings=True)
    p.ignore_nonstandard_types = False
    with open(path, encoding='utf-8') as f:
        db = bibtexparser.load(f, p)
    return {e['ID']: _to_csl(e) for e in db.entries}

CITE_RE = re.compile(r'\[(@[^\]\n]+)\]')
PIECE_RE = re.compile(r'@([A-Za-z0-9_:.\-]+)\s*(?:,\s*(.+))?$')

def parse_bracket(inner):
    pieces = []
    for part in inner.split(';'):
        m = PIECE_RE.match(part.strip())
        if not m:
            return None
        pieces.append((m.group(1), m.group(2).strip() if m.group(2) else None))
    return pieces

def iter_chapters(book):
    out = []
    def rec(items):
        for it in items:
            ch = it.get('Chapter')
            if ch is not None:
                out.append(ch)
                rec(ch.get('sub_items', []))
    rec(book['sections'])
    return out

def render_refs(order, bib):
    if not order:
        return '# References\n'
    from citeproc.source.json import CiteProcJSON
    from citeproc import (CitationStylesStyle, CitationStylesBibliography,
                          Citation, CitationItem, formatter)
    src = CiteProcJSON([bib[k] for k in order])
    style = CitationStylesStyle(CSL_PATH, validate=False)
    b = CitationStylesBibliography(style, src, formatter.html)
    for k in order:
        b.register(Citation([CitationItem(k)]))
    lines = ['# References', '']
    for item in b.bibliography():
        lines.append(re.sub(r'^(\[\d+\])\s*', r'\1 ', str(item)))
        lines.append('')
    return '\n'.join(lines)

def main():
    data = json.load(sys.stdin)
    book = data[1]
    bib = load_bib(BIB_PATH)
    chapters = iter_chapters(book)

    order, seen = [], set()
    for ch in chapters:
        for m in CITE_RE.finditer(ch.get('content') or ''):
            pieces = parse_bracket(m.group(1))
            if not pieces:
                continue
            for key, _ in pieces:
                if key in seen:
                    continue
                if key in bib:
                    seen.add(key); order.append(key)
                else:
                    log('WARNING unknown citation key:', key)
    num = {k: i + 1 for i, k in enumerate(order)}

    def repl(m):
        pieces = parse_bracket(m.group(1))
        if not pieces:
            return m.group(0)
        outs = []
        for key, loc in pieces:
            if key not in num:
                return m.group(0)
            outs.append('[{}, {}]'.format(num[key], loc) if loc else '[{}]'.format(num[key]))
        return ', '.join(outs)

    for ch in chapters:
        if ch.get('content'):
            ch['content'] = CITE_RE.sub(repl, ch['content'])

    refs_md = render_refs(order, bib)
    for ch in chapters:
        if (ch.get('path') or '').endswith('references.md'):
            ch['content'] = refs_md

    json.dump(book, sys.stdout)

if __name__ == '__main__':
    main()
