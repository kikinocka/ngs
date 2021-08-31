#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/oil_sands/amplicons/Lane26_18S_V9/')
table = open('otu_table.updated.tsv')

with open('otu_table.updated.no_chimera.tsv', 'w') as out:
	for line in table:
		if line.split('\t')[74] == 'Y': #check position of chimera assignment in the table
			pass
		else:
			out.write(line)
