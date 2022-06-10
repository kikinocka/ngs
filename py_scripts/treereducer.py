#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/RABs/rabs2-4-14')
inacc = open('delete.acc')
infasta = SeqIO.parse('/Users/kika/ownCloud/membrane-trafficking/trees/RABs/ver13/rabs.fa', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('rabs2-4-14.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
