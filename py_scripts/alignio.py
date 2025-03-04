#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/mnt/mokosz/home/kika/metamonads/MRO_proteins/3-MRO+HMMhits_muscle/')
files = [x for x in os.listdir() if x.endswith('.aln')]

# #number of sequences
# print(len(alignment))

with open(out, 'w') as result:
	for file in files:
		print(file)
		# name = file.split('.')[0]
		aln = AlignIO.read(file, 'fasta')
		#number of positions
		# result.write('{}\t{}\n'.format(name, aln.get_alignment_length()))
		result.write('{}\t{}\n'.format(file, aln.get_alignment_length()))
