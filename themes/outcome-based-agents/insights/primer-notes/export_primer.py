#!/usr/bin/env python3
"""Export insights/primer.md to primer.pdf and primer.docx, sized for a phone.
PDF: Chrome headless, 4.1 x 7.3 in pages, 10.5pt. Tables become stacked cards so nothing scrolls sideways.
DOCX: LibreOffice from the same HTML, then python-docx sets a 4.5 x 8 in page and fonts.
Usage: python3 export_primer.py [workdir]"""
import re, sys, subprocess, shutil, html
from pathlib import Path
import markdown
HERE = Path(__file__).resolve().parent.parent
MD = HERE / 'primer.md'
W = Path(sys.argv[1] if len(sys.argv) > 1 else '/tmp/primer-export'); W.mkdir(parents=True, exist_ok=True)

def prep(md):
    out, prev = [], ''
    for l in md.split('\n'):
        if re.match(r'^(\s*[-*] |\s*\d+\. )', l) and prev.strip() and not re.match(r'^(\s*[-*] |\s*\d+\. )', prev):
            out.append('')
        out.append(l); prev = l
    return '\n'.join(out)

def inline(s):
    return markdown.markdown(s.strip()).removeprefix('<p>').removesuffix('</p>')

def cards(md):
    lines, out, i = md.split('\n'), [], 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and re.match(r'^\|[-| :]+\|$', lines[i+1].strip()):
            hdr = [c.strip() for c in lines[i].strip().strip('|').split('|')]
            i += 2; rows = []
            while i < len(lines) and lines[i].startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')]); i += 1
            h = ['<div class="cards">']
            for r in rows:
                h.append('<div class="card"><div class="ct">' + inline(r[0]) + '</div>')
                for k, v in zip(hdr[1:], r[1:]):
                    h.append(f'<div class="cr"><span class="ck">{inline(k)}:</span> {inline(v)}</div>')
                h.append('</div>')
            h.append('</div>'); out.append('\n'.join(h)); out.append('')
        else:
            out.append(lines[i]); i += 1
    return '\n'.join(out)

md = MD.read_text()
body = markdown.markdown(cards(prep(md)), extensions=['sane_lists'])
css = '''@page { size: 4.1in 7.3in; margin: 0.22in 0.2in 0.3in 0.2in; }
body { font-family: "DejaVu Sans", Arial, sans-serif; font-size: 10.5pt; line-height: 1.38; color: #111; }
h1 { font-size: 15pt; margin: 0 0 6pt; } h2 { font-size: 13pt; margin: 12pt 0 4pt; border-bottom: 1px solid #999; }
h3 { font-size: 11.5pt; margin: 10pt 0 3pt; } p, li { margin: 3pt 0; } ul, ol { padding-left: 14pt; margin: 3pt 0; }
code { font-size: 9pt; } hr { border: 0; border-top: 1px solid #ccc; margin: 8pt 0; }
.cards { margin: 4pt 0 6pt; } .card { border: 1px solid #bbb; border-radius: 3pt; padding: 3pt 5pt; margin: 3pt 0; page-break-inside: avoid; }
.ct { font-weight: bold; } .cr { font-size: 9.5pt; margin: 1pt 0; } .ck { color: #444; font-weight: bold; }
a { color: #1a4fa0; word-break: break-all; }'''
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>OBA VC primer</title><style>{css}</style></head><body>{body}</body></html>'
hp = W / 'primer.html'; hp.write_text(doc)
subprocess.run(['google-chrome', '--headless', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer',
                f'--print-to-pdf={W/"primer.pdf"}', hp.as_uri()], check=True, capture_output=True)
subprocess.run(['soffice', '--headless', '--convert-to', 'docx:MS Word 2007 XML', '--outdir', str(W), str(hp)], check=True, capture_output=True)
import docx
from docx.shared import Inches, Pt
d = docx.Document(str(W / 'primer.docx'))
for s in d.sections:
    s.page_width, s.page_height = Inches(4.5), Inches(8)
    s.left_margin = s.right_margin = Inches(0.3); s.top_margin = s.bottom_margin = Inches(0.35)
for st in d.styles:
    try:
        if st.font is not None: st.font.name = 'Arial'
    except Exception: pass
d.styles['Normal'].font.size = Pt(11)
for t in d.tables:
    t.autofit = True
d.save(str(W / 'primer.docx'))
shutil.copy(W / 'primer.pdf', HERE / 'primer.pdf'); shutil.copy(W / 'primer.docx', HERE / 'primer.docx')
print('exported', HERE / 'primer.pdf', HERE / 'primer.docx')
