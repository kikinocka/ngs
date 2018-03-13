#!/usr/bin/python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/Data/EG_RNAseq/EGALL_6frames.fasta', 'fasta')
infile = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/in')
out = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/out', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		print(seq.name)
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
out.close()