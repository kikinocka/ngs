#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/prototheca_HGT')
accs = open('pzop.fungi.acc')
table = open('pzop_hits.nr.blast.tsv')

accessions = []
for acc in accs:
	accessions.append(acc.strip())

with open('pzop.fungi.tsv', 'w') as out:
	for line in table:
		if line.split('\t')[0].split(' ')[0] in accessions:
			out.write(line)
