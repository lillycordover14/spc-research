.PHONY: ingest index validate search new-company new-source stats

ingest:        ## normalize everything in inbox/ into sources/<type>/ (+ raw/)
	python3 scripts/ingest.py

index:         ## rebuild index/*.jsonl, companies.csv and index/anip.sqlite (FTS5)
	python3 scripts/build_index.py

validate:      ## check every frontmatter against schema/
	python3 scripts/validate.py

search:        ## make search q="rare earth refining"
	python3 scripts/search.py "$(q)"

new-company:   ## make new-company name="Nox Metals"
	python3 scripts/new.py company "$(name)"

new-source:    ## make new-source type=expert-call title="Call w/ ex-Hadrian ops lead"
	python3 scripts/new.py source "$(title)" --type $(type)

stats:         ## counts by type / layer / status
	python3 scripts/build_index.py --stats
