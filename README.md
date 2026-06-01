# Student Support Persona Cards

A K–12 teacher-facing web resource featuring 60 persona cards covering disabilities, chronic health conditions, and learning differences. Each card offers grade-band–specific observations, strengths, accommodations, assistive technology recommendations, IEP considerations, and family partnership tips — grounded in the principles of **Universal Design for Learning (UDL)** and the **Individuals with Disabilities Education Act (IDEA)**.

**Live site:** https://fyvr.net/student-personas/

---

## What's in this resource

- **60 persona cards** across 11 categories
- **3 grade bands per card** — Elementary (K–5), Middle School (6–8), High School (9–12)
- **Each grade band includes:**
  - What you might notice in class
  - Student strengths
  - Recommended accommodations
  - Assistive technology
  - UDL strategies
  - IEP considerations (IDEA eligibility, goal examples, service recommendations)
  - Who to collaborate with
  - Family partnership tip
- **Condition-specific references** on every card
- **Downloadable PDF** of the full set (`docs/student-support-persona-cards.pdf`)

### Categories

| Category | Cards |
|---|---|
| Learning Disabilities | 5 |
| Attention & Executive Function | 5 |
| Autism Spectrum | 5 |
| Emotional & Behavioral | 5 |
| Speech & Language | 5 |
| Sensory & Physical | 5 |
| Intellectual & Developmental | 5 |
| Complex & Intersectional | 5 |
| Chronic Health Conditions | 8 |
| Physical & Motor | 6 |
| Neurological & Other Health | 6 |

---

## File structure

```
inclusive-personas/
├── index.html              # Home page — all 60 cards in a filterable grid
├── card.html               # Individual card detail page (JS-rendered)
├── .htaccess               # Apache URL rewrites (/dyslexia → card.html?id=1)
├── css/
│   └── style.css           # All styles — WCAG 2.2 AA compliant
├── data/
│   └── cards.json          # Source data for all 60 cards
├── docs/
│   ├── README.md           # Index of all card markdown files
│   ├── card-01-dyslexia.md # One .md file per card (60 total)
│   └── student-support-persona-cards.pdf  # Full downloadable PDF
├── generate_pdf.py         # PDF generator (ReportLab + pikepdf)
└── server.py               # Local preview server (port 8766)
```

---

## Running locally

No build step or framework required — this is a static HTML app.

**Start the preview server:**
```bash
cd inclusive-personas
python3 server.py
```
Then open http://127.0.0.1:8766/

---

## Generating the PDF

The PDF is built with [ReportLab](https://www.reportlab.com/) and post-processed with [pikepdf](https://pikepdf.readthedocs.io/) for PDF/UA-1 accessibility compliance.

**Install dependencies:**
```bash
pip3 install reportlab pikepdf
```

**Rebuild the PDF:**
```bash
python3 generate_pdf.py --force
```

**Smart rebuild (only if data changed):**
```bash
python3 generate_pdf.py
```

**Check status without building:**
```bash
python3 generate_pdf.py --check
```

The script uses a hash + 14-day interval strategy — it compares an MD5 of `cards.json` against a sentinel file (`data/.pdf_build_sentinel`) and only rebuilds when the data has changed. `--force` always rebuilds regardless.

Output: `docs/student-support-persona-cards.pdf`

---

## URL routing

Card pages use clean slug URLs via Apache mod_rewrite (`.htaccess`):

```
https://fyvr.net/student-personas/dyslexia
https://fyvr.net/student-personas/cortical-visual-impairment
```

The `.htaccess` file must be placed in the `student-personas/` directory on the server. The JavaScript in `card.html` reads the slug from `window.location.pathname` and matches it against card titles — so `?id=N` query string links continue to work for local development and old bookmarks.

---

## Accessibility

- **WCAG 2.2 AA compliant** — verified with axe-core (0 violations)
- **PDF/UA-1 compliant** — 17/17 accessibility checks pass, including:
  - Tagged PDF with full structure tree (Document → Part → Sect → H1/P)
  - `/Lang = "en"` on document root
  - XMP metadata with `pdfuaid:part = 1`
  - Bookmarks for all 60 cards (11 categories + 60 entries)
  - `/Tabs = /S` on all pages
- Skip link, landmark regions, heading hierarchy, ARIA tabs pattern
- Atkinson Hyperlegible font (dyslexia-friendly)
- All contrast ratios exceed 4.5:1 (most are 11:1+)
- Touch targets ≥ 24px (WCAG 2.5.8)

---

## Frameworks & references

- [CAST Universal Design for Learning Guidelines](https://udlguidelines.cast.org/)
- [IDEA — Individuals with Disabilities Education Act](https://sites.ed.gov/idea/)
- [Understood.org](https://www.understood.org/)
- [CDC — Disability & Health](https://www.cdc.gov/ncbddd/disabilityandhealth/disability.html)
- [Wrightslaw Special Education Law](https://www.wrightslaw.com/)

---

## Card documentation

Individual markdown files for each card are in `docs/`. See [docs/README.md](docs/README.md) for the full index.

---

## License

This resource is intended for educational use by K–12 teachers, special educators, and support staff. Content is grounded in publicly available educational research and IDEA/Section 504 frameworks.
