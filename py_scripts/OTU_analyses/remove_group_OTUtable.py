#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/V4-sediment/')
table = open('otu_table.no_chimera.updated.only_euks.above99.tsv')

unwanted = ['Embryophyceae', 'Metazoa']

with open('otu_table.no_chimera.updated.only_euks.above99.no_Metazoa_Embryophyceae.tsv', 'w') as out:
	for line in table:
		if 'Embryophycea' in line or 'Metazoa' in line:
			pass
		else:
			out.write(line)
