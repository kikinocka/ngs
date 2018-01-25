#!/usr/bin/python3
import os
from Bio import SeqIO

contigs = SeqIO.parse('/home/kika/MEGAsync/Chlamydomonas/od_toma/Amazonie_transdecoder.faa', 'fasta')
names = open('/home/kika/MEGAsync/Chlamydomonas/od_toma/names.txt')

name_lst = []
for line in names:
	name_lst.append(line[:-1])

with open('/home/kika/MEGAsync/Chlamydomonas/od_toma/putative_pt_genes_aa.fa', 'w') as mit:
	for contig in contigs:
		if contig.description in name_lst:
			mit.write('>{}\n{}\n'.format(contig.description, contig.seq))