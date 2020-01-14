#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema/catalase/apx_tree/')
db = SeqIO.parse('ver19/apx_seqs.fa', 'fasta')
accessions = open('ver20/apx.acc')
out = open('ver20/apx_seqs.fa', 'w')

retrieve = set()
for line in accessions:
	retrieve.add(line[:-1])

for seq in db:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
	else:
		# print(seq.description)
		pass
out.close()
