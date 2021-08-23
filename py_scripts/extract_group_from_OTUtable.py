#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS_updated.no_chimera.tsv')

groups = {}
with open('breviatea_counts.tsv', 'w') as counts, open('breviatea.V9DS_updated.no_chimera.tsv', 'w') as out:
	for line in table:
		taxonomy = line.split('\t')[22]
		if 'Breviata' in taxonomy:
			out.write(line)
			if taxonomy.split('|')[3] not in groups:
				groups[taxonomy.split('|')[3]] = 1
			else:
				groups[taxonomy.split('|')[3]] +=1
	for key, value in groups.items():
		counts.write('{}\t{}\n'.format(key, value))
