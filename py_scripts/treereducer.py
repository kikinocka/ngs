#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/TBCs/')
inacc = open('tbc-Q/delete.acc')
infasta = SeqIO.parse('ver3/tbcs.mafft.aln', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('tbc-Q/tbc-Q.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
