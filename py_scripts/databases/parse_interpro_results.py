#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/blastocrithidia/predicted_proteins/')
table = open('bnonstop_predicted_proteins.interpro_dedupl.tsv')

dedupl = {}
for line in table:
	protein = line.split('\t')[0]
	pfam = line.split('\t')[1]
	desc = line.split('\t')[2]
	eval = line.strip().split('\t')[3]
	if protein not in dedupl:
		dedupl[protein] = [(pfam, desc, eval)]
	else:
		dedupl[protein].append((pfam, desc, eval))

with open('bnonstop_predicted_proteins.interpro_dedupl_merged.tsv', 'w') as out:
	for key, value in dedupl.items():
		out.write('{}\t'.format(key))
		# print(key)
		for v in value:
			out.write('| {}: {} ({}) '.format(v[0], v[1], v[2]))
		out.write('\n')
