#!/usr/bin/python3
from Bio import SeqIO

infile = SeqIO.parse('/home/kika/MEGAsync/blasto_project/genes/repair/NHEJ/jac/jac_nhej_aa.txt', 'fasta')
out = open('/home/kika/MEGAsync/blasto_project/genes/repair/jac_nhej_split.txt', 'w')

for seq in infile:
	if 'term' in seq.name or 'middle' in seq.name:
		out.write('>{}\n{}\n'.format(seq.name, seq.seq))
out.close()