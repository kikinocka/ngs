#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/18S-V4-2018/')
table = open('otu_table.tsv')

with open('otu_table.no_chimera.tsv', 'w') as out:
	for line in table:
		if line.startswith('OTU'):
			out.write(line)
		elif line.split('\t')[68] == 'N': #check position of chimera assignment in the table
			out.write(line)
		else:
			pass
