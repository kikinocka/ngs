#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema/catalase/apx_tree/ver17/')
infasta = SeqIO.parse('excavata.fasta', 'fasta')
infile = open('excavata.acc')
out = open('excavata.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
