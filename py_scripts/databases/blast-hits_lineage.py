#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/oil_sands/18S/blast/')
#file with blast query \t taxonomic group
taxonomy = open('eukaryota.lineage')

otu_dict = {}
for line in taxonomy:
	# print(line[:-1])
	if line.split('\t')[0] not in otu_dict:
		otu_dict[line.split('\t')[0]] = {'Bacteria' : 0, 'Archaea' : 0, 'Eukaryota' : 0, 'Viruses' : 0, 'unassigned' : 0, 'no hit' : 0}
		if line[:-1].split('\t')[1] == 'Bacteria':
			otu_dict[line.split('\t')[0]]['Bacteria'] += 1
		elif line[:-1].split('\t')[1] == 'Archaea':
			otu_dict[line.split('\t')[0]]['Archaea'] += 1
		elif line[:-1].split('\t')[1] == 'Eukaryota':
			otu_dict[line.split('\t')[0]]['Eukaryota'] += 1
		elif line[:-1].split('\t')[1] == 'Viruses':
			otu_dict[line.split('\t')[0]]['Viruses'] += 1
		elif line[:-1].split('\t')[1] == '0':
			otu_dict[line.split('\t')[0]]['unassigned'] += 1
		elif line[:-1].split('\t')[1] == '#N/A':
			otu_dict[line.split('\t')[0]]['no hit'] += 1
	else:
		if line[:-1].split('\t')[1] == 'Bacteria':
			otu_dict[line.split('\t')[0]]['Bacteria'] += 1
		elif line[:-1].split('\t')[1] == 'Archaea':
			otu_dict[line.split('\t')[0]]['Archaea'] += 1
		elif line[:-1].split('\t')[1] == 'Eukaryota':
			otu_dict[line.split('\t')[0]]['Eukaryota'] += 1
		elif line[:-1].split('\t')[1] == 'Viruses':
			otu_dict[line.split('\t')[0]]['Viruses'] += 1
		elif line[:-1].split('\t')[1] == '0':
			otu_dict[line.split('\t')[0]]['unassigned'] += 1
		elif line[:-1].split('\t')[1] == '#N/A':
			otu_dict[line.split('\t')[0]]['no hit'] += 1

with open('eukaryota-simplified.lineage', 'w') as result:
	for otu, groups in otu_dict.items():
		print(otu)
		result.write('{}\t'.format(otu))
		for group, count in groups.items():
			if count == 0:
				pass
			else:
				result.write('{} {}, '.format(group, count))
		result.write('\n')		







