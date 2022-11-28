#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/blastocrithidia/genes/tRNAs/ciliates/sequences/')
files = [x for x in os.listdir() if x.endswith('aragorn.fa')]
names = open('ciliates_names.txt')

nd = {}
for line in names:
	nd[line.split('\t')[0]] = line.strip().split('\t')[1]

with open('Gln-tRNAs_renamed.fa', 'w') as out:
	for file in files:
		print(file)
		fname = '{}_{}'.format(file.split('_')[0], file.split('_')[1])
		c = 0
		if fname in nd.keys():
			for seq in SeqIO.parse(file, 'fasta'):
				if 'Gln' in seq.name:
					c += 1
					out.write('>{}__{}__{}__{}\n{}\n'.format(nd[fname], fname, seq.name.split('(')[1].split(')')[0], c, seq.seq))
		else:
			print('{} not in names'.format(fname))
