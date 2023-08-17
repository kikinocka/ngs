#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/blasto_comparative/proteins/BLASTs+bedcov/')
table = open('Btri_proteins-final.interpro_sorted.tsv')

dedupl = {}
for line in table:
	protein = line.split('\t')[0]
	pfam = line.split('\t')[1]
	desc = line.split('\t')[2]
	eval = line.strip().split('\t')[3]
	if protein not in dedupl:
		dedupl[protein] = [(pfam, desc, eval)]
	else:
		# print(dedupl[protein][0][0])
		if pfam == dedupl[protein][0][0]:
			pass
		else:
			dedupl[protein].append((pfam, desc, eval))

with open('Btri_proteins-final.interpro_sorted_merged.tsv', 'w') as out:
	for key, value in dedupl.items():
		out.write('{}\t'.format(key))
		# print(key)
		for v in value:
			out.write('| {}: {} ({}) '.format(v[0], v[1], v[2]))
		out.write('\n')
