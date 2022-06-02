#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/ARFs/')
inacc = open('sarB_ver2/delete.acc')
infasta = SeqIO.parse('sarB_ver2/sarB.mafft.aln', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('sarB_ver3/sarB.mafft.aln', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
