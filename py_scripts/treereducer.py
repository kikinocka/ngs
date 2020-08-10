#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Users/kika/ownCloud/pelomyxa_schiedti/trees/NaS_transporter/ver3')
inacc = open('delete.acc')
infasta = SeqIO.parse('nast_v3.fa', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('nast_reduced.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
