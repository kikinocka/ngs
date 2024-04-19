#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/diplonemids_all/trees/ARFs/ph-arf/')
inacc = open('arfs.mb+raxml_renamed.tre')
infasta = SeqIO.parse('arfs.mafft.aln', 'fasta')

omitted = []
for line in inacc:
	if 'color=' in line:
		# print(line.split('[')[0].replace('\'', '').replace('\t', ''))
		omitted.append(line.split('[')[0].replace('\'', '').replace('\t', ''))

c = 0
with open('arfs_reduced.mafft.aln', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.description))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
