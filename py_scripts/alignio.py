#!/usr/bin/env python3
import os
from Bio import AlignIO

os.chdir('/mnt/mokosz/home/kika/metamonads_ancestral/OGs+HMMhits_trimal_gt-0.5_cons-50/')
files = [x for x in os.listdir() if x.endswith('.aln')]
out = 'trimal_gt-0.5_cons-50_len.tsv'

# #number of sequences
# print(len(alignment))

with open(out, 'w') as result:
	for file in files:
		print(file)
		name = file.split('.')[0]
		aln = AlignIO.read(file, 'fasta')
			
		try:
			#number of positions
			result.write('{}\t{}\n'.format(name, aln.get_alignment_length()))
		except ValueErorr:
			with open('trimal_errors.txt', 'a') as errors:
				errors.write('{}\n'.format(name))
