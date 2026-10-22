# Usage: make <target> [THEME=<slug|short>]     (THEME defaults to the only theme, or set it: THEME=anip)
THEME ?=
TH := $(if $(THEME),--theme $(THEME),)
.PHONY: help ingest index validate search new-company new-source new-theme sweep stats index-all validate-all

help:
	@grep -E '^[a-z-]+:.*##' Makefile | sed 's/:.*##/  -/'

ingest:        ## normalize themes/<theme>/inbox/* into sources/ (+ raw/)
	python3 scripts/ingest.py $(TH)

index:         ## rebuild index/ (STATS.md, QUEUE.md, companies.csv, *.jsonl, db.sqlite)
	python3 scripts/build_index.py $(TH)

validate:      ## check every frontmatter against schema/ + taxonomy.yml -> index/VALIDATION.md
	python3 scripts/validate.py $(TH)

search:        ## make search q="rare earth refining"
	python3 scripts/search.py $(TH) "$(q)"

new-company:   ## make new-company name="Nox Metals"
	python3 scripts/new.py $(TH) company "$(name)"

new-source:    ## make new-source type=expert-call title="Call w/ ex-Hadrian ops lead"
	python3 scripts/new.py $(TH) source "$(title)" --type $(type)

new-theme:     ## make new-theme slug=energy name="Energy" short=en
	python3 scripts/new_theme.py $(slug) "$(name)" --short $(short)

sweep:         ## pull new items from Google News + trade press RSS (+ --sites) -> sources/ as unread
	python3 scripts/sweep.py $(TH) $(ARGS)

stats:         ## counts by type / layer / status
	python3 scripts/build_index.py $(TH) --stats

index-all:     ## validate + index every theme (what the GitHub Action runs)
	@for t in $$(ls themes | grep -v '^_'); do echo "== $$t"; python3 scripts/validate.py --theme $$t || true; python3 scripts/build_index.py --theme $$t; done
