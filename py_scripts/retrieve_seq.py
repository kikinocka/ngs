#!/usr/bin/python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/Data/EG_RNAseq/EGALL_6frames.fasta', 'fasta')
infile = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/tic62_tree/in')
out = open('/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/import/TOC-TIC/tic62_tree/eg_seqs.txt', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
out.close()