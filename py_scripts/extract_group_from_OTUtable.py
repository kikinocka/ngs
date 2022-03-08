#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('filtration/v9.no_chimera.above99.no_prokaryota.tsv')

groups = {}
with open('above99_decontaminated/stramenopiles/stramenopiles_counts.tsv', 'w') as counts, open('above99_decontaminated/stramenopiles/stramenopiles.V9DS_updated.no_chimera.tsv', 'w') as out:
	for line in table:
		taxonomy = line.split('\t')[22]
		if 'Stramenopiles' in taxonomy:
			out.write(line)
			if taxonomy.split('|')[1] not in groups:
				groups[taxonomy.split('|')[1]] = 1
			else:
				groups[taxonomy.split('|')[1]] +=1
	for key, value in groups.items():
		counts.write('{}\t{}\n'.format(key, value))
