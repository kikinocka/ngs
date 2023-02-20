#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/kinetoplastids/AOX/tree/ver2/')
inacc = open('delete.acc')
infasta = SeqIO.parse('/Users/kika/ownCloud/kinetoplastids/AOX/tree/ver2/aox.fa', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('aox_reduced.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
