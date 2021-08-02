#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/')
table = open('otu_table.V9DS.tsv')

with open('otu_table.V9DS_updated.tsv', 'w') as out:
	for line in table:
		if line.startswith('OTU'):
			new_line = '{}\tlineage\t{}'.format('\t'.join(line.split('\t')[0:22]), '\t'.join(line.split('\t')[22:]))
			out.write(new_line)
		elif line.split('\t')[22] == 'No_hit':
			new_line = '{}\tNo_hit|No_hit|No_hit|No_hit|No_hit|No_hit|No_hit|No_hit\t{}'.format('\t'.join(line.split('\t')[0:22]), 
				'\t'.join(line.split('\t')[22:]))
			out.write(new_line)
		elif line.split('\t')[22] == 'Eukaryota|*|*|*|*|*|*|*':
			new_line = '{}\tEukaryota|Eukaryota_X|Eukaryota_XX|Eukaryota_XXX|Eukaryota_XXXX|Eukaryota_XXXXX|Eukaryota_XXXXXX|Eukaryota_XXXXXX_sp\t{}'.format(
				'\t'.join(line.split('\t')[0:22]), '\t'.join(line.split('\t')[22:]))
			out.write(new_line)
		else:
			new_line = '{}\t{}\t{}'.format('\t'.join(line.split('\t')[0:22]), line.split('\t')[22], '\t'.join(line.split('\t')[22:]))
			out.write(new_line)
