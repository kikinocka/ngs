#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ARFs/')
inacc = open('arl3/delete.acc')
infasta = SeqIO.parse('ver6/arfs.mafft.aln', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('arl3/arl3.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
