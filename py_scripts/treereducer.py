#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/metamonada/OGs/iqtree/cpn60/')
inacc = open('delete.acc')
infasta = SeqIO.parse('/Users/kika/ownCloud/metamonada/OGs/iqtree/cpn60/q2001042.og_hmm.muscle.aln', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('q2001042_reduced.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
