#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/mnt/mokosz/home/kika/workdir/')
files = [x for x in os.listdir() if x.endswith('.trimal_gt-0.8.aln')]
out = 'trimal_gt-0.8_len.tsv'

# #number of sequences
# print(len(alignment))

with open(out, 'w') as result:
	for file in files:
		print(file)
		name = file.split('.')[0]
		aln = AlignIO.read(file, 'fasta')
		#number of positions
		result.write('{}\t{}\n'.format(name, aln.get_alignment_length()))
