#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/ku_story/alignments/')
fasta = SeqIO.parse('ku80.fa', 'fasta')
out = open('ku80_reduced.fa', 'w')

pseudo = 0
incompl = 0
for seq in fasta:
	if 'X' in seq.seq:
		pseudo += 1
	elif 'M' != seq.seq[0]:
		incompl += 1
	else:
		out.write('>{}\n{}\n'.format(seq.description, str(seq.seq).replace('-', '')))

print('pseudogenes: ' + str(pseudo))
print('truncated: ' + str(incompl))

out.close()