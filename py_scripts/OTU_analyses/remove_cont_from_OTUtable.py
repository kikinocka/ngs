#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/Lane26_18S_V9/')
accessions = open('contamination.acc')
table = open('otu_table.tsv')


cont = set()
for line in accessions:
	cont.add(line.strip())

with open('otu_table.updated.tsv', 'w') as otu, open('contamination_table.tsv', 'w') as contamination:
	for line in table:
		if line.split('\t')[1] in cont:
			contamination.write(line)
		else:
			otu.write(line)
