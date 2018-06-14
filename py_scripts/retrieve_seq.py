#!/usr/bin/python3
from Bio import SeqIO

infasta = SeqIO.parse('/home/kika/MEGAsync/diplonema_mt/1601/genome_assembly/1601_DNA_scaffolds.fasta', 'fasta')
infile = open('/home/kika/MEGAsync/diplonema_mt/HMM/in')
out = open('/home/kika/MEGAsync/diplonema_mt/HMM/1601_y5-m1_contigs.fa', 'w')

retrieve = set()
for line in infile:
	retrieve.add(line[:-1])

for seq in infasta:
	if seq.name in retrieve:
		out.write('>{}\n{}\n'.format(seq.description, seq.seq))
	else:
		print(seq.description)
out.close()