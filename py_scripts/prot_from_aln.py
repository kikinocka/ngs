#!/usr/bin/python3
import os
from Bio import AlignIO

os.chdir('/home/kika/alignments/')
files = os.listdir()
out = open('jac_nucleoporins.txt', 'w')

for file in files:
	if '.aln' in file:
		alignment = AlignIO.read(file, 'fasta')
		for seq_list in alignment.get_all_seqs():
			if 'jac' in seq_list.name:
				sequence = str(seq_list.seq).replace('-', '')
				out.write('>{}\n{}\n'.format(seq_list.name, sequence))