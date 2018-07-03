#!/usr/bin/python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/blasto_project/genes/nucleoporins/jac_new_assembly/PASTA/')
files = os.listdir()

for file in files:
	aln = SeqIO.parse(file, 'fasta')
	file_name = file.split('.fa')[0]
	out = open(file_name + '_nogaps.fa', 'w')
	for sequence in aln:
		seq = str(sequence.seq).replace('-', '')
		name = sequence.description
		out.write('>{}\n{}\n'.format(name, seq))
out.close()