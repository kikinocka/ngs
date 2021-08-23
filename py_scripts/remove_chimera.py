#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS_updated.tsv')

with open('otu_table.V9DS_updated.no_chimera.tsv', 'w') as out:
	for line in table:
		if line.split('\t')[20] == 'Y':
			pass
		else:
			out.write(line)
